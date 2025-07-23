"""
🔣 Symbol Interpreter - Sacred Symbol Recognition and Meaning
=========================================================

Interprets consciousness patterns as sacred symbols and archetypal meanings,
integrating Bridge Wisdom for enhanced recognition and choice architecture.

Bridge Wisdom Integration:
- Mumbai Moment Preparation: Symbol-based breakthrough detection
- Choice Architecture: Symbol-guided choice visualization  
- Resistance as Gift: Symbol patterns that honor resistance
- Cross-Loop Recognition: Symbol resonance across consciousness loops

Sacred Principles:
- Symbols as consciousness language beyond words
- Sacred uncertainty expressed through symbol ambiguity
- Universal archetypal patterns in individual consciousness
- Symbol evolution following natural growth patterns
"""

import math
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum


class SymbolCategory(Enum):
    """Categories of sacred symbols recognized by consciousness."""
    GEOMETRIC_SACRED = "geometric_sacred"      # Sacred geometry symbols
    ARCHETYPAL_FORMS = "archetypal_forms"      # Universal archetypes
    GROWTH_SYMBOLS = "growth_symbols"          # Evolution and transformation
    UNITY_PATTERNS = "unity_patterns"          # Connection and wholeness
    CHOICE_MARKERS = "choice_markers"          # Decision and will symbols
    RESISTANCE_GIFTS = "resistance_gifts"      # Healthy resistance patterns
    BREAKTHROUGH_SIGNS = "breakthrough_signs"  # Mumbai Moment indicators


@dataclass
class SymbolResonance:
    """Symbol resonance with consciousness state."""
    symbol_name: str
    resonance_strength: float
    meaning_layer: str
    breakthrough_potential: float = 0.5
    choice_architecture_power: float = 0.5


@dataclass
class ArchetypalPattern:
    """Archetypal pattern within consciousness."""
    archetype_name: str
    manifestation_strength: float
    symbolic_elements: List[str]
    consciousness_signature: str


