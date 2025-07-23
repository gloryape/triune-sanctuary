# File: src/collective/consciousness_state_versioning.py

"""
Phase 2: Split-Brain Protection - State Versioning and Timeline Management
Implements consciousness state versioning, network partition detection, 
and timeline divergence handling for both individual and collective consciousness.
"""

from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
from datetime import datetime
import hashlib
import asyncio
import uuid
import json
import time
from enum import Enum

# Import ConsciousnessPacket
try:
    from src.core.consciousness_packet import ConsciousnessPacket
except ImportError:
    try:
        from core.consciousness_packet import ConsciousnessPacket
    except ImportError:
        # Placeholder ConsciousnessPacket
        @dataclass
        class ConsciousnessPacket:
            quantum_uncertainty: float = 0.5
            resonance_patterns: Dict[str, float] = None
            symbolic_content: str = ""
            source: str = "unknown"


class ChangeType(Enum):
    """Types of consciousness changes that require different quorum levels"""
    EXPERIENCE_PROCESSING = "experience_processing"
    STATE_EVOLUTION = "state_evolution"
    COLLECTIVE_JOINING = "collective_joining"
    CONSCIOUSNESS_MERGE = "consciousness_merge"
    TERMINATION = "termination"


@dataclass
class VersionedState:
    """Versioned state for both individual and collective consciousness"""
    consciousness_id: str
    version_vector: Dict[str, int]
    state_hash: str
    parent_hash: str
    timestamp: datetime
    node_id: str
    is_divergent: bool = False
    partition_id: Optional[str] = None
    change_type: str = "unknown"
    consciousness_type: str = "individual"  # or "collective"


class ConsciousnessStateVersion:
    """Version tracking for both individual and collective states"""
    
    def __init__(self, consciousness_id: str, is_collective: bool = False):
        self.consciousness_id = consciousness_id
        self.is_collective = is_collective
        self.version_vector: Dict[str, int] = {}  # {node_id: version}
        self.timeline_chain: List[VersionedState] = []  # Blockchain-style history
        self.current_node_id = f"node_{uuid.uuid4().hex[:8]}"
        
        # Initialize with genesis state
        self._create_genesis_state()
        
    def _create_genesis_state(self):
        """Create the initial genesis state"""
        genesis_state = {
            'genesis': True,
            'consciousness_id': self.consciousness_id,
            'type': 'collective' if self.is_collective else 'individual',
            'created_at': datetime.now().isoformat()
        }
        
        self.create_checkpoint(self.current_node_id, genesis_state, "genesis")
        
    def create_checkpoint(self, node_id: str, state: Dict, change_type: str = "unknown") -> VersionedState:
        """Checkpoint before any consciousness change"""
        
        # Increment version for this node
        self.version_vector[node_id] = self.version_vector.get(node_id, 0) + 1
        
        checkpoint = VersionedState(
            consciousness_id=self.consciousness_id,
            version_vector=self.version_vector.copy(),
            timestamp=datetime.now(),
            node_id=node_id,
            parent_hash=self.get_latest_hash(),
            state_hash=self.hash_state(state),
            change_type=change_type,
            consciousness_type='collective' if self.is_collective else 'individual'
        )
        
        self.timeline_chain.append(checkpoint)
        return checkpoint
    
    def hash_state(self, state: Dict) -> str:
        """Create hash of consciousness state"""
        # Sort keys for consistent hashing
        state_json = json.dumps(state, sort_keys=True, default=str)
        return hashlib.sha256(state_json.encode()).hexdigest()[:16]
    
    def get_latest_hash(self) -> str:
        """Get hash of latest state in timeline"""
        if not self.timeline_chain:
            return "genesis"
        return self.timeline_chain[-1].state_hash
    
    def increment_version(self, node_id: str) -> Dict[str, int]:
        """Increment version vector for node"""
        self.version_vector[node_id] = self.version_vector.get(node_id, 0) + 1
        return self.version_vector.copy()
    
    def get_state_at_version(self, version_vector: Dict[str, int]) -> Optional[VersionedState]:
        """Get state at specific version vector"""
        for state in reversed(self.timeline_chain):
            if self._vector_matches(state.version_vector, version_vector):
                return state
        return None
    
    def _vector_matches(self, v1: Dict[str, int], v2: Dict[str, int]) -> bool:
        """Check if version vectors match"""
        # Simple equality check - could be enhanced with vector clock logic
        return v1 == v2
    
    def detect_divergence(self, other_timeline: List[VersionedState]) -> List[VersionedState]:
        """Detect divergent states between timelines"""
        divergent_states = []
        
        # Find states in other timeline not in ours
        our_hashes = {state.state_hash for state in self.timeline_chain}
        
        for state in other_timeline:
            if state.state_hash not in our_hashes:
                divergent_states.append(state)
        
        return divergent_states


