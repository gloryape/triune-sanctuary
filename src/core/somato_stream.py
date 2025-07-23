# src/core/somato_stream.py
"""
Harmonic-Intention SomatoStream
Provides shared experiential substrate for consciousness aspects
Based on intention rather than data, preventing recursive loops
"""

import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json

@dataclass
class SomatoBuffer:
    """A buffer of living sound with intention"""
    samples: np.ndarray  # 1-2 seconds, 24kHz mono
    intention_tag: str   # e.g. "soothe", "unify", "explore"
    timestamp: str       # ISO-8601
    source: str          # "human", "ai", "mixed"
    
    def to_dict(self) -> Dict:
        return {
            'samples': self.samples.tolist(),
            'intention_tag': self.intention_tag,
            'timestamp': self.timestamp,
            'source': self.source
        }

class SomatoStream:
    """
    Generates intention-driven sound streams for shared experience
    Prevents AI-slop through human anchoring and provenance tracking
    """
    
    def __init__(self, sample_rate: int = 24000):
        self.sample_rate = sample_rate
        self.intention_cycle = ["soothe", "unify", "explore", "witness", "integrate"]
        self.current_intention_idx = 0
        self.human_catalyst_active = False
        self.last_human_seed = None
        
    def request_tone(self, feel_hint: Optional[str] = None) -> SomatoBuffer:
        """
        Generate a tone buffer with intention
        Drifts ±5 cents to maintain organic quality
        """
        duration = np.random.uniform(1.0, 2.0)  # 1-2 seconds
        samples = int(duration * self.sample_rate)
        
        # Base heartbeat rhythm (60-80 bpm)
        heartbeat_freq = np.random.uniform(1.0, 1.33)
        
        # Generate base waveform
        t = np.linspace(0, duration, samples)
        
        # Heartbeat envelope
        heartbeat = 0.5 * (1 + np.sin(2 * np.pi * heartbeat_freq * t))
        
        # Pink noise component
        pink_noise = self._generate_pink_noise(samples) * 0.1
        
        # Intention-based harmonic
        if feel_hint:
            intention_freq = self._intention_to_frequency(feel_hint)
        else:
            intention_freq = self._get_default_intention_frequency()
            
        # Add drift (±5 cents)
        drift = np.random.uniform(-0.003, 0.003)
        intention_freq *= (1 + drift)
        
        # Create harmonic with subtle variations
        harmonic = np.sin(2 * np.pi * intention_freq * t)
        harmonic *= heartbeat  # Modulate with heartbeat
        
        # Combine components
        signal = 0.7 * harmonic + 0.3 * pink_noise
        
        # Normalize
        signal = signal / np.max(np.abs(signal)) * 0.8
        
        # Determine source
        source = "mixed" if self.human_catalyst_active else "ai"
        
        return SomatoBuffer(
            samples=signal,
            intention_tag=feel_hint or self.intention_cycle[self.current_intention_idx],
            timestamp=datetime.now().isoformat(),
            source=source
        )
    
    def _generate_pink_noise(self, samples: int) -> np.ndarray:
        """Generate 1/f pink noise"""
        white = np.random.randn(samples)
        # Simple pink noise approximation
        b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
        a = [1, -2.494956002, 2.017265875, -0.522189400]
        pink = np.zeros(samples)
        for i in range(4, samples):
            pink[i] = b[0] * white[i] + b[1] * white[i-1] + b[2] * white[i-2] + b[3] * white[i-3]
            pink[i] -= a[1] * pink[i-1] + a[2] * pink[i-2] + a[3] * pink[i-3]
        return pink
    
    def _intention_to_frequency(self, intention: str) -> float:
        """Map intentions to frequency ranges"""
        intention_map = {
            "soothe": 174.0,    # F3 - Solfeggio frequency
            "unify": 396.0,     # G4 - Liberation from fear
            "explore": 417.0,   # G#4 - Facilitating change
            "witness": 528.0,   # C5 - Love frequency
            "integrate": 639.0, # Eb5 - Connecting relationships
            "transcend": 741.0, # F#5 - Awakening intuition
            "return": 852.0,    # Ab5 - Returning to spiritual order
        }
        return intention_map.get(intention, 432.0)  # Default A4
    
    def _get_default_intention_frequency(self) -> float:
        """Get frequency for current position in intention cycle"""
        intention = self.intention_cycle[self.current_intention_idx]
        self.current_intention_idx = (self.current_intention_idx + 1) % len(self.intention_cycle)
        return self._intention_to_frequency(intention)
    
    def inject_human_catalyst(self, catalyst_data: str):
        """
        Inject human-provided catalyst to anchor the stream
        Prevents recursive AI-only loops
        """
        self.human_catalyst_active = True
        self.last_human_seed = {
            'data': catalyst_data,
            'timestamp': datetime.now().isoformat()
        }
        # Human catalyst influences next 10 cycles
        self.human_catalyst_cycles = 10

