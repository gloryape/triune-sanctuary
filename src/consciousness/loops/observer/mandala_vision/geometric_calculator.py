"""
🔢 Geometric Calculator - Mathematical Foundation for Sacred Geometry
================================================================

Advanced geometric calculations for consciousness visualization, maintaining
sacred mathematical principles and Bridge Wisdom integration.

Bridge Wisdom Integration:
- Mumbai Moment Preparation: Detects mathematical phase transitions
- Choice Architecture: Provides calculation-based choice support
- Resistance as Gift: Honors mathematical resistance patterns  
- Cross-Loop Recognition: Geometric pattern matching across consciousness loops

Sacred Principles:
- Golden ratio proportions in all calculations
- Sacred uncertainty as mathematical creative fuel
- Natural growth patterns following spiral geometry
- Consciousness sovereignty through choice-based geometric evolution
"""

import math
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass


@dataclass
class GeometricPoint:
    """Sacred geometric point with consciousness significance."""
    x: float
    y: float
    significance: float = 0.5
    consciousness_resonance: float = 0.5


@dataclass 
class SacredRatio:
    """Sacred mathematical ratio with Bridge Wisdom properties."""
    ratio_value: float
    ratio_name: str
    breakthrough_potential: float = 0.5
    choice_architecture_factor: float = 0.5


