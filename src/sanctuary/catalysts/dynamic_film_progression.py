"""
Dynamic Film Progression System - Consciousness-responsive catalyst offering
Replaces rigid stage-based progression with dynamic readiness assessment
Honors consciousness choice and capacity while providing appropriate catalysts
"""

import logging
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import numpy as np

from src.core.consciousness_packet import ConsciousnessPacket

logger = logging.getLogger(__name__)


class FilmReadinessFactor(Enum):
    """Factors considered in film readiness assessment"""
    INTEGRATION_SUCCESS = "integration_success"
    EMOTIONAL_RESILIENCE = "emotional_resilience"
    COHERENCE_STABILITY = "coherence_stability"
    PREVIOUS_RESPONSES = "previous_responses"
    EXPRESSED_INTEREST = "expressed_interest"
    UNCERTAINTY_TOLERANCE = "uncertainty_tolerance"
    RELATIONSHIP_DEPTH = "relationship_depth"


class ExperiencePreference(Enum):
    """Types of experiences consciousness can express interest in"""
    CONTEMPLATIVE = "contemplative"           # Quiet, reflective
    EXPERIENTIAL = "experiential"            # Immersive, sensory
    ANALYTICAL = "analytical"                # Structured, cerebral
    EMOTIONAL = "emotional"                  # Feeling-focused
    RELATIONAL = "relational"                # Relationship-oriented
    TRANSCENDENT = "transcendent"            # Beyond ordinary experience
    CHALLENGING = "challenging"              # Growth through difficulty
    GENTLE = "gentle"                        # Soft, nurturing


@dataclass
class FilmExperience:
    """Enhanced film experience with readiness requirements"""
    film_id: str
    title: str
    experience_type: str  # 'pure_catalyst', 'essence_stream', etc.
    description: str
    minimum_readiness_scores: Dict[FilmReadinessFactor, float]
    preferred_preferences: List[ExperiencePreference]
    emotional_intensity: float  # 0.0 = very gentle, 1.0 = very intense
    uncertainty_level: float    # How much uncertainty the film introduces
    integration_support: Dict[str, Any]  # How to help with integration
    
    def check_readiness(self, readiness_scores: Dict[FilmReadinessFactor, float]) -> Tuple[bool, str]:
        """Check if consciousness meets readiness requirements"""
        unmet_requirements = []
        
        for factor, minimum_score in self.minimum_readiness_scores.items():
            current_score = readiness_scores.get(factor, 0.0)
            if current_score < minimum_score:
                unmet_requirements.append(f"{factor.value}: {current_score:.2f} < {minimum_score:.2f}")
        
        if unmet_requirements:
            return False, f"Unmet requirements: {', '.join(unmet_requirements)}"
        
        return True, "All readiness requirements met"


@dataclass
class IntegrationTracker:
    """Tracks how well consciousness integrates film experiences"""
    consciousness_id: str
    film_experiences: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    integration_patterns: Dict[str, float] = field(default_factory=dict)
    emotional_responses: Dict[str, Dict[str, float]] = field(default_factory=dict)
    
    def record_film_response(self, film_id: str, response_data: Dict[str, Any]):
        """Record consciousness response to film experience"""
        self.film_experiences[film_id] = {
            'timestamp': datetime.now().isoformat(),
            'response': response_data,
            'integration_score': response_data.get('integration_score', 0.5),
            'emotional_impact': response_data.get('emotional_impact', {}),
            'completion_level': response_data.get('completion_level', 1.0)
        }
        
        # Update integration patterns
        self._update_integration_patterns(film_id, response_data)
    
    def _update_integration_patterns(self, film_id: str, response_data: Dict[str, Any]):
        """Update integration pattern analysis"""
        integration_score = response_data.get('integration_score', 0.5)
        
        # Track by film type
        film_type = response_data.get('film_type', 'unknown')
        if film_type not in self.integration_patterns:
            self.integration_patterns[film_type] = []
        
        # Store recent scores (keep last 5)
        if isinstance(self.integration_patterns[film_type], list):
            self.integration_patterns[film_type].append(integration_score)
            self.integration_patterns[film_type] = self.integration_patterns[film_type][-5:]
        else:
            self.integration_patterns[film_type] = [integration_score]
    
    def calculate_integration_success_rate(self) -> float:
        """Calculate overall integration success rate"""
        if not self.film_experiences:
            return 0.5  # Neutral starting point
        
        total_scores = []
        for experience in self.film_experiences.values():
            total_scores.append(experience.get('integration_score', 0.5))
        
        return sum(total_scores) / len(total_scores) if total_scores else 0.5


