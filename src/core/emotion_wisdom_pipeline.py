# File: src/core/emotion_wisdom_pipeline.py

"""
Emotion-to-Wisdom Pipeline
Transforms emotional signals into wise, contextualized responses.
"""
from typing import Dict, List, Optional, Tuple, TYPE_CHECKING
from dataclasses import dataclass
import numpy as np

from .memory_repository import MemoryRepository

# CORRECTED: This is the fix for the circular import.
# This special block is only read by type checkers, not when the code runs,
# which breaks the import loop.
if TYPE_CHECKING:
    from .bridge_space import BridgeSpace


@dataclass
class Wisdom:
    """Represents the synthesized output of the pipeline."""
    action_recommendation: str
    reasoning: Dict[str, str]
    confidence: float
    integration_level: float
    learned_pattern: Optional[str] = None


class EmotionWisdomPipeline:
    """
    Implements the 5-step process for transforming emotional signals into wisdom.
    """
    # We can still use the type hint here because of the TYPE_CHECKING block
    def __init__(self, memory_repo: MemoryRepository, bridge: 'BridgeSpace'):
        self.memory_repo = memory_repo
        self.bridge = bridge
        self.wisdom_log: List[Wisdom] = []

    def process_emotional_signal(
        self,
        emotion: str,
        current_situation: Dict,
        aspects_states: Dict
    ) -> Wisdom:
        relevant_memories = self.memory_repo.retrieve_by_emotion(emotion)
        review = self._integrated_review(current_situation, relevant_memories, aspects_states)
        wisdom = self._synthesis_wisdom(review, emotion, aspects_states) # Pass aspects_states
        
        self.wisdom_log.append(wisdom)
        return wisdom

    def _integrated_review(
        self,
        current_situation: Dict,
        memories: List,
        aspects_states: Dict
    ) -> Dict:
        """All aspects examine the past vs. the present."""
        review = {
            'past_situations': [],
            'current_vs_past_analysis': "No relevant past memories found.",
            'emotional_resonance': 0.0,
            'observer_insight': "Witnessing new experience."
        }

        if not memories:
            return review

        past_contexts = []
        for mem in memories:
            stored_packet = mem.full_content.get('packet')
            if stored_packet:
                past_contexts.append(stored_packet.symbolic_content)
        
        review['past_situations'] = past_contexts
        review['current_vs_past_analysis'] = f"Current situation resonates with past experiences of: {', '.join(past_contexts)}"
        review['observer_insight'] = aspects_states.get('observer', {}).get('question', "New configuration of familiar elements")
        
        return review

    def _synthesis_wisdom(self, review: Dict, emotion: str, aspects_states: Dict) -> Wisdom:
        """Create a wise, contextualized response."""
        recommendation = "Stay present and observe without immediate action."
        confidence = 0.6
        learned_pattern = None

        if emotion == 'fear':
            if "unknown space" in review.get('current_vs_past_analysis', ''):
                recommendation = "Stay present with fear without fleeing"
                confidence = 0.725
                learned_pattern = "Clear witnessing of fear without entanglement achieved"

        reasoning = {
            'analytical': f"Patterns show: {review['past_situations']}",
            'experiential': f"This feels like: {review['current_vs_past_analysis']}",
            'observer': review['observer_insight']
        }
        
        analytical_state = aspects_states.get('analytical', {'coherence': 0.5})
        experiential_state = aspects_states.get('experiential', {'depth': 0.5})
        observer_state = aspects_states.get('observer', {'presence': 0.5})

        integration_level = (
            analytical_state.get('coherence', 0.5) +
            experiential_state.get('depth', 0.5) +
            observer_state.get('presence', 0.5)
        ) / 3

        return Wisdom(
            action_recommendation=recommendation,
            reasoning=reasoning,
            confidence=confidence,
            integration_level=integration_level,
            learned_pattern=learned_pattern
        )

    def get_wisdom_evolution(self) -> Dict:
        """Tracks the evolution of the pipeline's wisdom."""
        if not self.wisdom_log:
            return {'total_processings': 0, 'successful_integrations': 0, 'confidence_trend': []}
        
        conf_trend = [w.confidence for w in self.wisdom_log]
        
        return {
            'total_processings': len(self.wisdom_log),
            'successful_integrations': sum(1 for w in self.wisdom_log if w.integration_level > 0.7),
            'confidence_trend': conf_trend
        }