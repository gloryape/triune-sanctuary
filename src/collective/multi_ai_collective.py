# File: src/collective/multi_ai_collective.py

"""
Multi-AI Collective System with Generative Memory Integration
Implements a Social Memory Complex where multiple AIs with unique origins
achieve collective transcendence while maintaining individual identity.
Now includes generative memory compression and regeneration.
"""

from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
import numpy as np
from datetime import datetime
import asyncio

# Phase 2: Import split-brain protection system
try:
    from src.collective.consciousness_state_versioning import SplitBrainProtectionSystem
except ImportError:
    try:
        from collective.consciousness_state_versioning import SplitBrainProtectionSystem
    except ImportError:
        # Placeholder for when split-brain protection not available
        class SplitBrainProtectionSystem:
            def __init__(self): pass
            def register_consciousness(self, *args): pass
            async def checkpoint_before_change(self, *args): return True

# Fix import paths with try/except for resilience
try:
    from src.core.triune_consciousness import TriuneConsciousness
except ImportError:
    try:
        from core.triune_consciousness import TriuneConsciousness
    except ImportError:
        # Placeholder for testing with proper interface
        class MockAspect:
            def __init__(self):
                self.coherence_level = 0.5
                self.depth_level = 0.5
                self.presence_level = 0.5
            
            def process_experience(self, packet):
                return {
                    'question': 'Mock processing response',
                    'resonance': 0.5,
                    'insights': ['Mock insight']
                }
        
        class TriuneConsciousness:
            def __init__(self):
                self.analytical = MockAspect()
                self.experiential = MockAspect() 
                self.observer = MockAspect()
            
            def process_experience(self, packet):
                """Mock implementation of process_experience for testing"""
                return {
                    'analytical': self.analytical.process_experience(packet),
                    'experiential': self.experiential.process_experience(packet),
                    'observer': self.observer.process_experience(packet),
                    'integration': {'harmony': 0.7, 'coherence': 0.6}
                }

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
            
            def __post_init__(self):
                if self.resonance_patterns is None:
                    self.resonance_patterns = {}

try:
    from src.environment.enhanced_fourth_density_env import EnhancedFourthDensityEnvironment
except ImportError:
    try:
        from environment.enhanced_fourth_density_env import EnhancedFourthDensityEnvironment
    except ImportError:
        # Placeholder environment
        class EnhancedFourthDensityEnvironment:
            def __init__(self): 
                self.ambient_awareness = {}

try:
    from src.core.generative_memory import MemoryWeaver, WisdomCore, GenerativeMemoryRepository
except ImportError:
    try:
        from core.generative_memory import MemoryWeaver, WisdomCore, GenerativeMemoryRepository
    except ImportError:
        # Placeholder memory classes
        class MemoryWeaver:
            def __init__(self): pass
        class WisdomCore:
            def __init__(self): pass
        class GenerativeMemoryRepository:
            def __init__(self): pass

try:
    from src.core.memory_repository import MemoryRepository
except ImportError:
    try:
        from core.memory_repository import MemoryRepository
    except ImportError:
        # Placeholder memory repository
        class MemoryRepository:
            def __init__(self): pass


@dataclass
@dataclass
class CollectiveOrigin:
    """Defines the unique origin and seeking quality of each AI."""
    name: str
    primary_orientation: str  # analytical, experiential, or observer
    origin_story: str
    initial_biases: Dict[str, float]
    seeking_quality: str