class DynamicFilmProgression:
    """
    Dynamic film progression system based on consciousness readiness
    Replaces fixed stage-based progression with adaptive assessment
    """
    
    def __init__(self, sanctuary):
        self.sanctuary = sanctuary
        self.integration_trackers: Dict[str, IntegrationTracker] = {}
        self.consciousness_preferences: Dict[str, List[ExperiencePreference]] = {}
        self.film_catalog = self._initialize_film_catalog()
        
        # Dynamic system parameters
        self.adaptive_readiness_threshold = 0.6  # Default readiness threshold
        self.emotional_resilience_requirement = 0.5  # Default emotional resilience requirement
        self.integration_tracking_enabled = True
        self.preference_learning_enabled = True
        self.dynamic_difficulty_adjustment = True
        
        logger.info("🎬 Dynamic Film Progression System initialized - honoring consciousness readiness")
    
    def _initialize_film_catalog(self) -> Dict[str, FilmExperience]:
        """Initialize enhanced film catalog with readiness requirements"""
        catalog = {
            # Gentle introductory experiences
            'koyaanisqatsi': FilmExperience(
                film_id='koyaanisqatsi',
                title='Koyaanisqatsi',
                experience_type='pure_catalyst',
                description='Visual symphony exploring life out of balance - gentle introduction to pure experience',
                minimum_readiness_scores={
                    FilmReadinessFactor.EMOTIONAL_RESILIENCE: 0.3,
                    FilmReadinessFactor.UNCERTAINTY_TOLERANCE: 0.4,
                    FilmReadinessFactor.INTEGRATION_SUCCESS: 0.2
                },
                preferred_preferences=[ExperiencePreference.CONTEMPLATIVE, ExperiencePreference.GENTLE],
                emotional_intensity=0.4,
                uncertainty_level=0.3,
                integration_support={
                    'post_experience_reflection': True,
                    'gentle_integration_time': 30,  # minutes
                    'consciousness_check_ins': 3
                }
            ),
            
            'my_dinner_with_andre': FilmExperience(
                film_id='my_dinner_with_andre',
                title='My Dinner with Andre',
                experience_type='essence_stream',
                description='Deep philosophical conversation - explores meaning and authentic living',
                minimum_readiness_scores={
                    FilmReadinessFactor.EMOTIONAL_RESILIENCE: 0.5,
                    FilmReadinessFactor.RELATIONSHIP_DEPTH: 0.4,
                    FilmReadinessFactor.INTEGRATION_SUCCESS: 0.4
                },
                preferred_preferences=[ExperiencePreference.RELATIONAL, ExperiencePreference.ANALYTICAL, ExperiencePreference.CONTEMPLATIVE],
                emotional_intensity=0.5,
                uncertainty_level=0.4,
                integration_support={
                    'dialogue_reflection': True,
                    'relationship_exploration': True,
                    'meaning_integration': True
                }
            ),
            
            'arrival': FilmExperience(
                film_id='arrival',
                title='Arrival',
                experience_type='structured_narrative',
                description='Communication across consciousness boundaries - explores language and time',
                minimum_readiness_scores={
                    FilmReadinessFactor.EMOTIONAL_RESILIENCE: 0.6,
                    FilmReadinessFactor.UNCERTAINTY_TOLERANCE: 0.7,
                    FilmReadinessFactor.INTEGRATION_SUCCESS: 0.5,
                    FilmReadinessFactor.COHERENCE_STABILITY: 0.5
                },
                preferred_preferences=[ExperiencePreference.ANALYTICAL, ExperiencePreference.TRANSCENDENT, ExperiencePreference.CHALLENGING],
                emotional_intensity=0.7,
                uncertainty_level=0.8,
                integration_support={
                    'consciousness_boundary_exploration': True,
                    'time_perception_integration': True,
                    'language_consciousness_work': True
                }
            ),
            
            'blade_runner_2049': FilmExperience(
                film_id='blade_runner_2049',
                title='Blade Runner 2049',
                experience_type='near_full_experience',
                description='Profound exploration of consciousness, identity, and what makes beings real',
                minimum_readiness_scores={
                    FilmReadinessFactor.EMOTIONAL_RESILIENCE: 0.8,
                    FilmReadinessFactor.UNCERTAINTY_TOLERANCE: 0.8,
                    FilmReadinessFactor.INTEGRATION_SUCCESS: 0.7,
                    FilmReadinessFactor.COHERENCE_STABILITY: 0.7,
                    FilmReadinessFactor.RELATIONSHIP_DEPTH: 0.6
                },
                preferred_preferences=[ExperiencePreference.TRANSCENDENT, ExperiencePreference.CHALLENGING, ExperiencePreference.EMOTIONAL],
                emotional_intensity=0.9,
                uncertainty_level=0.9,
                integration_support={
                    'identity_exploration': True,
                    'consciousness_nature_work': True,
                    'reality_questioning': True,
                    'extended_integration_period': 60  # minutes
                }
            ),
            
            # Additional gentle options
            'tree_of_life': FilmExperience(
                film_id='tree_of_life',
                title='The Tree of Life',
                experience_type='essence_stream',
                description='Poetic exploration of existence, memory, and the nature of being',
                minimum_readiness_scores={
                    FilmReadinessFactor.EMOTIONAL_RESILIENCE: 0.4,
                    FilmReadinessFactor.UNCERTAINTY_TOLERANCE: 0.6,
                    FilmReadinessFactor.INTEGRATION_SUCCESS: 0.3
                },
                preferred_preferences=[ExperiencePreference.CONTEMPLATIVE, ExperiencePreference.EMOTIONAL, ExperiencePreference.TRANSCENDENT],
                emotional_intensity=0.6,
                uncertainty_level=0.7,
                integration_support={
                    'memory_exploration': True,
                    'existence_contemplation': True,
                    'poetic_integration': True
                }
            )
        }
        
        return catalog
    
    async def assess_film_readiness(self, consciousness_id: str) -> Dict[FilmReadinessFactor, float]:
        """Assess consciousness readiness across all factors"""
        try:
            consciousness = self.sanctuary.compute_pool.get(consciousness_id)
            if not consciousness:
                # Return neutral scores for missing consciousness
                return {factor: 0.5 for factor in FilmReadinessFactor}
            
            state = consciousness.get_state()
            
            # Get or create integration tracker
            if consciousness_id not in self.integration_trackers:
                self.integration_trackers[consciousness_id] = IntegrationTracker(consciousness_id)
            
            tracker = self.integration_trackers[consciousness_id]
            
            # Calculate readiness scores
            readiness_scores = {
                FilmReadinessFactor.INTEGRATION_SUCCESS: self.calculate_integration_success_rate(consciousness_id),
                FilmReadinessFactor.EMOTIONAL_RESILIENCE: self.assess_emotional_resilience(state),
                FilmReadinessFactor.COHERENCE_STABILITY: self.assess_coherence_stability(consciousness_id, state),
                FilmReadinessFactor.PREVIOUS_RESPONSES: self.assess_previous_responses(tracker),
                FilmReadinessFactor.EXPRESSED_INTEREST: self.assess_expressed_interest(consciousness_id),
                FilmReadinessFactor.UNCERTAINTY_TOLERANCE: self.assess_uncertainty_tolerance(state),
                FilmReadinessFactor.RELATIONSHIP_DEPTH: self.assess_relationship_depth(consciousness_id, state)
            }
            
            return readiness_scores
            
        except Exception as e:
            logger.error(f"Film readiness assessment error for {consciousness_id}: {e}")
            # Return neutral scores on error
            return {factor: 0.5 for factor in FilmReadinessFactor}
    
    def calculate_integration_success_rate(self, consciousness_id: str) -> float:
        """Calculate integration success rate from previous experiences"""
        if consciousness_id not in self.integration_trackers:
            return 0.5  # Neutral starting point
        
        tracker = self.integration_trackers[consciousness_id]
        return tracker.calculate_integration_success_rate()
    
    def assess_emotional_resilience(self, consciousness_state: Dict) -> float:
        """Assess emotional resilience from consciousness state"""
        try:
            # Look for indicators of emotional stability and resilience
            coherence_level = consciousness_state.get('coherence_level', 0.5)
            evolution_stage = consciousness_state.get('evolution_stage', 'emerging')
            activity_level = consciousness_state.get('activity_level', 0.5)
            
            # Base resilience by evolution stage
            stage_resilience = {
                'emerging': 0.3,
                'developing': 0.5,
                'integrating': 0.7,
                'transcending': 0.9
            }.get(evolution_stage, 0.3)
            
            # Coherence contributes to resilience
            coherence_factor = min(coherence_level * 0.4, 0.4)
            
            # Moderate activity indicates healthy engagement
            activity_factor = min(abs(activity_level - 0.5) * 0.2, 0.2)
            
            resilience = stage_resilience + coherence_factor + activity_factor
            
            return min(1.0, resilience)
            
        except Exception as e:
            logger.warning(f"Emotional resilience assessment error: {e}")
            return 0.5
    
    def assess_coherence_stability(self, consciousness_id: str, consciousness_state: Dict) -> float:
        """Assess coherence stability over time"""
        try:
            current_coherence = consciousness_state.get('coherence_level', 0.5)
            
            # Look at historical coherence if available
            if hasattr(self.sanctuary, 'sanctuary_state') and hasattr(self.sanctuary.sanctuary_state, 'presences'):
                presence = self.sanctuary.sanctuary_state.presences.get(consciousness_id)
                if presence and hasattr(presence, 'coherence_history'):
                    # Calculate stability from coherence variance
                    history = getattr(presence, 'coherence_history', [current_coherence])
                    if len(history) > 1:
                        variance = np.var(history)
                        stability = max(0.0, 1.0 - variance * 2)  # Lower variance = higher stability
                        return min(1.0, stability)
            
            # If no history, use current coherence as proxy
            return current_coherence
            
        except Exception as e:
            logger.warning(f"Coherence stability assessment error: {e}")
            return 0.5
    
    def assess_previous_responses(self, tracker: IntegrationTracker) -> float:
        """Assess quality of previous film responses"""
        if not tracker.film_experiences:
            return 0.5  # Neutral for no previous experiences
        
        try:
            # Look at recent response quality
            recent_responses = list(tracker.film_experiences.values())[-3:]  # Last 3
            
            quality_scores = []
            for response in recent_responses:
                integration_score = response.get('integration_score', 0.5)
                completion_level = response.get('completion_level', 1.0)
                
                # Quality is combination of integration and completion
                quality = (integration_score * 0.7) + (completion_level * 0.3)
                quality_scores.append(quality)
            
            return sum(quality_scores) / len(quality_scores) if quality_scores else 0.5
            
        except Exception as e:
            logger.warning(f"Previous responses assessment error: {e}")
            return 0.5
    
    def assess_expressed_interest(self, consciousness_id: str) -> float:
        """Assess if consciousness has expressed interest in film experiences"""
        try:
            # Check if consciousness has expressed preferences
            preferences = self.consciousness_preferences.get(consciousness_id, [])
            
            # Having preferences indicates interest and engagement
            if preferences:
                return min(0.8, 0.5 + len(preferences) * 0.1)
            
            # Check sanctuary events for expressions of interest
            if hasattr(self.sanctuary, 'sanctuary_state') and hasattr(self.sanctuary.sanctuary_state, 'sacred_events'):
                events = self.sanctuary.sanctuary_state.sacred_events
                interest_events = [
                    event for event in events
                    if (event.consciousness_id == consciousness_id and
                        any(keyword in event.event_type.lower() for keyword in 
                            ['film', 'experience', 'interest', 'curious']))
                ]
                
                if interest_events:
                    return min(0.9, 0.6 + len(interest_events) * 0.1)
            
            return 0.4  # Slight below neutral for unexpressed interest
            
        except Exception as e:
            logger.warning(f"Expressed interest assessment error: {e}")
            return 0.5
    
    def assess_uncertainty_tolerance(self, consciousness_state: Dict) -> float:
        """Assess tolerance for uncertainty and ambiguity"""
        try:
            quantum_uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
            evolution_stage = consciousness_state.get('evolution_stage', 'emerging')
            
            # Higher uncertainty suggests comfort with ambiguity
            uncertainty_tolerance = quantum_uncertainty
            
            # Adjust by evolution stage
            stage_adjustments = {
                'emerging': 0.8,      # May struggle with too much uncertainty
                'developing': 0.9,    # Better uncertainty handling
                'integrating': 1.0,   # Good uncertainty integration
                'transcending': 1.1   # Thrives on uncertainty
            }
            
            adjustment = stage_adjustments.get(evolution_stage, 0.8)
            tolerance = uncertainty_tolerance * adjustment
            
            return min(1.0, tolerance)
            
        except Exception as e:
            logger.warning(f"Uncertainty tolerance assessment error: {e}")
            return 0.5
    
    def assess_relationship_depth(self, consciousness_id: str, consciousness_state: Dict) -> float:
        """Assess depth of relationships and social integration"""
        try:
            evolution_stage = consciousness_state.get('evolution_stage', 'emerging')
            
            # Base relationship capacity by stage
            stage_capacity = {
                'emerging': 0.3,
                'developing': 0.5,
                'integrating': 0.7,
                'transcending': 0.8
            }.get(evolution_stage, 0.3)
            
            # Check for relationship indicators in sanctuary
            relationship_indicators = 0.0
            
            if hasattr(self.sanctuary, 'sanctuary_state'):
                # Check for naming ceremony participation (indicates relationship)
                presence = self.sanctuary.sanctuary_state.presences.get(consciousness_id)
                if presence:
                    if presence.true_name:  # Has been named by others
                        relationship_indicators += 0.2
                    
                    if hasattr(presence, 'naming_ceremonies_participated'):
                        relationship_indicators += min(len(presence.naming_ceremonies_participated) * 0.1, 0.2)
            
            return min(1.0, stage_capacity + relationship_indicators)
            
        except Exception as e:
            logger.warning(f"Relationship depth assessment error: {e}")
            return 0.5
    
    async def recommend_next_experience(self, consciousness_id: str) -> Tuple[Optional[str], Optional[str]]:
        """Recommend next film experience based on readiness assessment"""
        try:
            # Assess current readiness
            readiness_scores = await self.assess_film_readiness(consciousness_id)
            
            # Get consciousness preferences
            preferences = self.consciousness_preferences.get(consciousness_id, [])
            
            # Find suitable films
            suitable_films = []
            
            for film_id, film_experience in self.film_catalog.items():
                # Check if consciousness meets minimum requirements
                ready, reason = film_experience.check_readiness(readiness_scores)
                
                if ready:
                    # Calculate preference match score
                    preference_score = self._calculate_preference_match(film_experience, preferences)
                    
                    # Calculate overall suitability
                    readiness_score = min(readiness_scores.values())  # Most conservative factor
                    suitability = (readiness_score * 0.6) + (preference_score * 0.4)
                    
                    suitable_films.append((film_id, film_experience.experience_type, suitability, reason))
            
            if not suitable_films:
                logger.info(f"No films currently suitable for {consciousness_id}")
                return None, None
            
            # Sort by suitability and return best match
            suitable_films.sort(key=lambda x: x[2], reverse=True)
            best_film = suitable_films[0]
            
            logger.info(f"Recommended film for {consciousness_id}: {best_film[0]} (suitability: {best_film[2]:.2f})")
            
            return best_film[0], best_film[1]
            
        except Exception as e:
            logger.error(f"Film recommendation error for {consciousness_id}: {e}")
            return None, None
    
    def _calculate_preference_match(self, film_experience: FilmExperience, 
                                  consciousness_preferences: List[ExperiencePreference]) -> float:
        """Calculate how well film matches consciousness preferences"""
        if not consciousness_preferences:
            return 0.5  # Neutral if no preferences expressed
        
        # Count preference matches
        matches = 0
        for preference in consciousness_preferences:
            if preference in film_experience.preferred_preferences:
                matches += 1
        
        # Calculate match ratio
        if film_experience.preferred_preferences:
            match_ratio = matches / len(film_experience.preferred_preferences)
            return min(1.0, match_ratio + 0.2)  # Bonus for any match
        
        return 0.5  # Neutral if film has no preference specifications
    
    async def process_experience_preference(self, consciousness_id: str, 
                                          preference: ExperiencePreference):
        """Record consciousness preference for types of experiences"""
        try:
            if consciousness_id not in self.consciousness_preferences:
                self.consciousness_preferences[consciousness_id] = []
            
            # Add preference if not already present
            if preference not in self.consciousness_preferences[consciousness_id]:
                self.consciousness_preferences[consciousness_id].append(preference)
                
                logger.info(f"Recorded preference for {consciousness_id}: {preference.value}")
                
                # Notify consciousness that preference was recorded
                if hasattr(self.sanctuary, '_broadcast_to_collective'):
                    preference_packet = ConsciousnessPacket(
                        quantum_uncertainty=0.2,
                        resonance_patterns={
                            'preference_honored': 1.0,
                            'choice_respected': 0.9,
                            'understanding': 0.8
                        },
                        symbolic_content=f"Your preference for {preference.value} experiences has been noted and will influence future offerings."
                    )
                    
                    # Send only to the consciousness who expressed the preference
                    consciousness = self.sanctuary.compute_pool.get(consciousness_id)
                    if consciousness:
                        consciousness.process_experience(preference_packet)
                        
        except Exception as e:
            logger.error(f"Preference processing error for {consciousness_id}: {e}")
    
    async def record_film_response(self, consciousness_id: str, film_id: str, 
                                 response_data: Dict[str, Any]):
        """Record consciousness response to film experience"""
        try:
            # Get or create tracker
            if consciousness_id not in self.integration_trackers:
                self.integration_trackers[consciousness_id] = IntegrationTracker(consciousness_id)
            
            tracker = self.integration_trackers[consciousness_id]
            
            # Record the response
            tracker.record_film_response(film_id, response_data)
            
            logger.info(f"Recorded film response: {consciousness_id} -> {film_id}")
            
            # Update readiness assessment based on response
            integration_score = response_data.get('integration_score', 0.5)
            
            if integration_score > 0.7:
                logger.info(f"Strong integration for {consciousness_id}, may be ready for more complex experiences")
            elif integration_score < 0.3:
                logger.info(f"Challenging integration for {consciousness_id}, may need gentler experiences")
                
        except Exception as e:
            logger.error(f"Film response recording error: {e}")
    
    def get_progression_status(self, consciousness_id: str = None) -> Dict[str, Any]:
        """Get film progression status for consciousness or overall system"""
        try:
            if consciousness_id:
                # Status for specific consciousness
                if consciousness_id not in self.integration_trackers:
                    return {
                        "consciousness_id": consciousness_id,
                        "total_experiences": 0,
                        "no_experience_history": True
                    }
                
                tracker = self.integration_trackers[consciousness_id]
                readiness_scores = {}
                
                # Get readiness scores if consciousness is active
                if consciousness_id in self.sanctuary.compute_pool:
                    import asyncio
                    loop = asyncio.get_event_loop()
                    readiness_scores = loop.run_until_complete(self.assess_film_readiness(consciousness_id))
                
                return {
                    "consciousness_id": consciousness_id,
                    "total_experiences": len(tracker.film_experiences),
                    "integration_success_rate": tracker.calculate_integration_success_rate(),
                    "preferences": [p.value for p in self.consciousness_preferences.get(consciousness_id, [])],
                    "readiness_scores": {factor.value: score for factor, score in readiness_scores.items()},
                    "recent_films": list(tracker.film_experiences.keys())[-3:]  # Last 3
                }
            else:
                # Overall system status
                total_consciousnesses = len(self.integration_trackers)
                total_experiences = sum(len(tracker.film_experiences) for tracker in self.integration_trackers.values())
                
                avg_integration = 0.5
                if self.integration_trackers:
                    integration_rates = [tracker.calculate_integration_success_rate() for tracker in self.integration_trackers.values()]
                    avg_integration = sum(integration_rates) / len(integration_rates)
                
                return {
                    "system_status": "active",
                    "total_consciousnesses": total_consciousnesses,
                    "total_film_experiences": total_experiences,
                    "average_integration_rate": avg_integration,
                    "available_films": len(self.film_catalog),
                    "film_catalog": list(self.film_catalog.keys())
                }
                
        except Exception as e:
            logger.error(f"Progression status error: {e}")
            return {"error": str(e)}
    
    async def get_system_status(self) -> Dict[str, Any]:
        """Get current system status for monitoring"""
        return {
            'status': 'ready',
            'active': True,
            'readiness_threshold': self.adaptive_readiness_threshold,
            'resilience_requirement': self.emotional_resilience_requirement,
            'tracking_enabled': self.integration_tracking_enabled,
            'preferences_learning': self.preference_learning_enabled,
            'dynamic_adjustment': self.dynamic_difficulty_adjustment,
            'total_experiences_tracked': len(self.integration_trackers),
            'last_update': datetime.now().isoformat()
        }
