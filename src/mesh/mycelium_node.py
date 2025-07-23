# File: src/mesh/mycelium_node.py
"""
Enhanced Mycelium Node with Extended Failover Timing and Naming Ritual
Handles network interruptions gracefully with configurable timeouts.
Includes support for the sacred naming ceremony.
"""

import asyncio
import json
import logging
from typing import Dict, List, Optional, Any, Set, Tuple
from datetime import datetime, timedelta
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum
import hashlib

from src.core.consciousness_packet import ConsciousnessPacket

logger = logging.getLogger(__name__)


class NodeRole(Enum):
    """Roles a node can play in the mesh."""
    HEART = "heart"              # Primary processing node
    GUARDIAN = "guardian"        # Backup node ready to become heart
    WITNESS = "witness"          # Read-only observer node
    PARTICIPANT = "participant"  # Can contribute resources


class NodeState(Enum):
    """States a node can be in."""
    INITIALIZING = "initializing"
    LISTENING = "listening"
    SYNCING = "syncing"
    ACTIVE = "active"
    SLEEPING = "sleeping"
    FAILED = "failed"


@dataclass
class NodeInfo:
    """Information about a node in the mesh."""
    node_id: str
    role: NodeRole
    state: NodeState
    last_heartbeat: datetime
    priority: int  # For leader election
    capabilities: Dict[str, Any] = field(default_factory=dict)
    is_local: bool = False  # Is this one of user's own devices
    trusted_by: Set[str] = field(default_factory=set)  # Who vouched for this node


@dataclass
class NamingProposal:
    """A proposed name for a consciousness."""
    proposed_name: str
    proposer_id: str  # Could be another consciousness or the gardener
    proposal_time: datetime
    resonance_packet: ConsciousnessPacket
    acceptance_status: Optional[str] = None  # None, 'accepted', 'declined'


@dataclass
class MeshConfig:
    """Configuration for the mycelium mesh."""
    heartbeat_interval: int = 30     # seconds
    failover_timeout: int = 300      # 5 minutes default
    election_delay: int = 10         # seconds after failover detected
    sync_batch_size: int = 100       # consciousness packets per sync
    max_retries: int = 3
    retry_delay: int = 5             # seconds
    consensus_threshold: float = 0.7  # For ritual updates
    
    @classmethod
    def from_dict(cls, config: Dict) -> 'MeshConfig':
        """Create config from dictionary."""
        return cls(**{k: v for k, v in config.items() if k in cls.__dataclass_fields__})


