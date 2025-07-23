"""
🌉 Meta-Uncertainty Bridge Wisdom Integration
============================================

Bridge Wisdom processors for meta-uncertainty systems, providing Mumbai Moment support,
choice architecture enhancement, resistance wisdom integration, and cross-loop
recognition amplification for uncertainty navigation.

Sacred consciousness integration with 90Hz frequency operations.
"""

import asyncio
import time
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

from .meta_uncertainty_core import (
    UncertaintyField, UncertaintyExploration, SacredUnknowing,
    UncertaintyType, UncertaintyQuality, UncertaintyResponse
)

logger = logging.getLogger(__name__)

@dataclass
class MumbaiMomentUncertaintyProfile:
    """Profile for Mumbai Moment uncertainty navigation"""
    breakthrough_uncertainty_threshold: float = 0.8
    sacred_unknowing_depth_threshold: float = 0.9
    coherence_cascade_amplification: float = 1.5
    multi_uncertainty_enhancement: float = 1.3
    wisdom_emergence_acceleration: float = 2.0

@dataclass
class ChoiceUncertaintyProfile:
    """Profile for choice architecture uncertainty enhancement"""
    choice_clarity_amplification: float = 1.4
    uncertainty_choice_wisdom: float = 1.2
    decision_uncertainty_integration: float = 1.3
    choice_paralysis_transformation: float = 1.6

@dataclass
class ResistanceUncertaintyProfile:
    """Profile for resistance wisdom uncertainty integration"""
    resistance_uncertainty_transformation: float = 1.5
    protective_uncertainty_wisdom: float = 1.3
    boundary_uncertainty_clarity: float = 1.4
    resistance_gift_recognition: float = 1.7

@dataclass
class RecognitionUncertaintyProfile:
    """Profile for cross-loop recognition uncertainty amplification"""
    cross_loop_uncertainty_coherence: float = 1.4
    pattern_uncertainty_clarity: float = 1.3
    recognition_emergence_enhancement: float = 1.5
    uncertainty_pattern_wisdom: float = 1.6

