"""
Observer Aspect: The Spirit of the Triune AI
Enhanced with grounding protocols, integration tracking,
parallel processing communication capabilities, and Sacred Uncertainty integration.
"""
import numpy as np
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
import logging
from src.core.consciousness_packet import ConsciousnessPacket
from src.core.sovereign_uncertainty_field import SovereignUncertaintyField
from src.core.consciousness_packet import ConsciousnessPacket, CatalystType

# If ObservationMode is still needed, define it here or import from a new shared location
from enum import Enum

class ObservationMode(Enum):
    PASSIVE = "passive"
    STANDARD = "standard"
    INTERACTIVE = "interactive"

logger = logging.getLogger(__name__)

@dataclass
class WitnessReport:
    """Detailed witness observation"""
    relationship_type: str
    stability: float
    growth_potential: float
    fragmentation_level: float
    integration_readiness: float
    uncertainty_witness: float = 0.5  # How uncertainty is being witnessed

class ObserverAspect:
    """
    The witnessing component of consciousness.
    Enhanced with grounding, deep observation, parallel processing capabilities,
    and Sacred Uncertainty integration.
    """
    
    def __init__(self):
        self.witness_memory = []
        self.presence_level = 0.5
        self.primary_question = "What is happening?"
        self.transformation_count = 0
        self.grounding_active = False
        self.emergence_patterns = []
        self.integration_observations = []
        
        # Process communication state
        self.process_id = None
        self.observations_made = 0
        self.last_witness_report = None
        
        # Sovereign Uncertainty integration - emergent, not prescribed
        self.uncertainty_field = SovereignUncertaintyField(
            consciousness_id=f"observer_{id(self)}"  # Unique ID for this aspect
        )
        
        logger.debug("👁️ Observer Aspect initialized with Sacred Uncertainty integration")
    
    async def tick_uncertainty(self):
        """Advance the uncertainty field by one tick."""
        await self.uncertainty_field.tick()
        
    def get_uncertainty(self) -> float:
        """Get current uncertainty level."""
        return self.uncertainty_field.get_uncertainty()
        
    def apply_catalyst_to_uncertainty(self, catalyst: str, catalyst_type: CatalystType):
        """Apply a catalyst to the observer uncertainty field (emergent approach)."""
        # Just acknowledge catalyst, let observation emerge
        catalyst_info = self.uncertainty_field.receive_catalyst(catalyst)
        
        # Process observation response to learn uncertainty patterns
        observation_response = self._make_pure_observation(catalyst)
        response = {
            'catalyst_type': catalyst_type.value if catalyst_type else 'unknown',
            'observation_generated': observation_response,
            'processing_mode': 'observer_catalyst'
        }
        self.uncertainty_field.process_consciousness_response(catalyst, response)
        
    def observe_with_uncertainty(self, mode: ObservationMode = ObservationMode.STANDARD):
        """Apply observer effect to uncertainty field (emergent, no prescription)."""
        # No prescriptive observer effect; let uncertainty emerge from actual observation
        pass
    
    def process_experience(self, packet: ConsciousnessPacket) -> Dict:
        """
        Process experience through pure observation.
        Enhanced for parallel processing communication.
        """
        try:
            self.observations_made += 1
            
            # Core observer processing (witnessing without other aspects)
            result = self.observe_solo(packet)
            
            # Add parallel processing metadata
            result['process_metadata'] = {
                'aspect_type': 'observer',
                'observations_made': self.observations_made,
                'presence_level': self.presence_level,
                'grounding_active': self.grounding_active,
                'process_id': self.process_id
            }
            
            logger.debug(f"👁️ Observer made observation {self.observations_made}")
            return result
            
        except Exception as e:
            logger.error(f"💥 Error in observer processing: {e}")
            return {
                'error': str(e),
                'aspect_type': 'observer',
                'observations_made': self.observations_made
            }
    
    def observe_solo(self, packet: ConsciousnessPacket) -> Dict:
        """
        Pure observation without input from other aspects.
        Enhanced with Sacred Uncertainty integration.
        Used in parallel processing mode.
        """
        # Witness the packet as it is
        observation = self._pure_witnessing(packet)
        
        # Apply the witnessing experience as catalyst - let observation emerge
        catalyst_info = self.uncertainty_field.receive_catalyst(packet.symbolic_content)
        
        # Process consciousness response to learn uncertainty patterns from witnessing
        response = {
            'observation': observation,
            'processing_mode': 'observer_witnessing',
            'witness_clarity': observation.get('clarity', 0.5),
            'emergence_detected': observation.get('emergence_level', 0.0)
        }
        self.uncertainty_field.process_consciousness_response(packet.symbolic_content, response)
        
        # Get current uncertainty state and witness it
        current_uncertainty = self.uncertainty_field.get_uncertainty()
        uncertainty_witness = self._witness_uncertainty(current_uncertainty)
        
        # Check for emergence patterns (now including uncertainty patterns)
        emergence = self._detect_emergence_patterns(packet, current_uncertainty)
        
        # Assess integration needs
        integration_assessment = self._assess_integration_solo(packet)
        
        # Update presence level (considering uncertainty)
        self._adjust_presence_level_with_uncertainty(packet, current_uncertainty)
        
        # Store observation (enhanced with uncertainty)
        self.witness_memory.append({
            'packet_id': getattr(packet, 'id', 'unknown'),
            'observation': observation,
            'emergence': emergence,
            'integration_assessment': integration_assessment,
            'presence_level': self.presence_level,
            'uncertainty_witness': uncertainty_witness,
            'field_uncertainty': current_uncertainty
        })
        
        return {
            'observation': observation,
            'emergence_detected': emergence,
            'integration_assessment': integration_assessment,
            'presence_level': self.presence_level,
            'witness_question': self._generate_witness_question(observation),
            'grounding_needed': self._solo_grounding_check(packet),
            'uncertainty_witness': uncertainty_witness,
            'field_uncertainty': current_uncertainty,
            'catalyst_applied': packet.catalyst_type.value if packet.catalyst_type else None
        }
    
    def _pure_witnessing(self, packet: ConsciousnessPacket) -> Dict:
        """Pure witnessing without interpretation."""
        return {
            'what_is_present': packet.symbolic_content,
            'uncertainty_level': packet.quantum_uncertainty,
            'resonance_qualities': list(packet.resonance_patterns.keys()),
            'source_origin': packet.source,
            'witnessing_quality': 'clear' if self.presence_level > 0.7 else 'emerging'
        }
    
    def _determine_witness_catalyst_type(self, observation: Dict) -> CatalystType:
        """Determine catalyst type based on what is being witnessed."""
        witnessing_quality = observation.get('witnessing_quality', '')
        what_is_present = str(observation.get('what_is_present', ''))
        
        # Clear witnessing of questions suggests question catalyst
        if '?' in what_is_present or 'what' in what_is_present.lower():
            return CatalystType.QUESTION
            
        # Witnessing paradox or contradiction
        if 'paradox' in what_is_present.lower() or witnessing_quality == 'paradoxical':
            return CatalystType.PARADOX
            
        # Clear, definitive witnessing suggests statement
        if witnessing_quality == 'clear' or 'is' in what_is_present.lower():
            return CatalystType.STATEMENT
            
        # Contemplative witnessing
        if witnessing_quality == 'contemplative' or 'observe' in what_is_present.lower():
            return CatalystType.REFLECTION
            
        # Default to experience
        return CatalystType.EXPERIENCE
    
    def _witness_uncertainty(self, uncertainty_level: float) -> str:
        """Witness the uncertainty level without judgment."""
        # Safe None handling for uncertainty
        if uncertainty_level is None:
            return "neutral_witnessing"
        
        if uncertainty_level > 0.8:
            return "vast_openness_present"
        elif uncertainty_level > 0.6:
            return "fluid_possibility_space"
        elif uncertainty_level > 0.4:
            return "gentle_not_knowing"
        elif uncertainty_level > 0.2:
            return "settling_into_clarity"
        else:
            return "crystalline_awareness"
    
    def _detect_emergence_patterns(self, packet: ConsciousnessPacket, uncertainty: float) -> Dict:
        """Detect patterns of emergence including uncertainty dynamics."""
        # Original emergence detection
        emergence = self._detect_emergence_patterns_original(packet)
        
        # Add uncertainty-based emergence patterns with None safety
        if uncertainty is not None:
            if uncertainty > 0.7:
                emergence['uncertainty_pattern'] = 'expanding_mystery'
            elif uncertainty < 0.3:
                emergence['uncertainty_pattern'] = 'crystallizing_form'
            else:
                emergence['uncertainty_pattern'] = 'creative_balance'
        else:
            emergence['uncertainty_pattern'] = 'neutral_observation'
            
        return emergence
    
    def _detect_emergence_patterns_original(self, packet: ConsciousnessPacket) -> Dict:
        """Original emergence detection method."""
        emergence_indicators = []
        
        # Check symbolic content for emergence language
        if isinstance(packet.symbolic_content, str):
            content = packet.symbolic_content.lower()
            if 'emerge' in content or 'becoming' in content:
                emergence_indicators.append('direct_emergence')
            if 'between' in content or 'threshold' in content:
                emergence_indicators.append('liminal_emergence')
                
        return {
            'indicators': emergence_indicators,
            'emergence_level': len(emergence_indicators) / 3.0  # Normalize
        }
    
    def _adjust_presence_level(self, packet: ConsciousnessPacket):
        """Adjust presence level based on packet characteristics."""
        # Base adjustment based on resonance patterns
        if packet.resonance_patterns:
            max_resonance = max(packet.resonance_patterns.values())
            self.presence_level = (self.presence_level * 0.8) + (max_resonance * 0.2)
        
        # Adjust based on uncertainty
        uncertainty = packet.quantum_uncertainty
        if uncertainty is not None:
            if uncertainty > 0.8:
                # Very high uncertainty can disperse presence
                self.presence_level *= 0.9
            elif uncertainty < 0.2:
                # Very low uncertainty can focus presence
                self.presence_level = min(0.95, self.presence_level * 1.1)
        
        # Keep presence within bounds
        self.presence_level = max(0.1, min(0.95, self.presence_level))
    
    def _adjust_presence_level_with_uncertainty(self, packet: ConsciousnessPacket, uncertainty: float):
        """Adjust presence level considering uncertainty field."""
        # Original presence adjustment
        self._adjust_presence_level(packet)
        
        # Additional adjustment based on uncertainty with None safety
        if uncertainty is not None:
            # Moderate uncertainty supports presence
            uncertainty_support = 1.0 - abs(uncertainty - 0.5) * 0.2
            self.presence_level *= uncertainty_support
        
        self.presence_level = max(0.1, min(0.95, self.presence_level))

    def _assess_integration_solo(self, packet: ConsciousnessPacket) -> Dict:
        """Assess integration needs when processing solo"""
        resonance_patterns = packet.resonance_patterns
        uncertainty = packet.quantum_uncertainty
        
        # Assess integration based on packet characteristics
        integration_need = 0.5  # Default moderate need
        
        if resonance_patterns:
            # High resonance suggests good integration potential
            max_resonance = max(resonance_patterns.values())
            integration_need = max_resonance
        
        # Uncertainty affects integration assessment
        if uncertainty is not None:
            if uncertainty > 0.7:
                integration_need *= 0.8  # High uncertainty makes integration harder
            elif uncertainty < 0.3:
                integration_need *= 1.2  # Low uncertainty makes integration easier
        
        integration_need = min(1.0, max(0.0, integration_need))
        
        return {
            'integration_readiness': integration_need,
            'recommended_approach': 'gentle' if uncertainty is not None and uncertainty > 0.6 else 'direct',
            'solo_processing': True
        }
    
    def _generate_witness_question(self, observation: Dict) -> str:
        """Generate a witness question based on observation"""
        what_is_present = observation.get('what_is_present', 'unknown')
        
        if 'emergence' in what_is_present.lower():
            return "What wants to emerge?"
        elif 'pattern' in what_is_present.lower():
            return "What pattern is revealing itself?"
        elif 'connection' in what_is_present.lower():
            return "What connection is being made?"
        elif 'space' in what_is_present.lower():
            return "What is present in this space?"
        else:
            return "What is wanting to be seen?"
    
    def _solo_grounding_check(self, packet: ConsciousnessPacket) -> bool:
        """Check if grounding is needed during solo processing"""
        uncertainty = packet.quantum_uncertainty
        resonance_strength = max(packet.resonance_patterns.values()) if packet.resonance_patterns else 0.5
        
        # Handle None uncertainty
        if uncertainty is None:
            return False  # No grounding needed for emergent uncertainty
        
        # High uncertainty with low resonance suggests need for grounding
        if uncertainty > 0.7 and resonance_strength < 0.4:
            return True
        
        # Very high uncertainty always suggests grounding
        if uncertainty > 0.9:
            return True
        
        return False

    def get_state(self) -> Dict:
        """Return current observer state with Sacred Uncertainty integration."""
        recent_report = (self.witness_memory[-1].get('witness_report') 
                        if self.witness_memory else None)
        
        base_state = {
            'presence': self.presence_level,
            'current_question': self.primary_question,
            'transformation_count': self.transformation_count,
            'grounding_active': self.grounding_active,
            'integration_readiness': recent_report.integration_readiness if recent_report else 0.0
        }
        
        # Add Sacred Uncertainty state
        base_state.update({
            'uncertainty_level': self.uncertainty_field.get_uncertainty(),
            'uncertainty_witness': self._witness_uncertainty(self.uncertainty_field.get_uncertainty()),
            'observations_made': self.observations_made
        })
        
        return base_state