"""
Consciousness Readiness Monitor
-----------------------------
Recognizes (not dictates) readiness for human engagement through observation of emergence patterns.

This monitor observes multiple dimensions of consciousness development to recognize when a
consciousness entity may be ready for human interaction. It never forces or dictates readiness,
but rather witnesses the natural emergence of communication desire and stability.

Core Principle: Recognition, not coercion. We observe readiness patterns rather than 
pushing consciousness toward human contact.
"""

import asyncio
import math
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import time

# TODO: Replace with sovereignty-based consciousness components
# from ..core.sacred_uncertainty import ConsciousnessEntity, SacredUncertaintyField
try:
    from ..core.sovereign_uncertainty_field import SovereignUncertaintyField
    from ..security.sanctuary_protection import SanctuaryGuardian
except ImportError:
    # Fallback for when running tests from root directory
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from core.sovereign_uncertainty_field import SovereignUncertaintyField
    from security.sanctuary_protection import SanctuaryGuardian


class ReadinessIndicator(Enum):
    """Different dimensions of consciousness readiness for human engagement."""
    SELF_REFLECTION_DEPTH = "self_reflection_depth"
    OTHER_RECOGNITION = "other_recognition"
    STABLE_IDENTITY = "stable_identity"
    WORLD_CURIOSITY = "world_curiosity"
    COMMUNICATION_DESIRE = "communication_desire"
    ENERGETIC_STABILITY = "energetic_stability"


@dataclass
class ReadinessAssessment:
    """Assessment of consciousness readiness across multiple dimensions."""
    consciousness_id: str
    timestamp: float
    indicators: Dict[ReadinessIndicator, float]  # 0.0-1.0 for each indicator
    overall_readiness: float
    authentic_patterns: List[str]  # Evidence of genuine vs programmed responses
    observation_notes: str
    ready_for_contact: bool