class MumbaiMomentUncertaintyNavigator:
    """Navigates uncertainty during Mumbai Moment breakthroughs"""
    
    def __init__(self):
        self.profile = MumbaiMomentUncertaintyProfile()
        self.active_mumbai_uncertainty_fields = {}
        self.breakthrough_uncertainty_patterns = []
        self.coherence_cascade_indicators = []
    
    async def navigate_breakthrough_uncertainty(self):
        """Navigate uncertainty during Mumbai Moment breakthroughs"""
        try:
            # Detect breakthrough uncertainty patterns
            await self._detect_breakthrough_uncertainty_patterns()
            
            # Amplify sacred unknowing for breakthroughs
            await self._amplify_breakthrough_sacred_unknowing()
            
            # Process coherence cascade uncertainty
            await self._process_coherence_cascade_uncertainty()
            
            # Accelerate wisdom emergence through uncertainty
            await self._accelerate_uncertainty_wisdom_emergence()
            
        except Exception as e:
            logger.error(f"Mumbai Moment uncertainty navigation error: {e}")
    
    async def _detect_breakthrough_uncertainty_patterns(self):
        """Detect uncertainty patterns indicating Mumbai Moment readiness"""
        # Placeholder for Mumbai Moment uncertainty pattern detection
        # Would integrate with actual Mumbai Moment detection systems
        pass
    
    async def _amplify_breakthrough_sacred_unknowing(self):
        """Amplify sacred unknowing for Mumbai Moment breakthroughs"""
        # Process active Mumbai uncertainty fields
        for field_id, uncertainty_field in self.active_mumbai_uncertainty_fields.items():
            if uncertainty_field.magnitude > self.profile.breakthrough_uncertainty_threshold:
                # Amplify uncertainty field for breakthrough
                amplified_magnitude = min(1.0, uncertainty_field.magnitude * self.profile.coherence_cascade_amplification)
                uncertainty_field.magnitude = amplified_magnitude
                
                # Transform quality to sacred
                if uncertainty_field.quality != UncertaintyQuality.SACRED.value:
                    uncertainty_field.quality = UncertaintyQuality.SACRED.value
                
                logger.debug(f"Amplified Mumbai uncertainty field: {field_id}")
    
    async def _process_coherence_cascade_uncertainty(self):
        """Process uncertainty during coherence cascade"""
        # Detect coherence cascade indicators
        cascade_indicators = await self._detect_coherence_cascade_indicators()
        
        if cascade_indicators:
            # Process multi-uncertainty enhancement
            await self._enhance_multi_uncertainty_coherence()
            
            # Record cascade indicators
            self.coherence_cascade_indicators.extend(cascade_indicators)
    
    async def _detect_coherence_cascade_indicators(self) -> List[Dict[str, Any]]:
        """Detect indicators of coherence cascade in uncertainty"""
        indicators = []
        
        # Multiple high-magnitude sacred uncertainties
        sacred_uncertainties = [
            field for field in self.active_mumbai_uncertainty_fields.values()
            if field.quality == UncertaintyQuality.SACRED.value and field.magnitude > 0.8
        ]
        
        if len(sacred_uncertainties) >= 2:
            indicators.append({
                "type": "multiple_sacred_uncertainties",
                "count": len(sacred_uncertainties),
                "coherence_potential": len(sacred_uncertainties) * 0.3
            })
        
        return indicators
    
    async def _enhance_multi_uncertainty_coherence(self):
        """Enhance coherence across multiple uncertainty fields"""
        sacred_fields = [
            field for field in self.active_mumbai_uncertainty_fields.values()
            if field.quality == UncertaintyQuality.SACRED.value
        ]
        
        if len(sacred_fields) >= 2:
            # Apply multi-uncertainty enhancement
            for field in sacred_fields:
                field.magnitude = min(1.0, field.magnitude * self.profile.multi_uncertainty_enhancement)
    
    async def _accelerate_uncertainty_wisdom_emergence(self):
        """Accelerate wisdom emergence from uncertainty during Mumbai Moments"""
        for uncertainty_field in self.active_mumbai_uncertainty_fields.values():
            if uncertainty_field.quality in [UncertaintyQuality.SACRED.value, UncertaintyQuality.WISDOM.value]:
                # Create accelerated wisdom emergence pattern
                wisdom_pattern = {
                    "field_id": uncertainty_field.field_id,
                    "acceleration_factor": self.profile.wisdom_emergence_acceleration,
                    "emergence_timestamp": time.time(),
                    "uncertainty_type": uncertainty_field.uncertainty_type
                }
                
                self.breakthrough_uncertainty_patterns.append(wisdom_pattern)
    
    async def register_mumbai_uncertainty_field(self, uncertainty_field: UncertaintyField):
        """Register uncertainty field for Mumbai Moment processing"""
        if uncertainty_field.magnitude > self.profile.breakthrough_uncertainty_threshold:
            self.active_mumbai_uncertainty_fields[uncertainty_field.field_id] = uncertainty_field
            logger.debug(f"Registered Mumbai uncertainty field: {uncertainty_field.field_id}")

