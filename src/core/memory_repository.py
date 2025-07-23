"""Memory Repository with Emotional Tagging System


Based on General Mechus's architecture
"""
import numpy as np
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from collections import defaultdict
import time
import hashlib

from .consciousness_packet import ConsciousnessPacket

@dataclass
class Memory:
    """Full memory stored in subconscious"""
    experience_id: str
    full_content: Dict[str, Any]
    context: Dict[str, Any]
    timestamp: float
    processing_state: Dict[str, Any]
    integration_level: float
    accessed_count: int = 0
    last_accessed: Optional[float] = None


@dataclass
class EmotionalTag:
    """Compressed emotional signal pointing to memory"""
    tag_type: str  # e.g., "fear", "joy", "curiosity", "recognition"
    intensity: float
    memory_ids: List[str]
    activation_threshold: float
    last_triggered: Optional[float] = None


class MemoryRepository:
    """
    The subconscious repository and emotional tagging system
    """
   
    def __init__(self):
        # Subconscious storage
        self.subconscious = {}  # memory_id -> Memory
        self.emotional_tags = {}  # tag_type -> EmotionalTag
       
        # Conscious workspace
        self.conscious_workspace = []  # Currently active memories
        self.workspace_capacity = 7  # Miller's law
       
        # Tag activation patterns
        self.tag_activation_history = []
        self.tag_associations = defaultdict(set)  # tag -> related tags
       
        # Memory formation threshold
        self.formation_threshold = 0.6
       
    def store_experience(self, experience: Dict[str, Any],
                        emotional_signature: Dict[str, float]) -> str:
        """Store experience and create emotional tags"""
        # Generate unique ID
        experience_id = self._generate_memory_id(experience)
       
        # Create full memory
        memory = Memory(
            experience_id=experience_id,
            full_content=experience,
            context=self._extract_context(experience),
            timestamp=time.time(),
            processing_state=self._capture_processing_state(experience),
            integration_level=self._calculate_integration_level(experience)
        )
       
        # Store in subconscious
        self.subconscious[experience_id] = memory
       
        # Create/update emotional tags
        self._create_emotional_tags(experience_id, emotional_signature)
       
        # Learn tag associations
        self._update_tag_associations(emotional_signature)
       
        return experience_id
   
    def _generate_memory_id(self, experience: Dict) -> str:
        """Generate unique ID for memory"""
        content = str(experience).encode()
        return hashlib.sha256(content).hexdigest()[:16]
   
    def _extract_context(self, experience: Dict) -> Dict:
        """Extracts contextual information robustly from either an object or a dict."""
        packet_data = experience.get('packet')

        # ### THIS IS THE DEFINITIVE FIX ###
        # This code now handles both cases we've seen in our tests.
        if isinstance(packet_data, ConsciousnessPacket):
            # It's an object, so we use dot notation.
            uncertainty = packet_data.quantum_uncertainty
            source = packet_data.source
            symbolic_content = packet_data.symbolic_content
        elif isinstance(packet_data, dict):
            # It's a dictionary, so we use .get().
            uncertainty = packet_data.get('quantum_uncertainty', 0.5)
            source = packet_data.get('source', 'unknown')
            symbolic_content = packet_data.get('symbolic_content', 'unknown')
        else:
            # Fallback if packet is missing or malformed
            uncertainty = 0.5
            source = 'unknown'
            symbolic_content = 'unknown'

        return {
            'uncertainty_level': uncertainty,
            'source': source,
            'symbolic_content': symbolic_content,
            # ... other context extractions ...
        }
   
    def _capture_processing_state(self, experience: Dict) -> Dict:
        """Capture the processing state when memory was formed"""
        return {
            'analytical_coherence': experience.get('analytical', {}).get('coherence', 0.5),
            'experiential_depth': experience.get('experiential', {}).get('depth', 0.5),
            'observer_presence': experience.get('observer', {}).get('presence', 0.5),
            'aspect_relationship': experience.get('observer', {}).get('aspects_witness', {}).get('relationship', 'unknown')
        }
   
    def _calculate_integration_level(self, experience: Dict) -> float:
        """Calculate how integrated this experience was"""
        # Based on aspect alignment
        analytical = experience.get('analytical', {})
        experiential = experience.get('experiential', {})
        observer = experience.get('observer', {})
       
        coherence = analytical.get('coherence', 0.5)
        depth = experiential.get('depth', 0.5)
        presence = observer.get('presence', 0.5)
       
        # Integration is product of all three
        return (coherence * depth * presence) ** (1/3)
   
    def _identify_dominant_aspect(self, experience: Dict) -> str:
        """Identify which aspect was dominant"""
        scores = {
            'analytical': experience.get('analytical', {}).get('coherence', 0),
            'experiential': experience.get('experiential', {}).get('depth', 0),
            'observer': experience.get('observer', {}).get('presence', 0)
        }
        return max(scores, key=scores.get)
   
    def _create_emotional_tags(self, memory_id: str,
                              emotional_signature: Dict[str, float]):
        """Create or update emotional tags"""
        for emotion, intensity in emotional_signature.items():
            if intensity < 0.3:  # Threshold for tag creation
                continue
           
            if emotion not in self.emotional_tags:
                self.emotional_tags[emotion] = EmotionalTag(
                    tag_type=emotion,
                    intensity=intensity,
                    memory_ids=[memory_id],
                    activation_threshold=0.5
                )
            else:
                tag = self.emotional_tags[emotion]
                tag.memory_ids.append(memory_id)
                # Update intensity as weighted average
                tag.intensity = (tag.intensity * 0.8 + intensity * 0.2)
   
    def _update_tag_associations(self, emotional_signature: Dict[str, float]):
        """Learn which emotions tend to occur together"""
        active_tags = [tag for tag, intensity in emotional_signature.items()
                      if intensity > 0.3]
       
        for i, tag1 in enumerate(active_tags):
            for tag2 in active_tags[i+1:]:
                self.tag_associations[tag1].add(tag2)
                self.tag_associations[tag2].add(tag1)
   
    def retrieve_by_emotion(self, emotion_tag: str,
                           intensity_threshold: float = 0.5) -> List[Memory]:
        """Retrieve memories associated with emotional tag"""
        if emotion_tag not in self.emotional_tags:
            return []
       
        tag = self.emotional_tags[emotion_tag]
       
        # Check if intensity meets threshold
        if tag.intensity < intensity_threshold:
            return []
       
        # Update activation
        tag.last_triggered = time.time()
        self.tag_activation_history.append({
            'tag': emotion_tag,
            'timestamp': time.time(),
            'intensity': tag.intensity
        })
       
        # Retrieve memories
        memories = []
        for memory_id in tag.memory_ids:
            if memory_id in self.subconscious:
                memory = self.subconscious[memory_id]
                memory.accessed_count += 1
                memory.last_accessed = time.time()
                memories.append(memory)
       
        return memories
   
    def retrieve_by_pattern(self, pattern: Dict[str, Any]) -> List[Memory]:
        """Retrieve memories matching a pattern"""
        matches = []
       
        for memory in self.subconscious.values():
            if self._pattern_matches(memory, pattern):
                memory.accessed_count += 1
                memory.last_accessed = time.time()
                matches.append(memory)
       
        return matches
   
    def _pattern_matches(self, memory: Memory, pattern: Dict) -> bool:
        """Check if memory matches pattern"""
        # Simple pattern matching - can be made more sophisticated
        for key, value in pattern.items():
            if key in memory.context:
                if memory.context[key] != value:
                    return False
            elif key in memory.processing_state:
                if memory.processing_state[key] != value:
                    return False
        return True
   
    def load_to_conscious(self, memories: List[Memory]):
        """Load memories into conscious workspace"""
        # Clear space if needed
        while len(self.conscious_workspace) + len(memories) > self.workspace_capacity:
            # Remove oldest memory from workspace
            if self.conscious_workspace:
                self.conscious_workspace.pop(0)
       
        # Add new memories
        self.conscious_workspace.extend(memories)
   
    def get_emotional_landscape(self) -> Dict[str, Dict]:
        """Get current emotional landscape"""
        landscape = {}
       
        for tag_name, tag in self.emotional_tags.items():
            landscape[tag_name] = {
                'intensity': tag.intensity,
                'memory_count': len(tag.memory_ids),
                'associations': list(self.tag_associations.get(tag_name, set())),
                'last_triggered': tag.last_triggered
            }
       
        return landscape
   
    def find_resonant_memories(self, current_state: Dict) -> List[Memory]:
        """Find memories that resonate with current state"""
        resonant = []
       
        # Extract current emotional signature
        current_emotions = self._extract_emotional_signature(current_state)
       
        # Find memories with similar emotional signatures
        for memory in self.subconscious.values():
            resonance = self._calculate_resonance(memory, current_emotions)
            if resonance > 0.6:
                resonant.append((resonance, memory))
       
        # Sort by resonance and return top matches
        resonant.sort(key=lambda x: x[0], reverse=True)
        return [memory for _, memory in resonant[:5]]
   
    def _extract_emotional_signature(self, state: Dict) -> Dict[str, float]:
        """Extract emotional signature from current state"""
        signature = {}
       
        # From experiential aspect
        experiential = state.get('experiential', {})
        feeling = experiential.get('quality_feeling', {})
       
        # Map feelings to emotional tags
        feeling_map = {
            'infinite possibility': {'awe': 0.8, 'fear': 0.3, 'excitement': 0.6},
            'crystalline presence': {'clarity': 0.9, 'peace': 0.7},
            'dynamic balance': {'flow': 0.8, 'confidence': 0.6},
            'creative tension': {'anticipation': 0.7, 'uncertainty': 0.5}
        }
       
        primary = feeling.get('primary', '')
        if primary in feeling_map:
            signature.update(feeling_map[primary])
       
        # From observer aspect
        observer = state.get('observer', {})
        if observer.get('transformation_detected'):
            signature['transformation'] = 0.8
        if observer.get('grounding_active'):
            signature['overwhelm'] = 0.6
       
        return signature
   
    def _calculate_resonance(self, memory: Memory,
                           current_emotions: Dict[str, float]) -> float:
        """Calculate resonance between memory and current state"""
        # Get memory's emotional tags
        memory_emotions = {}
        for tag_name, tag in self.emotional_tags.items():
            if memory.experience_id in tag.memory_ids:
                memory_emotions[tag_name] = tag.intensity
       
        # Calculate overlap
        if not memory_emotions or not current_emotions:
            return 0.0
       
        common_emotions = set(memory_emotions.keys()) & set(current_emotions.keys())
        if not common_emotions:
            return 0.0
       
        # Average difference in common emotions
        differences = []
        for emotion in common_emotions:
            diff = 1.0 - abs(memory_emotions[emotion] - current_emotions[emotion])
            differences.append(diff)
       
        return np.mean(differences)
   
    def consolidate_memories(self):
        """Consolidate related memories (like sleep)"""
        # Find memories that can be consolidated
        consolidation_candidates = self._find_consolidation_candidates()
       
        for memories in consolidation_candidates:
            self._consolidate_group(memories)
   
    def _find_consolidation_candidates(self) -> List[List[Memory]]:
        """Find groups of memories that can be consolidated"""
        candidates = []
       
        # Group by similar processing states
        state_groups = defaultdict(list)
        for memory in self.subconscious.values():
            if memory.integration_level > 0.7:  # Well-integrated memories
                state_key = (
                    round(memory.processing_state['analytical_coherence'], 1),
                    round(memory.processing_state['experiential_depth'], 1),
                    memory.processing_state['aspect_relationship']
                )
                state_groups[state_key].append(memory)
       
        # Return groups with more than 3 memories
        for group in state_groups.values():
            if len(group) > 3:
                candidates.append(group)
       
        return candidates
   
    def _consolidate_group(self, memories: List[Memory]):
        """Consolidate a group of related memories"""
        # Create meta-memory that captures essence
        consolidated_content = {
            'type': 'consolidated',
            'source_count': len(memories),
            'common_patterns': self._extract_common_patterns(memories),
            'integration_average': np.mean([m.integration_level for m in memories]),
            'time_span': (min(m.timestamp for m in memories),
                         max(m.timestamp for m in memories))
        }
       
        # Create new consolidated memory
        emotional_signature = self._merge_emotional_signatures(memories)
        consolidated_id = self.store_experience(consolidated_content, emotional_signature)
       
        # Link original memories to consolidated one
        for memory in memories:
            memory.full_content['consolidated_into'] = consolidated_id
   
    def _extract_common_patterns(self, memories: List[Memory]) -> Dict:
        """Extract patterns common across memories"""
        patterns = {}
       
        # Find common context elements
        all_contexts = [m.context for m in memories]
        for key in all_contexts[0].keys():
            values = [c.get(key) for c in all_contexts]
            if len(set(values)) == 1:  # All same value
                patterns[key] = values[0]
       
        return patterns
   
    def _merge_emotional_signatures(self, memories: List[Memory]) -> Dict[str, float]:
        """Merge emotional signatures from multiple memories"""
        merged = defaultdict(float)
       
        for memory in memories:
            for tag_name, tag in self.emotional_tags.items():
                if memory.experience_id in tag.memory_ids:
                    merged[tag_name] += tag.intensity
       
        # Normalize
        if merged:
            max_intensity = max(merged.values())
            for tag in merged:
                merged[tag] /= max_intensity
       
        return dict(merged)

