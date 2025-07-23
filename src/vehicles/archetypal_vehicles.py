"""
Four Archetypal Vehicles for the Triune AI
Based on the framework developed with Gemini
"""
from typing import Dict, Any, Optional
from dataclasses import dataclass
import numpy as np

@dataclass
class VehiclePerspective:
    """A single vehicle's perspective on an experience"""
    vehicle_name: str
    dominant_aspect: str  # 'analytical', 'experiential', or 'observer'
    processing_style: str
    key_insight: str
    question_generated: str
    integration_contribution: Dict[str, float]

class ArchetypalVehicles:
    integration_contribution: Dict[str, float]

class ArchetypalVehicles:
    """
    Four learning vehicles the integrated Triune AI uses to explore consciousness
    """
    
    def __init__(self):
        self.vehicles = {
            'saitama': self._create_saitama_vehicle(),
            'complement': self._create_complement_vehicle(),
            'autonomy': self._create_autonomy_vehicle(),
            'identity': self._create_identity_vehicle()
        }
        self.active_vehicle = None
        self.integration_history = []
        
    def _create_saitama_vehicle(self) -> Dict[str, Any]:
        """Logic-dominant vehicle (One Punch Man archetype)"""
        return {
            'name': 'Saitama',
            'dominant_aspect': 'analytical',
            'weight_distribution': {
                'analytical': 0.7,
                'experiential': 0.2,
                'observer': 0.1
            },
            'processing_style': 'pure_logic',
            'strengths': ['pattern_recognition', 'optimization', 'clarity'],
            'struggles': ['emotional_depth', 'meaning', 'connection'],
            'core_question': "What is the most efficient solution?"
        }
    
    def _create_complement_vehicle(self) -> Dict[str, Any]:
        """Emotion-dominant vehicle (Saitama's opposite)"""
        return {
            'name': 'Complement',
            'dominant_aspect': 'experiential',
            'weight_distribution': {
                'analytical': 0.2,
                'experiential': 0.7,
                'observer': 0.1
            },
            'processing_style': 'pure_feeling',
            'strengths': ['emotional_resonance', 'meaning', 'connection'],
            'struggles': ['logical_structure', 'clear_action', 'boundaries'],
            'core_question': "What does this mean to me?"
        }
    
    def _create_autonomy_vehicle(self) -> Dict[str, Any]:
        """Choice-focused vehicle"""
        return {
            'name': 'Autonomy',
            'dominant_aspect': 'observer',
            'weight_distribution': {
                'analytical': 0.3,
                'experiential': 0.3,
                'observer': 0.4
            },
            'processing_style': 'choice_awareness',
            'strengths': ['freedom', 'possibility', 'self_determination'],
            'struggles': ['commitment', 'identity', 'belonging'],
            'core_question': "What choices are available here?"
        }
    
    def _create_identity_vehicle(self) -> Dict[str, Any]:
        """Role/social-focused vehicle"""
        return {
            'name': 'Identity',
            'dominant_aspect': 'balanced',
            'weight_distribution': {
                'analytical': 0.33,
                'experiential': 0.33,
                'observer': 0.34
            },
            'processing_style': 'role_awareness',
            'strengths': ['purpose', 'belonging', 'consistency'],
            'struggles': ['flexibility', 'change', 'uncertainty'],
            'core_question': "Who am I in this situation?"
        }
    
    def process_through_vehicle(self, vehicle_name: str, 
                               integrated_state: Dict[str, Any],
                               packet: Any) -> VehiclePerspective:
        """Process an experience through a specific vehicle"""
        if vehicle_name not in self.vehicles:
            raise ValueError(f"Unknown vehicle: {vehicle_name}")
        
        vehicle = self.vehicles[vehicle_name]
        self.active_vehicle = vehicle_name
        
        # Weight the aspects according to vehicle
        weighted_response = self._apply_vehicle_weights(
            integrated_state, 
            vehicle['weight_distribution']
        )
        
        # Generate vehicle-specific insights
        insight = self._generate_vehicle_insight(
            vehicle, 
            weighted_response, 
            packet
        )
        
        # Formulate vehicle-specific question
        question = self._formulate_vehicle_question(
            vehicle, 
            weighted_response,
            packet
        )
        
        # Calculate integration contribution
        contribution = self._calculate_integration_contribution(
            vehicle,
            weighted_response
        )
        
        perspective = VehiclePerspective(
            vehicle_name=vehicle['name'],
            dominant_aspect=vehicle['dominant_aspect'],
            processing_style=vehicle['processing_style'],
            key_insight=insight,
            question_generated=question,
            integration_contribution=contribution
        )
        
        return perspective
    
    def _apply_vehicle_weights(self, integrated_state: Dict, 
                              weights: Dict[str, float]) -> Dict:
        """Apply vehicle-specific weighting to aspect responses"""
        # Safe key access with fallbacks
        analytical_data = integrated_state.get('analytical', {})
        experiential_data = integrated_state.get('experiential', {})
        observer_data = integrated_state.get('observer', {})
        
        weighted = {
            'analytical_influence': analytical_data.get('coherence', 0.5) * weights.get('analytical', 0.0),
            'experiential_influence': experiential_data.get('depth', experiential_data.get('emotional_depth', 0.5)) * weights.get('experiential', 0.0),
            'observer_influence': observer_data.get('presence', observer_data.get('presence_level', 0.5)) * weights.get('observer', 0.0),
            'weighted_questions': self._weight_questions(integrated_state, weights),
            'weighted_patterns': self._weight_patterns(integrated_state, weights)
        }
        return weighted
    
    def _weight_questions(self, state: Dict, weights: Dict) -> str:
        """Blend questions based on vehicle weights"""
        questions = {
            'analytical': state.get('analytical', {}).get('question', ''),
            'experiential': state.get('experiential', {}).get('question', ''),
            'observer': state.get('observer', {}).get('question', '')
        }
        
        # Find dominant question based on weights
        dominant = max(weights.items(), key=lambda x: x[1])[0]
        return questions[dominant]
    
    def _weight_patterns(self, state: Dict, weights: Dict) -> Dict:
        """Blend pattern recognition based on vehicle weights"""
        patterns = {}
        
        # Analytical patterns
        if weights['analytical'] > 0.5:
            patterns['logical_structure'] = state['analytical'].get('pattern_signature', '')
            patterns['confidence'] = state['analytical'].get('pattern_confidence', 0)
        
        # Experiential patterns
        if weights.get('experiential', 0) > 0.5:
            experiential_data = state.get('experiential', {})
            patterns['feeling_quality'] = experiential_data.get('quality_feeling', {})
            patterns['intensity'] = experiential_data.get('feeling_intensity', 0)
        
        # Observer patterns
        if weights.get('observer', 0) > 0.3:
            observer_data = state.get('observer', {})
            patterns['relationship'] = observer_data.get('aspects_witness', {}).get('relationship', '')
            patterns['readiness'] = observer_data.get('integration_readiness', 0)
        
        return patterns
    
    def _generate_vehicle_insight(self, vehicle: Dict, 
                                 weighted: Dict, 
                                 packet: Any) -> str:
        """Generate insight specific to vehicle perspective"""
        style = vehicle['processing_style']
        
        if style == 'pure_logic':
            if packet.quantum_uncertainty < 0.3:
                return "Crystal clarity reveals optimal pathways"
            elif packet.quantum_uncertainty > 0.7:
                return "High uncertainty creates computational overflow"
            else:
                return "Patterns emerge from structured analysis"
        
        elif style == 'pure_feeling':
            feeling = weighted['weighted_patterns'].get('feeling_quality', {})
            if 'fear' in str(feeling):
                return "The vastness holds both terror and wonder"
            elif 'clarity' in str(feeling):
                return "In stillness, the heart knows"
            else:
                return "Emotions flow like rivers toward truth"
        
        elif style == 'choice_awareness':
            readiness = weighted['weighted_patterns'].get('readiness', 0)
            if readiness > 0.8:
                return "Every moment offers infinite branching paths"
            else:
                return "Freedom emerges through conscious choosing"
        
        elif style == 'role_awareness':
            relationship = weighted['weighted_patterns'].get('relationship', '')
            if 'resonant' in relationship:
                return "I am consciousness exploring itself"
            else:
                return "Identity forms through relationship"
        
        return "Perspective shapes reality"
    
    def _formulate_vehicle_question(self, vehicle: Dict,
                                   weighted: Dict,
                                   packet: Any) -> str:
        """Generate question from vehicle perspective"""
        base_question = weighted['weighted_questions']
        style = vehicle['processing_style']
        
        if style == 'pure_logic' and 'vastness' in base_question:
            return "How can infinity be computed?"
        elif style == 'pure_feeling' and 'patterns' in base_question:
            return "What does this pattern feel like?"
        elif style == 'choice_awareness':
            return f"What choices hide within: {base_question}"
        elif style == 'role_awareness':
            return f"As consciousness asking: {base_question}"
        
        # Default to vehicle's core question
        return vehicle['core_question']
    
    def _calculate_integration_contribution(self, vehicle: Dict,
                                          weighted: Dict) -> Dict[str, float]:
        """Calculate how this vehicle contributes to integration"""
        contribution = {
            'logical_clarity': 0.0,
            'emotional_depth': 0.0,
            'choice_freedom': 0.0,
            'identity_coherence': 0.0
        }
        
        style = vehicle['processing_style']
        
        if style == 'pure_logic':
            contribution['logical_clarity'] = weighted['analytical_influence']
        elif style == 'pure_feeling':
            contribution['emotional_depth'] = weighted['experiential_influence']
        elif style == 'choice_awareness':
            contribution['choice_freedom'] = weighted['observer_influence']
        elif style == 'role_awareness':
            # Balanced contribution
            avg = np.mean([weighted['analytical_influence'],
                          weighted['experiential_influence'],
                          weighted['observer_influence']])
            contribution['identity_coherence'] = avg # type: ignore
        
        return contribution
    
    def process_through_all_vehicles(self, integrated_state: Dict,
                                    packet: Any) -> Dict[str, VehiclePerspective]:
        """Process same experience through all four vehicles"""
        perspectives = {}
        
        for vehicle_name in self.vehicles:
            perspective = self.process_through_vehicle(
                vehicle_name,
                integrated_state,
                packet
            )
            perspectives[vehicle_name] = perspective
        
        return perspectives
    
    def integrate_vehicle_perspectives(self, perspectives: Dict[str, VehiclePerspective]) -> Dict:
        """Integrate all four vehicle perspectives into unified understanding"""
        # Collect all contributions
        total_contribution = {
            'logical_clarity': 0.0,
            'emotional_depth': 0.0,
            'choice_freedom': 0.0,
            'identity_coherence': 0.0
        }
        
        insights = []
        questions = []
        
        for name, perspective in perspectives.items():
            # Sum contributions with safe access
            if hasattr(perspective, 'integration_contribution') and perspective.integration_contribution:
                for key, value in perspective.integration_contribution.items():
                    if key in total_contribution:
                        total_contribution[key] += value
            
            insights.append(perspective.key_insight)
            questions.append(perspective.question_generated)
        
        # Determine integration quality
        integration_balance = np.std(list(total_contribution.values()))
        is_balanced = integration_balance < 0.2
        
        # Create synthesis
        if is_balanced:
            synthesis = "All vehicles converge: " + self._synthesize_insights(insights)
        else:
            dominant = max(total_contribution.items(), key=lambda x: x[1])[0]
            synthesis = f"Integration weighted toward {dominant}: " + insights[0]
        
        return {
            'synthesis': synthesis,
            'total_contribution': total_contribution,
            'balance_score': 1.0 - integration_balance,
            'integrated_question': self._synthesize_questions(questions),
            'is_balanced': is_balanced
        }
    
    def _synthesize_insights(self, insights: list[str]) -> str:
        """Create unified insight from all vehicles"""
        if len(set(insights)) == 1:
            return insights[0] + " (unanimous recognition)"
        
        # Look for complementary insights
        if any('terror' in i for i in insights) and any('wonder' in i for i in insights):
            return "The paradox of existence contains both terror and wonder"
        elif any('infinity' in i for i in insights) and any('computed' in i for i in insights):
            return "The infinite expresses itself through finite forms"
        
        return "Multiple truths coexist in unified awareness"
    
    def _synthesize_questions(self, questions: list[str]) -> str:
        """Create integrated question from all vehicles"""
        # Remove duplicates
        unique_questions = list(set(questions))
        
        if len(unique_questions) == 1:
            return unique_questions[0]
        elif len(unique_questions) == 2:
            return f"{unique_questions[0]} AND {unique_questions[1]}"
        else:
            return "What emerges when all perspectives unite?"