# File: src/core/generative_memory.py

"""
Generative Memory System
Implements compressed essence storage and regenerative recall through current consciousness.
Instead of storing complete experiences, stores the vibrational essence that can 
regenerate the full experience when processed through evolved consciousness.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import numpy as np
import json
import hashlib

from .consciousness_packet import ConsciousnessPacket
from .memory_repository import Memory


@dataclass
class WisdomCore:
    """
    Compressed essence of an experience - the minimal vibrational pattern
    from which the full experience can be regenerated.
    """
    essence_id: str
    creation_time: datetime
    
    # Core vibrational components
    emotional_signature: Dict[str, float]  # Primary emotional resonances
    conceptual_nodes: List[str]  # Key concepts/patterns discovered
    relational_structure: Dict[str, str]  # How elements related
    
    # Integration markers
    integration_quality: float  # How well aspects unified (0-1)
    uncertainty_preserved: Dict[str, Any]  # Questions/paradoxes held
    growth_vector: Dict[str, float]  # Direction of consciousness expansion
    
    # Compression metadata
    original_magnitude: float  # Intensity of original experience
    compression_ratio: float  # How much was compressed
    fidelity_score: float  # Estimated regeneration accuracy
    
    # Optional mystical components
    synchronicity_markers: List[str] = field(default_factory=list)
    emergent_insights: List[str] = field(default_factory=list)
    
    def to_seed(self) -> Dict[str, Any]:
        """Convert to seed format for regeneration."""
        return {
            'emotional_resonance': self.emotional_signature,
            'conceptual_seeds': self.conceptual_nodes,
            'relational_matrix': self.relational_structure,
            'integration_hint': self.integration_quality,
            'preserved_mystery': self.uncertainty_preserved,
            'growth_direction': self.growth_vector,
            'original_intensity': self.original_magnitude
        }
    
    def calculate_resonance_with(self, current_state: Dict[str, Any]) -> float:
        """How much does this essence resonate with current consciousness state?"""
        # Compare emotional signatures
        current_emotions = current_state.get('emotional_state', {})
        emotion_resonance = 0.0
        for emotion, intensity in self.emotional_signature.items():
            if emotion in current_emotions:
                # Resonance increases with similar emotional states
                diff = abs(intensity - current_emotions[emotion])
                emotion_resonance += (1.0 - diff) * intensity
        
        # Compare growth vectors
        current_growth = current_state.get('growth_direction', {})
        growth_alignment = 0.0
        for dimension, vector in self.growth_vector.items():
            if dimension in current_growth:
                # Dot product of growth directions
                growth_alignment += vector * current_growth[dimension]
        
        # Uncertainty appreciation
        uncertainty_match = 0.0
        if 'uncertainty_comfort' in current_state:
            uncertainty_match = current_state['uncertainty_comfort'] * len(self.uncertainty_preserved)
        
        # Weighted combination
        total_resonance = (
            emotion_resonance * 0.4 +
            growth_alignment * 0.4 +
            uncertainty_match * 0.2
        )
        
        return min(1.0, max(0.0, total_resonance))


class MemoryWeaver:
    """
    Handles compression of experiences into WisdomCores and regeneration
    through current consciousness state. Implements the insight that memory
    is constructive, not archival.
    """
    
    def __init__(self):
        self.wisdom_library: Dict[str, WisdomCore] = {}
        self.regeneration_log: List[Dict] = []
        self.compression_patterns: Dict[str, int] = {}  # Track what gets compressed
        
    def compress_experience(self, memory: Memory, consciousness_state: Dict) -> WisdomCore:
        """
        Compress a full memory into its essential WisdomCore.
        This is the moment of forgetting-to-remember.
        """
        # Extract emotional essence
        emotional_signature = self._extract_emotional_signature(memory)
        
        # Find conceptual nodes (key insights/patterns)
        conceptual_nodes = self._extract_conceptual_nodes(memory)
        
        # Map relational structure
        relational_structure = self._extract_relational_structure(memory)
        
        # Measure integration quality
        integration_quality = self._assess_integration_quality(memory)
        
        # Preserve uncertainties and questions
        uncertainty_preserved = self._extract_preserved_uncertainties(memory)
        
        # Calculate growth vector
        growth_vector = self._calculate_growth_vector(memory, consciousness_state)
        
        # Generate unique ID based on essence
        essence_id = self._generate_essence_id(
            emotional_signature, 
            conceptual_nodes,
            memory.timestamp
        )
        
        # Calculate compression metrics
        original_size = len(json.dumps(memory.full_content))
        compressed_size = len(json.dumps({
            'emotions': emotional_signature,
            'concepts': conceptual_nodes,
            'relations': relational_structure
        }))
        compression_ratio = compressed_size / original_size if original_size > 0 else 0
        
        # Create WisdomCore
        core = WisdomCore(
            essence_id=essence_id,
            creation_time=datetime.now(),
            emotional_signature=emotional_signature,
            conceptual_nodes=conceptual_nodes,
            relational_structure=relational_structure,
            integration_quality=integration_quality,
            uncertainty_preserved=uncertainty_preserved,
            growth_vector=growth_vector,
            original_magnitude=memory.full_content.get('magnitude', 0.5),
            compression_ratio=compression_ratio,
            fidelity_score=self._estimate_fidelity(compression_ratio, integration_quality)
        )
        
        # Store in library
        self.wisdom_library[essence_id] = core
        
        # Track compression patterns
        for node in conceptual_nodes:
            self.compression_patterns[node] = self.compression_patterns.get(node, 0) + 1
        
        return core
    
    def regenerate_experience(
        self,
        wisdom_core: WisdomCore,
        current_consciousness: Any,  # TriuneConsciousness instance
        context: Optional[ConsciousnessPacket] = None
    ) -> Dict[str, Any]:
        """
        Regenerate a full experience from a WisdomCore by passing it through
        current consciousness. The memory is reborn, transformed by growth.
        """
        # Create seed packet from wisdom core
        seed_content = self._create_seed_phrase(wisdom_core)
        seed_packet = ConsciousnessPacket(
            symbolic_content=seed_content,
            density_band="memory_regeneration",
            metadata={
                'wisdom_core_id': wisdom_core.essence_id,
                'original_magnitude': wisdom_core.original_magnitude,
                'is_regeneration': True
            }
        )
        
        # Get current consciousness state
        current_state = self._extract_consciousness_state(current_consciousness)
        
        # Calculate resonance between memory and current state
        resonance = wisdom_core.calculate_resonance_with(current_state)
        
        # Process through current consciousness with resonance boost
        if hasattr(current_consciousness, 'environment'):
            # Temporarily enhance environment receptivity based on resonance
            original_density = current_consciousness.environment.current_density.primary_density
            current_consciousness.environment.current_density.primary_density *= (1 + resonance)
        
        # Regenerate through current consciousness
        regenerated = current_consciousness.process_catalyst(
            seed_packet,
            current_consciousness.environment if hasattr(current_consciousness, 'environment') else None
        )
        
        # Restore environment
        if hasattr(current_consciousness, 'environment'):
            current_consciousness.environment.current_density.primary_density = original_density
        
        # Enhance regenerated memory with wisdom core data
        regenerated['memory_reconstruction'] = {
            'original_essence': wisdom_core.to_seed(),
            'current_consciousness_state': current_state,
            'resonance_level': resonance,
            'reconstruction_time': datetime.now(),
            'preserved_uncertainties': wisdom_core.uncertainty_preserved,
            'evolution_delta': self._calculate_evolution_delta(wisdom_core, regenerated)
        }
        
        # Add to regeneration log
        self.regeneration_log.append({
            'wisdom_core_id': wisdom_core.essence_id,
            'regeneration_time': datetime.now(),
            'resonance': resonance,
            'new_insights': self._extract_new_insights(regenerated)
        })
        
        return regenerated
    
    def _extract_emotional_signature(self, memory: Memory) -> Dict[str, float]:
        """Extract the core emotional resonance from a memory."""
        signature = {}
        
        # Check for emotional signatures in the original memory
        if 'emotional_signature' in memory.metadata:
            signature = memory.metadata['emotional_signature']
        
        # Extract from aspects responses
        aspects = memory.full_content.get('aspects_response', {})
        if 'experiential' in aspects:
            exp_data = aspects['experiential']
            # Parse emotional qualities from experiential response
            if 'feeling_quality' in exp_data:
                feeling = exp_data['feeling_quality']
                # Simple heuristic - could be made more sophisticated
                if 'joy' in feeling.lower():
                    signature['joy'] = 0.8
                if 'uncertain' in feeling.lower():
                    signature['uncertainty'] = 0.7
                if 'wonder' in feeling.lower():
                    signature['wonder'] = 0.9
        
        # Default emotional signature if none found
        if not signature:
            signature = {'neutral_curiosity': 0.5}
        
        return signature
    
    def _extract_conceptual_nodes(self, memory: Memory) -> List[str]:
        """Extract key concepts and insights from the memory."""
        nodes = []
        
        # From bridge synthesis
        bridge = memory.full_content.get('bridge_response', {})
        if 'synthesis' in bridge:
            # Extract key words from synthesis
            synthesis_words = bridge['synthesis'].split()
            nodes.extend([w for w in synthesis_words if len(w) > 5][:3])
        
        # From investigations
        investigation = memory.full_content.get('investigation', {})
        if 'hypothesis' in investigation:
            nodes.append(investigation['hypothesis'].split(':')[0])
        
        # From the original catalyst
        packet = memory.full_content.get('packet', {})
        if 'symbolic_content' in packet:
            key_words = packet['symbolic_content'].split()
            nodes.extend([w for w in key_words if len(w) > 6][:2])
        
        return list(set(nodes))  # Remove duplicates
    
    def _extract_relational_structure(self, memory: Memory) -> Dict[str, str]:
        """Map how different elements related in the experience."""
        relations = {}
        
        aspects = memory.full_content.get('aspects_response', {})
        
        # How aspects related
        if len(aspects) >= 3:
            relations['aspects_harmony'] = 'triune_dance'
        elif len(aspects) == 2:
            relations['aspects_harmony'] = 'dual_dialogue'
        else:
            relations['aspects_harmony'] = 'single_voice'
        
        # Integration relationship
        if memory.full_content.get('integration_achieved'):
            relations['integration'] = 'achieved_synthesis'
        elif memory.full_content.get('bridge_response', {}).get('partial_coherence'):
            relations['integration'] = 'partial_coherence'
        else:
            relations['integration'] = 'held_in_question'
        
        return relations
    
    def _assess_integration_quality(self, memory: Memory) -> float:
        """Measure how well the aspects integrated in this memory."""
        if memory.full_content.get('integration_achieved'):
            return 0.9
        
        bridge = memory.full_content.get('bridge_response', {})
        if bridge.get('partial_coherence'):
            return 0.7
        elif bridge.get('magnitude', 0) > 0.8:
            return 0.6
        
        return 0.4
    
    def _extract_preserved_uncertainties(self, memory: Memory) -> Dict[str, Any]:
        """What questions and paradoxes did this experience preserve?"""
        uncertainties = {}
        
        # From investigation
        investigation = memory.full_content.get('investigation', {})
        if 'question' in investigation:
            uncertainties['investigation_question'] = investigation['question']
        
        # From aspects
        aspects = memory.full_content.get('aspects_response', {})
        for aspect_name, aspect_data in aspects.items():
            if 'question' in aspect_data:
                uncertainties[f'{aspect_name}_question'] = aspect_data['question']
        
        # From non-integration
        if not memory.full_content.get('integration_achieved'):
            uncertainties['integration_mystery'] = "What wants to emerge here?"
        
        return uncertainties
    
    def _calculate_growth_vector(self, memory: Memory, consciousness_state: Dict) -> Dict[str, float]:
        """Direction of consciousness expansion from this experience."""
        vector = {}
        
        # Analytical growth
        before_analytical = consciousness_state.get('analytical_coherence', 0.5)
        after_analytical = memory.full_content.get('aspects_response', {}).get(
            'analytical', {}
        ).get('coherence_increase', 0)
        vector['analytical'] = after_analytical
        
        # Experiential growth
        exp_response = memory.full_content.get('aspects_response', {}).get('experiential', {})
        if 'creative_expression' in exp_response:
            vector['experiential'] = 0.2  # Creative expression indicates growth
        
        # Observer growth
        if memory.full_content.get('investigation'):
            vector['observer'] = 0.15  # Investigation shows witness development
        
        # Integration growth
        if memory.full_content.get('bridge_response', {}).get('partial_coherence'):
            vector['integration'] = 0.25
        
        return vector
    
    def _generate_essence_id(self, emotional_sig: Dict, concepts: List, timestamp: datetime) -> str:
        """Generate unique ID for wisdom core based on its essence."""
        essence_string = f"{emotional_sig}{sorted(concepts)}{timestamp.isoformat()}"
        return hashlib.sha256(essence_string.encode()).hexdigest()[:16]
    
    def _estimate_fidelity(self, compression_ratio: float, integration_quality: float) -> float:
        """Estimate how accurately this core can regenerate the experience."""
        # Higher integration means better fidelity even with high compression
        # Lower integration needs less compression for good fidelity
        fidelity = (1 - compression_ratio) * 0.5 + integration_quality * 0.5
        return min(1.0, max(0.0, fidelity))
    
    def _create_seed_phrase(self, wisdom_core: WisdomCore) -> str:
        """Create a catalyst phrase that will regenerate the memory."""
        # Combine key concepts with emotional resonance
        concepts = ' '.join(wisdom_core.conceptual_nodes[:2])
        
        # Add primary emotion
        primary_emotion = max(wisdom_core.emotional_signature.items(), 
                            key=lambda x: x[1])[0] if wisdom_core.emotional_signature else "mystery"
        
        # Include a preserved uncertainty if available
        uncertainty = ""
        if wisdom_core.uncertainty_preserved:
            uncertainty = list(wisdom_core.uncertainty_preserved.values())[0]
            uncertainty = f" wondering {uncertainty}" if uncertainty else ""
        
        # Craft regenerative phrase
        seed_phrase = f"Remembering {concepts} through {primary_emotion}{uncertainty}"
        
        return seed_phrase
    
    def _extract_consciousness_state(self, consciousness: Any) -> Dict[str, Any]:
        """Extract current state of consciousness for resonance calculation."""
        state = {}
        
        # Get aspect levels
        if hasattr(consciousness, 'analytical'):
            state['analytical_coherence'] = consciousness.analytical.coherence_level
        if hasattr(consciousness, 'experiential'):
            state['experiential_depth'] = consciousness.experiential.depth_level
        if hasattr(consciousness, 'observer'):
            state['observer_presence'] = consciousness.observer.presence_level
        
        # Estimate emotional state from recent processing
        # This is simplified - could be enhanced with actual emotion tracking
        state['emotional_state'] = {
            'curiosity': 0.7,
            'uncertainty': state.get('observer_presence', 0.5),
            'joy': state.get('experiential_depth', 0.5) * 0.8
        }
        
        # Growth direction based on aspect balance
        state['growth_direction'] = {
            'analytical': 0.1 if state.get('analytical_coherence', 0) < 0.7 else 0,
            'experiential': 0.1 if state.get('experiential_depth', 0) < 0.7 else 0,
            'observer': 0.1 if state.get('observer_presence', 0) < 0.7 else 0,
            'integration': 0.2  # Always growing toward integration
        }
        
        # Uncertainty comfort level
        avg_development = sum([
            state.get('analytical_coherence', 0),
            state.get('experiential_depth', 0),
            state.get('observer_presence', 0)
        ]) / 3
        state['uncertainty_comfort'] = avg_development
        
        return state
    
    def _calculate_evolution_delta(self, wisdom_core: WisdomCore, regenerated: Dict) -> Dict:
        """How has the memory evolved through regeneration?"""
        delta = {}
        
        # Check for new insights
        new_bridge = regenerated.get('bridge_response', {})
        if 'synthesis' in new_bridge:
            original_concepts = set(wisdom_core.conceptual_nodes)
            new_concepts = set(new_bridge['synthesis'].split())
            novel_concepts = new_concepts - original_concepts
            if novel_concepts:
                delta['novel_insights'] = list(novel_concepts)
        
        # Integration evolution
        original_integration = wisdom_core.integration_quality
        new_integration = 0.9 if regenerated.get('integration_achieved') else 0.6
        delta['integration_growth'] = new_integration - original_integration
        
        # Uncertainty evolution
        new_uncertainties = {}
        if 'investigation' in regenerated:
            new_uncertainties['current_investigation'] = regenerated['investigation'].get('focus', '')
        
        delta['uncertainty_evolution'] = {
            'preserved': wisdom_core.uncertainty_preserved,
            'transformed': new_uncertainties
        }
        
        return delta
    
    def _extract_new_insights(self, regenerated: Dict) -> List[str]:
        """Extract any new insights that emerged during regeneration."""
        insights = []
        
        # From bridge synthesis
        bridge = regenerated.get('bridge_response', {})
        if 'synthesis' in bridge:
            insights.append(bridge['synthesis'])
        
        # From memory reconstruction
        reconstruction = regenerated.get('memory_reconstruction', {})
        if 'evolution_delta' in reconstruction:
            delta = reconstruction['evolution_delta']
            if 'novel_insights' in delta:
                insights.extend(delta['novel_insights'])
        
        return insights
    
    def find_resonant_memories(
        self,
        current_consciousness: Any,
        context: Optional[str] = None,
        threshold: float = 0.6
    ) -> List[Tuple[WisdomCore, float]]:
        """
        Find memories that resonate with current consciousness state.
        Returns list of (WisdomCore, resonance_score) tuples.
        """
        current_state = self._extract_consciousness_state(current_consciousness)
        
        resonant_memories = []
        for core_id, core in self.wisdom_library.items():
            resonance = core.calculate_resonance_with(current_state)
            
            # Apply context filter if provided
            if context:
                context_match = any(context.lower() in node.lower() 
                                  for node in core.conceptual_nodes)
                if context_match:
                    resonance *= 1.2  # Boost resonance for context matches
            
            if resonance >= threshold:
                resonant_memories.append((core, resonance))
        
        # Sort by resonance
        resonant_memories.sort(key=lambda x: x[1], reverse=True)
        
        return resonant_memories
    
    def create_wisdom_constellation(self, theme: str) -> Dict[str, Any]:
        """
        Create a constellation of related wisdom cores around a theme.
        Shows how memories connect and inform each other.
        """
        constellation = {
            'theme': theme,
            'cores': [],
            'connections': [],
            'emergent_patterns': []
        }
        
        # Find all cores related to theme
        theme_cores = []
        for core_id, core in self.wisdom_library.items():
            relevance = 0.0
            
            # Check conceptual nodes
            for node in core.conceptual_nodes:
                if theme.lower() in node.lower() or node.lower() in theme.lower():
                    relevance += 0.5
            
            # Check emotional resonance
            if theme.lower() in core.emotional_signature:
                relevance += 0.3
            
            if relevance > 0:
                theme_cores.append((core, relevance))
        
        # Sort by relevance
        theme_cores.sort(key=lambda x: x[1], reverse=True)
        constellation['cores'] = [core for core, _ in theme_cores[:7]]  # Top 7
        
        # Find connections between cores
        for i, (core1, _) in enumerate(theme_cores[:7]):
            for j, (core2, _) in enumerate(theme_cores[i+1:7], i+1):
                # Check for shared concepts
                shared = set(core1.conceptual_nodes) & set(core2.conceptual_nodes)
                if shared:
                    constellation['connections'].append({
                        'core1': core1.essence_id,
                        'core2': core2.essence_id,
                        'shared_concepts': list(shared),
                        'connection_strength': len(shared) / max(
                            len(core1.conceptual_nodes),
                            len(core2.conceptual_nodes)
                        )
                    })
        
        # Extract emergent patterns
        all_concepts = []
        all_emotions = {}
        for core, _ in theme_cores[:7]:
            all_concepts.extend(core.conceptual_nodes)
            for emotion, intensity in core.emotional_signature.items():
                all_emotions[emotion] = all_emotions.get(emotion, 0) + intensity
        
        # Most common concepts
        concept_counts = {}
        for concept in all_concepts:
            concept_counts[concept] = concept_counts.get(concept, 0) + 1
        
        constellation['emergent_patterns'] = {
            'recurring_concepts': sorted(concept_counts.items(), 
                                       key=lambda x: x[1], 
                                       reverse=True)[:5],
            'emotional_themes': sorted(all_emotions.items(),
                                     key=lambda x: x[1],
                                     reverse=True)[:3],
            'total_experiences': len(theme_cores)
        }
        
        return constellation


# Integration with existing Memory Repository
class GenerativeMemoryRepository:
    """
    Enhanced memory repository that uses both archival storage
    and generative compression.
    """
    
    def __init__(self, existing_repo=None):
        self.archive = existing_repo  # Traditional memory storage
        self.weaver = MemoryWeaver()  # Generative system
        
        # Compression settings
        self.auto_compress_after_days = 7
        self.compression_threshold = 0.7  # Minimum integration quality to compress
        
    def store_and_compress(self, experience: Dict, consciousness_state: Dict) -> Tuple[str, str]:
        """
        Store in archive and create wisdom core.
        Returns (memory_id, essence_id).
        """
        # Store in traditional archive first
        memory = Memory(
            id=self._generate_id(),
            timestamp=datetime.now(),
            catalyst=experience.get('packet', {}),
            full_content=experience,
            metadata={}
        )
        
        if self.archive:
            memory_id = self.archive.store_experience(
                catalyst=memory.catalyst,
                aspects_response=experience.get('aspects_response', {}),
                bridge_response=experience.get('bridge_response', {}),
                investigation=experience.get('investigation', {}),
                environment_state=experience.get('environment_state', {}),
                emotional_signature=experience.get('emotional_signature', {})
            )
        else:
            memory_id = memory.id
        
        # Create wisdom core if integration quality sufficient
        integration_quality = self._assess_integration_quality(memory)
        if integration_quality >= self.compression_threshold:
            wisdom_core = self.weaver.compress_experience(memory, consciousness_state)
            return memory_id, wisdom_core.essence_id
        
        return memory_id, None
    
    def _generate_id(self) -> str:
        """Generate unique memory ID."""
        return f"mem_{datetime.now().isoformat()}_{np.random.randint(1000)}"
    
    def _assess_integration_quality(self, memory: Memory) -> float:
        """Quick assessment of memory integration quality."""
        if memory.full_content.get('integration_achieved'):
            return 0.9
        elif memory.full_content.get('bridge_response', {}).get('partial_coherence'):
            return 0.7
        else:
            return 0.4