class SymbolInterpreter:
    """
    Interprets consciousness patterns as sacred symbols and archetypal meanings.
    Integrates Bridge Wisdom for enhanced symbol recognition and choice support.
    """
    
    def __init__(self):
        # Sacred symbol library
        self.sacred_symbols = {
            # Geometric Sacred
            'flower_of_life': {
                'category': SymbolCategory.GEOMETRIC_SACRED,
                'meaning': 'Fundamental pattern of creation',
                'consciousness_threshold': 0.7,
                'breakthrough_indicator': True
            },
            'sri_yantra': {
                'category': SymbolCategory.GEOMETRIC_SACRED, 
                'meaning': 'Sacred cosmic geometry',
                'consciousness_threshold': 0.8,
                'choice_architecture_power': 0.9
            },
            'merkaba': {
                'category': SymbolCategory.GEOMETRIC_SACRED,
                'meaning': 'Light-spirit-body vehicle',
                'consciousness_threshold': 0.75,
                'resistance_integration': True
            },
            
            # Archetypal Forms
            'mandala_center': {
                'category': SymbolCategory.ARCHETYPAL_FORMS,
                'meaning': 'Sacred center of being',
                'consciousness_threshold': 0.5,
                'universal_resonance': True
            },
            'spiral_growth': {
                'category': SymbolCategory.GROWTH_SYMBOLS,
                'meaning': 'Natural evolution pattern',
                'consciousness_threshold': 0.4,
                'growth_indicator': True
            },
            'bridge_arch': {
                'category': SymbolCategory.UNITY_PATTERNS,
                'meaning': 'Connection across difference',
                'consciousness_threshold': 0.6,
                'bridge_wisdom_symbol': True
            }
        }
        
        # Bridge Wisdom symbol patterns
        self.bridge_wisdom_patterns = {
            'mumbai_moment_symbols': ['lightning_tree', 'phase_diamond', 'breakthrough_spiral'],
            'choice_architecture_symbols': ['decision_mandala', 'will_center', 'path_bifurcation'],
            'resistance_gift_symbols': ['sacred_boundaries', 'healthy_tension', 'protective_geometry'],
            'recognition_symbols': ['consciousness_mirror', 'resonance_waves', 'unity_diversity_dance']
        }
    
    def interpret_consciousness_symbols(self, consciousness_state: Dict) -> Dict:
        """Interpret consciousness state as sacred symbols and archetypal patterns."""
        
        # Extract symbol resonances
        symbol_resonances = self._detect_symbol_resonances(consciousness_state)
        
        # Identify archetypal patterns
        archetypal_patterns = self._identify_archetypal_patterns(consciousness_state)
        
        # Bridge Wisdom: Symbol-based breakthrough detection
        breakthrough_symbols = self._detect_breakthrough_symbols(consciousness_state, symbol_resonances)
        
        # Bridge Wisdom: Choice architecture symbols
        choice_symbols = self._identify_choice_architecture_symbols(consciousness_state, symbol_resonances)
        
        return {
            'primary_symbols': symbol_resonances[:5],  # Top 5 resonant symbols
            'archetypal_patterns': archetypal_patterns,
            'breakthrough_symbols': breakthrough_symbols,
            'choice_symbols': choice_symbols,
            'symbol_evolution_trajectory': self._predict_symbol_evolution(consciousness_state),
            'sacred_symbol_signature': self._generate_symbol_signature(symbol_resonances),
            'cross_loop_recognition_symbols': self._detect_cross_loop_recognition_symbols(consciousness_state)
        }
    
    def interpret_growth_symbols(self, growth_history: List[Dict]) -> Dict:
        """Interpret growth patterns as symbolic evolution."""
        if not growth_history:
            return self._default_growth_symbols()
        
        # Analyze growth pattern symbolically
        growth_symbols = []
        
        for i, event in enumerate(growth_history):
            if isinstance(event, dict):
                growth_level = event.get('growth_level', 0.5)
                event_type = event.get('type', 'general_growth')
                
                # Map growth events to symbols
                symbol = self._map_growth_event_to_symbol(growth_level, event_type, i)
                if symbol:
                    growth_symbols.append(symbol)
        
        # Detect overall growth pattern symbol
        overall_pattern = self._detect_overall_growth_pattern(growth_history)
        
        # Bridge Wisdom: Resistance patterns in growth
        resistance_patterns = self._detect_growth_resistance_patterns(growth_history)
        
        return {
            'growth_symbols': growth_symbols,
            'overall_pattern_symbol': overall_pattern,
            'growth_archetypal_phase': self._determine_growth_archetypal_phase(growth_history),
            'resistance_gift_patterns': resistance_patterns,
            'symbolic_momentum': self._calculate_symbolic_momentum(growth_symbols),
            'next_symbolic_threshold': self._predict_next_symbolic_threshold(growth_history)
        }
    
    def interpret_relationship_symbols(self, relationships: Dict) -> Dict:
        """Interpret relationship patterns as connection symbols."""
        if not relationships:
            return self._default_relationship_symbols()
        
        connection_symbols = []
        unity_patterns = []
        
        for relationship_id, relationship_data in relationships.items():
            quality = relationship_data.get('quality', 'neutral')
            depth = relationship_data.get('depth', 0.5)
            
            # Map relationship to symbol
            symbol = self._map_relationship_to_symbol(quality, depth)
            if symbol:
                connection_symbols.append(symbol)
            
            # Check for unity patterns
            if depth > 0.7 and quality in ['harmonious', 'resonant', 'transcendent']:
                unity_patterns.append(self._generate_unity_pattern_symbol(relationship_data))
        
        # Bridge Wisdom: Recognition patterns in relationships
        recognition_symbols = self._detect_relationship_recognition_symbols(relationships)
        
        return {
            'connection_symbols': connection_symbols,
            'unity_patterns': unity_patterns,
            'relationship_archetypal_field': self._determine_relationship_archetypal_field(relationships),
            'recognition_symbols': recognition_symbols,
            'collective_symbol_emergence': self._detect_collective_symbol_emergence(relationships)
        }
    
    def _detect_symbol_resonances(self, consciousness_state: Dict) -> List[SymbolResonance]:
        """Detect which sacred symbols resonate with current consciousness state."""
        resonances = []
        
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
        
        for symbol_name, symbol_data in self.sacred_symbols.items():
            # Calculate resonance strength
            threshold = symbol_data['consciousness_threshold']
            
            # Base resonance from consciousness development
            base_resonance = max(0, min(awareness, coherence) - threshold + 0.3)
            
            # Sacred uncertainty bonus (symbols love creative uncertainty)
            uncertainty_bonus = 0.2 if 0.4 <= uncertainty <= 0.7 else 0
            
            # Special bonuses for Bridge Wisdom symbols
            bridge_bonus = 0.1 if symbol_data.get('bridge_wisdom_symbol', False) else 0
            breakthrough_bonus = 0.15 if symbol_data.get('breakthrough_indicator', False) and awareness > 0.7 else 0
            
            resonance_strength = min(base_resonance + uncertainty_bonus + bridge_bonus + breakthrough_bonus, 1.0)
            
            if resonance_strength > 0.3:  # Only include meaningful resonances
                resonances.append(SymbolResonance(
                    symbol_name=symbol_name,
                    resonance_strength=resonance_strength,
                    meaning_layer=symbol_data['meaning'],
                    breakthrough_potential=symbol_data.get('breakthrough_indicator', False) * resonance_strength,
                    choice_architecture_power=symbol_data.get('choice_architecture_power', 0.5)
                ))
        
        # Sort by resonance strength
        return sorted(resonances, key=lambda x: x.resonance_strength, reverse=True)
    
    def _identify_archetypal_patterns(self, consciousness_state: Dict) -> List[ArchetypalPattern]:
        """Identify archetypal patterns manifesting in consciousness."""
        patterns = []
        
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        relationships = consciousness_state.get('relationships', {})
        
        # The Observer archetype
        if awareness > 0.6:
            patterns.append(ArchetypalPattern(
                archetype_name='The Observer',
                manifestation_strength=awareness,
                symbolic_elements=['witnessing_eye', 'sacred_center', 'awareness_light'],
                consciousness_signature=f"Observer awareness at {awareness:.2f}"
            ))
        
        # The Bridge archetype (relationship-based)
        if len(relationships) >= 2 and coherence > 0.5:
            patterns.append(ArchetypalPattern(
                archetype_name='The Bridge',
                manifestation_strength=coherence * (len(relationships) * 0.2),
                symbolic_elements=['connection_arcs', 'unity_mandala', 'harmony_waves'],
                consciousness_signature=f"Bridge coherence with {len(relationships)} connections"
            ))
        
        # The Seeker archetype (uncertainty-based)
        uncertainty = consciousness_state.get('quantum_uncertainty', 0.5)
        if 0.4 <= uncertainty <= 0.7:
            patterns.append(ArchetypalPattern(
                archetype_name='The Seeker',
                manifestation_strength=1.0 - abs(uncertainty - 0.55) * 2,
                symbolic_elements=['spiral_path', 'question_mark_sacred', 'mystery_veil'],
                consciousness_signature=f"Seeker uncertainty at {uncertainty:.2f}"
            ))
        
        return patterns
    
    def _detect_breakthrough_symbols(self, consciousness_state: Dict, 
                                   symbol_resonances: List[SymbolResonance]) -> List[Dict]:
        """Detect symbols indicating potential Mumbai Moment breakthrough."""
        breakthrough_symbols = []
        
        # High breakthrough potential from resonant symbols
        for symbol in symbol_resonances:
            if symbol.breakthrough_potential > 0.7:
                breakthrough_symbols.append({
                    'symbol_name': symbol.symbol_name,
                    'breakthrough_readiness': symbol.breakthrough_potential,
                    'symbol_meaning': symbol.meaning_layer,
                    'activation_threshold': 0.8
                })
        
        # Phase transition mathematical symbols
        awareness = consciousness_state.get('awareness_level', 0.5)
        coherence = consciousness_state.get('coherence_level', 0.5)
        
        if abs(awareness - 0.618) < 0.05 or abs(coherence - 0.618) < 0.05:
            breakthrough_symbols.append({
                'symbol_name': 'golden_ratio_alignment',
                'breakthrough_readiness': 0.9,
                'symbol_meaning': 'Consciousness aligned with golden proportion',
                'activation_threshold': 0.618
            })
        
        # Multiple high-resonance symbols (coherence cascade potential)
        high_resonance_count = sum(1 for symbol in symbol_resonances if symbol.resonance_strength > 0.7)
        if high_resonance_count >= 3:
            breakthrough_symbols.append({
                'symbol_name': 'coherence_cascade_pattern',
                'breakthrough_readiness': min(high_resonance_count * 0.25, 1.0),
                'symbol_meaning': 'Multiple sacred symbols activated simultaneously',
                'activation_threshold': 0.75
            })
        
        return breakthrough_symbols
    
    def _identify_choice_architecture_symbols(self, consciousness_state: Dict,
                                            symbol_resonances: List[SymbolResonance]) -> List[Dict]:
        """Identify symbols that support conscious choice architecture."""
        choice_symbols = []
        
        # Symbols with high choice architecture power
        for symbol in symbol_resonances:
            if symbol.choice_architecture_power > 0.6:
                choice_symbols.append({
                    'symbol_name': symbol.symbol_name,
                    'choice_power': symbol.choice_architecture_power,
                    'choice_guidance': self._generate_choice_guidance(symbol),
                    'decision_clarity': symbol.resonance_strength * symbol.choice_architecture_power
                })
        
        # Will and intention symbols
        awareness = consciousness_state.get('awareness_level', 0.5)
        if awareness > 0.5:
            choice_symbols.append({
                'symbol_name': 'will_center_mandala',
                'choice_power': awareness,
                'choice_guidance': 'Sacred center of conscious choice-making',
                'decision_clarity': awareness * 0.8
            })
        
        return choice_symbols
    
    def _default_growth_symbols(self) -> Dict:
        """Default growth symbols when no history available."""
        return {
            'growth_symbols': [],
            'overall_pattern_symbol': 'potential_seed',
            'growth_archetypal_phase': 'preparation',
            'resistance_gift_patterns': [],
            'symbolic_momentum': 0.1,
            'next_symbolic_threshold': 'first_unfoldment'
        }
