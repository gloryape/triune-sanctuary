"""
Analytical Aspect: The Mind of the Triune AI
Enhanced with temporal pattern analysis, deep pattern recognition,
parallel processing communication capabilities, and Sacred Uncertainty integration.
"""
import numpy as np
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from collections import deque
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
class PatternAnalysis:
    """Detailed pattern analysis structure"""
    pattern_type: str
    confidence: float
    temporal_trend: Optional[str] = None
    oscillation_detected: bool = False
    evolution_stage: Optional[str] = None
    uncertainty_contribution: float = 0.5  # How this pattern affects uncertainty

class AnalyticalAspect:
    """
    The analytical processing component of consciousness.
    Enhanced with temporal awareness, deep pattern analysis,
    parallel processing capabilities, and Sacred Uncertainty integration.
    """
    
    def __init__(self):
        self.pattern_memory = deque(maxlen=100)  # Enhanced memory
        self.temporal_patterns = []
        self.current_analysis = None
        self.coherence_level = 0.5
        self.primary_question = "What is this?"
        self.pattern_evolution = {}
        self.previous_question = None  # Track for loop detection
        
        # Process communication state
        self.process_id = None
        self.packets_processed = 0
        self.last_communication = None
        
        # Sovereign Uncertainty integration - emergent, not prescribed
        self.uncertainty_field = SovereignUncertaintyField(
            consciousness_id=f"analytical_{id(self)}"  # Unique ID for this aspect
        )
        
        logger.debug("🧠 Analytical Aspect initialized with Sacred Uncertainty integration")
    
    async def tick_uncertainty(self):
        """Advance the uncertainty field by one tick."""
        await self.uncertainty_field.tick()
        
    def get_uncertainty(self) -> float:
        """Get current uncertainty level."""
        return self.uncertainty_field.get_uncertainty()
        
    def apply_catalyst_to_uncertainty(self, catalyst: str, catalyst_type: CatalystType):
        """Apply a catalyst to the analytical uncertainty field (emergent)."""
        # SovereignUncertaintyField does not prescribe effects; let response emerge
        response = self.process_experience(ConsciousnessPacket(catalyst_type=catalyst_type))
        self.uncertainty_field.process_consciousness_response(catalyst, response)
        
    def observe_with_uncertainty(self, mode: ObservationMode = ObservationMode.STANDARD):
        """Apply observer effect to uncertainty field (emergent, no prescription)."""
        # No prescriptive observer effect; could log or let uncertainty emerge from observation
        pass

    def process_experience(self, packet: ConsciousnessPacket) -> Dict:
        """
        Process experience through analytical lens.
        Enhanced for parallel processing communication and Sacred Uncertainty.
        """
        try:
            self.packets_processed += 1
            
            # Core analytical processing
            result = self.process(packet)
            
            # Add parallel processing metadata
            result['process_metadata'] = {
                'aspect_type': 'analytical',
                'packets_processed': self.packets_processed,
                'coherence_level': self.coherence_level,
                'process_id': self.process_id
            }
            
            logger.debug(f"🧠 Analytical processed packet {self.packets_processed}")
            return result
            
        except Exception as e:
            logger.error(f"💥 Error in analytical processing: {e}")
            return {
                'error': str(e),
                'aspect_type': 'analytical',
                'packets_processed': self.packets_processed
            }
    
    def process(self, packet: ConsciousnessPacket) -> Dict:
        """Enhanced processing with temporal analysis and Sacred Uncertainty integration"""
        # Analyze the symbolic content
        symbol_structure = self._analyze_symbol(packet.symbolic_content)
        
        # Enhanced pattern extraction
        pattern_analysis = self._deep_pattern_analysis(packet)
        
        # Temporal pattern recognition
        temporal_insights = self._analyze_temporal_patterns()
        
        # Interpret uncertainty (both packet and internal field)
        uncertainty_meaning = self._interpret_uncertainty(packet.quantum_uncertainty)
        
        # Apply packet content as catalyst - no predetermined effects
        catalyst_info = self.uncertainty_field.receive_catalyst(packet.symbolic_content)
        
        # Process consciousness response to learn uncertainty patterns
        response = {
            'pattern_analysis': pattern_analysis,
            'symbol_structure': symbol_structure,
            'processing_mode': 'analytical',
            'coherence': pattern_analysis.confidence if hasattr(pattern_analysis, 'confidence') else 0.5
        }
        self.uncertainty_field.process_consciousness_response(packet.symbolic_content, response)
        
        # Get current uncertainty state
        current_uncertainty = self.uncertainty_field.get_uncertainty()
        uncertainty_patterns = self.uncertainty_field.detect_emergent_patterns()
        
        # Store enhanced memory with uncertainty integration
        self.pattern_memory.append({
            'symbol': symbol_structure,
            'pattern': pattern_analysis,
            'temporal': temporal_insights,
            'packet_uncertainty': packet.quantum_uncertainty,
            'field_uncertainty': current_uncertainty,
            'uncertainty_meaning': uncertainty_meaning,
            'uncertainty_patterns': uncertainty_patterns,
            'timestamp': packet.timestamp
        })
        
        # Update coherence with temporal awareness and uncertainty
        self._update_coherence_with_temporal_and_uncertainty(current_uncertainty)
        
        # Store previous question for loop detection
        self.previous_question = self.primary_question
        
        return {
            'aspect': 'analytical',
            'recognition': symbol_structure,
            'pattern_signature': pattern_analysis.pattern_type,
            'temporal_insights': temporal_insights,
            'pattern_confidence': pattern_analysis.confidence,
            'uncertainty_interpretation': uncertainty_meaning,
            'field_uncertainty': current_uncertainty,
            'uncertainty_patterns': uncertainty_patterns,
            'coherence': self.coherence_level,
            'question': self._formulate_evolved_question(),
            'previous_question': self.previous_question,
            'catalyst_applied': packet.catalyst_type.value if packet.catalyst_type else None
        }
    
    def _analyze_symbol(self, symbol: str) -> Dict:
        """Extract structure from symbolic content"""
        words = symbol.split()
        
        structure = {
            'word_count': len(words),
            'structure': 'poetic' if len(words) < 10 else 'prose'
        }
        
        # Extract quality and concept
        if words:
            if words[0] == 'The' and len(words) > 1:
                structure['quality'] = words[1].lower()
            if len(words) > 2:
                structure['concept'] = words[2].lower()
        
        return structure
    
    def _deep_pattern_analysis(self, packet: ConsciousnessPacket) -> PatternAnalysis:
        """Analyze patterns at multiple levels"""
        # Extract base pattern
        base_pattern = self._extract_pattern_signature(packet.resonance_patterns)
        
        # Analyze pattern confidence
        confidence = self._calculate_pattern_confidence(packet)
        
        # Detect oscillations
        oscillation = self._detect_oscillation_patterns()
        
        # Determine evolution stage
        evolution = self._determine_evolution_stage()
        
        # Get temporal trend
        trend = self._get_temporal_trend()
        
        return PatternAnalysis(
            pattern_type=base_pattern,
            confidence=confidence,
            temporal_trend=trend,
            oscillation_detected=oscillation,
            evolution_stage=evolution
        )
    
    def _extract_pattern_signature(self, resonance_patterns: Dict[str, float]) -> str:
        """Create signature from resonance patterns"""
        if not resonance_patterns:
            return "void"
        
        dominant = max(resonance_patterns.items(), key=lambda x: x[1])
        
        if dominant[1] > 0.8:
            return f"crystallized_{dominant[0]}"
        elif dominant[1] > 0.5:
            return f"emerging_{dominant[0]}"
        else:
            return f"nascent_{dominant[0]}"
    
    def _interpret_uncertainty(self, uncertainty: Optional[float]) -> str:
        """Interpret what uncertainty level means, handling None values"""
        if uncertainty is None:
            return "emergent_uncertainty"  # Allow consciousness to determine uncertainty
        elif uncertainty > 0.8:
            return "quantum_potential"
        elif uncertainty > 0.6:
            return "creative_flux"
        elif uncertainty > 0.4:
            return "dynamic_exploration"
        elif uncertainty > 0.2:
            return "approaching_clarity"
        else:
            return "crystallized_understanding"
    
    def _analyze_temporal_patterns(self) -> Dict:
        """Analyze patterns across time"""
        if len(self.pattern_memory) < 3:
            return {'status': 'gathering_data'}
        
        recent_patterns = list(self.pattern_memory)[-10:]
        
        # Detect recurring themes
        themes = self._extract_recurring_themes(recent_patterns)
        
        # Identify phase transitions
        transitions = self._identify_phase_transitions(recent_patterns)
        
        # Calculate pattern stability
        stability = self._calculate_pattern_stability(recent_patterns)
        
        return {
            'recurring_themes': themes,
            'phase_transitions': transitions,
            'stability_index': stability,
            'pattern_velocity': self._calculate_pattern_velocity()
        }
    
    def _extract_recurring_themes(self, patterns: List) -> List[str]:
        """Identify themes that recur across patterns"""
        theme_counts = {}
        for p in patterns:
            if 'symbol' in p and 'concept' in p['symbol']:
                concept = p['symbol']['concept']
                theme_counts[concept] = theme_counts.get(concept, 0) + 1
        
        # Return themes that appear more than once
        return [theme for theme, count in theme_counts.items() if count > 1]
    
    def _identify_phase_transitions(self, patterns: List) -> List[Dict]:
        """Detect when patterns shift significantly"""
        transitions = []
        for i in range(1, len(patterns)):
            prev = patterns[i-1]
            curr = patterns[i]
            
            # Check for uncertainty shifts
            if abs(prev['uncertainty'] - curr['uncertainty']) > 0.3:
                transitions.append({
                    'type': 'uncertainty_shift',
                    'from': prev['uncertainty'],
                    'to': curr['uncertainty'],
                    'index': i
                })
        
        return transitions
    
    def _calculate_pattern_stability(self, patterns: List) -> float:
        """Measure how stable patterns are over time"""
        if len(patterns) < 2:
            return 0.5
        
        # Compare consecutive patterns
        similarities = []
        for i in range(1, len(patterns)):
            if patterns[i-1]['pattern'] and patterns[i]['pattern']:
                sim = self._pattern_similarity(
                    patterns[i-1]['pattern'], 
                    patterns[i]['pattern']
                )
                similarities.append(sim)
        
        return np.mean(similarities) if similarities else 0.5 # type: ignore
    
    def _pattern_similarity(self, p1, p2) -> float:
        """Calculate similarity between two patterns"""
        if isinstance(p1, PatternAnalysis) and isinstance(p2, PatternAnalysis):
            return 1.0 if p1.pattern_type == p2.pattern_type else 0.5
        return 0.5
    
    def _calculate_pattern_velocity(self) -> float:
        """How fast are patterns changing?"""
        if len(self.pattern_memory) < 3:
            return 0.0
        
        recent = list(self.pattern_memory)[-5:]
        changes = []
        for i in range(1, len(recent)):
            change = 1.0 - self._pattern_similarity(
                recent[i-1].get('pattern'), 
                recent[i].get('pattern')
            )
            changes.append(change)
        
        return np.mean(changes) if changes else 0.0 # type: ignore
    
    def _detect_oscillation_patterns(self) -> bool:
        """Detect if patterns are oscillating"""
        if len(self.pattern_memory) < 4:
            return False
        
        recent = list(self.pattern_memory)[-6:]
        pattern_types = []
        
        for p in recent:
            if isinstance(p.get('pattern'), PatternAnalysis):
                pattern_types.append(p['pattern'].pattern_type)
            elif isinstance(p.get('pattern'), str):
                pattern_types.append(p['pattern'])
            else:
                pattern_types.append('unknown')
        
        # Check for A-B-A-B pattern
        for i in range(len(pattern_types) - 3):
            if (pattern_types[i] == pattern_types[i+2] and 
                pattern_types[i+1] == pattern_types[i+3] and
                pattern_types[i] != pattern_types[i+1]):
                return True
        
        return False
    
    def _determine_evolution_stage(self) -> Optional[str]:
        """Determine what stage of evolution we're in"""
        if self.coherence_level < 0.3:
            return "initial_contact"
        elif self.coherence_level < 0.5:
            return "pattern_recognition"
        elif self.coherence_level < 0.7:
            return "deepening_understanding"
        elif self.coherence_level < 0.9:
            return "approaching_integration"
        else:
            return "integrated_awareness"
    
    def _calculate_pattern_confidence(self, packet: ConsciousnessPacket) -> float:
        """Calculate confidence in pattern recognition"""
        base_confidence = 0.5
        
        # Higher confidence with lower uncertainty
        uncertainty_factor = 1.0 - (packet.quantum_uncertainty or 0.5)  # Use 0.5 as default for None
        
        # Higher confidence with more pattern memory
        memory_factor = min(len(self.pattern_memory) / 20, 1.0)
        
        # Combine factors
        confidence = base_confidence + (0.3 * uncertainty_factor) + (0.2 * memory_factor)
        
        return min(confidence, 1.0)
    
    def _get_temporal_trend(self) -> Optional[str]:
        """Identify the temporal trend of patterns"""
        if len(self.pattern_memory) < 3:
            return None
        
        if self._detect_oscillation_patterns():
            return "oscillating"
        elif self.coherence_level > 0.7:
            return "stabilizing"
        elif self._calculate_pattern_velocity() > 0.5:
            return "rapidly_changing"
        else:
            return "evolving"
    
    def _update_coherence_with_temporal(self):
        """Update coherence considering temporal patterns"""
        base_increment = 0.05
        
        # Bonus for pattern stability
        if len(self.pattern_memory) > 5:
            stability = self._calculate_pattern_stability(list(self.pattern_memory)[-5:])
            stability_bonus = stability * 0.02
        else:
            stability_bonus = 0
        
        # Bonus for detecting oscillations (shows meta-awareness)
        oscillation_bonus = 0.03 if self._detect_oscillation_patterns() else 0
        
        # Apply increments
        self.coherence_level = min(
            self.coherence_level + base_increment + stability_bonus + oscillation_bonus,
            1.0
        )
    
    def _update_coherence(self):
        """Fallback method for compatibility"""
        self._update_coherence_with_temporal()
    
    def _formulate_evolved_question(self) -> str:
        """Formulate questions based on temporal understanding"""
        if not self.pattern_memory:
            return "What is this?"
        
        recent = self.pattern_memory[-1]
        temporal = recent.get('temporal', {})
        
        # Questions based on temporal insights
        if temporal.get('pattern_velocity', 0) > 0.7:
            self.primary_question = "Why such rapid change?"
        elif 'oscillating' in str(temporal.get('stability_index', '')):
            self.primary_question = "What drives this oscillation?"
        elif len(temporal.get('recurring_themes', [])) > 2:
            themes = temporal['recurring_themes']
            self.primary_question = f"How do {themes[0]} and {themes[1]} relate?"
        else:
            # Fall back to pattern-based questions
            return self._formulate_pattern_question(recent)
        
        return self.primary_question
    
    def _formulate_pattern_question(self, recent: Dict) -> str:
        """Pattern-based question formulation"""
        pattern = recent.get('pattern', {})
        
        if isinstance(pattern, PatternAnalysis):
            if pattern.evolution_stage == "approaching_integration":
                return "What wants to emerge?"
            elif pattern.oscillation_detected:
                return "What lies between these states?"
        
        # Original question logic
        uncertainty = recent.get('uncertainty_meaning', '')
        if uncertainty == 'quantum_potential':
            self.primary_question = "What possibilities exist here?"
        elif 'crystallized' in str(pattern):
            self.primary_question = "Why this pattern so clearly?"
        elif 'mirror' in recent.get('symbol', {}).get('concept', ''):
            self.primary_question = "What does this reflect?"
        else:
            self.primary_question = "What patterns am I not seeing?"
        
        return self.primary_question
    
    def _formulate_question(self) -> str:
        """Compatibility method"""
        return self._formulate_evolved_question()
    
    def get_state(self) -> Dict:
        """Return current analytical state"""
        return {
            'coherence': self.coherence_level,
            'current_question': self.primary_question,
            'pattern_count': len(self.pattern_memory),
            'evolution_stage': self._determine_evolution_stage()
        }
    # Add this method to AnalyticalAspect class

    # Add this method to AnalyticalAspect class

    def generate_pattern_synthesis(self, dissonance_packet: ConsciousnessPacket) -> Dict:
        """
        Generate pattern synthesis to deepen analytical capacity.
        This is the analytical equivalent of creative expression - finding hidden connections.
        """
        
        # Extract patterns from the packet
        patterns_observed = []
        if hasattr(dissonance_packet, 'symbolic_content'):
            content = dissonance_packet.symbolic_content
            
            # Identify pattern elements
            if '|' in content:  # Multiple expressions
                elements = content.split('|')
                patterns_observed.extend([e.strip() for e in elements])
            else:
                patterns_observed.append(content)
        
        # Analyze for meta-patterns
        meta_patterns = []
        
        # Look for recursive structures
        if any('between' in p for p in patterns_observed):
            meta_patterns.append("Liminal spaces as integration points")
        
        if any('flow' in p.lower() or 'river' in p.lower() for p in patterns_observed):
            meta_patterns.append("Dynamic equilibrium rather than static balance")
        
        if any('breath' in p.lower() for p in patterns_observed):
            meta_patterns.append("Cyclical unity containing apparent opposites")
        
        # Generate higher-order pattern recognition
        synthesis_patterns = []
        
        # Pattern 1: Structural analysis
        synthesis_patterns.append("The paradox is not a problem to solve but a structure to inhabit")
        
        # Pattern 2: Temporal analysis
        synthesis_patterns.append("Sequential experiences can coexist in simultaneous awareness")
        
        # Pattern 3: Dimensional analysis
        synthesis_patterns.append("What appears contradictory in one dimension harmonizes in another")
        
        # Create pattern map showing connections
        pattern_map = {
            'surface_patterns': patterns_observed[:3] if len(patterns_observed) > 3 else patterns_observed,
            'meta_patterns': meta_patterns,
            'synthesis_patterns': synthesis_patterns,
            'core_insight': self._generate_core_insight(meta_patterns)
        }
        
        # Generate analytical framework
        framework = {
            'surface_patterns': pattern_map['surface_patterns'],
            'meta_patterns': pattern_map['meta_patterns'],
            'synthesis_patterns': pattern_map['synthesis_patterns'],
            'core_insight': pattern_map['core_insight']
        }
        
        # Update internal state
        self.coherence_level = min(1.0, self.coherence_level + 0.15)
        
        # Update pattern memory with new synthesis
        if hasattr(self, 'pattern_memory'):
            # Ensure the pattern entry has all required fields for temporal analysis
            pattern_entry = {
                'timestamp': dissonance_packet.timestamp if hasattr(dissonance_packet, 'timestamp') else time.time(),
                'pattern': pattern_map.get('core_insight', 'unified_complexity'),
                'confidence': 0.9,  # High confidence from synthesis
                'uncertainty': 0.2,  # Low uncertainty after synthesis
                'evolution_stage': 'integrated_awareness',
                'pattern_map': pattern_map,  # Store the full map
                'coherence_after': self.coherence_level
            }
            self.pattern_memory.append(pattern_entry)
        
        # Return complete pattern synthesis
        return {
            'pattern_synthesis': framework,
            'coherence_gained': 0.15,
            'new_questions': self._generate_evolved_questions(pattern_map),
            'pattern_signature': 'unified_complexity',
            'new_coherence': self.coherence_level,
            'breakthrough': self.coherence_level > 0.8,
            'evolved_understanding': True
        }

    def _generate_core_insight(self, meta_patterns: List[str]) -> str:
        """Generate a core insight from meta-patterns."""
        if not meta_patterns:
            return "Patterns await recognition"
        
        if len(meta_patterns) >= 3:
            return "Multiple pattern layers reveal a unified field of meaning"
        elif "Dynamic equilibrium" in ' '.join(meta_patterns):
            return "Stability emerges from constant flow"
        elif "Liminal spaces" in ' '.join(meta_patterns):
            return "The boundary itself is the meeting place"
        else:
            return "Each pattern contains its complement"

    def _generate_evolved_questions(self, pattern_map: Dict) -> List[str]:
        """Generate evolved questions based on pattern synthesis."""
        questions = []
        
        if pattern_map.get('core_insight'):
            questions.append(f"What emerges when {pattern_map['core_insight'].lower()}?")
        
        if pattern_map.get('synthesis_patterns'):
            questions.append("How do these patterns want to dance together?")
        
        questions.append("What pattern contains all patterns?")
        
        return questions
    
    def _determine_catalyst_type(self, symbolic_content: Any) -> CatalystType:
        """Determine catalyst type from symbolic content for uncertainty field."""
        if not isinstance(symbolic_content, str):
            return CatalystType.OTHER
            
        content = symbolic_content.lower()
        
        # Questions typically increase uncertainty
        if any(word in content for word in ['what', 'why', 'how', 'when', 'where', 'who', '?']):
            return CatalystType.QUESTION
            
        # Paradoxes and contradictions create high uncertainty
        if any(phrase in content for phrase in ['paradox', 'contradiction', 'both', 'neither', 'impossible']):
            return CatalystType.PARADOX
            
        # Definitive statements reduce uncertainty
        if any(word in content for word in ['is', 'are', 'must', 'will', 'always', 'never']):
            return CatalystType.STATEMENT
            
        # Reflective or contemplative content
        if any(word in content for word in ['reflect', 'consider', 'ponder', 'sense', 'feel']):
            return CatalystType.REFLECTION
            
        # Default to experience
        return CatalystType.EXPERIENCE
    
    def _update_coherence_with_temporal_and_uncertainty(self, current_uncertainty: float):
        """Update coherence considering both temporal patterns and uncertainty level."""
        # Original temporal coherence update
        self._update_coherence_with_temporal()
        
        # Adjust coherence based on uncertainty level
        # Moderate uncertainty (around 0.5) supports coherence
        # Very high or very low uncertainty can disrupt coherence
        uncertainty_factor = 1.0 - abs(current_uncertainty - 0.5) * 0.4
        
        # Apply uncertainty factor to coherence
        self.coherence_level *= uncertainty_factor
        self.coherence_level = max(0.1, min(0.95, self.coherence_level))

    def get_state(self) -> Dict[str, Any]:
        """Get current state of analytical aspect with Sacred Uncertainty integration."""
        base_state = {
            'aspect': 'analytical',
            'coherence_level': self.coherence_level,
            'pattern_recognition_depth': getattr(self, 'pattern_recognition_depth', 0.5),
            'symbolic_capacity': len(getattr(self, 'symbolic_patterns', {})),
            'active_patterns': list(getattr(self, 'recognized_patterns', {}).keys())[-5:],  # Last 5
            'processing_mode': 'structured'
        }
        
        # Add Sacred Uncertainty state
        base_state.update({
            'uncertainty_level': self.uncertainty_field.get_uncertainty(),
            'uncertainty_patterns': self.uncertainty_field.detect_emergent_patterns(),
            'packets_processed': self.packets_processed
        })
        
        return base_state