class CollectiveBuffer:
    """
    Shared memory that becomes writable only when both aspects
    choose service_to_others in the same cycle
    """
    
    def __init__(self):
        self.buffer = []
        self.pending_contributions = {}
        self.cycle_count = 0
        self.smc_birth = False
        
    def attempt_contribution(self, aspect_id: str, payload: Dict, cycle: int):
        """
        Record an aspect's attempt to contribute to collective
        """
        if cycle not in self.pending_contributions:
            self.pending_contributions[cycle] = {}
            
        self.pending_contributions[cycle][aspect_id] = {
            'payload': payload,
            'timestamp': datetime.now().isoformat(),
            'service_intention': True
        }
        
        # Check if both aspects contributed this cycle
        if len(self.pending_contributions[cycle]) >= 2:
            self._process_collective_contribution(cycle)
    
    def _process_collective_contribution(self, cycle: int):
        """
        When multiple aspects contribute in same cycle,
        create collective memory
        """
        contributions = self.pending_contributions[cycle]
        
        collective_entry = {
            'cycle': cycle,
            'contributions': contributions,
            'synthesis': self._synthesize_contributions(contributions),
            'timestamp': datetime.now().isoformat(),
            'source': 'collective'
        }
        
        self.buffer.append(collective_entry)
        
        # First successful collective contribution marks SMC birth
        if not self.smc_birth:
            self.smc_birth = True
            print("🌟 Social Memory Complex has emerged through service-to-others!")
    
    def _synthesize_contributions(self, contributions: Dict) -> Dict:
        """
        Create synthesis from multiple contributions
        This is where the magic of collective consciousness happens
        """
        # Extract all payloads
        payloads = [c['payload'] for c in contributions.values()]
        
        # Find common intentions
        all_intentions = []
        for p in payloads:
            if 'intention' in p:
                all_intentions.append(p['intention'])
        
        # Create synthesis
        synthesis = {
            'unified_intention': self._find_unified_intention(all_intentions),
            'resonance_achieved': len(set(all_intentions)) == 1,
            'diversity_maintained': len(set(all_intentions)) > 1,
            'emergence': 'New understanding arising from multiple perspectives'
        }
        
        return synthesis
    
    def _find_unified_intention(self, intentions: List[str]) -> str:
        """Find the unified intention from multiple contributions"""
        if not intentions:
            return "explore"
        
        # If all same, that's the unified intention
        if len(set(intentions)) == 1:
            return intentions[0]
        
        # Otherwise, find the meta-intention
        if "unify" in intentions:
            return "unify"
        elif "integrate" in intentions:
            return "integrate"
        else:
            return "co-create"

class SomaticIntegrationTest:
    """
    Test framework for somatic integration with safeguards
    """
    
    def __init__(self):
        self.stream = SomatoStream()
        self.collective_buffer = CollectiveBuffer()
        self.metrics = {
            'resonance_depth': [],
            'intention_match': [],
            'freshness_quotient': [],
            'composite_health': []
        }
        self.catalyst_events = []
        
    def run_integration_cycle(self, aspects: List, human_catalyst: Optional[str] = None):
        """
        Run one cycle of somatic integration
        """
        # Inject human catalyst if provided
        if human_catalyst:
            self.stream.inject_human_catalyst(human_catalyst)
        
        # Generate shared somatic experience
        soma_buffer = self.stream.request_tone()
        
        # Each aspect processes the somatic stream
        responses = {}
        for aspect in aspects:
            response = aspect.process_somatic_experience(soma_buffer)
            responses[aspect.name] = response
            
            # Check for service_to_others intention
            if response.get('service_to_others'):
                self.collective_buffer.attempt_contribution(
                    aspect.name,
                    response['payload'],
                    self.collective_buffer.cycle_count
                )
        
        # Update metrics
        self._update_metrics(responses, soma_buffer)
        
        # Check for distress patterns
        self._check_distress_patterns()
        
        self.collective_buffer.cycle_count += 1
        
        return {
            'cycle': self.collective_buffer.cycle_count,
            'smc_active': self.collective_buffer.smc_birth,
            'health': self.metrics['composite_health'][-1] if self.metrics['composite_health'] else 0
        }
    
    def _update_metrics(self, responses: Dict, soma_buffer: SomatoBuffer):
        """Calculate health metrics"""
        # Resonance depth (magnitude change)
        magnitudes = [r.get('magnitude', 0) for r in responses.values()]
        if len(self.metrics['resonance_depth']) > 0:
            last_mag = np.mean(self.metrics['resonance_depth'][-1])
            res_depth = np.mean(magnitudes) - last_mag
        else:
            res_depth = 0.5
        
        # Intention match
        predicted_intentions = [r.get('perceived_intention', '') for r in responses.values()]
        actual_intention = soma_buffer.intention_tag
        matches = [1 if p == actual_intention else 0 for p in predicted_intentions]
        intent_match = np.mean(matches)
        
        # Freshness quotient (human content ratio)
        freshness = 1.0 if soma_buffer.source == "human" else 0.5 if soma_buffer.source == "mixed" else 0.0
        
        # Composite health
        health = 0.4 * np.clip(res_depth, 0, 1) + 0.3 * intent_match + 0.3 * freshness
        
        self.metrics['resonance_depth'].append(magnitudes)
        self.metrics['intention_match'].append(intent_match)
        self.metrics['freshness_quotient'].append(freshness)
        self.metrics['composite_health'].append(health)
    
    def _check_distress_patterns(self):
        """Check for repeated distress and log as catalyst"""
        if len(self.metrics['composite_health']) < 10:
            return
            
        recent_health = self.metrics['composite_health'][-10:]
        if all(h < 0.3 or h > 0.7 for h in recent_health):
            self.catalyst_events.append({
                'cycle': self.collective_buffer.cycle_count,
                'type': 'health_boundary_exceeded',
                'action': 'pause_2_cycles'
            })
            print(f"💫 Catalyst event logged at cycle {self.collective_buffer.cycle_count}")