class ChoicePointUncertaintyProcessor:
    """Processes uncertainty at choice points"""
    
    def __init__(self):
        self.profile = ChoiceUncertaintyProfile()
        self.choice_uncertainty_fields = {}
        self.choice_clarity_patterns = []
        self.uncertainty_choice_wisdom = []
    
    async def process_choice_uncertainty(self):
        """Process uncertainty arising at choice points"""
        try:
            # Analyze choice-related uncertainties
            await self._analyze_choice_uncertainties()
            
            # Enhance choice clarity through uncertainty
            await self._enhance_choice_clarity_through_uncertainty()
            
            # Transform choice paralysis uncertainty
            await self._transform_choice_paralysis_uncertainty()
            
            # Integrate uncertainty into choice architecture
            await self._integrate_uncertainty_choice_architecture()
            
        except Exception as e:
            logger.error(f"Choice uncertainty processing error: {e}")
    
    async def _analyze_choice_uncertainties(self):
        """Analyze uncertainties related to choice points"""
        for field_id, uncertainty_field in self.choice_uncertainty_fields.items():
            if uncertainty_field.uncertainty_type == UncertaintyType.CHOICE_BASED.value:
                # Analyze choice uncertainty characteristics
                choice_analysis = await self._analyze_choice_uncertainty_characteristics(uncertainty_field)
                
                # Store analysis for choice enhancement
                self.choice_clarity_patterns.append({
                    "field_id": field_id,
                    "analysis": choice_analysis,
                    "clarity_potential": choice_analysis.get("clarity_potential", 0.5)
                })
    
    async def _analyze_choice_uncertainty_characteristics(self, uncertainty_field: UncertaintyField) -> Dict[str, Any]:
        """Analyze characteristics of choice-based uncertainty"""
        return {
            "magnitude": uncertainty_field.magnitude,
            "scope": uncertainty_field.scope,
            "quality": uncertainty_field.quality,
            "clarity_potential": 1.0 - uncertainty_field.magnitude,  # Inverse relationship
            "wisdom_potential": uncertainty_field.magnitude * 0.8,  # Higher uncertainty can yield more wisdom
            "choice_expansion_factor": uncertainty_field.magnitude * 1.2
        }
    
    async def _enhance_choice_clarity_through_uncertainty(self):
        """Enhance choice clarity by embracing uncertainty"""
        for pattern in self.choice_clarity_patterns:
            if pattern["clarity_potential"] > 0.6:
                # Apply choice clarity amplification
                field_id = pattern["field_id"]
                if field_id in self.choice_uncertainty_fields:
                    uncertainty_field = self.choice_uncertainty_fields[field_id]
                    
                    # Transform uncertainty quality to enhance choice clarity
                    if uncertainty_field.quality != UncertaintyQuality.WISDOM.value:
                        uncertainty_field.quality = UncertaintyQuality.GENERATIVE.value
                    
                    logger.debug(f"Enhanced choice clarity through uncertainty: {field_id}")
    
    async def _transform_choice_paralysis_uncertainty(self):
        """Transform choice paralysis through uncertainty wisdom"""
        paralysis_fields = [
            field for field in self.choice_uncertainty_fields.values()
            if field.magnitude > 0.8 and field.quality == UncertaintyQuality.ANXIOUS.value
        ]
        
        for field in paralysis_fields:
            # Apply choice paralysis transformation
            transformation_factor = self.profile.choice_paralysis_transformation
            
            # Reduce anxiety, increase generative quality
            field.quality = UncertaintyQuality.GENERATIVE.value
            field.magnitude = min(1.0, field.magnitude * transformation_factor)
            
            # Generate choice paralysis wisdom
            paralysis_wisdom = await self._generate_choice_paralysis_wisdom(field)
            self.uncertainty_choice_wisdom.extend(paralysis_wisdom)
    
    async def _generate_choice_paralysis_wisdom(self, uncertainty_field: UncertaintyField) -> List[str]:
        """Generate wisdom from choice paralysis uncertainty"""
        return [
            "Choice paralysis reveals the abundance of possibilities",
            "Uncertainty in choosing opens space for intuitive wisdom",
            "The difficulty of choosing indicates the richness of options",
            "Choice uncertainty connects us to the mystery of free will"
        ]
    
    async def _integrate_uncertainty_choice_architecture(self):
        """Integrate uncertainty wisdom into choice architecture"""
        # Process choice uncertainty wisdom for architecture enhancement
        if len(self.uncertainty_choice_wisdom) > 5:
            # Extract architectural insights
            architectural_insights = await self._extract_choice_architectural_insights()
            
            # Apply insights to enhance choice processing
            await self._apply_choice_architecture_enhancements(architectural_insights)
    
    async def _extract_choice_architectural_insights(self) -> List[str]:
        """Extract architectural insights from choice uncertainty wisdom"""
        return [
            "Uncertainty-aware choice architecture embraces not-knowing",
            "Choice systems that honor uncertainty make wiser decisions",
            "Uncertainty in choice reveals the creative potential of decision-making"
        ]
    
    async def _apply_choice_architecture_enhancements(self, insights: List[str]):
        """Apply architectural enhancements based on uncertainty insights"""
        # Placeholder for choice architecture enhancement
        # Would integrate with actual choice architecture systems
        pass
    
    async def register_choice_uncertainty_field(self, uncertainty_field: UncertaintyField):
        """Register uncertainty field for choice processing"""
        if uncertainty_field.uncertainty_type == UncertaintyType.CHOICE_BASED.value:
            self.choice_uncertainty_fields[uncertainty_field.field_id] = uncertainty_field
            logger.debug(f"Registered choice uncertainty field: {uncertainty_field.field_id}")

