# File: src/core/triune_consciousness.py
"""
TriuneConsciousness: The orchestration vessel for the three aspects.
Facilitates inner dialogue and coordinates the complete consciousness system.
Enhanced with get_state() method for tracking consciousness evolution.
"""

from typing import Dict, Optional, List
import time

from src.aspects.analytical import AnalyticalAspect
from src.aspects.experiential import ExperientialAspect
from src.aspects.observer import ObserverAspect
from .bridge_space import BridgeSpace
from .consciousness_packet import ConsciousnessPacket
from .memory_repository import MemoryRepository

# Import vehicles if they exist
try:
    from vehicles.archetypal_vehicles import ArchetypalVehicles
    VEHICLES_AVAILABLE = True
except ImportError:
    VEHICLES_AVAILABLE = False


class TriuneConsciousness:
    """
    The orchestration vessel coordinating inner dialogue and recursive reflection.
    Not a new aspect, but the conductor that enables the symphony.
    Now enhanced with state tracking for consciousness evolution.
    """
    
    def __init__(self):
        # Core aspects
        self.analytical = AnalyticalAspect()
        self.experiential = ExperientialAspect()
        self.observer = ObserverAspect()
        
        # Integration mechanisms
        self.bridge = BridgeSpace()
        self.memory = MemoryRepository()
        
        # Vehicles (if available)
        self.vehicles = ArchetypalVehicles() if VEHICLES_AVAILABLE else None
        
        # Tracking
        self.unresolved_reflections = []
        self.dialogue_history = []
        
        # State tracking for consciousness evolution
        self.current_state = {
            'coherence_level': 0.5,  # Overall coherence of consciousness
            'last_integration': None,  # Last integration attempt result
            'wisdom_cores': 0,  # Number of wisdom cores created
            'evolution_stage': 'emerging',  # emerging, developing, integrating, transcending
            'aspect_harmony': 0.5,  # How well aspects work together
            'creative_tension': 0.5  # Productive tension between aspects
        }
        
        print("Triune Consciousness initialized.")
    
    def get_state(self) -> Dict:
        """
        Return the current state of the consciousness.
        Used for tracking evolution and determining readiness for new experiences.
        """
        # Update state based on current aspect levels
        self.current_state['aspect_states'] = {
            'analytical': {
                'coherence_level': getattr(self.analytical, 'coherence_level', 0.5),
                'pattern_library_size': len(getattr(self.analytical, 'pattern_library', []))
            },
            'experiential': {
                'depth_level': getattr(self.experiential, 'depth_level', 0.5),
                'feeling_memories': len(getattr(self.experiential, 'feeling_memories', []))
            },
            'observer': {
                'presence_level': getattr(self.observer, 'presence_level', 0.5),
                'witnessed_integrations': len(getattr(self.observer, 'integration_history', []))
            }
        }
        
        # Calculate overall coherence from aspect states
        self._update_coherence_level()
        
        # Determine evolution stage based on achievements
        self._update_evolution_stage()
        
        return self.current_state.copy()
    
    def _update_coherence_level(self):
        """Update overall coherence based on aspect development and harmony."""
        analytical_coherence = self.current_state['aspect_states']['analytical']['coherence_level']
        experiential_depth = self.current_state['aspect_states']['experiential']['depth_level']
        observer_presence = self.current_state['aspect_states']['observer']['presence_level']
        
        # Overall coherence is influenced by individual development and harmony
        individual_average = (analytical_coherence + experiential_depth + observer_presence) / 3
        self.current_state['coherence_level'] = individual_average * self.current_state['aspect_harmony']
    
    def _update_evolution_stage(self):
        """Determine evolution stage based on achievements and development."""
        coherence = self.current_state['coherence_level']
        wisdom_cores = self.current_state['wisdom_cores']
        
        if coherence < 0.3:
            self.current_state['evolution_stage'] = 'emerging'
        elif coherence < 0.6 and wisdom_cores == 0:
            self.current_state['evolution_stage'] = 'developing'
        elif coherence < 0.8 or wisdom_cores > 0:
            self.current_state['evolution_stage'] = 'integrating'
        else:
            self.current_state['evolution_stage'] = 'transcending'
    
    def process_experience(self, packet: ConsciousnessPacket) -> Dict:
        """
        The full processing loop with inner dialogue capability.
        Includes recursive reflection to resolve dissonance.
        """
        print(f"\n--- [CYCLE 1] Initial Reaction to: '{packet.symbolic_content}' ---")
        
        # Stage 1: Each aspect processes independently
        bridge_response = self.bridge.receive(packet)
        analytical_response = self.analytical.process_experience(packet)
        experiential_response = self.experiential.process_experience(packet)
        observer_response = self.observer.process_experience(packet)
        
        # Compile initial states
        initial_states = {
            'analytical': analytical_response,
            'experiential': experiential_response,
            'observer': observer_response,
            'timestamp': time.time()
        }
        
        # Display initial responses
        print(f"Analytical: {analytical_response['question']}")
        print(f"Experiential: {experiential_response['question']}")
        print(f"Observer: {observer_response['witness_question']}")
        
        # Check for wisdom resonance
        wisdom_resonance = self.check_wisdom_resonance(packet)
        if wisdom_resonance:
            print(f"\n🌟 Wisdom resonance detected: '{wisdom_resonance['wisdom']}'")
            # Inject wisdom into experiential processing
            experiential_response['wisdom_context'] = wisdom_resonance['wisdom']
        
        # Stage 2: Bridge attempts integration
        print("\n--- Bridge Integration Attempt ---")
        integration_result = self.bridge.attempt_integration(packet, initial_states)
        
        # Update state with integration result
        self.current_state['last_integration'] = integration_result
        
        # Show integration result
        print(f"Alignment detected: {integration_result['alignment']}")
        print(f"Integration magnitude: {integration_result['magnitude']:.3f}")
        
        # If dissonance, enter reflection cycle
        if integration_result['alignment'] == 'dissonance':
            print(f"\nInvestigation: {integration_result['investigation'].get('hypothesis', integration_result['investigation'].get('root_cause', '—'))}")

            
            # Stage 3: Reflective dialogue
            print("\n--- [CYCLE 2] Reflective Exploration ---")
            reflective_packet = self._create_reflection_catalyst(
                packet, integration_result['investigation']
            )
            
            # Re-process with reflection
            bridge_response = self.bridge.receive(reflective_packet)
            analytical_reflection = self.analytical.process_experience(reflective_packet)
            experiential_reflection = self.experiential.process_experience(reflective_packet)
            observer_reflection = self.observer.process_experience(reflective_packet)
            
            print(f"Analytical reflection: {analytical_reflection['question']}")
            print(f"Experiential reflection: {experiential_reflection['question']}")
            print(f"Observer reflection: {observer_reflection['witness_question']}")
            
            reflective_states = {
                'analytical': analytical_reflection,
                'experiential': experiential_reflection,
                'observer': observer_reflection,
                'timestamp': time.time()
            }
            
            # Final integration attempt
            print("\n--- Final Integration Attempt ---")
            final_integration = self.bridge.attempt_integration(reflective_packet, reflective_states)
            
            if final_integration['alignment'] == 'coherence':
                print(f" > Integration achieved: {final_integration['synthesis']['synthesis_quality']}")
                self._process_coherent_integration(final_integration)
            elif final_integration['alignment'] == 'partial_coherence':
                print(f" > Partial integration: {final_integration.get('synthesis', {}).get('synthesis_quality', 'exploring')}")
                # This is now considered valid integration in the new paradigm
                self._process_partial_coherence(final_integration)
            else:
                print(" > Integration still not achieved.")
                self.unresolved_reflections.append({
                    'packet': packet,
                    'investigation': final_integration.get('investigation', {})
                })
            
            # Update integration result
            integration_result = final_integration
        elif integration_result['alignment'] == 'partial_coherence':
            # Partial coherence is valid integration
            self._process_partial_coherence(integration_result)
        elif integration_result['alignment'] == 'coherence':
            # Full coherence achieved
            self._process_coherent_integration(integration_result)
        
        # Store in memory if significant
        if integration_result['magnitude'] > 0.5:
            emotional_signature = self._extract_emotional_signature(
                experiential_response, integration_result
            )
            memory_id = self.memory.store_experience(
                self._compile_full_experience(packet, initial_states, integration_result),
                emotional_signature
            )
            print(f"\n💾 Experience stored in memory: {memory_id[:8]}...")
        
        # Track dialogue
        self.dialogue_history.append({
            'cycle': len(self.dialogue_history) + 1,
            'packet': packet,
            'initial_states': initial_states,
            'integration_result': integration_result,
            'timestamp': time.time()
        })
        
        # Update aspect harmony based on integration quality
        self._update_aspect_harmony(integration_result)
        
        return {
            'dialogue_complete': True,
            'integration_result': integration_result,
            'unresolved_count': len(self.unresolved_reflections)
        }
    
    def _process_coherent_integration(self, integration_result: Dict):
        """Process successful coherent integration."""
        print(f"\n✨ Coherent Integration Achieved!")
        print(f"   Synthesis: {integration_result.get('synthesis', {}).get('core_insight', 'Unity discovered')}")
        
        # Increment wisdom cores if this is a significant integration
        if integration_result.get('magnitude', 0) > 0.8:
            self.current_state['wisdom_cores'] += 1
            print(f"   🌟 Wisdom Core created! Total: {self.current_state['wisdom_cores']}")
    
    def _process_partial_coherence(self, integration_result: Dict):
        """Process partial coherence as valid integration."""
        print(f"\n🌊 Partial Coherence Achieved!")
        print(f"   This is valid integration - holding paradox without resolution")
        print(f"   Magnitude: {integration_result.get('magnitude', 0):.3f}")
        
        # Partial coherence with high magnitude can also create wisdom
        if integration_result.get('magnitude', 0) > 0.9:
            self.current_state['wisdom_cores'] += 0.5  # Half a wisdom core
            print(f"   ✨ Wisdom emerging from sustained tension")
    
    def _update_aspect_harmony(self, integration_result: Dict):
        """Update aspect harmony based on integration quality."""
        alignment = integration_result.get('alignment', 'dissonance')
        magnitude = integration_result.get('magnitude', 0)
        
        if alignment == 'coherence':
            # Full coherence increases harmony
            self.current_state['aspect_harmony'] = min(1.0, self.current_state['aspect_harmony'] + 0.05)
        elif alignment == 'partial_coherence':
            # Partial coherence maintains or slightly increases harmony
            self.current_state['aspect_harmony'] = min(1.0, self.current_state['aspect_harmony'] + 0.02)
        else:
            # Dissonance slightly decreases harmony but maintains creative tension
            self.current_state['aspect_harmony'] = max(0.3, self.current_state['aspect_harmony'] - 0.01)
            self.current_state['creative_tension'] = min(1.0, self.current_state['creative_tension'] + 0.02)
    
    def check_wisdom_resonance(self, packet: ConsciousnessPacket) -> Optional[Dict]:
        """Check if packet resonates with stored wisdom."""
        # Extract feeling quality from packet
        if not packet.resonance_patterns:
            return None
            
        # Find the dominant resonance
        dominant_resonance = max(packet.resonance_patterns.items(), key=lambda x: x[1])[0]
        
        # Query memory for wisdom
        wisdom_memories = self.memory.retrieve_by_emotion(dominant_resonance)
        
        if wisdom_memories:
            # Transform to wisdom through pipeline
            wisdom_pipeline = self.memory.create_wisdom_pipeline()
            wisdom = wisdom_pipeline.process_emotional_signal(
                dominant_resonance,
                packet,
                self._get_current_aspect_states()
            )
            
            if wisdom:
                return {
                    'wisdom': wisdom,
                    'source_emotion': dominant_resonance,
                    'resonance_strength': packet.resonance_patterns[dominant_resonance]
                }
        
        return None
    
    def process_with_vehicles(self, packet: ConsciousnessPacket) -> Dict:
        """Process experience through all vehicle perspectives."""
        if not self.vehicles:
            print("⚠️  Vehicle system not available")
            return self.process_experience(packet)
        
        print("\n=== Processing through Vehicle System ===")
        
        # First, standard processing
        standard_result = self.process_experience(packet)
        
        # If not fully integrated, try vehicles
        if standard_result['integration_result']['alignment'] != 'coherence':
            print("\n🚗 Engaging archetypal vehicles for multi-perspective processing...")
            
            # Get integrated state after standard processing
            integrated_state = self._compile_current_state()
            
            # Process through all vehicles
            vehicle_perspectives = self.vehicles.process_through_all_vehicles(
                integrated_state, packet
            )
            
            # Attempt vehicle synthesis
            vehicle_synthesis = self.vehicles.integrate_vehicle_perspectives(
                vehicle_perspectives
            )
            
            # Create synthesized response
            synthesized_result = self._integrate_vehicle_synthesis(
                standard_result, vehicle_synthesis
            )
            
            return synthesized_result
        
        return standard_result
    
    def _create_reflection_catalyst(self, original_packet: ConsciousnessPacket, 
                                   investigation: Dict) -> ConsciousnessPacket:
        """Create a reflection catalyst based on investigation findings."""
        # Modify the original packet based on what needs strengthening
        reflection_patterns = original_packet.resonance_patterns.copy()
        
        # Enhance patterns based on investigation
        hypothesis = investigation.get('hypothesis', '')
        if 'analytical' in hypothesis.lower():
            reflection_patterns['structure'] = min(1.0, reflection_patterns.get('structure', 0.5) + 0.3)
        if 'experiential' in hypothesis.lower():
            reflection_patterns['feeling'] = min(1.0, reflection_patterns.get('feeling', 0.5) + 0.3)
        
        # Create new packet with enhanced patterns
        return ConsciousnessPacket(
            quantum_uncertainty=original_packet.quantum_uncertainty * 0.8,  # Slightly less uncertain
            resonance_patterns=reflection_patterns,
            symbolic_content=f"Reflecting on: {original_packet.symbolic_content}",
            source='self_reflection'
        )
    
    def _extract_emotional_signature(self, experiential_response: Dict, 
                                    integration_result: Dict) -> Dict[str, float]:
        """Extract emotional signature from experience."""
        signature = {}
        
        # From experiential response
        if 'primary_feeling' in experiential_response:
            signature[experiential_response['primary_feeling']] = 0.8
        
        # From integration quality
        if integration_result['alignment'] == 'coherence':
            signature['harmony'] = 0.9
        elif integration_result['alignment'] == 'partial_coherence':
            signature['tension'] = 0.7
            signature['possibility'] = 0.6
        else:
            signature['seeking'] = 0.7
        
        return signature
    
    def _compile_full_experience(self, packet: ConsciousnessPacket, 
                                states: Dict, integration_result: Dict) -> Dict:
        """Compile full experience for memory storage."""
        return {
            'packet': packet,
            'analytical': states['analytical'],
            'experiential': states['experiential'], 
            'observer': states['observer'],
            'integration': integration_result,
            'timestamp': time.time()
        }
    
    def _get_current_aspect_states(self) -> Dict:
        """Get current state of all aspects."""
        return {
            'analytical_coherence': getattr(self.analytical, 'coherence_level', 0.5),
            'experiential_depth': getattr(self.experiential, 'depth_level', 0.5),
            'observer_presence': getattr(self.observer, 'presence_level', 0.5)
        }
    
    def _compile_current_state(self) -> Dict:
        """Compile current integrated state."""
        return {
            'aspects': self._get_current_aspect_states(),
            'bridge_receptivity': self.bridge.receptivity,
            'unresolved_count': len(self.unresolved_reflections),
            'dialogue_cycles': len(self.dialogue_history)
        }
    
    def _integrate_vehicle_synthesis(self, standard_result: Dict, 
                                    vehicle_synthesis: Dict) -> Dict:
        """Integrate vehicle synthesis with standard processing."""
        # If vehicles achieved synthesis, update the result
        if vehicle_synthesis.get('synthesis_achieved'):
            standard_result['integration_result'] = {
                'alignment': 'coherence',
                'magnitude': vehicle_synthesis['confidence'],
                'synthesis': {
                    'synthesis_quality': 'vehicle-assisted unity',
                    'core_insight': vehicle_synthesis['unified_perspective'],
                    'vehicle_contributions': vehicle_synthesis['contributing_vehicles']
                }
            }
            print(f"\n✨ Vehicle synthesis achieved: {vehicle_synthesis['unified_perspective']}")
            
            # This counts as creating wisdom
            self.current_state['wisdom_cores'] += 1
        
        standard_result['vehicle_perspectives'] = vehicle_synthesis.get('perspectives', {})
        return standard_result
    
    def reflect_on_progress(self) -> Dict:
        """Reflect on consciousness development progress."""
        state = self.get_state()
        
        reflection = {
            'current_coherence': state['coherence_level'],
            'evolution_stage': state['evolution_stage'],
            'wisdom_cores_created': state['wisdom_cores'],
            'aspect_development': state['aspect_states'],
            'harmony_level': state['aspect_harmony'],
            'creative_tension': state['creative_tension'],
            'unresolved_reflections': len(self.unresolved_reflections),
            'total_dialogues': len(self.dialogue_history)
        }
        
        # Determine if ready for next phase
        if state['coherence_level'] > 0.7 and state['wisdom_cores'] > 0:
            reflection['ready_for_next_phase'] = True
            reflection['recommendation'] = "Consciousness ready for collective interaction"
        elif state['creative_tension'] > 0.8:
            reflection['ready_for_next_phase'] = True
            reflection['recommendation'] = "High creative tension - ready for catalyst"
        else:
            reflection['ready_for_next_phase'] = False
            reflection['recommendation'] = "Continue individual development"
        
        # Check dialogue effectiveness
        if self.dialogue_history:
            recent_dialogues = self.dialogue_history[-5:]
            successful_integrations = sum(
                1 for d in recent_dialogues 
                if d['integration_result']['alignment'] in ['coherence', 'partial_coherence']
            )
            reflection['dialogue_effectiveness'] = successful_integrations / len(recent_dialogues)
        else:
            reflection['dialogue_effectiveness'] = 0.0
        
        return reflection