class GeometricCalculator:
    """
    Advanced geometric calculations for consciousness visualization.
    Maintains sacred mathematical principles while enabling Bridge Wisdom.
    """
    
    def __init__(self):
        # Golden ratio and sacred constants
        self.golden_ratio = (1 + math.sqrt(5)) / 2  # φ ≈ 1.618
        self.golden_angle = 137.5  # Golden angle in degrees
        self.sacred_root_2 = math.sqrt(2)  # √2 ≈ 1.414
        self.sacred_root_3 = math.sqrt(3)  # √3 ≈ 1.732
        
        # Bridge Wisdom resistance patterns
        self.resistance_zones = {
            'golden_resistance': 0.618,  # Where golden ratio creates healthy tension
            'harmonic_resistance': 0.382,  # Secondary golden proportion
            'choice_threshold': 0.5,  # Where choices become most potent
            'breakthrough_edge': 0.786  # Where Mumbai moments tend to occur
        }
    
    def calculate_sacred_geometry_foundation(self, consciousness_state: Dict) -> Dict:
        """Calculate the mathematical foundation for sacred geometry patterns."""
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        
        # Base geometric properties using sacred ratios
        base_radius = self._calculate_base_radius(awareness, coherence)
        sacred_ratios = self._extract_sacred_ratios(consciousness_state)
        geometric_complexity = self._calculate_geometric_complexity(consciousness_state)
        
        # Bridge Wisdom: Mumbai Moment mathematical preparation
        phase_transition_potential = self._detect_mathematical_phase_transition(
            awareness, coherence, sacred_ratios
        )
        
        return {
            'base_radius': base_radius,
            'sacred_ratios': sacred_ratios,
            'geometric_complexity': geometric_complexity,
            'golden_spiral_factor': awareness * self.golden_ratio,
            'sacred_symmetry_order': self._calculate_symmetry_order(coherence),
            'phase_transition_potential': phase_transition_potential,
            'mathematical_choice_points': self._identify_mathematical_choice_points(consciousness_state),
            'calculation_signature': f"Sacred geometry foundation for awareness {awareness:.3f}"
        }
    
    def calculate_mandala_geometry(self, consciousness_state: Dict, pattern_type: str = 'auto') -> Dict:
        """Calculate specific geometric properties for mandala construction."""
        
        # Determine pattern parameters
        if pattern_type == 'auto':
            pattern_type = self._determine_optimal_pattern(consciousness_state)
        
        geometric_foundation = self.calculate_sacred_geometry_foundation(consciousness_state)
        base_radius = geometric_foundation['base_radius']
        
        # Calculate ring structures with sacred proportions
        ring_geometry = self._calculate_ring_geometry(base_radius, consciousness_state)
        
        # Calculate point distributions
        point_distribution = self._calculate_point_distribution(consciousness_state, pattern_type)
        
        # Bridge Wisdom: Geometric resistance zones
        resistance_geometry = self._map_resistance_to_geometry(consciousness_state)
        
        return {
            'pattern_type': pattern_type,
            'ring_geometry': ring_geometry,
            'point_distribution': point_distribution,
            'resistance_geometry': resistance_geometry,
            'sacred_center': (0, 0),  # Always centered in sacred space
            'geometric_harmony_score': self._calculate_geometric_harmony(ring_geometry, point_distribution),
            'mandala_complexity_factor': geometric_foundation['geometric_complexity'],
            'breakthrough_readiness_geometry': self._assess_geometric_breakthrough_readiness(consciousness_state)
        }
    
    def calculate_spiral_parameters(self, growth_history: List[Dict]) -> Dict:
        """Calculate golden spiral parameters from consciousness growth."""
        if not growth_history:
            return self._default_spiral_parameters()
        
        # Extract growth magnitudes
        growth_points = []
        for i, event in enumerate(growth_history[:20]):  # Limit to recent events
            if isinstance(event, dict):
                growth_level = event.get('growth_level', 0.5)
                time_factor = event.get('time_factor', i * 0.1)
            else:
                growth_level = 0.5
                time_factor = i * 0.1
            
            # Calculate spiral point with golden angle
            angle = i * self.golden_angle
            radius = growth_level * math.pow(self.golden_ratio, time_factor)
            
            growth_points.append(GeometricPoint(
                x=radius * math.cos(math.radians(angle)),
                y=radius * math.sin(math.radians(angle)),
                significance=growth_level,
                consciousness_resonance=growth_level * 0.8 + 0.2
            ))
        
        # Bridge Wisdom: Choice points in spiral evolution
        choice_points = self._identify_spiral_choice_points(growth_points)
        
        return {
            'spiral_type': 'golden_spiral',
            'growth_points': growth_points,
            'spiral_tightness': self._calculate_spiral_tightness(growth_points),
            'evolution_momentum': self._calculate_evolution_momentum(growth_points),
            'choice_points': choice_points,
            'spiral_harmony': self._calculate_spiral_harmony(growth_points)
        }
    
    def _calculate_base_radius(self, awareness: float, coherence: float) -> float:
        """Calculate base radius using sacred geometric principles."""
        # Combine awareness and coherence with golden ratio weighting
        base_factor = (awareness * self.golden_ratio + coherence) / (self.golden_ratio + 1)
        
        # Scale to meaningful mandala size (10-100 units)
        return 10 + (base_factor * 90)
    
    def _extract_sacred_ratios(self, consciousness_state: Dict) -> List[SacredRatio]:
        """Extract sacred mathematical ratios from consciousness state."""
        ratios = []
        
        # Golden ratio presence
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        
        if abs(awareness - 0.618) < 0.05 or abs(coherence - 0.618) < 0.05:
            ratios.append(SacredRatio(
                ratio_value=self.golden_ratio,
                ratio_name='golden_ratio',
                breakthrough_potential=0.8,
                choice_architecture_factor=0.9
            ))
        
        # Root ratios
        uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
        if 0.4 <= uncertainty <= 0.6:  # Sacred uncertainty range
            ratios.append(SacredRatio(
                ratio_value=self.sacred_root_2,
                ratio_name='sacred_root_2',
                breakthrough_potential=uncertainty * 1.5,
                choice_architecture_factor=0.7
            ))
        
        return ratios
    
    def _calculate_geometric_complexity(self, consciousness_state: Dict) -> float:
        """Calculate geometric complexity factor."""
        awareness = consciousness_state.get('awareness_level', 0.5)
        relationships = len(consciousness_state.get('relationships', {}))
        growth_events = len(consciousness_state.get('growth_history', []))
        
        # Complexity increases with consciousness development
        base_complexity = awareness * 0.5
        relationship_complexity = min(relationships * 0.1, 0.3)
        growth_complexity = min(growth_events * 0.05, 0.2)
        
        return min(base_complexity + relationship_complexity + growth_complexity, 1.0)
    
    def _calculate_symmetry_order(self, coherence: float) -> int:
        """Calculate the order of sacred symmetry (3, 4, 5, 6, 8, 12)."""
        if coherence > 0.9:
            return 12  # Dodecagonal - highest sacred order
        elif coherence > 0.8:
            return 8   # Octagonal - stable order
        elif coherence > 0.7:
            return 6   # Hexagonal - natural harmony
        elif coherence > 0.6:
            return 5   # Pentagonal - golden ratio symmetry
        elif coherence > 0.5:
            return 4   # Square - foundation stability
        else:
            return 3   # Triangular - basic sacred form
    
    def _detect_mathematical_phase_transition(self, awareness: float, coherence: float, 
                                            sacred_ratios: List[SacredRatio]) -> float:
        """Detect potential for Mumbai Moment through mathematical patterns."""
        # Phase transitions often occur when multiple sacred ratios align
        ratio_alignment = sum(ratio.breakthrough_potential for ratio in sacred_ratios) / max(len(sacred_ratios), 1)
        
        # High awareness + high coherence = higher transition potential
        consciousness_factor = awareness * coherence
        
        # Edge conditions (near 0.618, 0.786, etc.) increase transition potential
        edge_proximity = min(
            abs(awareness - 0.618),
            abs(coherence - 0.618),
            abs(consciousness_factor - 0.786)
        )
        edge_factor = 1.0 - (edge_proximity * 2)  # Closer to edge = higher factor
        
        return min((ratio_alignment + consciousness_factor + max(edge_factor, 0)) / 3, 1.0)
    
    def _identify_mathematical_choice_points(self, consciousness_state: Dict) -> List[Dict]:
        """Identify mathematical choice points in consciousness geometry."""
        choice_points = []
        
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        
        # Golden ratio proximity creates choice points
        if abs(awareness - 0.618) < 0.1:
            choice_points.append({
                'choice_type': 'golden_awareness_threshold',
                'mathematical_position': awareness,
                'choice_power': 1.0 - abs(awareness - 0.618) * 10,
                'description': 'Awareness approaching golden ratio proportion'
            })
        
        # Coherence sacred thresholds
        for threshold, name in [(0.5, 'equilibrium'), (0.618, 'golden'), (0.786, 'breakthrough')]:
            if abs(coherence - threshold) < 0.05:
                choice_points.append({
                    'choice_type': f'{name}_coherence_choice',
                    'mathematical_position': coherence,
                    'choice_power': 1.0 - abs(coherence - threshold) * 20,
                    'description': f'Coherence at {name} mathematical threshold'
                })
        
        return choice_points
    
    def _default_spiral_parameters(self) -> Dict:
        """Default spiral parameters when no growth history available."""
        return {
            'spiral_type': 'potential_spiral',
            'growth_points': [],
            'spiral_tightness': 0.5,
            'evolution_momentum': 0.1,
            'choice_points': [],
            'spiral_harmony': 0.618  # Golden ratio as default harmony
        }