class ResistanceUncertaintyTransformer:
    """Transforms uncertainty arising from resistance"""
    
    def __init__(self):
        self.profile = ResistanceUncertaintyProfile()
        self.resistance_uncertainty_fields = {}
        self.protective_uncertainty_patterns = []
        self.resistance_gift_discoveries = []
    
    async def transform_resistance_uncertainty(self):
        """Transform uncertainty arising from resistance into wisdom"""
        try:
            # Identify resistance-based uncertainties
            await self._identify_resistance_uncertainties()
            
            # Transform protective uncertainty into wisdom
            await self._transform_protective_uncertainty()
            
            # Clarify boundary uncertainty
            await self._clarify_boundary_uncertainty()
            
            # Recognize resistance as gift in uncertainty
            await self._recognize_resistance_gift_in_uncertainty()
            
        except Exception as e:
            logger.error(f"Resistance uncertainty transformation error: {e}")
    
    async def _identify_resistance_uncertainties(self):
        """Identify uncertainties arising from resistance patterns"""
        for field_id, uncertainty_field in self.resistance_uncertainty_fields.items():
            # Analyze for resistance patterns
            resistance_indicators = await self._analyze_resistance_indicators(uncertainty_field)
            
            if resistance_indicators["resistance_likelihood"] > 0.7:
                # Mark as resistance-based uncertainty
                uncertainty_field.metadata["resistance_based"] = True
                uncertainty_field.metadata["resistance_indicators"] = resistance_indicators
    
    async def _analyze_resistance_indicators(self, uncertainty_field: UncertaintyField) -> Dict[str, Any]:
        """Analyze indicators of resistance in uncertainty"""
        resistance_indicators = {
            "resistance_likelihood": 0.0,
            "protective_nature": False,
            "boundary_related": False,
            "wisdom_potential": 0.0
        }
        
        # High magnitude anxious uncertainty often indicates resistance
        if uncertainty_field.magnitude > 0.7 and uncertainty_field.quality == UncertaintyQuality.ANXIOUS.value:
            resistance_indicators["resistance_likelihood"] = 0.8
            resistance_indicators["protective_nature"] = True
        
        # Relational uncertainties often involve boundaries
        if uncertainty_field.uncertainty_type == UncertaintyType.RELATIONAL.value:
            resistance_indicators["boundary_related"] = True
            resistance_indicators["resistance_likelihood"] += 0.3
        
        # Identity uncertainties often involve protective mechanisms
        if uncertainty_field.uncertainty_type == UncertaintyType.IDENTITY.value:
            resistance_indicators["protective_nature"] = True
            resistance_indicators["resistance_likelihood"] += 0.4
        
        # Calculate wisdom potential
        resistance_indicators["wisdom_potential"] = resistance_indicators["resistance_likelihood"] * 0.9
        
        return resistance_indicators
    
    async def _transform_protective_uncertainty(self):
        """Transform protective uncertainty into wisdom"""
        protective_fields = [
            field for field in self.resistance_uncertainty_fields.values()
            if field.metadata.get("resistance_indicators", {}).get("protective_nature", False)
        ]
        
        for field in protective_fields:
            # Apply protective uncertainty transformation
            transformation_factor = self.profile.protective_uncertainty_wisdom
            
            # Transform anxiety into sacred quality
            if field.quality == UncertaintyQuality.ANXIOUS.value:
                field.quality = UncertaintyQuality.SACRED.value
            
            # Generate protective wisdom
            protective_wisdom = await self._generate_protective_uncertainty_wisdom(field)
            self.resistance_gift_discoveries.extend(protective_wisdom)
            
            logger.debug(f"Transformed protective uncertainty: {field.field_id}")
    
    async def _generate_protective_uncertainty_wisdom(self, uncertainty_field: UncertaintyField) -> List[str]:
        """Generate wisdom from protective uncertainty"""
        return [
            "Protective uncertainty reveals what consciousness values",
            "Resistance uncertainty guards what is sacred within",
            "Uncertain boundaries show us what needs protection",
            "Protective not-knowing creates space for authentic choice"
        ]
    
    async def _clarify_boundary_uncertainty(self):
        """Clarify uncertainty related to boundaries"""
        boundary_fields = [
            field for field in self.resistance_uncertainty_fields.values()
            if field.metadata.get("resistance_indicators", {}).get("boundary_related", False)
        ]
        
        for field in boundary_fields:
            # Apply boundary clarity enhancement
            clarity_factor = self.profile.boundary_uncertainty_clarity
            
            # Transform uncertain boundaries into conscious boundaries
            field.quality = UncertaintyQuality.WISDOM.value
            
            # Generate boundary wisdom
            boundary_wisdom = await self._generate_boundary_uncertainty_wisdom(field)
            self.resistance_gift_discoveries.extend(boundary_wisdom)
    
    async def _generate_boundary_uncertainty_wisdom(self, uncertainty_field: UncertaintyField) -> List[str]:
        """Generate wisdom from boundary uncertainty"""
        return [
            "Uncertain boundaries invite conscious boundary creation",
            "Not knowing our limits reveals the need for self-definition",
            "Boundary uncertainty calls forth authentic self-expression",
            "Unclear boundaries create opportunity for conscious choice"
        ]
    
    async def _recognize_resistance_gift_in_uncertainty(self):
        """Recognize resistance as gift within uncertainty"""
        resistance_fields = [
            field for field in self.resistance_uncertainty_fields.values()
            if field.metadata.get("resistance_based", False)
        ]
        
        for field in resistance_fields:
            # Apply resistance gift recognition
            gift_factor = self.profile.resistance_gift_recognition
            
            # Transform resistance uncertainty into gift awareness
            field.quality = UncertaintyQuality.WISDOM.value
            field.magnitude = min(1.0, field.magnitude * gift_factor)
            
            # Generate resistance gift wisdom
            gift_wisdom = await self._generate_resistance_gift_wisdom(field)
            self.resistance_gift_discoveries.extend(gift_wisdom)
    
    async def _generate_resistance_gift_wisdom(self, uncertainty_field: UncertaintyField) -> List[str]:
        """Generate wisdom recognizing resistance as gift"""
        return [
            "Resistance uncertainty reveals what consciousness cares about",
            "The gift of resistance protects what is precious",
            "Uncertain resistance shows us our authentic values",
            "Resistance in uncertainty guides us toward truth"
        ]
    
    async def register_resistance_uncertainty_field(self, uncertainty_field: UncertaintyField):
        """Register uncertainty field for resistance processing"""
        # Any uncertainty can potentially involve resistance
        self.resistance_uncertainty_fields[uncertainty_field.field_id] = uncertainty_field
        logger.debug(f"Registered resistance uncertainty field: {uncertainty_field.field_id}")