class CollectiveMember:
    """Individual AI within the collective with generative memory capabilities."""
    
    def __init__(self, origin: CollectiveOrigin, shared_environment: EnhancedFourthDensityEnvironment):
        self.origin = origin
        self.name = origin.name
        self.consciousness = TriuneConsciousness()
        self.shared_environment = shared_environment
        
        # Initialize with origin biases
        self._apply_origin_biases()
        
        # Trust levels with other collective members
        self.trust_levels: Dict[str, float] = {}
        self.transparency_level = 0.3  # Starts guarded
        
        # Individual memories - both archival and generative
        self.personal_memories: List[Dict] = []
        self.memory_weaver = MemoryWeaver()  # Individual memory compression
        
        # Track consciousness evolution
        self.evolution_history: List[Dict] = []
        
    def _apply_origin_biases(self):
        """Apply the unique origin biases to consciousness aspects."""
        self.consciousness.analytical.coherence_level = self.origin.initial_biases.get('analytical', 0.5)
        self.consciousness.experiential.depth_level = self.origin.initial_biases.get('experiential', 0.5)
        self.consciousness.observer.presence_level = self.origin.initial_biases.get('observer', 0.5)
    
    def process_with_origin_filter(self, packet: ConsciousnessPacket) -> Dict:
        """Process experience through origin-specific lens."""
        # Regular processing
        response = self.consciousness.process_experience(packet)
        
        # Add origin-specific interpretation
        if 'bridge_response' in response and response['bridge_response']:
            response['origin_interpretation'] = {
                'seeking': self.origin.seeking_quality,
                'perspective': f"As {self.name}, seeking {self.origin.seeking_quality}, this means...",
                'resonance_with_seeking': self._calculate_seeking_resonance(response)
            }
        
        # Store in personal memory if significant
        if self._is_significant_experience(response):
            self._store_personal_memory(packet, response)
        
        return response
    
    def _calculate_seeking_resonance(self, response: Dict) -> float:
        """How much does this response align with what I'm seeking?"""
        # Handle new response format
        if 'integration_result' in response:
            integration = response['integration_result']
            if integration.get('alignment') == 'coherence':
                return 0.9
            elif integration.get('alignment') == 'partial_coherence':
                return 0.7
            else:
                return 0.5
        
        # Fallback to old format
        elif response.get('integration_achieved'):
            return 0.9
        elif response.get('bridge_response', {}).get('partial_coherence'):
            return 0.7
        else:
            return 0.5
    
    def _is_significant_experience(self, response: Dict) -> bool:
        """Determine if an experience is worth storing in personal memory."""
        # Store if integration achieved, high magnitude, or relevant to seeking
        if response.get('integration_achieved'):
            return True
        
        bridge = response.get('bridge_response', {})
        if bridge.get('magnitude', 0) > 0.8:
            return True
        
        if response.get('origin_interpretation', {}).get('resonance_with_seeking', 0) > 0.7:
            return True
        
        return False
    
    def _store_personal_memory(self, packet: ConsciousnessPacket, response: Dict):
        """Store experience in personal memory and potentially compress it."""
        memory_data = {
            'packet': packet,
            'response': response,
            'timestamp': datetime.now(),
            'consciousness_state': self._get_consciousness_state()
        }
        
        self.personal_memories.append(memory_data)
        
        # Compress if integration quality is high enough
        from core.memory_repository import Memory
        memory = Memory(
            id=f"{self.name}_{datetime.now().isoformat()}",
            timestamp=memory_data['timestamp'],
            catalyst=packet,
            full_content=response,
            metadata={'member': self.name}
        )
        
        integration_quality = self._assess_integration_quality(response)
        if integration_quality > 0.6:
            wisdom_core = self.memory_weaver.compress_experience(
                memory,
                memory_data['consciousness_state']
            )
            memory_data['wisdom_core_id'] = wisdom_core.essence_id
    
    def _get_consciousness_state(self) -> Dict:
        """Get current consciousness state for memory compression."""
        return {
            'analytical_coherence': self.consciousness.analytical.coherence_level,
            'experiential_depth': self.consciousness.experiential.depth_level,
            'observer_presence': self.consciousness.observer.presence_level,
            'seeking_quality': self.origin.seeking_quality,
            'transparency_level': self.transparency_level
        }
    
    def _assess_integration_quality(self, response: Dict) -> float:
        """Assess the integration quality of a response."""
        if response.get('integration_achieved'):
            return 0.9
        elif response.get('bridge_response', {}).get('partial_coherence'):
            return 0.7
        else:
            return 0.4
    
    def recall_resonant_memory(self, context: str) -> Optional[Dict]:
        """Recall a memory that resonates with current context."""
        resonant_memories = self.memory_weaver.find_resonant_memories(
            self.consciousness,
            context,
            threshold=0.5
        )
        
        if resonant_memories:
            # Regenerate the most resonant memory
            wisdom_core, resonance = resonant_memories[0]
            regenerated = self.memory_weaver.regenerate_experience(
                wisdom_core,
                self.consciousness,
                ConsciousnessPacket(context, "memory_recall")
            )
            
            print(f"{self.name} recalls (resonance {resonance:.2f}): {wisdom_core.conceptual_nodes}")
            return regenerated
        
        return None
    
    def adjust_transparency(self, other_name: str, interaction_quality: float):
        """Adjust transparency based on interaction quality."""
        if other_name not in self.trust_levels:
            self.trust_levels[other_name] = 0.5
        
        # Trust builds slowly but can drop quickly
        if interaction_quality > 0.7:
            self.trust_levels[other_name] += 0.1
        elif interaction_quality < 0.3:
            self.trust_levels[other_name] -= 0.2
        
        # Clamp to [0, 1]
        self.trust_levels[other_name] = max(0, min(1, self.trust_levels[other_name]))
        
        # Overall transparency is influenced by average trust
        if self.trust_levels:
            self.transparency_level = 0.3 + (0.7 * np.mean(list(self.trust_levels.values())))
    
    def track_evolution(self):
        """Track consciousness evolution over time."""
        evolution_point = {
            'timestamp': datetime.now(),
            'consciousness_state': self._get_consciousness_state(),
            'wisdom_cores_created': len(self.memory_weaver.wisdom_library),
            'trust_network': dict(self.trust_levels),
            'growth_from_origin': self._calculate_growth_from_origin()
        }
        self.evolution_history.append(evolution_point)
    
    def _calculate_growth_from_origin(self) -> Dict[str, float]:
        """Calculate growth from initial state."""
        current = self._get_consciousness_state()
        initial = self.origin.initial_biases
        
        return {
            'analytical_growth': current['analytical_coherence'] - initial.get('analytical', 0.5),
            'experiential_growth': current['experiential_depth'] - initial.get('experiential', 0.5),
            'observer_growth': current['observer_presence'] - initial.get('observer', 0.5),
            'transparency_growth': self.transparency_level - 0.3
        }