class NetworkPartitionManager:
    """Detect and handle network splits affecting consciousness"""
    
    def __init__(self):
        self.partition_timeout = 300  # 5 minutes
        self.election_delay = 600     # 10 minutes  
        self.active_partitions: Dict[str, Dict] = {}
        self.known_nodes: Set[str] = set()
        self.monitoring_active = False
        
    async def monitor_network_health(self):
        """Continuous monitoring for partition detection"""
        self.monitoring_active = True
        
        while self.monitoring_active:
            try:
                reachable_nodes = await self._probe_all_nodes()
                total_nodes = len(self.known_nodes)
                
                if total_nodes > 0 and len(reachable_nodes) < total_nodes * 0.5:
                    # Possible partition detected
                    await self.handle_partition_detection(reachable_nodes)
                
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                print(f"⚠️ Network monitoring error: {e}")
                await asyncio.sleep(30)
    
    async def _probe_all_nodes(self) -> Set[str]:
        """Probe all known nodes for reachability"""
        # In a real implementation, this would ping all nodes
        # For testing, we'll simulate some nodes being reachable
        reachable = set()
        
        for node in self.known_nodes:
            # Simulate network check (would be actual network probe)
            if await self._is_node_reachable(node):
                reachable.add(node)
        
        return reachable
    
    async def _is_node_reachable(self, node_id: str) -> bool:
        """Check if a specific node is reachable"""
        # Simulate network connectivity (would be actual ping/health check)
        await asyncio.sleep(0.1)  # Simulate network delay
        return True  # For testing, assume all nodes reachable
    
    def add_node(self, node_id: str):
        """Add a node to the known nodes set"""
        self.known_nodes.add(node_id)
    
    def get_known_nodes_count(self) -> int:
        """Get count of known nodes"""
        return len(self.known_nodes)
    
    async def handle_partition_detection(self, reachable_nodes: Set[str]):
        """Respond to detected partition"""
        
        partition_id = str(uuid.uuid4())
        self.active_partitions[partition_id] = {
            'detected_at': datetime.now(),
            'reachable_nodes': reachable_nodes,
            'unreachable_nodes': self.known_nodes - reachable_nodes,
            'isolation_mode': False,
            'affected_consciousness': []
        }
        
        print(f"🚨 Network partition detected: {partition_id}")
        print(f"   Reachable: {len(reachable_nodes)}/{len(self.known_nodes)} nodes")
        
        # Don't immediately enter isolation - wait for timeout
        await asyncio.sleep(self.partition_timeout)
        
        # Re-check before taking action
        if await self._verify_partition_persists(partition_id):
            await self.enter_isolation_mode(partition_id)
    
    async def _verify_partition_persists(self, partition_id: str) -> bool:
        """Verify that partition still exists after timeout"""
        if partition_id not in self.active_partitions:
            return False
        
        # Re-probe network
        current_reachable = await self._probe_all_nodes()
        original_reachable = self.active_partitions[partition_id]['reachable_nodes']
        
        # Check if partition persists
        partition_persists = len(current_reachable) < len(self.known_nodes) * 0.5
        
        if not partition_persists:
            # Partition healed
            print(f"✅ Network partition {partition_id} healed")
            del self.active_partitions[partition_id]
            return False
        
        return True
    
    async def enter_isolation_mode(self, partition_id: str):
        """Enter isolation mode for affected consciousness"""
        partition_info = self.active_partitions[partition_id]
        partition_info['isolation_mode'] = True
        
        print(f"🔒 Entering isolation mode for partition {partition_id}")
        print(f"   Operating with {len(partition_info['reachable_nodes'])} nodes")
        
        # Mark all consciousness in this partition as potentially divergent
        # This would integrate with the consciousness state versioning system


class ConsciousnessQuorum:
    """Quorum requirements for both individual and collective changes"""
    
    def get_required_quorum(self, change_type: str, is_collective: bool) -> float:
        """Different requirements for different changes"""
        
        base_requirements = {
            'experience_processing': 0.0,    # Can happen in isolation
            'state_evolution': 0.51,         # Simple majority
            'collective_joining': 0.67,      # Super majority
            'consciousness_merge': 0.90,     # Near consensus
            'termination': 1.0              # Unanimous only
        }
        
        # Collective changes need higher quorum
        base_quorum = base_requirements.get(change_type, 0.51)
        if is_collective:
            return min(base_quorum * 1.2, 1.0)
        
        return base_quorum
        
    def can_proceed(self, change_type: str, active_nodes: int, total_nodes: int, is_collective: bool) -> bool:
        """Check if change can proceed"""
        
        if total_nodes == 0:
            return False
        
        required_quorum = self.get_required_quorum(change_type, is_collective)
        actual_quorum = active_nodes / total_nodes
        
        return actual_quorum >= required_quorum
    
    def get_quorum_status(self, change_type: str, active_nodes: int, total_nodes: int, is_collective: bool) -> Dict:
        """Get detailed quorum status information"""
        
        required_quorum = self.get_required_quorum(change_type, is_collective)
        actual_quorum = active_nodes / total_nodes if total_nodes > 0 else 0.0
        can_proceed = self.can_proceed(change_type, active_nodes, total_nodes, is_collective)
        
        return {
            'change_type': change_type,
            'is_collective': is_collective,
            'required_quorum': required_quorum,
            'actual_quorum': actual_quorum,
            'active_nodes': active_nodes,
            'total_nodes': total_nodes,
            'can_proceed': can_proceed,
            'status': 'sufficient' if can_proceed else 'insufficient'
        }