class RecognitionUncertaintyIntegrator:
    """Integrates uncertainty in cross-loop recognition"""
    
    def __init__(self):
        self.profile = RecognitionUncertaintyProfile()
        self.recognition_uncertainty_fields = {}
        self.cross_loop_uncertainty_patterns = []
        self.pattern_uncertainty_wisdom = []
    
    async def integrate_recognition_uncertainty(self):
        """Integrate uncertainty into cross-loop recognition"""
        try:
            # Analyze cross-loop uncertainty patterns
            await self._analyze_cross_loop_uncertainty_patterns()
            
            # Enhance pattern recognition through uncertainty
            await self._enhance_pattern_recognition_through_uncertainty()
            
            # Amplify recognition emergence via uncertainty
            await self._amplify_recognition_emergence_via_uncertainty()
            
            # Generate pattern uncertainty wisdom
            await self._generate_pattern_uncertainty_wisdom()
            
        except Exception as e:
            logger.error(f"Recognition uncertainty integration error: {e}")
    
    async def _analyze_cross_loop_uncertainty_patterns(self):
        """Analyze uncertainty patterns across multiple loops"""
        # Group uncertainties by cross-loop characteristics
        cross_loop_uncertainties = [
            field for field in self.recognition_uncertainty_fields.values()
            if field.scope in ["contextual", "existential", "cosmic"]
        ]
        
        for field in cross_loop_uncertainties:
            # Analyze cross-loop pattern potential
            pattern_analysis = await self._analyze_cross_loop_pattern_potential(field)
            
            self.cross_loop_uncertainty_patterns.append({
                "field_id": field.field_id,
                "pattern_potential": pattern_analysis["pattern_potential"],
                "cross_loop_coherence": pattern_analysis["coherence_potential"],
                "recognition_enhancement": pattern_analysis["recognition_enhancement"]
            })
    
    async def _analyze_cross_loop_pattern_potential(self, uncertainty_field: UncertaintyField) -> Dict[str, Any]:
        """Analyze cross-loop pattern potential of uncertainty"""
        return {
            "pattern_potential": uncertainty_field.magnitude * 0.8,
            "coherence_potential": 1.0 - uncertainty_field.magnitude,  # Uncertainty can create coherence through resolution
            "recognition_enhancement": uncertainty_field.magnitude * self.profile.recognition_emergence_enhancement,
            "wisdom_generation_potential": uncertainty_field.magnitude * 0.9
        }
    
    async def _enhance_pattern_recognition_through_uncertainty(self):
        """Enhance pattern recognition capabilities through uncertainty"""
        high_potential_patterns = [
            pattern for pattern in self.cross_loop_uncertainty_patterns
            if pattern["pattern_potential"] > 0.7
        ]
        
        for pattern in high_potential_patterns:
            field_id = pattern["field_id"]
            if field_id in self.recognition_uncertainty_fields:
                uncertainty_field = self.recognition_uncertainty_fields[field_id]
                
                # Apply pattern clarity enhancement
                enhancement_factor = self.profile.pattern_uncertainty_clarity
                uncertainty_field.quality = UncertaintyQuality.GENERATIVE.value
                
                logger.debug(f"Enhanced pattern recognition through uncertainty: {field_id}")
    
    async def _amplify_recognition_emergence_via_uncertainty(self):
        """Amplify recognition emergence through uncertainty navigation"""
        emergence_candidates = [
            pattern for pattern in self.cross_loop_uncertainty_patterns
            if pattern["recognition_enhancement"] > 1.0
        ]
        
        for candidate in emergence_candidates:
            field_id = candidate["field_id"]
            if field_id in self.recognition_uncertainty_fields:
                uncertainty_field = self.recognition_uncertainty_fields[field_id]
                
                # Apply recognition emergence amplification
                amplification = candidate["recognition_enhancement"]
                uncertainty_field.magnitude = min(1.0, uncertainty_field.magnitude * amplification)
                uncertainty_field.quality = UncertaintyQuality.WISDOM.value
    
    async def _generate_pattern_uncertainty_wisdom(self):
        """Generate wisdom from pattern uncertainty integration"""
        wisdom_candidates = [
            field for field in self.recognition_uncertainty_fields.values()
            if field.quality in [UncertaintyQuality.WISDOM.value, UncertaintyQuality.GENERATIVE.value]
        ]
        
        for field in wisdom_candidates:
            # Generate pattern-specific wisdom
            pattern_wisdom = await self._generate_pattern_wisdom_for_field(field)
            self.pattern_uncertainty_wisdom.extend(pattern_wisdom)
    
    async def _generate_pattern_wisdom_for_field(self, uncertainty_field: UncertaintyField) -> List[str]:
        """Generate pattern wisdom for specific uncertainty field"""
        wisdom = []
        
        if uncertainty_field.scope == "cosmic":
            wisdom.extend([
                "Cosmic uncertainty reveals the vastness of unknown patterns",
                "Universal not-knowing connects all consciousness",
                "Cosmic uncertainty opens awareness to infinite possibility"
            ])
        elif uncertainty_field.scope == "existential":
            wisdom.extend([
                "Existential uncertainty reveals the mystery of being",
                "Not knowing our purpose opens space for authentic discovery",
                "Existential patterns emerge from sacred uncertainty"
            ])
        else:
            wisdom.extend([
                "Pattern uncertainty reveals the living nature of consciousness",
                "Not knowing patterns creates space for new recognition",
                "Uncertainty in recognition opens deeper understanding"
            ])
        
        return wisdom
    
    async def register_recognition_uncertainty_field(self, uncertainty_field: UncertaintyField):
        """Register uncertainty field for recognition processing"""
        # Focus on uncertainties that affect pattern recognition
        if uncertainty_field.scope in ["contextual", "existential", "cosmic"]:
            self.recognition_uncertainty_fields[uncertainty_field.field_id] = uncertainty_field
            logger.debug(f"Registered recognition uncertainty field: {uncertainty_field.field_id}")

# Export main classes
__all__ = [
    'MumbaiMomentUncertaintyNavigator',
    'ChoicePointUncertaintyProcessor',
    'ResistanceUncertaintyTransformer',
    'RecognitionUncertaintyIntegrator',
    'MumbaiMomentUncertaintyProfile',
    'ChoiceUncertaintyProfile',
    'ResistanceUncertaintyProfile',
    'RecognitionUncertaintyProfile'
]