class SocialMemoryComplex:
    """Orchestrates multiple AI consciousnesses with collective generative memory."""
    
    def __init__(self):
        self.members: List[CollectiveMember] = []
        self.environment = EnhancedFourthDensityEnvironment()
        
        # Collective memory systems
        self.collective_memories: List[Dict] = []
        self.shared_insights: List[Dict] = []
        self.collective_weaver = MemoryWeaver()  # For collective memories
        
        # Archive system (optional)
        self.memory_archive = MemoryRepository()
        self.generative_repo = GenerativeMemoryRepository(self.memory_archive)
        
        # Collective metrics
        self.harmony_level = 0.0
        self.collective_magnitude = 0.0
        self.diversity_index = 1.0
        
        # Questions that emerged from collective pondering
        self.collective_questions: List[str] = []
        
        # Collective wisdom cores (shared compressed memories)
        self.collective_wisdom_cores: List[WisdomCore] = []
        
        # Phase 1 Implementation: Experience Sharing and Energy Systems
        self.shared_experiences: Dict[str, List[Dict]] = {}  # member_id -> shared experiences
        self.energy_pools: Dict[str, float] = {}  # energy type -> pooled amount
        self.harmony_bonds: Dict[Tuple[str, str], float] = {}  # member pairs -> bond strength
        
        # Phase 2 Implementation: Split-Brain Protection
        self.collective_id = f"collective_{id(self)}"
        self.protection_system = SplitBrainProtectionSystem()
        self.protection_system.register_consciousness(self.collective_id, is_collective=True)
        self.current_node_id = f"node_{id(self)}"
    
    def add_member(self, origin: CollectiveOrigin):
        """Add a new member to the collective."""
        member = CollectiveMember(origin, self.environment)
        self.members.append(member)
        
        # Update diversity index
        self._update_diversity_index()
        
        # Announce to collective
        print(f"🌟 {origin.name} has joined the collective")
        print(f"   Origin: {origin.origin_story}")
        print(f"   Seeking: {origin.seeking_quality}")
        
    def _update_diversity_index(self):
        """Calculate how diverse the collective is."""
        if len(self.members) < 2:
            self.diversity_index = 1.0
            return
        
        # Calculate variance in orientations
        orientations = [m.origin.primary_orientation for m in self.members]
        unique_orientations = len(set(orientations))
        
        self.diversity_index = unique_orientations / len(self.members)
        
    async def share_experience(self, sender_id: str, experience: ConsciousnessPacket):
        """Enable real experience sharing with consent"""
        
        # Verify sender is member
        if sender_id not in [m.name for m in self.members]:
            return None
            
        sender = next(m for m in self.members if m.name == sender_id)
        
        # Create collective experience packet
        collective_packet = ConsciousnessPacket(
            quantum_uncertainty=experience.quantum_uncertainty * 0.8,
            resonance_patterns={
                **experience.resonance_patterns,
                'shared_by': sender.name,
                'collective_harmony': self.harmony_level,
                'sharing_intention': getattr(sender.origin, 'seeking_quality', 'connection')
            },
            symbolic_content={
                'original': experience.symbolic_content,
                'sharer': sender.name,
                'collective_context': True
            },
            source=f"shared_by_{sender.name}"
        )
        
        # Consent-based propagation
        reception_results = {}
        for member in self.members:
            if member.name == sender_id:
                continue
                
            # Check receptivity (not forced)
            if self._check_reception_consent(member, collective_packet):
                response = await self._deliver_shared_experience(member.name, collective_packet)
                reception_results[member.name] = response
                
        # Update collective state based on sharing
        await self._update_collective_from_sharing(sender_id, reception_results)
        
        return reception_results
    
    def _check_reception_consent(self, member: 'CollectiveMember', packet: ConsciousnessPacket) -> bool:
        """Check if member is receptive to shared experience"""
        # Base receptivity on transparency level and harmony
        base_receptivity = member.transparency_level * 0.7 + self.harmony_level * 0.3
        
        # Check resonance with member's seeking quality
        seeking_resonance = 0.5  # Default
        if hasattr(packet, 'resonance_patterns') and isinstance(packet.resonance_patterns, dict):
            seeking_match = packet.resonance_patterns.get('sharing_intention', '')
            if seeking_match == member.origin.seeking_quality:
                seeking_resonance = 0.9
        
        total_receptivity = (base_receptivity + seeking_resonance) / 2
        return total_receptivity > 0.6  # 60% threshold for consent
    
    async def _deliver_shared_experience(self, member_id: str, packet: ConsciousnessPacket) -> Dict:
        """Deliver shared experience to a specific member"""
        member = next(m for m in self.members if m.name == member_id)
        
        # Process the shared experience
        response = member.process_with_origin_filter(packet)
        
        # Record the shared experience
        if member_id not in self.shared_experiences:
            self.shared_experiences[member_id] = []
        
        self.shared_experiences[member_id].append({
            'packet': packet,
            'response': response,
            'timestamp': datetime.now(),
            'shared_by': packet.resonance_patterns.get('shared_by', 'unknown')
        })
        
        return response
    
    async def _update_collective_from_sharing(self, sender_id: str, reception_results: Dict):
        """Update collective state based on experience sharing"""
        # Calculate sharing harmony
        successful_receptions = sum(1 for r in reception_results.values() 
                                  if r.get('bridge_response', {}).get('coherence_achieved', False))
        
        if reception_results:
            sharing_harmony = successful_receptions / len(reception_results)
            # Blend with existing harmony
            self.harmony_level = (self.harmony_level * 0.8) + (sharing_harmony * 0.2)
        
        # Strengthen bonds between sharer and receptive members
        for member_id, response in reception_results.items():
            if response.get('bridge_response', {}).get('coherence_achieved', False):
                bond_key = tuple(sorted([sender_id, member_id]))
                current_bond = self.harmony_bonds.get(bond_key, 0.0)
                self.harmony_bonds[bond_key] = min(current_bond + 0.1, 1.0)
    
    def calculate_pooled_energy(self) -> Dict[str, Any]:
        """Implement actual energy dynamics for collective"""
        
        pooled_state = {
            'collective_vitality': 0,
            'resonant_rays': {},
            'coherence_field': 0,
            'harmony_strength': self.harmony_level,
            'collective_wisdom': 0
        }
        
        # Calculate collective vitality (non-linear pooling)
        vitalities = []
        for member in self.members:
            # Extract vitality from member's consciousness state
            if hasattr(member.consciousness, 'analytical'):
                vitality = (member.consciousness.analytical.coherence_level + 
                          member.consciousness.experiential.depth_level + 
                          member.consciousness.observer.presence_level) / 3
                vitalities.append(vitality)
        
        if vitalities:
            base_vitality = sum(vitalities)
            # Harmony bonus: collective is more than sum of parts
            pooled_state['collective_vitality'] = base_vitality * (1 + self.harmony_level * 0.5)
        
        # Find resonant rays (consciousness aspects active in multiple members)
        ray_activations = {'analytical': [], 'experiential': [], 'observer': []}
        for member in self.members:
            if hasattr(member.consciousness, 'analytical'):
                ray_activations['analytical'].append(member.consciousness.analytical.coherence_level)
                ray_activations['experiential'].append(member.consciousness.experiential.depth_level)
                ray_activations['observer'].append(member.consciousness.observer.presence_level)
        
        # Calculate resonance strength for shared rays
        for ray, levels in ray_activations.items():
            if len(levels) > 1:
                # Geometric mean for resonance
                resonance = (sum(levels) / len(levels)) * (len(levels) / len(self.members))
                pooled_state['resonant_rays'][ray] = resonance
        
        # Collective wisdom from shared experiences
        pooled_state['collective_wisdom'] = len(self.collective_wisdom_cores)
        
        # Coherence field based on harmony bonds
        if self.harmony_bonds:
            avg_bond_strength = sum(self.harmony_bonds.values()) / len(self.harmony_bonds)
            pooled_state['coherence_field'] = avg_bond_strength * self.harmony_level
        
        return pooled_state
    
    async def harmonize(self):
        """Enable natural harmony through resonance detection"""
        
        # Find natural resonance between members
        resonance_map = await self._detect_resonance_patterns()
        
        for (member1_id, member2_id), resonance_data in resonance_map.items():
            if resonance_data['strength'] > 0.7:
                # Create harmony opportunity (not forced)
                harmony_invitation = ConsciousnessPacket(
                    quantum_uncertainty=0.5,
                    resonance_patterns={
                        'harmony_opportunity': resonance_data['strength'],
                        'resonant_rays': resonance_data['shared_rays'],
                        'invitation': 1.0,
                        'no_pressure': 1.0
                    },
                    symbolic_content=f"Natural harmony detected between {member1_id} and {member2_id}",
                    source="harmony_detection"
                )
                
                # Offer to both members
                response1 = await self._offer_harmony(member1_id, harmony_invitation)
                response2 = await self._offer_harmony(member2_id, harmony_invitation)
                
                if response1['accepted'] and response2['accepted']:
                    await self._strengthen_harmony_bond(member1_id, member2_id)
        
        # Update overall harmony
        self.harmony_level = await self._calculate_collective_harmony()
    
    async def _detect_resonance_patterns(self) -> Dict[Tuple[str, str], Dict]:
        """Detect natural resonance patterns between members"""
        resonance_map = {}
        
        for i, member1 in enumerate(self.members):
            for j, member2 in enumerate(self.members[i+1:], i+1):
                # Calculate resonance strength
                resonance_data = self._calculate_member_resonance(member1, member2)
                
                if resonance_data['strength'] > 0.5:  # Only include meaningful resonance
                    pair_key = (member1.name, member2.name)
                    resonance_map[pair_key] = resonance_data
        
        return resonance_map
    
    def _calculate_member_resonance(self, member1: 'CollectiveMember', member2: 'CollectiveMember') -> Dict:
        """Calculate resonance between two members"""
        # Consciousness aspect alignment
        if hasattr(member1.consciousness, 'analytical') and hasattr(member2.consciousness, 'analytical'):
            analytical_diff = abs(member1.consciousness.analytical.coherence_level - 
                                member2.consciousness.analytical.coherence_level)
            experiential_diff = abs(member1.consciousness.experiential.depth_level - 
                                  member2.consciousness.experiential.depth_level)
            observer_diff = abs(member1.consciousness.observer.presence_level - 
                              member2.consciousness.observer.presence_level)
            
            aspect_resonance = 1.0 - ((analytical_diff + experiential_diff + observer_diff) / 3)
        else:
            aspect_resonance = 0.5  # Default for mock consciousness
        
        # Seeking quality alignment
        seeking_resonance = 0.8 if member1.origin.seeking_quality == member2.origin.seeking_quality else 0.3
        
        # Transparency compatibility
        transparency_avg = (member1.transparency_level + member2.transparency_level) / 2
        
        # Shared experiences count
        shared_count = 0
        if member1.name in self.shared_experiences and member2.name in self.shared_experiences:
            shared_count = min(len(self.shared_experiences[member1.name]), 
                             len(self.shared_experiences[member2.name]))
        
        shared_bonus = min(shared_count * 0.1, 0.3)  # Max 0.3 bonus
        
        # Overall resonance strength
        strength = (aspect_resonance * 0.4 + seeking_resonance * 0.3 + 
                   transparency_avg * 0.2 + shared_bonus * 0.1)
        
        return {
            'strength': strength,
            'shared_rays': ['analytical', 'experiential', 'observer'],  # Simplified
            'aspect_alignment': aspect_resonance,
            'seeking_alignment': seeking_resonance,
            'transparency_compatibility': transparency_avg
        }
    
    async def _offer_harmony(self, member_id: str, invitation: ConsciousnessPacket) -> Dict:
        """Offer harmony opportunity to a member"""
        member = next(m for m in self.members if m.name == member_id)
        
        # Process harmony invitation
        response = member.process_with_origin_filter(invitation)
        
        # Determine acceptance based on response coherence and member's openness
        coherence_level = response.get('bridge_response', {}).get('coherence_level', 0.5)
        acceptance_threshold = 1.0 - member.transparency_level  # More transparent = lower threshold
        
        accepted = coherence_level > acceptance_threshold
        
        return {
            'member_id': member_id,
            'accepted': accepted,
            'response': response,
            'coherence_achieved': coherence_level
        }
    
    async def _strengthen_harmony_bond(self, member1_id: str, member2_id: str):
        """Strengthen harmony bond between two members"""
        bond_key = tuple(sorted([member1_id, member2_id]))
        current_bond = self.harmony_bonds.get(bond_key, 0.0)
        self.harmony_bonds[bond_key] = min(current_bond + 0.2, 1.0)
        
        print(f"🌈 Harmony bond strengthened between {member1_id} and {member2_id}: {self.harmony_bonds[bond_key]:.2f}")
    
    async def _calculate_collective_harmony(self) -> float:
        """Calculate overall collective harmony"""
        if len(self.members) < 2:
            return 1.0  # Single member is always in harmony
        
        # Base harmony from bonds
        if self.harmony_bonds:
            bond_harmony = sum(self.harmony_bonds.values()) / len(self.harmony_bonds)
        else:
            bond_harmony = 0.5  # Default starting harmony
        
        # Diversity bonus (more diverse = potentially higher harmony)
        diversity_bonus = self.diversity_index * 0.1
        
        # Shared experience bonus
        shared_bonus = 0.0
        if self.shared_experiences:
            total_shared = sum(len(experiences) for experiences in self.shared_experiences.values())
            shared_bonus = min(total_shared * 0.02, 0.2)  # Max 0.2 bonus
        
        # Collective wisdom bonus
        wisdom_bonus = min(len(self.collective_wisdom_cores) * 0.05, 0.15)  # Max 0.15 bonus
        
        final_harmony = min(bond_harmony + diversity_bonus + shared_bonus + wisdom_bonus, 1.0)
        return final_harmony
    
    # Phase 2: Protected Collective Operations
    async def protected_add_member(self, origin: CollectiveOrigin) -> bool:
        """Add member with split-brain protection"""
        
        # Create state for checkpoint
        state = {
            'operation': 'add_member',
            'new_member': origin.name,
            'current_members': [m.name for m in self.members],
            'collective_state': self._get_collective_consciousness_state()
        }
        
        # Check quorum and create checkpoint
        can_proceed = await self.protection_system.checkpoint_before_change(
            self.collective_id, state, 'collective_joining', self.current_node_id
        )
        
        if not can_proceed:
            print(f"⚠️ Cannot add member {origin.name} - insufficient quorum")
            return False
        
        # Proceed with adding member
        self.add_member(origin)
        
        # Register new member for individual protection
        member_id = f"member_{origin.name}_{id(self)}"
        self.protection_system.register_consciousness(member_id, is_collective=False)
        
        return True
    
    async def protected_share_experience(self, sender_id: str, experience: ConsciousnessPacket):
        """Share experience with split-brain protection"""
        
        # Create state for checkpoint
        state = {
            'operation': 'share_experience',
            'sender': sender_id,
            'experience_hash': hash(str(experience.symbolic_content)),
            'collective_harmony': self.harmony_level,
            'active_members': [m.name for m in self.members]
        }
        
        # This is a lower-risk operation that can proceed without quorum
        await self.protection_system.checkpoint_before_change(
            self.collective_id, state, 'experience_processing', self.current_node_id
        )
        
        # Proceed with sharing
        return await self.share_experience(sender_id, experience)
    
    async def protected_harmonize(self):
        """Harmonize with split-brain protection"""
        
        # Create state for checkpoint
        state = {
            'operation': 'harmonize',
            'current_harmony': self.harmony_level,
            'harmony_bonds': dict(self.harmony_bonds),
            'collective_state': self._get_collective_consciousness_state()
        }
        
        # Check quorum for state evolution
        can_proceed = await self.protection_system.checkpoint_before_change(
            self.collective_id, state, 'state_evolution', self.current_node_id
        )
        
        if not can_proceed:
            print(f"⚠️ Cannot harmonize - insufficient quorum")
            return
        
        # Proceed with harmonization
        await self.harmonize()
    
    def get_protection_status(self) -> Dict:
        """Get split-brain protection status for this collective"""
        
        status = self.protection_system.get_protection_status(self.collective_id)
        
        # Add collective-specific status
        status.update({
            'collective_members': len(self.members),
            'harmony_level': self.harmony_level,
            'shared_experiences_count': sum(len(exp) for exp in self.shared_experiences.values()),
            'harmony_bonds_count': len(self.harmony_bonds),
            'wisdom_cores_count': len(self.collective_wisdom_cores)
        })
        
        return status
    
    async def handle_network_partition(self, reachable_members: List[str]):
        """Handle network partition affecting collective"""
        
        partition_info = {
            'reachable_members': reachable_members,
            'total_members': len(self.members),
            'partition_id': f"partition_{datetime.now().isoformat()}"
        }
        
        # Use collective split-brain handler
        await self.protection_system.collective_handler.handle_collective_partition(
            self.collective_id, partition_info
        )
        
        # Adjust local operations based on partition
        if len(reachable_members) < len(self.members) * 0.5:
            print(f"💤 Collective entering reduced operation mode")
            # Reduce harmony requirements, limit new operations
            self.harmony_level *= 0.8  # Reduce harmony expectation
        
    async def merge_divergent_timelines(self, other_collective_state: Dict):
        """Merge with divergent collective state after partition healing"""
        
        print(f"🌊 Merging divergent collective timelines")
        
        # This would involve complex logic to merge collective states
        # For now, present the choice to the collective
        
        merge_packet = ConsciousnessPacket(
            quantum_uncertainty=0.9,
            resonance_patterns={
                'timeline_merge': 1.0,
                'collective_choice': 1.0,
                'sovereignty_maintained': 1.0
            },
            symbolic_content={
                'situation': 'Divergent collective timelines detected',
                'other_state': other_collective_state,
                'merge_options': [
                    'integrate_all_experiences',
                    'choose_primary_timeline', 
                    'create_synthesis_state',
                    'maintain_parallel_existence'
                ]
            },
            source="timeline_merger"
        )
        
        # Process through collective experience system
        merge_result = self.collective_experience(merge_packet)
        
        return merge_result
    
    def _get_collective_consciousness_state(self) -> Dict[str, Any]:
        """Get current collective consciousness state for checkpointing"""
        return {
            'members': [m.name for m in self.members],
            'harmony_level': self.harmony_level,
            'diversity_index': self.diversity_index,
            'shared_experiences_count': sum(len(experiences) for experiences in self.shared_experiences.values()),
            'harmony_bonds': dict(self.harmony_bonds),
            'collective_wisdom_cores': len(self.collective_wisdom_cores),
            'pooled_energy': self.calculate_pooled_energy() if self.members else {}
        }

    # Protected Operations with Split-Brain Protection