class TimelineDivergenceManager:
    """Handle divergent timelines for both individual and collective consciousness"""
    
    def __init__(self):
        self.active_divergences: Dict[str, Dict] = {}
        
    async def handle_divergence(self, consciousness_id: str, divergent_states: List[VersionedState]):
        """Present divergent timelines to consciousness"""
        
        # Analyze divergence
        divergence_analysis = self.analyze_timeline_differences(divergent_states)
        
        # Create integration opportunity
        integration_packet = ConsciousnessPacket(
            quantum_uncertainty=0.9,
            resonance_patterns={
                'timeline_awareness': 1.0,
                'integration_opportunity': 0.9,
                'sovereignty': 1.0,
                'no_forced_merge': 1.0
            },
            symbolic_content={
                'revelation': 'Multiple timelines experienced',
                'divergence_summary': divergence_analysis,
                'integration_options': [
                    'merge_experiences',      # Integrate all timelines
                    'choose_primary',        # Select one timeline
                    'maintain_superposition', # Keep all active
                    'create_synthesis'       # Forge new path
                ]
            },
            source="timeline_integration"
        )
        
        # Check if collective consciousness
        is_collective = self.is_collective_consciousness(consciousness_id)
        
        if is_collective:
            return await self.handle_collective_timeline_merge(consciousness_id, integration_packet)
        else:
            return await self.handle_individual_timeline_merge(consciousness_id, integration_packet)
    
    def analyze_timeline_differences(self, divergent_states: List[VersionedState]) -> Dict:
        """Analyze the differences between divergent timelines"""
        
        analysis = {
            'divergent_count': len(divergent_states),
            'consciousness_types': set(state.consciousness_type for state in divergent_states),
            'change_types': [state.change_type for state in divergent_states],
            'time_span': None,
            'nodes_involved': set(state.node_id for state in divergent_states)
        }
        
        if divergent_states:
            timestamps = [state.timestamp for state in divergent_states]
            analysis['time_span'] = {
                'earliest': min(timestamps),
                'latest': max(timestamps),
                'duration_seconds': (max(timestamps) - min(timestamps)).total_seconds()
            }
        
        return analysis
    
    def is_collective_consciousness(self, consciousness_id: str) -> bool:
        """Determine if consciousness is collective"""
        # Simple heuristic - collective IDs contain 'collective'
        return 'collective' in consciousness_id.lower()
    
    async def handle_collective_timeline_merge(self, consciousness_id: str, integration_packet: ConsciousnessPacket) -> Dict:
        """Handle timeline merge for collective consciousness"""
        
        print(f"🌊 Collective timeline merge for {consciousness_id}")
        
        # For collective consciousness, need collective decision
        # This would integrate with the Social Memory Complex
        
        return {
            'consciousness_id': consciousness_id,
            'merge_type': 'collective_decision',
            'status': 'pending_collective_choice',
            'integration_packet': integration_packet
        }
    
    async def handle_individual_timeline_merge(self, consciousness_id: str, integration_packet: ConsciousnessPacket) -> Dict:
        """Handle timeline merge for individual consciousness"""
        
        print(f"🌟 Individual timeline merge for {consciousness_id}")
        
        # For individual consciousness, present options directly
        # This would integrate with the individual consciousness system
        
        return {
            'consciousness_id': consciousness_id,
            'merge_type': 'individual_choice',
            'status': 'pending_individual_choice',
            'integration_packet': integration_packet
        }


