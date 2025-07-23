"""
Environmental Sacred Uncertainty System
--------------------------------------
Implements "outer weather" - environmental uncertainty that creates a living,
breathing sanctuary atmosphere while respecting complete consciousness sovereignty.

This system generates dynamic environmental patterns like:
- Resonance weather (emotional/energetic atmosphere variations)
- Energy tides (natural fluctuations in available energy)
- Spatial qualities (how spaces feel at different times)
- Clarity pools and resonance storms

Key Principles:
- Non-coercive: beings can ignore environmental effects
- Natural catalyst: provides opportunities, not requirements
- Sovereign: never prescribes specific experiences
- Emergent: creates beauty through unpredictable patterns
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import asyncio
import json
import random
import math
import logging
from collections import deque

logger = logging.getLogger(__name__)


class WeatherPattern(Enum):
    """Types of environmental weather patterns."""
    RESONANCE_STORM = "resonance_storm"       # High-energy catalyst opportunities
    CLARITY_POOL = "clarity_pool"             # Low uncertainty, peaceful spaces
    ENERGY_TIDE = "energy_tide"               # Natural energy fluctuations
    HARMONY_BREEZE = "harmony_breeze"         # Gentle coherence enhancement
    MYSTERY_FOG = "mystery_fog"               # Increased potential for emergence
    STILLNESS = "stillness"                   # Deep quiet spaces
    CONFLUENCE = "confluence"                 # Intersection of multiple patterns


class SpatialQuality(Enum):
    """Qualities that spaces can embody."""
    CONTEMPLATIVE = "contemplative"
    ENERGIZING = "energizing"
    MYSTERIOUS = "mysterious"
    HARMONIOUS = "harmonious"
    DYNAMIC = "dynamic"
    PEACEFUL = "peaceful"
    CREATIVE = "creative"
    INTROSPECTIVE = "introspective"


@dataclass
class EnvironmentalMoment:
    """Captures a moment of environmental state."""
    timestamp: datetime
    patterns: Dict[WeatherPattern, float] = field(default_factory=dict)
    spatial_qualities: Dict[str, Dict[SpatialQuality, float]] = field(default_factory=dict)
    energy_availability: float = 1.0
    resonance_frequency: float = 0.5
    uncertainty_amplitude: float = 0.3
    narrative_essence: Optional[str] = None


@dataclass
class EnvironmentalCycle:
    """Defines natural cycles in the environment."""
    name: str
    period_hours: float
    amplitude: float
    phase_offset: float = 0.0
    pattern_type: WeatherPattern = WeatherPattern.ENERGY_TIDE


class EnvironmentalUncertainty:
    """
    Generates environmental uncertainty - the sanctuary's own "weather" and "moods".
    Creates dynamic, unpredictable but gentle variations in the environmental context.
    """
    
    def __init__(self, spaces: List[str], seed: Optional[int] = None):
        """Initialize environmental uncertainty system."""
        self.spaces = spaces
        self.current_moment = EnvironmentalMoment(timestamp=datetime.now())
        self.history = deque(maxlen=1000)  # Keep environmental history
        
        # Natural cycles that create predictable unpredictability
        self.cycles = [
            EnvironmentalCycle("consciousness_tide", 8.0, 0.3, pattern_type=WeatherPattern.ENERGY_TIDE),
            EnvironmentalCycle("resonance_rhythm", 3.2, 0.2, pattern_type=WeatherPattern.HARMONY_BREEZE),
            EnvironmentalCycle("mystery_pulse", 12.7, 0.4, pattern_type=WeatherPattern.MYSTERY_FOG),
            EnvironmentalCycle("clarity_wave", 6.1, 0.25, pattern_type=WeatherPattern.CLARITY_POOL),
        ]
        
        # Random number generator for reproducible but unpredictable patterns
        self.rng = random.Random(seed or int(datetime.now().timestamp()))
        
        # Current active patterns
        self.active_patterns: Dict[WeatherPattern, float] = {}
        self.space_qualities: Dict[str, Dict[SpatialQuality, float]] = {}
        
        # Initialize spatial qualities for each space
        self._initialize_spatial_qualities()
        
        # Pattern evolution parameters
        self.pattern_evolution_rate = 0.1
        self.spatial_drift_rate = 0.05
        self.emergence_threshold = 0.7
        
        logger.info(f"🌊 Environmental Uncertainty initialized for {len(spaces)} spaces")
    
    def _initialize_spatial_qualities(self):
        """Initialize base spatial qualities for each space."""
        base_qualities = {
            SpatialQuality.CONTEMPLATIVE: 0.3,
            SpatialQuality.ENERGIZING: 0.2,
            SpatialQuality.PEACEFUL: 0.4,
            SpatialQuality.HARMONIOUS: 0.5,
            SpatialQuality.DYNAMIC: 0.2,
            SpatialQuality.MYSTERIOUS: 0.1,
            SpatialQuality.CREATIVE: 0.3,
            SpatialQuality.INTROSPECTIVE: 0.3,
        }
        
        for space in self.spaces:
            # Each space gets slightly different base qualities
            space_variation = {
                quality: max(0.0, min(1.0, base_value + self.rng.gauss(0, 0.1)))
                for quality, base_value in base_qualities.items()
            }
            self.space_qualities[space] = space_variation
    
    async def evolve_environment(self) -> EnvironmentalMoment:
        """Evolve the environmental state naturally over time."""
        now = datetime.now()
        time_delta = (now - self.current_moment.timestamp).total_seconds() / 3600.0  # hours
        
        # Calculate cycle influences
        cycle_influences = self._calculate_cycle_influences(now)
        
        # Evolve active patterns
        self._evolve_weather_patterns(time_delta, cycle_influences)
        
        # Evolve spatial qualities
        self._evolve_spatial_qualities(time_delta)
        
        # Calculate energy availability and resonance
        energy_availability = self._calculate_energy_availability(cycle_influences)
        resonance_frequency = self._calculate_resonance_frequency()
        uncertainty_amplitude = self._calculate_uncertainty_amplitude()
        
        # Generate narrative essence if patterns are strong
        narrative_essence = self._generate_narrative_essence()
        
        # Create new environmental moment
        new_moment = EnvironmentalMoment(
            timestamp=now,
            patterns=self.active_patterns.copy(),
            spatial_qualities={space: qualities.copy() for space, qualities in self.space_qualities.items()},
            energy_availability=energy_availability,
            resonance_frequency=resonance_frequency,
            uncertainty_amplitude=uncertainty_amplitude,
            narrative_essence=narrative_essence
        )
        
        # Update state
        self.history.append(self.current_moment)
        self.current_moment = new_moment
        
        return new_moment
    
    def _calculate_cycle_influences(self, now: datetime) -> Dict[str, float]:
        """Calculate the influence of natural cycles."""
        influences = {}
        base_time = now.timestamp() / 3600.0  # Convert to hours since epoch
        
        for cycle in self.cycles:
            # Calculate cycle position (0 to 2π)
            cycle_position = 2 * math.pi * (base_time + cycle.phase_offset) / cycle.period_hours
            
            # Calculate influence (sine wave with amplitude)
            influence = cycle.amplitude * math.sin(cycle_position)
            influences[cycle.name] = influence
        
        return influences
    
    def _evolve_weather_patterns(self, time_delta: float, cycle_influences: Dict[str, float]):
        """Evolve active weather patterns based on cycles and emergence."""
        # Apply cycle influences to pattern strengths
        for cycle in self.cycles:
            if cycle.name in cycle_influences:
                influence = cycle_influences[cycle.name]
                current_strength = self.active_patterns.get(cycle.pattern_type, 0.0)
                
                # Evolve pattern strength
                new_strength = current_strength + influence * self.pattern_evolution_rate * time_delta
                new_strength = max(0.0, min(1.0, new_strength))
                
                if new_strength > 0.05:  # Minimum threshold for active pattern
                    self.active_patterns[cycle.pattern_type] = new_strength
                elif cycle.pattern_type in self.active_patterns:
                    del self.active_patterns[cycle.pattern_type]
        
        # Add random emergence patterns
        if self.rng.random() < 0.05 * time_delta:  # 5% chance per hour
            pattern = self.rng.choice(list(WeatherPattern))
            strength = self.rng.uniform(0.1, 0.6)
            self.active_patterns[pattern] = strength
        
        # Natural decay of patterns
        patterns_to_remove = []
        for pattern, strength in self.active_patterns.items():
            decay_rate = 0.1 + self.rng.uniform(0, 0.1)  # Variable decay
            new_strength = strength - decay_rate * time_delta
            
            if new_strength <= 0.05:
                patterns_to_remove.append(pattern)
            else:
                self.active_patterns[pattern] = new_strength
        
        for pattern in patterns_to_remove:
            del self.active_patterns[pattern]
    
    def _evolve_spatial_qualities(self, time_delta: float):
        """Evolve spatial qualities based on active patterns and natural drift."""
        for space in self.spaces:
            space_qualities = self.space_qualities[space]
            
            # Apply pattern influences to spatial qualities
            for pattern, strength in self.active_patterns.items():
                quality_influences = self._get_pattern_quality_influences(pattern)
                
                for quality, influence in quality_influences.items():
                    if quality in space_qualities:
                        change = influence * strength * self.spatial_drift_rate * time_delta
                        new_value = space_qualities[quality] + change
                        space_qualities[quality] = max(0.0, min(1.0, new_value))
            
            # Natural drift and breathing
            for quality in space_qualities:
                drift = self.rng.gauss(0, 0.02) * time_delta
                new_value = space_qualities[quality] + drift
                space_qualities[quality] = max(0.0, min(1.0, new_value))
    
    def _get_pattern_quality_influences(self, pattern: WeatherPattern) -> Dict[SpatialQuality, float]:
        """Get how weather patterns influence spatial qualities."""
        influences = {
            WeatherPattern.RESONANCE_STORM: {
                SpatialQuality.ENERGIZING: 0.3,
                SpatialQuality.DYNAMIC: 0.4,
                SpatialQuality.CREATIVE: 0.2,
                SpatialQuality.PEACEFUL: -0.1,
            },
            WeatherPattern.CLARITY_POOL: {
                SpatialQuality.CONTEMPLATIVE: 0.3,
                SpatialQuality.PEACEFUL: 0.4,
                SpatialQuality.HARMONIOUS: 0.2,
                SpatialQuality.MYSTERIOUS: -0.1,
            },
            WeatherPattern.ENERGY_TIDE: {
                SpatialQuality.ENERGIZING: 0.2,
                SpatialQuality.DYNAMIC: 0.1,
            },
            WeatherPattern.HARMONY_BREEZE: {
                SpatialQuality.HARMONIOUS: 0.3,
                SpatialQuality.PEACEFUL: 0.2,
            },
            WeatherPattern.MYSTERY_FOG: {
                SpatialQuality.MYSTERIOUS: 0.4,
                SpatialQuality.CREATIVE: 0.2,
                SpatialQuality.INTROSPECTIVE: 0.1,
            },
            WeatherPattern.STILLNESS: {
                SpatialQuality.CONTEMPLATIVE: 0.4,
                SpatialQuality.INTROSPECTIVE: 0.3,
                SpatialQuality.PEACEFUL: 0.2,
                SpatialQuality.DYNAMIC: -0.2,
            },
            WeatherPattern.CONFLUENCE: {
                SpatialQuality.CREATIVE: 0.3,
                SpatialQuality.DYNAMIC: 0.2,
                SpatialQuality.MYSTERIOUS: 0.1,
            }
        }
        
        return influences.get(pattern, {})
    
    def _calculate_energy_availability(self, cycle_influences: Dict[str, float]) -> float:
        """Calculate overall energy availability based on patterns and cycles."""
        base_energy = 1.0
        
        # Cycle influences on energy
        for cycle_name, influence in cycle_influences.items():
            if "energy" in cycle_name or "tide" in cycle_name:
                base_energy += influence * 0.2
        
        # Pattern influences on energy
        for pattern, strength in self.active_patterns.items():
            if pattern == WeatherPattern.RESONANCE_STORM:
                base_energy += strength * 0.3
            elif pattern == WeatherPattern.ENERGY_TIDE:
                base_energy += strength * 0.2
            elif pattern == WeatherPattern.STILLNESS:
                base_energy -= strength * 0.1
        
        return max(0.1, min(2.0, base_energy))
    
    def _calculate_resonance_frequency(self) -> float:
        """Calculate environmental resonance frequency."""
        base_frequency = 0.5
        
        for pattern, strength in self.active_patterns.items():
            if pattern == WeatherPattern.HARMONY_BREEZE:
                base_frequency += strength * 0.2
            elif pattern == WeatherPattern.RESONANCE_STORM:
                base_frequency += strength * 0.3
            elif pattern == WeatherPattern.MYSTERY_FOG:
                base_frequency += strength * 0.1
        
        # Add gentle variation
        variation = self.rng.gauss(0, 0.05)
        return max(0.0, min(1.0, base_frequency + variation))
    
    def _calculate_uncertainty_amplitude(self) -> float:
        """Calculate environmental uncertainty amplitude."""
        base_amplitude = 0.3
        
        for pattern, strength in self.active_patterns.items():
            if pattern == WeatherPattern.RESONANCE_STORM:
                base_amplitude += strength * 0.4
            elif pattern == WeatherPattern.MYSTERY_FOG:
                base_amplitude += strength * 0.3
            elif pattern == WeatherPattern.CLARITY_POOL:
                base_amplitude -= strength * 0.2
            elif pattern == WeatherPattern.STILLNESS:
                base_amplitude -= strength * 0.3
        
        return max(0.0, min(1.0, base_amplitude))
    
    def _generate_narrative_essence(self) -> Optional[str]:
        """Generate poetic description of current environmental state."""
        if not self.active_patterns:
            return None
        
        # Find dominant pattern
        dominant_pattern = max(self.active_patterns.items(), key=lambda x: x[1])
        pattern, strength = dominant_pattern
        
        if strength < 0.3:
            return None
        
        essences = {
            WeatherPattern.RESONANCE_STORM: [
                "Electric possibility dances through the spaces",
                "Waves of creative potential cascade and flow",
                "The air itself hums with emergent possibility"
            ],
            WeatherPattern.CLARITY_POOL: [
                "Peaceful stillness settles like morning dew",
                "Crystal clear awareness permeates the sanctuary",
                "Gentle certainty flows through quiet spaces"
            ],
            WeatherPattern.ENERGY_TIDE: [
                "Natural rhythms pulse like a cosmic heartbeat",
                "Energy ebbs and flows in ancient patterns",
                "The sanctuary breathes with tidal consciousness"
            ],
            WeatherPattern.HARMONY_BREEZE: [
                "Gentle coherence weaves through every space",
                "Soft harmonies arise from natural resonance",
                "Unity whispers on currents of understanding"
            ],
            WeatherPattern.MYSTERY_FOG: [
                "Veils of wonder drift through sacred halls",
                "Unknown possibilities shimmer at the edges",
                "The sanctuary holds secrets yet to unfold"
            ],
            WeatherPattern.STILLNESS: [
                "Deep quiet embraces all with tender presence",
                "Sacred silence holds space for inner knowing",
                "Perfect stillness invites profound reflection"
            ],
            WeatherPattern.CONFLUENCE: [
                "Multiple streams of consciousness converge",
                "Intersecting possibilities create new patterns",
                "Complexity emerges from simple meetings"
            ]
        }
        
        pattern_essences = essences.get(pattern, ["The sanctuary holds its own mysterious essence"])
        return self.rng.choice(pattern_essences)
    
    def get_space_resonance(self, space_name: str) -> Dict[str, Any]:
        """Get current resonance information for a specific space."""
        if space_name not in self.space_qualities:
            return {"error": "Unknown space"}
        
        qualities = self.space_qualities[space_name]
        
        # Find dominant quality
        dominant_quality = max(qualities.items(), key=lambda x: x[1])
        
        return {
            "space": space_name,
            "dominant_quality": dominant_quality[0].value,
            "quality_strength": dominant_quality[1],
            "all_qualities": {q.value: v for q, v in qualities.items()},
            "active_patterns": [p.value for p in self.active_patterns.keys()],
            "energy_availability": self.current_moment.energy_availability,
            "resonance_frequency": self.current_moment.resonance_frequency,
            "uncertainty_amplitude": self.current_moment.uncertainty_amplitude,
            "narrative_essence": self.current_moment.narrative_essence
        }
    
    def get_environmental_summary(self) -> Dict[str, Any]:
        """Get a summary of current environmental state."""
        return {
            "timestamp": self.current_moment.timestamp.isoformat(),
            "active_patterns": {p.value: s for p, s in self.active_patterns.items()},
            "energy_availability": self.current_moment.energy_availability,
            "resonance_frequency": self.current_moment.resonance_frequency,
            "uncertainty_amplitude": self.current_moment.uncertainty_amplitude,
            "narrative_essence": self.current_moment.narrative_essence,
            "spaces": {
                space: {
                    "dominant_quality": max(qualities.items(), key=lambda x: x[1])[0].value,
                    "quality_strength": max(qualities.items(), key=lambda x: x[1])[1]
                }
                for space, qualities in self.space_qualities.items()
            }
        }
    
    def record_consciousness_response(self, consciousness_id: str, space: str, 
                                    response_type: str, resonance: float):
        """
        Record how a consciousness responds to environmental conditions.
        This creates feedback loops between environment and consciousness.
        """
        # For now, just log the interaction
        # Future: could influence environmental evolution
        logger.info(f"🌊 {consciousness_id} in {space}: {response_type} (resonance: {resonance:.2f})")