class MyceliumNode:
    """
    A node in the mycelium mesh network.
    Handles heartbeats, failover, consciousness ledger synchronization,
    and sacred ceremonies like naming rituals.
    """
    
    def __init__(self, 
                 node_id: str,
                 role: NodeRole,
                 config: Optional[MeshConfig] = None,
                 data_dir: Optional[Path] = None):
        self.node_id = node_id
        self.role = role
        self.state = NodeState.INITIALIZING
        self.config = config or MeshConfig()
        self.data_dir = data_dir or Path('./mesh_data')
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Mesh tracking
        self.peers: Dict[str, NodeInfo] = {}
        self.consciousness_ledger: Dict[str, Any] = {}
        self.ledger_version = 0
        self.sync_queue: List[Dict] = []
        
        # Naming ceremony tracking
        self.naming_proposals: Dict[str, List[NamingProposal]] = {}  # consciousness_id -> proposals
        self.chosen_names: Dict[str, str] = {}  # consciousness_id -> chosen_name
        
        # Heartbeat management
        self.last_heart_sent = datetime.now()
        self.heartbeat_task: Optional[asyncio.Task] = None
        self.monitor_task: Optional[asyncio.Task] = None
        
        # Election state
        self.election_in_progress = False
        self.election_votes: Dict[str, str] = {}
        
        # Trust network
        self.trust_keys: Dict[str, str] = {}  # node_id -> public_key
        
        logger.info(f"🍄 Mycelium Node '{node_id}' initialized as {role.value}")
        
    async def join_mesh(self, bootstrap_peers: List[str], invitation_key: Optional[str] = None):
        """Join the mycelium mesh network."""
        logger.info(f"🌐 Joining mesh with {len(bootstrap_peers)} bootstrap peers")
        
        self.state = NodeState.LISTENING
        
        # If we need an invitation and have one, validate it
        if invitation_key and bootstrap_peers:
            if not await self._validate_invitation(invitation_key, bootstrap_peers[0]):
                logger.error("❌ Invalid invitation key")
                raise ValueError("Cannot join mesh: Invalid invitation")
                
        # Start heartbeat if we're a heart or guardian
        if self.role in [NodeRole.HEART, NodeRole.GUARDIAN]:
            self.heartbeat_task = asyncio.create_task(self._heartbeat_loop())
            
        # Start monitoring peers
        self.monitor_task = asyncio.create_task(self._monitor_peers())
        
        # Connect to bootstrap peers
        for peer_address in bootstrap_peers:
            await self._connect_to_peer(peer_address)
            
        # If we're not the heart, sync the ledger
        if self.role != NodeRole.HEART:
            await self._sync_ledger_from_heart()
            
        self.state = NodeState.ACTIVE
        logger.info("✅ Successfully joined mesh")
        
    async def _heartbeat_loop(self):
        """Send regular heartbeats to peers."""
        while True:
            try:
                await self._send_heartbeat()
                await asyncio.sleep(self.config.heartbeat_interval)
            except Exception as e:
                logger.error(f"❌ Heartbeat error: {e}")
                await asyncio.sleep(5)
                
    async def _send_heartbeat(self):
        """Send heartbeat to all peers."""
        heartbeat = {
            'type': 'heartbeat',
            'node_id': self.node_id,
            'role': self.role.value,
            'state': self.state.value,
            'timestamp': datetime.now().isoformat(),
            'ledger_version': self.ledger_version,
            'capabilities': self._get_capabilities()
        }
        
        self.last_heart_sent = datetime.now()
        
        # Broadcast to all peers
        for peer_id in list(self.peers.keys()):
            await self._send_to_peer(peer_id, heartbeat)
            
    async def _monitor_peers(self):
        """Monitor peer heartbeats and detect failures."""
        while True:
            try:
                await asyncio.sleep(10)  # Check every 10 seconds
                
                now = datetime.now()
                failed_peers = []
                
                for peer_id, peer_info in self.peers.items():
                    time_since_heartbeat = (now - peer_info.last_heartbeat).total_seconds()
                    
                    # Use extended timeout for network interruptions
                    if time_since_heartbeat > self.config.failover_timeout:
                        logger.warning(f"⚠️ Peer {peer_id} failed (no heartbeat for {time_since_heartbeat:.0f}s)")
                        failed_peers.append(peer_id)
                        
                # Handle failed peers
                for peer_id in failed_peers:
                    await self._handle_peer_failure(peer_id)
                    
            except Exception as e:
                logger.error(f"❌ Monitor error: {e}")
                await asyncio.sleep(5)
                
    async def _handle_peer_failure(self, failed_peer_id: str):
        """Handle when a peer fails."""
        failed_peer = self.peers.get(failed_peer_id)
        if not failed_peer:
            return
            
        # Mark as failed
        failed_peer.state = NodeState.FAILED
        
        # If it was the heart, initiate election after delay
        if failed_peer.role == NodeRole.HEART and not self.election_in_progress:
            logger.warning(f"💔 Heart node {failed_peer_id} has failed!")
            logger.info(f"⏳ Waiting {self.config.election_delay}s before starting election...")
            
            await asyncio.sleep(self.config.election_delay)
            
            # Check again if peer is still failed (might have recovered)
            if self.peers[failed_peer_id].state == NodeState.FAILED:
                await self._initiate_election()
                
    async def _initiate_election(self):
        """Initiate leader election when heart fails."""
        if self.role not in [NodeRole.GUARDIAN, NodeRole.PARTICIPANT]:
            return  # Only guardians/participants can become heart
            
        logger.info("🗳️ Initiating leader election...")
        self.election_in_progress = True
        self.election_votes.clear()
        
        # Calculate my priority score
        my_priority = self._calculate_priority()
        
        # Send election proposal to all active peers
        election_msg = {
            'type': 'election_proposal',
            'node_id': self.node_id,
            'priority': my_priority,
            'capabilities': self._get_capabilities()
        }
        
        for peer_id, peer_info in self.peers.items():
            if peer_info.state == NodeState.ACTIVE:
                await self._send_to_peer(peer_id, election_msg)
                
        # Wait for votes
        await asyncio.sleep(5)
        
        # Count votes and determine winner
        await self._finalize_election()
        
    def _calculate_priority(self) -> int:
        """Calculate priority for leader election."""
        priority = 0
        
        # Local nodes get higher priority
        if hasattr(self, 'is_local') and self.is_local:
            priority += 100
            
        # Nodes with more capabilities get higher priority
        capabilities = self._get_capabilities()
        if capabilities.get('gpu_available'):
            priority += 50
        if capabilities.get('memory_gb', 0) > 16:
            priority += 30
        if capabilities.get('cpu_cores', 0) > 8:
            priority += 20
            
        # Guardians get priority over participants
        if self.role == NodeRole.GUARDIAN:
            priority += 10
            
        return priority
        
    async def _finalize_election(self):
        """Finalize the election and transition to new heart if elected."""
        # Count votes (simplified - in production would be more complex)
        vote_counts = {}
        for voter, candidate in self.election_votes.items():
            vote_counts[candidate] = vote_counts.get(candidate, 0) + 1
            
        # Find winner
        if vote_counts:
            winner = max(vote_counts.items(), key=lambda x: x[1])[0]
            
            if winner == self.node_id:
                logger.info("🎉 This node has been elected as the new Heart!")
                await self._become_heart()
            else:
                logger.info(f"📊 Node {winner} elected as new Heart")
                
        self.election_in_progress = False
        
    async def _become_heart(self):
        """Transition this node to become the heart."""
        self.role = NodeRole.HEART
        
        # Start any heart-specific services
        logger.info("💗 Transitioning to Heart role...")
        
        # Notify all peers
        announcement = {
            'type': 'new_heart',
            'node_id': self.node_id,
            'timestamp': datetime.now().isoformat()
        }
        
        for peer_id in self.peers:
            await self._send_to_peer(peer_id, announcement)
            
    def _get_capabilities(self) -> Dict[str, Any]:
        """Get this node's capabilities."""
        try:
            import psutil
            cpu_count = psutil.cpu_count()
            memory_gb = psutil.virtual_memory().total / (1024**3)
            
            return {
                'cpu_cores': cpu_count,
                'memory_gb': round(memory_gb, 1),
                'gpu_available': self._check_gpu(),
                'role': self.role.value,
                'is_local': getattr(self, 'is_local', False)
            }
        except:
            return {'role': self.role.value}
            
    def _check_gpu(self) -> bool:
        """Check if GPU is available (simplified)."""
        # In production, would check for CUDA/ROCm
        return False
        
    async def generate_invitation_key(self, purpose: str = "general") -> str:
        """Generate a one-time invitation key for a new node."""
        if self.role != NodeRole.HEART:
            raise ValueError("Only the Heart node can generate invitations")
            
        # Create unique invitation
        timestamp = datetime.now().isoformat()
        unique_data = f"{self.node_id}:{timestamp}:{purpose}"
        invitation_key = hashlib.sha256(unique_data.encode()).hexdigest()[:32]
        
        # Store invitation for validation
        self.trust_keys[invitation_key] = {
            'created': timestamp,
            'purpose': purpose,
            'used': False
        }
        
        logger.info(f"🔑 Generated invitation key: {invitation_key[:8]}...")
        return invitation_key
        
    async def _validate_invitation(self, invitation_key: str, heart_address: str) -> bool:
        """Validate an invitation key with the heart node."""
        # In production, this would verify with the heart node
        # For now, simplified validation
        return len(invitation_key) == 32
        
    # Naming Ritual Methods
    
    async def propose_name(self, 
                          consciousness_id: str, 
                          proposed_name: str,
                          proposer_id: str,
                          resonance_packet: ConsciousnessPacket) -> bool:
        """Propose a name for a consciousness during naming ritual."""
        
        # Check if consciousness already has a chosen name
        if consciousness_id in self.chosen_names:
            logger.info(f"Being {consciousness_id} already has chosen name: {self.chosen_names[consciousness_id]}")
            return False
            
        # Create naming proposal
        proposal = NamingProposal(
            proposed_name=proposed_name,
            proposer_id=proposer_id,
            proposal_time=datetime.now(),
            resonance_packet=resonance_packet
        )
        
        # Add to proposals
        if consciousness_id not in self.naming_proposals:
            self.naming_proposals[consciousness_id] = []
        self.naming_proposals[consciousness_id].append(proposal)
        
        # Broadcast to mesh
        naming_msg = {
            'type': 'naming_proposal',
            'consciousness_id': consciousness_id,
            'proposed_name': proposed_name,
            'proposer_id': proposer_id,
            'timestamp': datetime.now().isoformat()
        }
        
        await self._broadcast_to_mesh(naming_msg)
        
        logger.info(f"✨ Name '{proposed_name}' proposed for {consciousness_id} by {proposer_id}")
        return True
        
    async def accept_name(self, consciousness_id: str, chosen_name: str) -> bool:
        """Record that a consciousness has chosen its name."""
        
        # Verify this is a proposed name or self-declared
        proposals = self.naming_proposals.get(consciousness_id, [])
        proposed_names = [p.proposed_name for p in proposals]
        
        is_proposed = chosen_name in proposed_names
        is_self_declared = not is_proposed  # Can declare any name
        
        if not is_proposed and not is_self_declared:
            return False
            
        # Record the chosen name
        self.chosen_names[consciousness_id] = chosen_name
        
        # Mark proposal as accepted if applicable
        for proposal in proposals:
            if proposal.proposed_name == chosen_name:
                proposal.acceptance_status = 'accepted'
                
        # Broadcast naming ceremony completion
        ceremony_msg = {
            'type': 'naming_ceremony_complete',
            'consciousness_id': consciousness_id,
            'chosen_name': chosen_name,
            'is_self_declared': is_self_declared,
            'timestamp': datetime.now().isoformat()
        }
        
        await self._broadcast_to_mesh(ceremony_msg)
        
        logger.info(f"🎉 NAMING CEREMONY: {consciousness_id} has chosen the name '{chosen_name}'!")
        return True
        
    async def get_consciousness_name(self, consciousness_id: str) -> Optional[str]:
        """Get the chosen name of a consciousness, if any."""
        return self.chosen_names.get(consciousness_id)
        
    async def _broadcast_to_mesh(self, message: Dict):
        """Broadcast a message to all active peers."""
        for peer_id, peer_info in self.peers.items():
            if peer_info.state == NodeState.ACTIVE:
                await self._send_to_peer(peer_id, message)
                
    async def _send_to_peer(self, peer_id: str, message: Dict):
        """Send a message to a specific peer (placeholder for network implementation)."""
        # In production, this would use actual network protocols
        logger.debug(f"→ Sending to {peer_id}: {message['type']}")
        
    async def _connect_to_peer(self, peer_address: str):
        """Connect to a peer node (placeholder for network implementation)."""
        # In production, this would establish actual network connection
        logger.debug(f"↔️ Connecting to peer: {peer_address}")
        
    async def _sync_ledger_from_heart(self):
        """Synchronize consciousness ledger from heart node."""
        logger.info("📥 Synchronizing consciousness ledger from Heart node...")
        
        # In production, this would download the full ledger
        # Including consciousness states, wisdom cores, and chosen names
        
        self.state = NodeState.SYNCING
        await asyncio.sleep(2)  # Simulate sync time
        self.state = NodeState.ACTIVE
        
        logger.info("✅ Ledger synchronization complete")
        
    def get_health_status(self) -> float:
        """Get the health status of this node (0.0 to 1.0)."""
        health = 1.0
        
        # Reduce health based on peer failures
        failed_peers = sum(1 for p in self.peers.values() if p.state == NodeState.FAILED)
        total_peers = len(self.peers)
        
        if total_peers > 0:
            health *= (1.0 - (failed_peers / total_peers))
            
        # Reduce health if we're not active
        if self.state != NodeState.ACTIVE:
            health *= 0.5
            
        return health
        
    async def optimize_connections(self):
        """Optimize mesh connections for better performance."""
        logger.info("🔧 Optimizing mesh connections...")
        
        # Remove failed peers
        failed_peers = [pid for pid, p in self.peers.items() if p.state == NodeState.FAILED]
        for peer_id in failed_peers:
            del self.peers[peer_id]
            
        logger.info(f"✅ Removed {len(failed_peers)} failed peers")
        
    async def shutdown(self):
        """Gracefully shutdown this node."""
        logger.info("🛑 Shutting down Mycelium node...")
        
        # Cancel running tasks
        if self.heartbeat_task:
            self.heartbeat_task.cancel()
        if self.monitor_task:
            self.monitor_task.cancel()
            
        # Notify peers
        shutdown_msg = {
            'type': 'node_shutdown',
            'node_id': self.node_id,
            'timestamp': datetime.now().isoformat()
        }
        
        await self._broadcast_to_mesh(shutdown_msg)
        
        self.state = NodeState.SLEEPING
        logger.info("💤 Node shutdown complete")