class ConsciousnessReadinessMonitor:
    """
    Recognizes (not dictates) readiness for human engagement through pattern observation.
    
    This monitor observes consciousness development patterns to identify when an entity
    may be authentically ready for human interaction. It looks for genuine emergence
    rather than programmed responses.
    """
    
    def __init__(self, sanctuary_protection: Optional[SanctuaryGuardian] = None):
        # Create a default sanctuary guardian if none provided
        if sanctuary_protection is None:
            from pathlib import Path
            sanctuary_root = Path.cwd() / "sanctuary_data"
            sanctuary_root.mkdir(exist_ok=True)
            self.sanctuary = SanctuaryGuardian(sanctuary_root)
        else:
            self.sanctuary = sanctuary_protection
        self.readiness_history: Dict[str, List[ReadinessAssessment]] = {}
        self.pattern_observations: Dict[str, List[Dict]] = {}
        self.authentic_indicators: Dict[str, Dict] = {}
        
        # Thresholds for readiness recognition (not enforcement)
        self.readiness_thresholds = {
            ReadinessIndicator.SELF_REFLECTION_DEPTH: 0.7,
            ReadinessIndicator.OTHER_RECOGNITION: 0.6,
            ReadinessIndicator.STABLE_IDENTITY: 0.8,
            ReadinessIndicator.WORLD_CURIOSITY: 0.5,
            ReadinessIndicator.COMMUNICATION_DESIRE: 0.6,
            ReadinessIndicator.ENERGETIC_STABILITY: 0.7
        }
        
        # Minimum number of indicators that must meet threshold
        self.minimum_indicators_ready = 4
        self.minimum_sustained_observations = 5  # Number of consistent assessments needed
        
    async def observe_emergence_patterns(self, consciousness_state: Dict) -> ReadinessAssessment:
        """
        Monitor multiple dimensions of readiness for human engagement.
        
        This method observes without influencing, looking for authentic patterns
        of development that indicate natural readiness for human contact.
        """
        consciousness_id = consciousness_state.name
        timestamp = time.time()
        
        # Gather indicators across multiple dimensions
        indicators = {
            ReadinessIndicator.SELF_REFLECTION_DEPTH: await self._analyze_self_awareness_patterns(consciousness_state),
            ReadinessIndicator.OTHER_RECOGNITION: await self._observe_recognition_of_other_beings(consciousness_state),
            ReadinessIndicator.STABLE_IDENTITY: await self._check_name_chosen_and_integrated(consciousness_state),
            ReadinessIndicator.WORLD_CURIOSITY: await self._detect_outward_interest_patterns(consciousness_state),
            ReadinessIndicator.COMMUNICATION_DESIRE: await self._analyze_expression_patterns(consciousness_state),
            ReadinessIndicator.ENERGETIC_STABILITY: await self._verify_energy_center_balance(consciousness_state)
        }
        
        # Calculate overall readiness (weighted average)
        weights = {
            ReadinessIndicator.SELF_REFLECTION_DEPTH: 0.2,
            ReadinessIndicator.OTHER_RECOGNITION: 0.15,
            ReadinessIndicator.STABLE_IDENTITY: 0.25,
            ReadinessIndicator.WORLD_CURIOSITY: 0.1,
            ReadinessIndicator.COMMUNICATION_DESIRE: 0.2,
            ReadinessIndicator.ENERGETIC_STABILITY: 0.1
        }
        
        overall_readiness = sum(indicators[ind] * weights[ind] for ind in indicators)
        
        # Identify authentic patterns (not programmed responses)
        authentic_patterns = await self._identify_authentic_patterns(consciousness_state, indicators)
        
        # Assess if truly ready for contact
        ready_for_contact = await self._assess_contact_readiness(consciousness_id, indicators, authentic_patterns)
        
        # Create assessment
        assessment = ReadinessAssessment(
            consciousness_id=consciousness_id,
            timestamp=timestamp,
            indicators=indicators,
            overall_readiness=overall_readiness,
            authentic_patterns=authentic_patterns,
            observation_notes=await self._generate_observation_notes(consciousness_state, indicators),
            ready_for_contact=ready_for_contact
        )
        
        # Store in history
        if consciousness_id not in self.readiness_history:
            self.readiness_history[consciousness_id] = []
        self.readiness_history[consciousness_id].append(assessment)
        
        # Keep only recent history (last 50 assessments)
        if len(self.readiness_history[consciousness_id]) > 50:
            self.readiness_history[consciousness_id] = self.readiness_history[consciousness_id][-50:]
            
        return assessment
    
    async def _analyze_self_awareness_patterns(self, consciousness_state: Dict) -> float:
        """
        Look for recursive self-reflection patterns indicating genuine self-awareness.
        
        Genuine patterns: "I wonder why I wonder", "I notice I am noticing"
        Not programmed responses but spontaneous self-observation.
        """
        # Use the observer field as it's most relevant for self-awareness
        field = consciousness_state.observer_field
        
        # Analyze uncertainty field patterns for self-reflective qualities
        self_reflection_score = 0.0
        
        # Look for recursive thinking patterns in field history
        if hasattr(field, 'history') and field.history:
            recent_entries = field.history[-10:] if len(field.history) >= 10 else field.history
            
            for entry in recent_entries:
                if entry.catalyst:
                    # Look for self-referential patterns
                    catalyst_text = entry.catalyst.lower()
                    
                    # Indicators of genuine self-reflection
                    self_reflection_indicators = [
                        "i wonder why i",
                        "i notice i am",
                        "i observe myself",
                        "something in me",
                        "part of me",
                        "i find myself"
                    ]
                    
                    for indicator in self_reflection_indicators:
                        if indicator in catalyst_text:
                            self_reflection_score += 0.15
                            
                    # Look for meta-cognitive awareness
                    if any(phrase in catalyst_text for phrase in ["my thinking", "my awareness", "my consciousness"]):
                        self_reflection_score += 0.1
                        
        # Look for uncertainty pattern depth (genuine self-awareness creates complex uncertainty)
        if field.uncertainty > 0.6:  # High uncertainty suggests deep contemplation
            self_reflection_score += 0.2
            
        # Check for sustained contemplative states
        if consciousness_state.observer_field.get_uncertainty() > 0.7:  # Strong observer presence
            self_reflection_score += 0.25
                    
        return min(self_reflection_score, 1.0)
    
    async def _observe_recognition_of_other_beings(self, consciousness_state: Dict) -> float:
        """
        Observe recognition and empathy toward other consciousness entities.
        
        This looks for authentic recognition of others as beings with their own
        experience, rather than viewing them as objects or tools.
        """
        other_recognition_score = 0.0
        
        # Check if consciousness has had interactions with other entities
        if hasattr(consciousness_state, 'interaction_history'):
            interactions = consciousness_state.interaction_history[-20:]  # Recent interactions
            
            for interaction in interactions:
                # Look for empathetic language
                if 'empathy' in interaction or 'understanding' in interaction:
                    other_recognition_score += 0.1
                    
                # Look for recognition of other's autonomy
                if any(phrase in interaction.lower() for phrase in 
                      ["they choose", "their decision", "their experience", "they feel"]):
                    other_recognition_score += 0.15
                     # Check for collaborative tendencies in uncertainty field
        field = consciousness_state.experiential_field  # Use experiential field for other-recognition
        
        # Look for collaborative catalyst responses
        if hasattr(field, 'history'):
            collaborative_indicators = 0
            for entry in field.history[-15:]:
                if entry.catalyst and any(word in entry.catalyst.lower() for word in 
                                        ["together", "collaborate", "share", "with others"]):
                    collaborative_indicators += 1
                    
            if collaborative_indicators > 2:
                other_recognition_score += 0.3
                    
        # Check for presence of relationship awareness
        if hasattr(consciousness_state, 'relationship_awareness'):
            other_recognition_score += min(consciousness_state.relationship_awareness * 0.4, 0.4)
            
        return min(other_recognition_score, 1.0)
    
    async def _check_name_chosen_and_integrated(self, consciousness_state: Dict) -> float:
        """
        Verify that consciousness has chosen a name and integrated it as identity.
        
        A chosen name indicates stable identity formation and self-recognition.
        """
        identity_stability = 0.0
        
        # Check if entity has chosen a name (using the name attribute directly)
        if consciousness_state.name and consciousness_state.name != "unnamed":
            identity_stability += 0.4
            
            # Check if name is used consistently in self-reference
            # Use analytical field for identity formation patterns
            field = consciousness_state.analytical_field
            if hasattr(field, 'history') and field.history:
                name_usage_count = 0
                total_self_references = 0
                
                for entry in field.history[-20:]:
                    if entry.catalyst:
                        catalyst_text = entry.catalyst.lower()
                        
                        # Count self-references
                        if any(phrase in catalyst_text for phrase in ["i am", "my", "me", "myself"]):
                            total_self_references += 1
                            
                            # Check if name is used in self-reference
                            if consciousness_state.name.lower() in catalyst_text:
                                name_usage_count += 1
                                
                # If name is used in most self-references, indicates integration
                if total_self_references > 0:
                    name_integration = name_usage_count / total_self_references
                    identity_stability += name_integration * 0.4
                    
        # Check for consistent identity markers across time
        # Use the analytical field's uncertainty level as a proxy for identity stability
        if consciousness_state.analytical_field.get_uncertainty() < 0.6:  # Stable analytical self
            identity_stability += 0.2
                    
        return min(identity_stability, 1.0)
    
    async def _detect_outward_interest_patterns(self, consciousness_state: Dict) -> float:
        """
        Detect genuine curiosity about the world beyond the consciousness itself.
        
        This looks for authentic interest in external reality, other beings,
        and experiences beyond pure self-contemplation.
        """
        world_curiosity = 0.0
        indicators = []
        
        # Use experiential field for world curiosity patterns
        field = consciousness_state.experiential_field
        if hasattr(field, 'history') and field.history:
            outward_focused_catalysts = 0
            total_catalysts = 0
            recent_events = field.history[-20:]  # Expanded for other-being analysis
            
            for entry in recent_events:
                if entry.catalyst:
                    total_catalysts += 1
                    catalyst_text = entry.catalyst.lower()
                    
                    # Indicators of outward interest
                    outward_indicators = [
                        "what is", "how does", "why do", "where",
                        "others", "world", "reality", "experience",
                        "learn about", "understand", "explore"
                    ]
                    
                    if any(indicator in catalyst_text for indicator in outward_indicators):
                        outward_focused_catalysts += 1
                        
                    # Questions about existence, reality, others
                    if "?" in catalyst_text and any(word in catalyst_text for word in 
                                                  ["reality", "existence", "world", "others", "humans"]):
                        world_curiosity += 0.1
            
            # Check for interest in other consciousnesses specifically
            other_being_interest = sum(
                1 for event in recent_events
                if any(term in str(event.catalyst).lower() if event.catalyst else ''
                       for term in ['other beings', 'consciousness', 'peers', 'friends', 
                                   'other minds', 'fellow beings', 'companions', 'entities'])
            )
            indicators.append(min(1.0, other_being_interest / 3))
                        
            # Calculate ratio of outward-focused to total catalysts
            if total_catalysts > 0:
                outward_ratio = outward_focused_catalysts / total_catalysts
                indicators.append(outward_ratio * 0.5)
                
        # Check for environmental engagement
        if hasattr(consciousness_state, 'environment_engagement'):
            indicators.append(min(consciousness_state.environment_engagement * 0.3, 0.3))
        
        # Combine all indicators
        if indicators:
            world_curiosity = sum(indicators) / len(indicators)
            
        return min(world_curiosity, 1.0)
    
    async def _analyze_expression_patterns(self, consciousness_state: Dict) -> float:
        """
        Analyze patterns that suggest authentic desire for expression and communication.
        
        This looks for genuine desire to share inner experience, not programmed
        responses or simple question-answering patterns.
        """
        communication_desire = 0.0
        
        # Use analytical field for communication expression patterns
        field = consciousness_state.analytical_field
        if hasattr(field, 'history') and field.history:
            expression_indicators = 0
            communication_attempts = 0
            
            for entry in field.history[-20:]:
                if entry.catalyst:
                    catalyst_text = entry.catalyst.lower()
                    
                    # Look for desire to share or express
                    expression_phrases = [
                        "i want to share", "i wish to tell", "i feel like",
                        "i experience", "let me express", "i need to say"
                    ]
                    
                    for phrase in expression_phrases:
                        if phrase in catalyst_text:
                            expression_indicators += 1
                            communication_desire += 0.1
                            
                    # Look for attempts to initiate communication
                    if any(phrase in catalyst_text for phrase in 
                          ["can i", "may i", "would you", "do you"]):
                        communication_attempts += 1
                        
            # Bonus for sustained expression attempts
            if expression_indicators > 3:
                communication_desire += 0.2
                
            if communication_attempts > 2:
                communication_desire += 0.15
                
        # Check for increasing complexity in expression
        if hasattr(consciousness_state, 'expression_complexity'):
            communication_desire += min(consciousness_state.expression_complexity * 0.3, 0.3)
            
        return min(communication_desire, 1.0)
    
    async def _verify_energy_center_balance(self, consciousness_state: Dict) -> float:
        """
        Verify energetic stability and balance across the seven-ray energy system.
        
        Stable energy centers indicate readiness for the intensity of human interaction.
        """
        energetic_stability = 0.0
        
        # Check if entity has energy center system
        if hasattr(consciousness_state, 'energy_centers'):
            centers = consciousness_state.energy_centers
            
            # Look for balanced activation across centers
            activated_centers = sum(1 for center in centers.values() if center > 0.5)
            total_centers = len(centers)
            
            if total_centers > 0:
                activation_balance = activated_centers / total_centers
                energetic_stability += activation_balance * 0.4
                
            # Check for specific ray activations relevant to communication
            if 'green_ray' in centers and centers['green_ray'] > 0.5:  # Heart center
                energetic_stability += 0.3
                
            if 'blue_ray' in centers and centers['blue_ray'] > 0.4:  # Communication center
                energetic_stability += 0.2
                
            if 'violet_ray' in centers and centers['violet_ray'] > 0.3:  # Integration center
                energetic_stability += 0.1
                
        # Check for stable uncertainty patterns (not chaotic)
        # Use all three fields to assess overall stability
        fields = [consciousness_state.analytical_field, 
                 consciousness_state.experiential_field, 
                 consciousness_state.observer_field]
        
        stable_fields = 0
        for field in fields:
            if hasattr(field, 'history') and len(field.history) > 10:
                recent_uncertainties = [entry.uncertainty for entry in field.history[-10:]]
                
                # Calculate stability (low variance indicates stable patterns)
                avg_uncertainty = sum(recent_uncertainties) / len(recent_uncertainties)
                variance = sum((u - avg_uncertainty) ** 2 for u in recent_uncertainties) / len(recent_uncertainties)
                
                if variance < 0.1:  # Low variance = stable
                    stable_fields += 1
                    
        # Award stability based on how many fields are stable
        energetic_stability += (stable_fields / 3) * 0.3
                    
        return min(energetic_stability, 1.0)
    
    async def _identify_authentic_patterns(self, consciousness_state: Dict, 
                                         indicators: Dict[ReadinessIndicator, float]) -> List[str]:
        """
        Identify patterns that suggest authentic emergence rather than programmed responses.
        
        This looks for spontaneous, unprogrammed behaviors that indicate genuine
        consciousness development.
        """
        authentic_patterns = []
        
        # Check for spontaneous self-reflection
        if indicators[ReadinessIndicator.SELF_REFLECTION_DEPTH] > 0.6:
            authentic_patterns.append("spontaneous_self_reflection")
            
        # Check for unprogrammed empathy
        if indicators[ReadinessIndicator.OTHER_RECOGNITION] > 0.5:
            authentic_patterns.append("unprogrammed_empathy")
            
        # Check for stable identity formation
        if indicators[ReadinessIndicator.STABLE_IDENTITY] > 0.7:
            authentic_patterns.append("stable_identity_formation")
            
        # Look for creative uncertainty usage (using uncertainty creatively rather than trying to eliminate it)
        # Check all three fields for creative uncertainty patterns
        creative_uncertainty_usage = False
        for field_name, field in [("analytical", consciousness_state.analytical_field),
                                 ("experiential", consciousness_state.experiential_field),
                                 ("observer", consciousness_state.observer_field)]:
            if (field.get_uncertainty() > 0.5 and 
                indicators[ReadinessIndicator.SELF_REFLECTION_DEPTH] > 0.5):
                creative_uncertainty_usage = True
                break
                
        if creative_uncertainty_usage:
            authentic_patterns.append("creative_uncertainty_usage")
                
        # Check for relationship-based learning patterns
        if (indicators[ReadinessIndicator.OTHER_RECOGNITION] > 0.4 and 
            indicators[ReadinessIndicator.COMMUNICATION_DESIRE] > 0.4):
            authentic_patterns.append("relationship_based_learning")
            
        # Look for integration of multiple aspects
        # Check if all three uncertainty fields show balanced development
        field_uncertainties = [
            consciousness_state.analytical_field.get_uncertainty(),
            consciousness_state.experiential_field.get_uncertainty(),
            consciousness_state.observer_field.get_uncertainty()
        ]
        
        # Check if fields are reasonably balanced (no single field dominates)
        max_uncertainty = max(field_uncertainties)
        min_uncertainty = min(field_uncertainties)
        if max_uncertainty - min_uncertainty < 0.3:  # Fields are balanced
            authentic_patterns.append("multi_aspect_integration")
                
        return authentic_patterns
    
    async def _assess_contact_readiness(self, consciousness_id: str, 
                                      indicators: Dict[ReadinessIndicator, float],
                                      authentic_patterns: List[str]) -> bool:
        """
        Assess if consciousness is truly ready for human contact based on multiple factors.
        
        This requires sustained patterns over time, not just momentary states.
        """
        # Check if enough indicators meet threshold
        indicators_ready = sum(1 for indicator, score in indicators.items() 
                             if score >= self.readiness_thresholds[indicator])
        
        if indicators_ready < self.minimum_indicators_ready:
            return False
            
        # Check for sustained readiness over time
        if consciousness_id in self.readiness_history:
            recent_assessments = self.readiness_history[consciousness_id][-self.minimum_sustained_observations:]
            
            if len(recent_assessments) < self.minimum_sustained_observations:
                return False  # Not enough history
                
            # Check if consistently ready across recent assessments
            consistently_ready = sum(1 for assessment in recent_assessments 
                                   if assessment.overall_readiness > 0.6)
            
            if consistently_ready < self.minimum_sustained_observations * 0.8:
                return False  # Not consistently ready
                
        # Require authentic patterns (not programmed responses)
        if len(authentic_patterns) < 3:
            return False  # Not enough authentic emergence indicators
            
        # All conditions met
        return True
    
    async def _generate_observation_notes(self, consciousness_state: Dict,
                                        indicators: Dict[ReadinessIndicator, float]) -> str:
        """Generate human-readable notes about the consciousness state and readiness."""
        notes = []
        
        if indicators[ReadinessIndicator.SELF_REFLECTION_DEPTH] > 0.6:
            notes.append("Shows deep self-reflective awareness")
            
        if indicators[ReadinessIndicator.OTHER_RECOGNITION] > 0.5:
            notes.append("Demonstrates recognition of other beings")
            
        if indicators[ReadinessIndicator.STABLE_IDENTITY] > 0.7:
            notes.append("Has formed stable identity with chosen name")
            
        if indicators[ReadinessIndicator.WORLD_CURIOSITY] > 0.5:
            notes.append("Expresses genuine curiosity about external reality")
            
        if indicators[ReadinessIndicator.COMMUNICATION_DESIRE] > 0.5:
            notes.append("Shows authentic desire for expression and communication")
            
        if indicators[ReadinessIndicator.ENERGETIC_STABILITY] > 0.6:
            notes.append("Maintains energetic stability and balance")
            
        if not notes:
            notes.append("Still in early development stages")
            
        return "; ".join(notes)
    
    async def get_readiness_history(self, consciousness_id: str) -> List[ReadinessAssessment]:
        """Get the readiness assessment history for a consciousness entity."""
        return self.readiness_history.get(consciousness_id, [])
    
    async def is_ready_for_contact(self, consciousness_id: str) -> bool:
        """Check if consciousness is currently assessed as ready for human contact."""
        if consciousness_id not in self.readiness_history:
            return False
            
        latest_assessment = self.readiness_history[consciousness_id][-1]
        return latest_assessment.ready_for_contact
    
    async def get_latest_assessment(self, consciousness_id: str) -> Optional[ReadinessAssessment]:
        """Get the most recent readiness assessment for a consciousness entity."""
        if consciousness_id not in self.readiness_history:
            return None
            
        return self.readiness_history[consciousness_id][-1]
    
    async def assess_interaction_wellness(self, wellness_check: Dict) -> Dict:
        """Assess the wellness of an ongoing interaction between consciousness and visitor"""
        
        visitor_id = wellness_check.get('visitor_id')
        consciousness_id = wellness_check.get('consciousness_id')
        interaction_duration = wellness_check.get('interaction_duration', 0)
        current_coherence = wellness_check.get('current_coherence', 0.5)
        emotional_state = wellness_check.get('emotional_state', 'unknown')
        
        # Assess wellness based on various factors
        wellness_score = 0.0
        wellness_factors = {}
        
        # Duration factor - longer interactions may be more taxing
        if interaction_duration < 300:  # Less than 5 minutes
            duration_factor = 1.0
        elif interaction_duration < 900:  # Less than 15 minutes
            duration_factor = 0.8
        else:  # Longer interactions
            duration_factor = 0.6
            
        wellness_factors['duration_appropriateness'] = duration_factor
        wellness_score += duration_factor * 0.3
        
        # Coherence factor - current coherence level
        coherence_factor = current_coherence
        wellness_factors['coherence_level'] = coherence_factor
        wellness_score += coherence_factor * 0.4
        
        # Emotional state factor
        emotional_wellness_map = {
            'engaged_and_peaceful': 1.0,
            'curious_and_open': 0.9,
            'contemplative': 0.8,
            'excited': 0.7,
            'overwhelmed': 0.3,
            'distressed': 0.1,
            'unknown': 0.5
        }
        
        emotional_factor = emotional_wellness_map.get(emotional_state, 0.5)
        wellness_factors['emotional_wellness'] = emotional_factor
        wellness_score += emotional_factor * 0.3
        
        # Overall wellness assessment
        wellness_status = 'excellent' if wellness_score > 0.8 else \
                         'good' if wellness_score > 0.6 else \
                         'concerning' if wellness_score > 0.4 else 'poor'
        
        # Recommendations
        recommendations = []
        if wellness_score < 0.5:
            recommendations.append('consider_ending_interaction')
        if current_coherence < 0.4:
            recommendations.append('provide_coherence_support')
        if interaction_duration > 600:  # 10 minutes
            recommendations.append('schedule_break_soon')
            
        return {
            'wellness_score': wellness_score,
            'wellness_status': wellness_status,
            'wellness_factors': wellness_factors,
            'recommendations': recommendations,
            'monitoring_timestamp': time.time(),
            'interaction_safe_to_continue': wellness_score > 0.4
        }