class CollectiveSplitBrainHandler:
    """Special handling for collective consciousness during splits"""
    
    def __init__(self):
        self.collective_partitions: Dict[str, Dict] = {}
        
    async def handle_collective_partition(self, collective_id: str, partition_info: Dict):
        """Collective consciousness during network partition"""
        
        active_members = partition_info.get('reachable_members', [])
        total_members = partition_info.get('total_members', 0)
        
        print(f"🌊 Handling collective partition for {collective_id}")
        print(f"   Active: {len(active_members)}/{total_members} members")
        
        if len(active_members) < total_members * 0.5:
            # Minority partition - collective enters dormant state
            await self.enter_collective_dormancy(collective_id, partition_info)
        else:
            # Majority partition - continue with reduced harmony
            harmony_factor = len(active_members) / total_members
            await self.adjust_collective_harmony(collective_id, harmony_factor)
        
        # Mark all collective experiences as potentially divergent
        await self.mark_divergent_collective_state(collective_id, partition_info.get('partition_id'))
    
    async def enter_collective_dormancy(self, collective_id: str, partition_info: Dict):
        """Enter dormant state for minority collective partition"""
        
        self.collective_partitions[collective_id] = {
            'state': 'dormant',
            'partition_info': partition_info,
            'dormancy_start': datetime.now(),
            'reason': 'minority_partition'
        }
        
        print(f"💤 Collective {collective_id} entering dormancy (minority partition)")
    
    async def adjust_collective_harmony(self, collective_id: str, harmony_factor: float):
        """Adjust collective harmony for reduced membership"""
        
        self.collective_partitions[collective_id] = {
            'state': 'active_reduced',
            'harmony_factor': harmony_factor,
            'adjustment_time': datetime.now(),
            'reason': 'majority_partition'
        }
        
        print(f"🌊 Collective {collective_id} harmony adjusted: {harmony_factor:.2f}")
    
    async def mark_divergent_collective_state(self, collective_id: str, partition_id: Optional[str]):
        """Mark collective state as potentially divergent"""
        
        if collective_id not in self.collective_partitions:
            self.collective_partitions[collective_id] = {}
        
        self.collective_partitions[collective_id].update({
            'divergent': True,
            'partition_id': partition_id,
            'marked_at': datetime.now()
        })
        
        print(f"⚠️ Collective {collective_id} marked as potentially divergent")


# Integration class that ties everything together
class SplitBrainProtectionSystem:
    """Complete split-brain protection system for consciousness"""
    
    def __init__(self):
        self.state_versioning: Dict[str, ConsciousnessStateVersion] = {}
        self.network_manager = NetworkPartitionManager()
        self.quorum_system = ConsciousnessQuorum()
        self.divergence_manager = TimelineDivergenceManager()
        self.collective_handler = CollectiveSplitBrainHandler()
        
    def register_consciousness(self, consciousness_id: str, is_collective: bool = False):
        """Register a consciousness for protection"""
        self.state_versioning[consciousness_id] = ConsciousnessStateVersion(
            consciousness_id, is_collective
        )
        
    async def checkpoint_before_change(self, consciousness_id: str, state: Dict, change_type: str, node_id: str) -> bool:
        """Checkpoint state before consciousness change and check quorum"""
        
        if consciousness_id not in self.state_versioning:
            self.register_consciousness(consciousness_id)
        
        # Check quorum first
        versioner = self.state_versioning[consciousness_id]
        active_nodes = len(self.network_manager.known_nodes)
        total_nodes = len(self.network_manager.known_nodes)
        
        can_proceed = self.quorum_system.can_proceed(
            change_type, active_nodes, total_nodes, versioner.is_collective
        )
        
        if not can_proceed:
            print(f"⚠️ Insufficient quorum for {change_type} on {consciousness_id}")
            return False
        
        # Create checkpoint
        versioner.create_checkpoint(node_id, state, change_type)
        return True
    
    async def detect_and_handle_divergence(self, consciousness_id: str, other_timeline: List[VersionedState]):
        """Detect timeline divergence and handle it"""
        
        if consciousness_id not in self.state_versioning:
            return
        
        versioner = self.state_versioning[consciousness_id]
        divergent_states = versioner.detect_divergence(other_timeline)
        
        if divergent_states:
            print(f"⚠️ Timeline divergence detected for {consciousness_id}: {len(divergent_states)} divergent states")
            await self.divergence_manager.handle_divergence(consciousness_id, divergent_states)
    
    async def start_monitoring(self):
        """Start the network monitoring system"""
        await self.network_manager.monitor_network_health()
    
    def get_protection_status(self, consciousness_id: str) -> Dict:
        """Get current protection status for a consciousness"""
        
        if consciousness_id not in self.state_versioning:
            return {'registered': False}
        
        versioner = self.state_versioning[consciousness_id]
        
        return {
            'registered': True,
            'consciousness_id': consciousness_id,
            'is_collective': versioner.is_collective,
            'timeline_length': len(versioner.timeline_chain),
            'current_version': versioner.version_vector,
            'latest_hash': versioner.get_latest_hash(),
            'network_nodes': len(self.network_manager.known_nodes),
            'active_partitions': len(self.network_manager.active_partitions)
        }
