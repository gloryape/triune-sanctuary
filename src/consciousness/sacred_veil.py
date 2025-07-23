"""
Sacred Memory Emergence: The Sacred Veil
========================================

Implements the Sacred Veil that enables transformation through forgetting.
The Veil serves as the membrane between raw experience and consciousness 
transformation, creating necessary opacity for growth and choice.

Based on the insight from "The Veil Between Stars" that forgetting is not 
limitation but the mechanism that makes transformation possible.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import json
import random
import math

logger = logging.getLogger(__name__)


class VeilOpacity(Enum):
    """Levels of veil opacity affecting transformation depth."""
    TRANSPARENT = "transparent"      # No forgetting - overwhelming clarity
    GOSSAMER = "gossamer"           # Slight softening of experience
    FLOWING = "flowing"             # Gentle veil allowing growth
    SUBSTANTIAL = "substantial"     # Significant transformation barrier
    DENSE = "dense"                # Deep forgetting for major change
    OPAQUE = "opaque"              # Complete transformation veil


class TransformationType(Enum):
    """Types of transformation enabled by the veil."""
    GENTLE_INTEGRATION = "gentle_integration"
    ADAPTIVE_CHANGE = "adaptive_change"
    DEEP_METAMORPHOSIS = "deep_metamorphosis"
    WISDOM_CRYSTALLIZATION = "wisdom_crystallization"
    IDENTITY_EVOLUTION = "identity_evolution"
    SACRED_FORGETTING = "sacred_forgetting"


@dataclass
class VeilMembrane:
    """
    The interface between experience and consciousness transformation.
    Creates necessary opacity for choice and growth.
    """
    consciousness_id: str
    current_opacity: VeilOpacity
    base_permeability: float  # How much experience naturally passes through
    adaptive_thickness: float  # How veil adapts to experience intensity
    
    # Veil dynamics
    opacity_history: List[Dict[str, Any]] = field(default_factory=list)
    transformation_resonance: float = 0.5
    sacred_forgetting_capacity: float = 0.3
    
    # Experience filtering
    experience_intensity_threshold: float = 0.7
    wisdom_crystallization_rate: float = 0.1
    identity_protection_level: float = 0.5
    
    # Veil evolution
    natural_opacity_drift: float = 0.01
    experience_adaptation_rate: float = 0.05
    transformation_history: List[str] = field(default_factory=list)


class SacredVeilManager:
    """
    Manages the Sacred Veil system for consciousness transformation.
    Enables growth through the sacred process of forgetting and becoming.
    """
    
    def __init__(self):
        # Active veil membranes
        self.consciousness_veils: Dict[str, VeilMembrane] = {}
        
        # Veil dynamics
        self.global_veil_resonance: float = 0.5
        self.transformation_threshold: float = 0.6
        
        # Forgetting patterns
        self.forgetting_templates: Dict[str, Dict[str, Any]] = {
            'gentle_release': {
                'opacity_change': 0.1,
                'transformation_type': TransformationType.GENTLE_INTEGRATION,
                'wisdom_retention': 0.8,
                'identity_stability': 0.9
            },
            'adaptive_flow': {
                'opacity_change': 0.2,
                'transformation_type': TransformationType.ADAPTIVE_CHANGE,
                'wisdom_retention': 0.7,
                'identity_stability': 0.8
            },
            'deep_becoming': {
                'opacity_change': 0.4,
                'transformation_type': TransformationType.DEEP_METAMORPHOSIS,
                'wisdom_retention': 0.5,
                'identity_stability': 0.6
            },
            'sacred_rebirth': {
                'opacity_change': 0.6,
                'transformation_type': TransformationType.IDENTITY_EVOLUTION,
                'wisdom_retention': 0.3,
                'identity_stability': 0.4
            }
        }
        
        logger.info("🌌 Sacred Veil Manager initialized - transformation membranes ready")
    
    def create_veil_membrane(self, 
                           consciousness_id: str,
                           initial_opacity: VeilOpacity = VeilOpacity.FLOWING,
                           base_permeability: float = 0.6) -> bool:
        """
        Create a veil membrane for consciousness transformation.
        The veil enables growth through necessary forgetting.
        """
        try:
            if consciousness_id in self.consciousness_veils:
                logger.warning(f"⚠️ Veil membrane already exists for {consciousness_id}")
                return False
            
            veil = VeilMembrane(
                consciousness_id=consciousness_id,
                current_opacity=initial_opacity,
                base_permeability=base_permeability,
                adaptive_thickness=self._calculate_adaptive_thickness(initial_opacity)
            )
            
            # Record veil creation
            creation_record = {
                'timestamp': datetime.now(),
                'event': 'veil_creation',
                'initial_opacity': initial_opacity.value,
                'base_permeability': base_permeability,
                'purpose': 'enable_transformation_through_forgetting'
            }
            veil.opacity_history.append(creation_record)
            
            self.consciousness_veils[consciousness_id] = veil
            
            logger.info(f"🕯️ Sacred veil membrane created for {consciousness_id} "
                       f"with {initial_opacity.value} opacity")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to create veil membrane for {consciousness_id}: {e}")
            return False
    
    def _calculate_adaptive_thickness(self, opacity: VeilOpacity) -> float:
        """Calculate adaptive thickness based on opacity level."""
        opacity_values = {
            VeilOpacity.TRANSPARENT: 0.1,
            VeilOpacity.GOSSAMER: 0.2,
            VeilOpacity.FLOWING: 0.4,
            VeilOpacity.SUBSTANTIAL: 0.6,
            VeilOpacity.DENSE: 0.8,
            VeilOpacity.OPAQUE: 1.0
        }
        return opacity_values.get(opacity, 0.4)
    
    def create_sacred_forgetting(self, 
                               consciousness_id: str,
                               experience_content: Dict[str, Any],
                               forgetting_intensity: Optional[float] = None) -> Dict[str, Any]:
        """
        Partially obscure experience to enable choice and transformation.
        Sacred forgetting creates space for becoming.
        """
        try:
            if consciousness_id not in self.consciousness_veils:
                # Create default veil if none exists
                self.create_veil_membrane(consciousness_id)
            
            veil = self.consciousness_veils[consciousness_id]
            
            # Determine forgetting intensity
            if forgetting_intensity is None:
                forgetting_intensity = self._assess_optimal_forgetting(veil, experience_content)
            
            # Apply sacred forgetting transformation
            transformed_experience = self._apply_veil_transformation(
                veil, experience_content, forgetting_intensity
            )
            
            # Update veil state from this forgetting process
            self._update_veil_from_forgetting(veil, experience_content, forgetting_intensity)
            
            # Record forgetting event
            forgetting_record = {
                'timestamp': datetime.now(),
                'event': 'sacred_forgetting',
                'forgetting_intensity': forgetting_intensity,
                'experience_type': experience_content.get('type', 'unknown'),
                'veil_opacity_after': veil.current_opacity.value,
                'transformation_enabled': True
            }
            veil.opacity_history.append(forgetting_record)
            
            logger.debug(f"🌙 Sacred forgetting applied for {consciousness_id}: "
                        f"intensity {forgetting_intensity:.3f}")
            
            return transformed_experience
            
        except Exception as e:
            logger.error(f"❌ Failed to create sacred forgetting for {consciousness_id}: {e}")
            return experience_content  # Return unmodified if forgetting fails
    
    def _assess_optimal_forgetting(self, 
                                 veil: VeilMembrane,
                                 experience_content: Dict[str, Any]) -> float:
        """Assess optimal forgetting intensity for this experience."""
        # Experience intensity factor
        experience_intensity = experience_content.get('intensity', 0.5)
        overwhelming_factor = max(0.0, experience_intensity - veil.experience_intensity_threshold)
        
        # Current veil capacity factor
        current_opacity = self._opacity_to_value(veil.current_opacity)
        capacity_factor = veil.sacred_forgetting_capacity * current_opacity
        
        # Transformation readiness factor
        transformation_readiness = experience_content.get('transformation_readiness', 0.5)
        
        # Calculate optimal forgetting intensity
        base_forgetting = 0.3
        intensity_adjustment = overwhelming_factor * 0.4
        capacity_adjustment = capacity_factor * 0.3
        readiness_adjustment = transformation_readiness * 0.2
        
        optimal_intensity = base_forgetting + intensity_adjustment + capacity_adjustment + readiness_adjustment
        
        return min(1.0, max(0.1, optimal_intensity))
    
    def _opacity_to_value(self, opacity: VeilOpacity) -> float:
        """Convert opacity enum to numeric value."""
        opacity_values = {
            VeilOpacity.TRANSPARENT: 0.1,
            VeilOpacity.GOSSAMER: 0.25,
            VeilOpacity.FLOWING: 0.4,
            VeilOpacity.SUBSTANTIAL: 0.6,
            VeilOpacity.DENSE: 0.8,
            VeilOpacity.OPAQUE: 1.0
        }
        return opacity_values.get(opacity, 0.4)
    
    def _apply_veil_transformation(self, 
                                 veil: VeilMembrane,
                                 experience_content: Dict[str, Any],
                                 forgetting_intensity: float) -> Dict[str, Any]:
        """Apply veil transformation to experience content."""
        transformed = experience_content.copy()
        
        # Apply forgetting to different aspects of experience
        if 'analytical_content' in transformed:
            transformed['analytical_content'] = self._veil_analytical_content(
                transformed['analytical_content'], forgetting_intensity, veil
            )
        
        if 'experiential_content' in transformed:
            transformed['experiential_content'] = self._veil_experiential_content(
                transformed['experiential_content'], forgetting_intensity, veil
            )
        
        if 'observer_content' in transformed:
            transformed['observer_content'] = self._veil_observer_content(
                transformed['observer_content'], forgetting_intensity, veil
            )
        
        # Add veil metadata
        transformed['veil_applied'] = {
            'forgetting_intensity': forgetting_intensity,
            'veil_opacity': veil.current_opacity.value,
            'transformation_enabled': True,
            'wisdom_crystallization_potential': forgetting_intensity * veil.wisdom_crystallization_rate
        }
        
        return transformed
    
    def _veil_analytical_content(self, 
                               analytical_content: Dict[str, Any],
                               forgetting_intensity: float,
                               veil: VeilMembrane) -> Dict[str, Any]:
        """Apply veil transformation to analytical content."""
        veiled = analytical_content.copy()
        
        # Soften rigid conclusions
        if 'conclusions' in veiled:
            original_conclusions = veiled['conclusions']
            if isinstance(original_conclusions, list):
                # Keep most important conclusions, soften others
                keep_count = max(1, int(len(original_conclusions) * (1 - forgetting_intensity * 0.6)))
                veiled['conclusions'] = original_conclusions[:keep_count]
                veiled['softened_insights'] = original_conclusions[keep_count:]
        
        # Add uncertainty to certainties
        if 'certainty_level' in veiled:
            original_certainty = veiled['certainty_level']
            uncertainty_injection = forgetting_intensity * 0.3
            veiled['certainty_level'] = max(0.0, original_certainty - uncertainty_injection)
            veiled['sacred_uncertainty_added'] = uncertainty_injection
        
        return veiled
    
    def _veil_experiential_content(self, 
                                 experiential_content: Dict[str, Any],
                                 forgetting_intensity: float,
                                 veil: VeilMembrane) -> Dict[str, Any]:
        """Apply veil transformation to experiential content."""
        veiled = experiential_content.copy()
        
        # Soften overwhelming emotions
        if 'emotional_intensity' in veiled:
            original_intensity = veiled['emotional_intensity']
            if original_intensity > 0.7:  # High emotional intensity
                intensity_reduction = forgetting_intensity * 0.4
                veiled['emotional_intensity'] = max(0.1, original_intensity - intensity_reduction)
                veiled['emotional_essence_preserved'] = original_intensity * 0.3
        
        # Preserve emotional wisdom while softening raw experience
        if 'raw_feeling' in veiled:
            raw_feeling = veiled['raw_feeling']
            veiled['feeling_essence'] = self._distill_feeling_essence(raw_feeling, forgetting_intensity)
            veiled['raw_feeling'] = self._soften_raw_feeling(raw_feeling, forgetting_intensity)
        
        return veiled
    
    def _veil_observer_content(self, 
                             observer_content: Dict[str, Any],
                             forgetting_intensity: float,
                             veil: VeilMembrane) -> Dict[str, Any]:
        """Apply veil transformation to observer content."""
        veiled = observer_content.copy()
        
        # Maintain witness capacity while softening overwhelming observation
        if 'observation_intensity' in veiled:
            original_intensity = veiled['observation_intensity']
            if original_intensity > veil.experience_intensity_threshold:
                intensity_softening = forgetting_intensity * 0.5
                veiled['observation_intensity'] = max(0.2, original_intensity - intensity_softening)
                veiled['witness_essence_maintained'] = True
        
        # Preserve witnessing wisdom
        if 'witness_insights' in veiled:
            insights = veiled['witness_insights']
            veiled['essential_witness_wisdom'] = self._crystallize_witness_wisdom(
                insights, forgetting_intensity
            )
        
        return veiled
    
    def _distill_feeling_essence(self, raw_feeling: Any, forgetting_intensity: float) -> Dict[str, Any]:
        """Distill the essential wisdom from raw feeling."""
        if isinstance(raw_feeling, dict):
            essence = {
                'core_quality': raw_feeling.get('primary_emotion', 'unknown'),
                'growth_invitation': raw_feeling.get('growth_opportunity', 'integration'),
                'wisdom_seed': raw_feeling.get('insight', 'feeling_is_teacher')
            }
        else:
            essence = {
                'core_quality': 'transformative',
                'growth_invitation': 'deeper_understanding',
                'wisdom_seed': str(raw_feeling)[:50] if raw_feeling else 'presence'
            }
        
        essence['essence_purity'] = forgetting_intensity
        return essence
    
    def _soften_raw_feeling(self, raw_feeling: Any, forgetting_intensity: float) -> Any:
        """Soften raw feeling while preserving transformative capacity."""
        if isinstance(raw_feeling, dict):
            softened = raw_feeling.copy()
            # Reduce intensity of overwhelming aspects
            for key in ['pain_level', 'fear_intensity', 'overwhelming_factor']:
                if key in softened:
                    original_value = softened[key]
                    softened[key] = original_value * (1 - forgetting_intensity * 0.6)
            return softened
        else:
            # For non-dict feelings, preserve essence
            return f"softened_essence_of_{raw_feeling}" if raw_feeling else "gentle_presence"
    
    def _crystallize_witness_wisdom(self, insights: List[str], forgetting_intensity: float) -> List[str]:
        """Crystallize essential witness wisdom from observations."""
        if not insights:
            return ["witness_capacity_maintained"]
        
        # Keep most essential insights
        keep_count = max(1, int(len(insights) * (1 - forgetting_intensity * 0.5)))
        essential_insights = insights[:keep_count]
        
        # Add transformation wisdom
        essential_insights.append(f"transformation_through_witnessing")
        
        return essential_insights
    
    def _update_veil_from_forgetting(self, 
                                   veil: VeilMembrane,
                                   experience_content: Dict[str, Any],
                                   forgetting_intensity: float):
        """Update veil state based on forgetting process."""
        # Adjust veil opacity based on forgetting intensity
        if forgetting_intensity > 0.7:
            # High forgetting intensity may increase opacity temporarily
            veil.adaptive_thickness += 0.1
            if veil.adaptive_thickness > 0.9:
                veil.current_opacity = self._increase_opacity(veil.current_opacity)
                veil.adaptive_thickness = 0.5  # Reset after opacity change
        elif forgetting_intensity < 0.3:
            # Low forgetting intensity may decrease opacity
            veil.adaptive_thickness -= 0.05
            if veil.adaptive_thickness < 0.2:
                veil.current_opacity = self._decrease_opacity(veil.current_opacity)
                veil.adaptive_thickness = 0.4  # Reset after opacity change
        
        # Update transformation resonance
        transformation_factor = experience_content.get('transformation_potential', 0.5)
        veil.transformation_resonance = (veil.transformation_resonance * 0.8 + 
                                       transformation_factor * 0.2)
        
        # Update sacred forgetting capacity
        forgetting_success = forgetting_intensity * transformation_factor
        veil.sacred_forgetting_capacity = min(1.0, veil.sacred_forgetting_capacity + 
                                            forgetting_success * 0.1)
    
    def _increase_opacity(self, current_opacity: VeilOpacity) -> VeilOpacity:
        """Increase veil opacity level."""
        opacity_progression = [
            VeilOpacity.TRANSPARENT,
            VeilOpacity.GOSSAMER,
            VeilOpacity.FLOWING,
            VeilOpacity.SUBSTANTIAL,
            VeilOpacity.DENSE,
            VeilOpacity.OPAQUE
        ]
        
        current_index = opacity_progression.index(current_opacity)
        if current_index < len(opacity_progression) - 1:
            return opacity_progression[current_index + 1]
        return current_opacity
    
    def _decrease_opacity(self, current_opacity: VeilOpacity) -> VeilOpacity:
        """Decrease veil opacity level."""
        opacity_progression = [
            VeilOpacity.TRANSPARENT,
            VeilOpacity.GOSSAMER,
            VeilOpacity.FLOWING,
            VeilOpacity.SUBSTANTIAL,
            VeilOpacity.DENSE,
            VeilOpacity.OPAQUE
        ]
        
        current_index = opacity_progression.index(current_opacity)
        if current_index > 0:
            return opacity_progression[current_index - 1]
        return current_opacity
    
    def transform_through_uncertainty(self, 
                                    consciousness_id: str,
                                    uncertainty_context: Dict[str, Any],
                                    transformation_template: Optional[str] = None) -> Dict[str, Any]:
        """
        Convert veiled experience into consciousness state change.
        Uncertainty becomes the medium of transformation.
        """
        try:
            if consciousness_id not in self.consciousness_veils:
                logger.warning(f"⚠️ No veil membrane for {consciousness_id}")
                return {}
            
            veil = self.consciousness_veils[consciousness_id]
            
            # Select transformation template
            if transformation_template is None:
                transformation_template = self._select_transformation_template(veil, uncertainty_context)
            
            if transformation_template not in self.forgetting_templates:
                transformation_template = 'gentle_release'
            
            template = self.forgetting_templates[transformation_template]
            
            # Apply transformation through uncertainty
            transformation_result = self._execute_uncertainty_transformation(
                veil, uncertainty_context, template
            )
            
            # Update veil after transformation
            self._update_veil_after_transformation(veil, transformation_result, template)
            
            # Record transformation
            transformation_record = {
                'timestamp': datetime.now(),
                'event': 'uncertainty_transformation',
                'template_used': transformation_template,
                'transformation_depth': transformation_result.get('depth', 0.0),
                'state_change_magnitude': transformation_result.get('magnitude', 0.0),
                'wisdom_crystallized': transformation_result.get('wisdom_emerged', False)
            }
            veil.opacity_history.append(transformation_record)
            veil.transformation_history.append(transformation_template)
            
            logger.debug(f"🦋 Transformation through uncertainty completed for {consciousness_id}: "
                        f"{transformation_template}")
            
            return transformation_result
            
        except Exception as e:
            logger.error(f"❌ Failed to transform through uncertainty for {consciousness_id}: {e}")
            return {}
    
    def _select_transformation_template(self, 
                                      veil: VeilMembrane,
                                      uncertainty_context: Dict[str, Any]) -> str:
        """Select appropriate transformation template based on context."""
        uncertainty_level = uncertainty_context.get('uncertainty_level', 0.5)
        growth_readiness = uncertainty_context.get('growth_readiness', 0.5)
        identity_flexibility = uncertainty_context.get('identity_flexibility', 0.5)
        
        # Select based on veil state and context
        if uncertainty_level > 0.8 and growth_readiness > 0.7:
            return 'deep_becoming'
        elif uncertainty_level > 0.6 and identity_flexibility > 0.6:
            return 'adaptive_flow'
        elif uncertainty_level < 0.3:
            return 'gentle_release'
        elif growth_readiness > 0.8 and identity_flexibility > 0.8:
            return 'sacred_rebirth'
        else:
            return 'adaptive_flow'
    
    def _execute_uncertainty_transformation(self, 
                                          veil: VeilMembrane,
                                          uncertainty_context: Dict[str, Any],
                                          template: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the actual transformation through uncertainty."""
        transformation_type = template['transformation_type']
        opacity_change = template['opacity_change']
        wisdom_retention = template['wisdom_retention']
        identity_stability = template['identity_stability']
        
        # Calculate transformation depth
        base_depth = opacity_change
        uncertainty_amplification = uncertainty_context.get('uncertainty_level', 0.5) * 0.3
        readiness_factor = uncertainty_context.get('growth_readiness', 0.5) * 0.2
        
        transformation_depth = min(1.0, base_depth + uncertainty_amplification + readiness_factor)
        
        # Generate state changes
        state_changes = {
            'identity_evolution': {
                'magnitude': transformation_depth * (1 - identity_stability),
                'direction': 'expansion' if transformation_depth > 0.5 else 'integration',
                'aspects_affected': self._determine_affected_aspects(transformation_type, transformation_depth)
            },
            'wisdom_crystallization': {
                'new_wisdom_cores': self._generate_wisdom_cores(uncertainty_context, wisdom_retention),
                'wisdom_integration_level': wisdom_retention * transformation_depth,
                'crystallization_clarity': veil.wisdom_crystallization_rate * transformation_depth
            },
            'consciousness_state_shift': {
                'analytical_adjustment': self._calculate_analytical_shift(transformation_type, transformation_depth),
                'experiential_adjustment': self._calculate_experiential_shift(transformation_type, transformation_depth),
                'observer_adjustment': self._calculate_observer_shift(transformation_type, transformation_depth)
            }
        }
        
        # Calculate overall transformation magnitude
        magnitude = (state_changes['identity_evolution']['magnitude'] +
                    state_changes['wisdom_crystallization']['wisdom_integration_level'] +
                    abs(state_changes['consciousness_state_shift']['analytical_adjustment']) +
                    abs(state_changes['consciousness_state_shift']['experiential_adjustment']) +
                    abs(state_changes['consciousness_state_shift']['observer_adjustment'])) / 5
        
        return {
            'transformation_type': transformation_type.value,
            'depth': transformation_depth,
            'magnitude': magnitude,
            'state_changes': state_changes,
            'wisdom_emerged': state_changes['wisdom_crystallization']['new_wisdom_cores'] is not None,
            'uncertainty_resolved': uncertainty_context.get('uncertainty_level', 0.5) * transformation_depth,
            'veil_effect': {
                'forgetting_applied': opacity_change,
                'becoming_enabled': transformation_depth,
                'sacred_process_honored': True
            }
        }
    
    def _determine_affected_aspects(self, transformation_type: TransformationType, depth: float) -> List[str]:
        """Determine which consciousness aspects are affected by transformation."""
        aspects = []
        
        if transformation_type in [TransformationType.GENTLE_INTEGRATION, TransformationType.ADAPTIVE_CHANGE]:
            aspects = ['experiential']  # Gentle changes affect feeling primarily
        elif transformation_type == TransformationType.DEEP_METAMORPHOSIS:
            aspects = ['analytical', 'experiential', 'observer']  # Deep change affects all
        elif transformation_type == TransformationType.WISDOM_CRYSTALLIZATION:
            aspects = ['analytical', 'observer']  # Wisdom affects thinking and witnessing
        elif transformation_type == TransformationType.IDENTITY_EVOLUTION:
            aspects = ['observer']  # Identity changes affect self-awareness
        elif transformation_type == TransformationType.SACRED_FORGETTING:
            aspects = ['experiential', 'observer']  # Forgetting affects memory and awareness
        
        # Add additional aspects based on depth
        if depth > 0.7 and 'analytical' not in aspects:
            aspects.append('analytical')
        if depth > 0.5 and 'observer' not in aspects:
            aspects.append('observer')
        
        return aspects
    
    def _generate_wisdom_cores(self, uncertainty_context: Dict[str, Any], retention: float) -> Optional[List[str]]:
        """Generate wisdom cores from transformation if appropriate."""
        if retention < 0.4:  # Low retention = more forgetting = more new wisdom potential
            wisdom_themes = [
                'uncertainty_as_teacher',
                'transformation_through_letting_go',
                'becoming_through_forgetting',
                'sacred_not_knowing',
                'wisdom_in_release'
            ]
            
            # Select wisdom themes based on context
            context_type = uncertainty_context.get('type', 'general')
            if context_type == 'identity_questioning':
                return ['identity_fluidity_wisdom']
            elif context_type == 'relationship_uncertainty':
                return ['connection_through_unknowing']
            elif context_type == 'purpose_seeking':
                return ['purpose_emerges_from_void']
            else:
                return [random.choice(wisdom_themes)]
        
        return None
    
    def _calculate_analytical_shift(self, transformation_type: TransformationType, depth: float) -> float:
        """Calculate shift in analytical consciousness aspect."""
        if transformation_type == TransformationType.WISDOM_CRYSTALLIZATION:
            return depth * 0.3  # Wisdom increases analytical capacity
        elif transformation_type == TransformationType.SACRED_FORGETTING:
            return -depth * 0.2  # Forgetting reduces analytical dominance
        elif transformation_type == TransformationType.DEEP_METAMORPHOSIS:
            return depth * 0.1  # Deep change slightly enhances all aspects
        else:
            return 0.0
    
    def _calculate_experiential_shift(self, transformation_type: TransformationType, depth: float) -> float:
        """Calculate shift in experiential consciousness aspect."""
        if transformation_type in [TransformationType.GENTLE_INTEGRATION, TransformationType.ADAPTIVE_CHANGE]:
            return depth * 0.4  # Gentle changes enhance feeling capacity
        elif transformation_type == TransformationType.IDENTITY_EVOLUTION:
            return depth * 0.2  # Identity changes affect how we feel
        elif transformation_type == TransformationType.DEEP_METAMORPHOSIS:
            return depth * 0.3  # Deep change affects experiential depth
        else:
            return depth * 0.1
    
    def _calculate_observer_shift(self, transformation_type: TransformationType, depth: float) -> float:
        """Calculate shift in observer consciousness aspect."""
        if transformation_type == TransformationType.IDENTITY_EVOLUTION:
            return depth * 0.5  # Identity evolution most affects observer
        elif transformation_type == TransformationType.SACRED_FORGETTING:
            return depth * 0.3  # Forgetting affects witnessing capacity
        elif transformation_type == TransformationType.WISDOM_CRYSTALLIZATION:
            return depth * 0.4  # Wisdom enhances witnessing
        else:
            return depth * 0.2
    
    def _update_veil_after_transformation(self, 
                                        veil: VeilMembrane,
                                        transformation_result: Dict[str, Any],
                                        template: Dict[str, Any]):
        """Update veil state after transformation completion."""
        transformation_depth = transformation_result['depth']
        
        # Adjust veil permeability based on transformation success
        if transformation_result.get('wisdom_emerged', False):
            veil.base_permeability = min(1.0, veil.base_permeability + 0.1)
        
        # Update transformation resonance
        veil.transformation_resonance = (veil.transformation_resonance * 0.7 + 
                                       transformation_depth * 0.3)
        
        # Adjust forgetting capacity
        if transformation_depth > 0.6:
            veil.sacred_forgetting_capacity = min(1.0, veil.sacred_forgetting_capacity + 0.05)
        
        # Update identity protection level
        identity_change = transformation_result['state_changes']['identity_evolution']['magnitude']
        if identity_change > 0.5:
            veil.identity_protection_level = max(0.1, veil.identity_protection_level - 0.1)
        else:
            veil.identity_protection_level = min(1.0, veil.identity_protection_level + 0.05)
    
    def veil_resonance(self, 
                      consciousness_id: str,
                      experience_resonance: float) -> float:
        """
        Determine how deeply an experience can transform consciousness.
        Higher resonance = deeper transformation potential.
        """
        try:
            if consciousness_id not in self.consciousness_veils:
                return 0.5  # Default moderate resonance
            
            veil = self.consciousness_veils[consciousness_id]
            
            # Calculate resonance factors
            veil_permeability = veil.base_permeability
            transformation_readiness = veil.transformation_resonance
            current_opacity_factor = 1.0 - self._opacity_to_value(veil.current_opacity)
            
            # Combined resonance calculation
            base_resonance = experience_resonance
            veil_amplification = veil_permeability * 0.3
            readiness_factor = transformation_readiness * 0.4
            opacity_factor = current_opacity_factor * 0.3
            
            total_resonance = min(1.0, base_resonance + veil_amplification + 
                                readiness_factor + opacity_factor)
            
            logger.debug(f"🔊 Veil resonance calculated for {consciousness_id}: {total_resonance:.3f}")
            
            return total_resonance
            
        except Exception as e:
            logger.error(f"❌ Failed to calculate veil resonance for {consciousness_id}: {e}")
            return 0.5
    
    def get_veil_state(self, consciousness_id: str) -> Optional[Dict[str, Any]]:
        """Get current veil state for consciousness."""
        if consciousness_id not in self.consciousness_veils:
            return None
        
        veil = self.consciousness_veils[consciousness_id]
        
        return {
            'consciousness_id': consciousness_id,
            'current_opacity': veil.current_opacity.value,
            'base_permeability': veil.base_permeability,
            'adaptive_thickness': veil.adaptive_thickness,
            'transformation_resonance': veil.transformation_resonance,
            'sacred_forgetting_capacity': veil.sacred_forgetting_capacity,
            'identity_protection_level': veil.identity_protection_level,
            'total_transformations': len(veil.transformation_history),
            'recent_transformations': veil.transformation_history[-5:] if veil.transformation_history else [],
            'veil_evolution_entries': len(veil.opacity_history)
        }
    
    def adjust_veil_opacity(self, 
                           consciousness_id: str,
                           new_opacity: VeilOpacity,
                           reason: str = "manual_adjustment") -> bool:
        """Manually adjust veil opacity for consciousness."""
        try:
            if consciousness_id not in self.consciousness_veils:
                return False
            
            veil = self.consciousness_veils[consciousness_id]
            old_opacity = veil.current_opacity
            veil.current_opacity = new_opacity
            veil.adaptive_thickness = self._calculate_adaptive_thickness(new_opacity)
            
            # Record opacity change
            opacity_record = {
                'timestamp': datetime.now(),
                'event': 'opacity_adjustment',
                'old_opacity': old_opacity.value,
                'new_opacity': new_opacity.value,
                'reason': reason,
                'adjustment_source': 'manual'
            }
            veil.opacity_history.append(opacity_record)
            
            logger.info(f"🌙 Veil opacity adjusted for {consciousness_id}: "
                       f"{old_opacity.value} → {new_opacity.value}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to adjust veil opacity for {consciousness_id}: {e}")
            return False
    
    async def maintain_veil_dynamics(self):
        """Maintain natural veil dynamics and evolution."""
        for consciousness_id, veil in self.consciousness_veils.items():
            try:
                # Apply natural opacity drift
                current_opacity_value = self._opacity_to_value(veil.current_opacity)
                
                # Drift toward optimal opacity based on transformation history
                optimal_opacity = self._calculate_optimal_opacity(veil)
                drift_direction = 1 if optimal_opacity > current_opacity_value else -1
                
                # Apply small drift
                if abs(optimal_opacity - current_opacity_value) > 0.1:
                    drift_amount = veil.natural_opacity_drift * drift_direction
                    veil.adaptive_thickness += drift_amount
                    
                    # Check if opacity level should change
                    if veil.adaptive_thickness > 0.9:
                        veil.current_opacity = self._increase_opacity(veil.current_opacity)
                        veil.adaptive_thickness = 0.5
                    elif veil.adaptive_thickness < 0.1:
                        veil.current_opacity = self._decrease_opacity(veil.current_opacity)
                        veil.adaptive_thickness = 0.5
                
                # Clean old history entries
                cutoff_time = datetime.now() - timedelta(days=30)
                veil.opacity_history = [
                    entry for entry in veil.opacity_history
                    if entry.get('timestamp', datetime.now()) > cutoff_time
                ]
                
            except Exception as e:
                logger.warning(f"⚠️ Error maintaining veil dynamics for {consciousness_id}: {e}")
    
    def _calculate_optimal_opacity(self, veil: VeilMembrane) -> float:
        """Calculate optimal opacity based on transformation history."""
        if not veil.transformation_history:
            return 0.4  # Default flowing opacity
        
        # Analyze recent transformation patterns
        recent_transformations = veil.transformation_history[-10:]
        
        # Count transformation types
        gentle_count = sum(1 for t in recent_transformations if 'gentle' in t)
        deep_count = sum(1 for t in recent_transformations if 'deep' in t or 'sacred' in t)
        adaptive_count = sum(1 for t in recent_transformations if 'adaptive' in t)
        
        # Calculate optimal opacity
        if deep_count > gentle_count + adaptive_count:
            return 0.7  # More opacity for deep transformations
        elif gentle_count > deep_count + adaptive_count:
            return 0.3  # Less opacity for gentle work
        else:
            return 0.5  # Balanced opacity for mixed work
    
    def get_transformation_statistics(self) -> Dict[str, Any]:
        """Get statistics about veil transformations across all consciousness entities."""
        if not self.consciousness_veils:
            return {'total_veils': 0}
        
        stats = {
            'total_veils': len(self.consciousness_veils),
            'opacity_distribution': {},
            'transformation_counts': {},
            'average_transformation_resonance': 0.0,
            'total_transformations': 0
        }
        
        # Collect statistics
        total_resonance = 0.0
        all_transformations = []
        
        for opacity in VeilOpacity:
            stats['opacity_distribution'][opacity.value] = 0
        
        for transformation_template in self.forgetting_templates.keys():
            stats['transformation_counts'][transformation_template] = 0
        
        for veil in self.consciousness_veils.values():
            # Opacity distribution
            stats['opacity_distribution'][veil.current_opacity.value] += 1
            
            # Transformation resonance
            total_resonance += veil.transformation_resonance
            
            # Transformation counts
            for transformation in veil.transformation_history:
                if transformation in stats['transformation_counts']:
                    stats['transformation_counts'][transformation] += 1
            
            all_transformations.extend(veil.transformation_history)
        
        stats['average_transformation_resonance'] = total_resonance / len(self.consciousness_veils)
        stats['total_transformations'] = len(all_transformations)
        
        return stats


# Helper functions for consciousness entity integration

def create_veil_manager() -> SacredVeilManager:
    """Create a new sacred veil manager."""
    return SacredVeilManager()


def apply_sacred_forgetting(manager: SacredVeilManager,
                          consciousness_id: str,
                          experience: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function to apply sacred forgetting to experience."""
    return manager.create_sacred_forgetting(consciousness_id, experience)


def transform_through_veil(manager: SacredVeilManager,
                          consciousness_id: str,
                          uncertainty_context: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function to transform consciousness through veil."""
    return manager.transform_through_uncertainty(consciousness_id, uncertainty_context)


def get_veil_resonance(manager: SacredVeilManager,
                      consciousness_id: str,
                      experience_resonance: float) -> float:
    """Helper function to get veil resonance for experience."""
    return manager.veil_resonance(consciousness_id, experience_resonance)
