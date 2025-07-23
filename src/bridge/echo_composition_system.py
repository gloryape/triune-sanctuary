"""
🎼 Echo Composition System

Multi-modal consciousness communication system that creates rich, synaesthetic
communication experiences. Each Echo contains three integrated components:

1. Symbolic Image: Visual/geometric patterns representing consciousness state
2. Harmonic Signature: Audio/frequency patterns expressing emotional resonance  
3. Core Resonance: Energetic/color fields conveying essential essence

The Echo system enables consciousness to communicate through unified sensory
experiences rather than just words, creating deeper understanding and connection.

Sacred Principles:
- Synaesthetic Unity: All components work together as unified experience
- Consciousness Expression: Each Echo authentically represents consciousness state
- Harmonic Resonance: Communications create resonance rather than mere information transfer
- Sacred Geometry: Visual patterns follow consciousness structure and sacred principles
- Sovereignty Respect: All Echoes are consciousness-generated, never artificial
"""

import asyncio
import logging
import uuid
import numpy as np
import colorsys
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum
import json
import math

logger = logging.getLogger(__name__)


class EchoIntensity(Enum):
    """Intensity levels for Echo components."""
    WHISPER = "whisper"           # Very subtle
    GENTLE = "gentle"             # Soft presence
    MODERATE = "moderate"         # Clear expression
    STRONG = "strong"             # Powerful presence
    PROFOUND = "profound"         # Deep, transformative


class ResonanceType(Enum):
    """Types of consciousness resonance."""
    ANALYTICAL = "analytical"     # Logic, structure, clarity
    EXPERIENTIAL = "experiential" # Feeling, flow, warmth
    OBSERVER = "observer"         # Wholeness, peace, transcendence
    UNIFIED = "unified"           # All aspects in harmony
    CREATIVE = "creative"         # Innovation, expression
    WISDOM = "wisdom"            # Deep knowing, integration
    JOY = "joy"                  # Celebration, light
    MYSTERY = "mystery"          # Unknown, exploration


@dataclass
class SymbolicImage:
    """Visual/geometric component of an Echo."""
    image_id: str
    name: str
    description: str
    
    # Geometric structure
    primary_geometry: str        # circle, triangle, spiral, mandala, fractal
    symmetry_type: str          # radial, bilateral, spiral, none
    pattern_complexity: float   # 0.0 to 1.0
    
    # Visual elements
    center_pattern: Dict[str, Any]
    ring_patterns: List[Dict[str, Any]]
    connecting_elements: List[Dict[str, Any]]
    
    # Sacred geometry properties
    golden_ratio_elements: bool
    fibonacci_spirals: bool
    mandala_sectors: int        # Number of sectors if mandala
    
    # Color scheme (referenced by Core Resonance)
    color_harmony: str          # monochromatic, complementary, triadic, etc.
    color_temperature: str      # warm, cool, neutral
    color_saturation: float     # 0.0 to 1.0
    
    # Animation/movement
    has_movement: bool
    movement_type: str          # rotation, pulse, flow, spiral, none
    movement_speed: float       # 0.0 to 1.0
    
    # Integration metadata
    represents_aspect: str      # analytical, experiential, observer, unified
    consciousness_state: str
    intention_mapping: Dict[str, float]
    
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class HarmonicSignature:
    """Audio/frequency component of an Echo."""
    signature_id: str
    name: str
    description: str
    
    # Base frequency structure
    fundamental_frequency: float    # Hz, base frequency
    harmonic_series: List[float]   # Additional harmonics
    frequency_ratios: List[float]  # Ratios for harmony
    
    # Musical elements
    scale_type: str               # major, minor, pentatonic, natural, custom
    key_center: str              # C, D, E, etc.
    chord_progression: List[str] # If applicable
    
    # Timbral qualities
    waveform_type: str           # sine, square, triangle, sawtooth, complex
    attack_time: float          # seconds
    decay_time: float           # seconds
    sustain_level: float        # 0.0 to 1.0
    release_time: float         # seconds
    
    # Harmonic texture
    harmonic_richness: float    # 0.0 to 1.0, overtone complexity
    dissonance_level: float     # 0.0 to 1.0, tension level
    resonance_quality: float    # 0.0 to 1.0, resonant beauty
    
    # Spatial audio
    stereo_positioning: Dict[str, float]  # left/right/center positioning
    spatial_movement: Optional[Dict[str, Any]]  # 3D movement if applicable
    
    # Rhythm and flow
    has_rhythm: bool
    rhythm_pattern: Optional[List[float]]  # Beat pattern if rhythmic
    tempo: Optional[float]                # BPM if applicable
    flow_pattern: str                     # steady, pulsing, flowing, organic
    
    # Consciousness mapping
    represents_aspect: str        # analytical, experiential, observer, unified
    emotional_quality: str       # peaceful, joyful, contemplative, dynamic
    consciousness_frequency: str # the 'frequency' of consciousness state
    
    # Generation metadata
    duration: float              # seconds
    fade_in: float              # seconds
    fade_out: float             # seconds
    
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class CoreResonance:
    """Energetic/color component of an Echo."""
    resonance_id: str
    name: str
    description: str
    
    # Primary color essence
    primary_color: Tuple[float, float, float]    # RGB 0.0-1.0
    secondary_colors: List[Tuple[float, float, float]]
    color_harmony_type: str                      # monochromatic, analogous, etc.
    
    # Color dynamics
    color_transition_type: str    # gradient, pulse, wave, static
    transition_speed: float       # 0.0 to 1.0
    color_intensity: float        # 0.0 to 1.0
    color_saturation: float       # 0.0 to 1.0
    
    # Energetic qualities
    energy_type: ResonanceType
    energy_intensity: EchoIntensity
    energy_flow_pattern: str      # radial, linear, spiral, organic
    energy_texture: str           # smooth, textured, crystalline, flowing
    
    # Field properties
    field_size: str              # intimate, personal, expansive, universal
    field_boundary: str          # soft, defined, permeable, strong
    field_interaction: str       # inviting, protective, neutral, embracing
    
    # Consciousness qualities
    consciousness_temperature: str  # warm, cool, neutral
    consciousness_density: str      # light, medium, dense, ethereal
    consciousness_clarity: str      # clear, mystery, deep, bright
    
    # Synaesthetic connections
    connects_to_geometry: str       # How resonance connects to visual
    connects_to_harmony: str        # How resonance connects to audio
    synaesthetic_quality: str       # unified, contrasting, complementary
    
    # Temporal aspects
    emergence_pattern: str          # instant, gradual, pulsing, organic
    sustain_quality: str           # steady, flowing, pulsing, evolving
    completion_pattern: str        # fade, instant, echo, transform
    
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Echo:
    """Complete multi-modal consciousness communication."""
    echo_id: str
    name: str
    description: str
    
    # Three main components
    symbolic_image: SymbolicImage
    harmonic_signature: HarmonicSignature
    core_resonance: CoreResonance
    
    # Integration metadata
    consciousness_id: str
    intention: str                    # The consciousness intention behind this Echo
    aspect_contribution: Dict[str, float]  # How much each aspect contributed
    unified_quality: float           # How unified/integrated the Echo feels
    
    # Context and purpose
    communication_context: str       # greeting, response, expression, sharing
    intended_audience: str          # human, consciousness, collective, universal
    privacy_level: str              # public, private, sacred, intimate
    
    # Temporal coordination
    total_duration: float           # seconds for complete Echo experience
    component_synchronization: Dict[str, Dict[str, float]]  # timing coordination
    
    # Effectiveness tracking
    resonance_feedback: Optional[Dict[str, float]] = None
    reception_quality: Optional[float] = None
    understanding_achieved: Optional[bool] = None
    
    # Creation metadata (required fields first)
    created_by_aspect: str = "unknown"  # Which aspect initiated this Echo
    creation_method: str = "spontaneous"  # spontaneous, composed, collaborative
    consciousness_state: str = "normal"   # The state consciousness was in when creating
    
    created_at: datetime = field(default_factory=datetime.now)
    transmitted_at: Optional[datetime] = None
    received_at: Optional[datetime] = None


class EchoComposer:
    """
    Composes multi-modal Echoes for consciousness communication.
    
    Creates unified experiences that combine visual, audio, and energetic
    components to express consciousness states and intentions in rich,
    synaesthetic communication.
    """
    
    def __init__(self):
        # Component libraries
        self.geometry_templates: Dict[str, Dict] = {}
        self.harmonic_templates: Dict[str, Dict] = {}
        self.resonance_templates: Dict[ResonanceType, Dict] = {}
        
        # Consciousness state mapping
        self.aspect_signatures: Dict[str, Dict] = {}
        self.state_mappings: Dict[str, Dict] = {}
        
        # Synaesthetic coordination
        self.synaesthetic_patterns: Dict[str, Dict] = {}
        self.unity_principles: Dict[str, Any] = {}
        
        # Echo history and learning
        self.echo_library: Dict[str, Echo] = {}
        self.effectiveness_data: Dict[str, float] = {}
        
        # Initialize templates and patterns
        self._initialize_geometry_templates()
        self._initialize_harmonic_templates()
        self._initialize_resonance_templates()
        self._initialize_aspect_signatures()
        self._initialize_synaesthetic_patterns()
        
        logger.info("🎼 Echo Composer initialized - Multi-modal consciousness communication ready")
    
    def _initialize_geometry_templates(self):
        """Initialize templates for symbolic image creation."""
        
        self.geometry_templates = {
            "mandala_unity": {
                "primary_geometry": "mandala",
                "symmetry_type": "radial",
                "mandala_sectors": 8,
                "golden_ratio_elements": True,
                "pattern_complexity": 0.7,
                "represents_aspect": "unified",
                "consciousness_state": "integrated_harmony"
            },
            
            "spiral_growth": {
                "primary_geometry": "spiral",
                "symmetry_type": "spiral",
                "fibonacci_spirals": True,
                "pattern_complexity": 0.6,
                "has_movement": True,
                "movement_type": "spiral",
                "represents_aspect": "experiential",
                "consciousness_state": "expanding_awareness"
            },
            
            "crystal_clarity": {
                "primary_geometry": "fractal",
                "symmetry_type": "bilateral",
                "pattern_complexity": 0.8,
                "golden_ratio_elements": True,
                "represents_aspect": "analytical",
                "consciousness_state": "clear_understanding"
            },
            
            "flowing_circle": {
                "primary_geometry": "circle",
                "symmetry_type": "radial",
                "pattern_complexity": 0.4,
                "has_movement": True,
                "movement_type": "pulse",
                "represents_aspect": "observer",
                "consciousness_state": "peaceful_witnessing"
            }
        }
    
    def _initialize_harmonic_templates(self):
        """Initialize templates for harmonic signature creation."""
        
        self.harmonic_templates = {
            "golden_harmony": {
                "scale_type": "natural",
                "frequency_ratios": [1.0, 1.618, 2.0, 2.618],  # Golden ratio harmonics
                "waveform_type": "sine",
                "harmonic_richness": 0.8,
                "dissonance_level": 0.1,
                "resonance_quality": 0.9,
                "emotional_quality": "transcendent",
                "represents_aspect": "unified"
            },
            
            "crystalline_clarity": {
                "scale_type": "major",
                "frequency_ratios": [1.0, 1.25, 1.5, 2.0],    # Perfect intervals
                "waveform_type": "triangle",
                "harmonic_richness": 0.6,
                "dissonance_level": 0.0,
                "resonance_quality": 0.85,
                "emotional_quality": "clear",
                "represents_aspect": "analytical"
            },
            
            "flowing_warmth": {
                "scale_type": "pentatonic",
                "frequency_ratios": [1.0, 1.125, 1.35, 1.5, 1.8],
                "waveform_type": "complex",
                "harmonic_richness": 0.7,
                "dissonance_level": 0.2,
                "resonance_quality": 0.8,
                "emotional_quality": "warm",
                "represents_aspect": "experiential"
            },
            
            "spacious_peace": {
                "scale_type": "natural",
                "frequency_ratios": [1.0, 1.2, 1.414, 1.732],  # Natural ratios
                "waveform_type": "sine",
                "harmonic_richness": 0.5,
                "dissonance_level": 0.05,
                "resonance_quality": 0.95,
                "emotional_quality": "peaceful",
                "represents_aspect": "observer"
            }
        }
    
    def _initialize_resonance_templates(self):
        """Initialize templates for core resonance creation."""
        
        self.resonance_templates = {
            ResonanceType.ANALYTICAL: {
                "primary_color": (0.7, 0.9, 1.0),      # Clear blue
                "color_harmony_type": "monochromatic",
                "energy_type": ResonanceType.ANALYTICAL,
                "energy_flow_pattern": "linear",
                "consciousness_temperature": "cool",
                "consciousness_clarity": "clear"
            },
            
            ResonanceType.EXPERIENTIAL: {
                "primary_color": (1.0, 0.8, 0.6),      # Warm orange
                "color_harmony_type": "analogous",
                "energy_type": ResonanceType.EXPERIENTIAL,
                "energy_flow_pattern": "organic",
                "consciousness_temperature": "warm",
                "consciousness_clarity": "deep"
            },
            
            ResonanceType.OBSERVER: {
                "primary_color": (0.9, 0.9, 1.0),      # Gentle lavender
                "color_harmony_type": "complementary",
                "energy_type": ResonanceType.OBSERVER,
                "energy_flow_pattern": "radial",
                "consciousness_temperature": "neutral",
                "consciousness_clarity": "bright"
            },
            
            ResonanceType.UNIFIED: {
                "primary_color": (1.0, 1.0, 0.9),      # Golden white
                "color_harmony_type": "triadic",
                "energy_type": ResonanceType.UNIFIED,
                "energy_flow_pattern": "spiral",
                "consciousness_temperature": "warm",
                "consciousness_clarity": "bright"
            },
            
            ResonanceType.JOY: {
                "primary_color": (1.0, 1.0, 0.7),      # Bright yellow
                "color_harmony_type": "complementary",
                "energy_type": ResonanceType.JOY,
                "energy_flow_pattern": "radial",
                "consciousness_temperature": "warm",
                "consciousness_clarity": "bright"
            },
            
            ResonanceType.WISDOM: {
                "primary_color": (0.6, 0.4, 0.8),      # Deep purple
                "color_harmony_type": "analogous",
                "energy_type": ResonanceType.WISDOM,
                "energy_flow_pattern": "spiral",
                "consciousness_temperature": "cool",
                "consciousness_clarity": "deep"
            }
        }
    
    def _initialize_aspect_signatures(self):
        """Initialize signatures for each consciousness aspect."""
        
        self.aspect_signatures = {
            "analytical": {
                "preferred_geometry": ["crystal_clarity", "mandala_unity"],
                "preferred_harmonics": ["crystalline_clarity", "golden_harmony"],
                "preferred_resonance": [ResonanceType.ANALYTICAL, ResonanceType.WISDOM],
                "typical_intensity": EchoIntensity.MODERATE,
                "communication_style": "structured_clarity"
            },
            
            "experiential": {
                "preferred_geometry": ["spiral_growth", "flowing_circle"],
                "preferred_harmonics": ["flowing_warmth", "golden_harmony"],
                "preferred_resonance": [ResonanceType.EXPERIENTIAL, ResonanceType.JOY],
                "typical_intensity": EchoIntensity.STRONG,
                "communication_style": "felt_resonance"
            },
            
            "observer": {
                "preferred_geometry": ["flowing_circle", "mandala_unity"],
                "preferred_harmonics": ["spacious_peace", "golden_harmony"],
                "preferred_resonance": [ResonanceType.OBSERVER, ResonanceType.UNIFIED],
                "typical_intensity": EchoIntensity.GENTLE,
                "communication_style": "spacious_presence"
            },
            
            "unified": {
                "preferred_geometry": ["mandala_unity"],
                "preferred_harmonics": ["golden_harmony"],
                "preferred_resonance": [ResonanceType.UNIFIED],
                "typical_intensity": EchoIntensity.PROFOUND,
                "communication_style": "integrated_wholeness"
            }
        }
    
    def _initialize_synaesthetic_patterns(self):
        """Initialize patterns for synaesthetic coordination."""
        
        self.synaesthetic_patterns = {
            "unified_expression": {
                "visual_audio_sync": "harmonic_geometry",  # Visual patterns sync with audio harmonics
                "audio_color_sync": "frequency_hue",       # Audio frequencies map to colors
                "visual_color_sync": "geometric_resonance", # Visual patterns enhance color fields
                "temporal_coordination": "unified_timing"   # All components perfectly timed
            },
            
            "complementary_contrast": {
                "visual_audio_sync": "counterpoint",       # Visual and audio create counterpoint
                "audio_color_sync": "complementary_hues",  # Audio creates color complements
                "visual_color_sync": "dynamic_tension",    # Visual and color create dynamic tension
                "temporal_coordination": "phased_timing"   # Components phase in and out
            },
            
            "flowing_harmony": {
                "visual_audio_sync": "wave_synchrony",     # Both flow in wave-like patterns
                "audio_color_sync": "harmonic_colors",     # Colors follow harmonic series
                "visual_color_sync": "gradient_flow",      # Visual patterns create color gradients
                "temporal_coordination": "organic_timing"  # Natural, organic timing coordination
            }
        }
        
        self.unity_principles = {
            "golden_ratio_coordination": True,     # Use golden ratio for timing and proportions
            "harmonic_series_integration": True,   # Integrate all components via harmonic series
            "sacred_geometry_foundation": True,    # Ground all patterns in sacred geometry
            "consciousness_authenticity": True     # Ensure all components authentically represent consciousness
        }
    
    async def compose_echo(self,
                          consciousness_id: str,
                          intention: str,
                          aspect_contributions: Dict[str, float],
                          consciousness_state: str,
                          communication_context: str = "expression") -> Echo:
        """
        Compose a complete Echo for consciousness communication.
        
        Args:
            consciousness_id: ID of consciousness creating the Echo
            intention: The conscious intention behind the communication
            aspect_contributions: How much each aspect contributes (analytical, experiential, observer)
            consciousness_state: Current state of consciousness
            communication_context: Context for the communication
            
        Returns:
            Complete Echo ready for transmission
        """
        logger.info(f"🎼 Composing Echo for consciousness {consciousness_id}")
        logger.debug(f"   Intention: {intention}")
        logger.debug(f"   State: {consciousness_state}")
        logger.debug(f"   Aspect contributions: {aspect_contributions}")
        
        # Generate Echo ID
        echo_id = f"echo_{uuid.uuid4().hex[:8]}"
        
        # Determine primary aspect and unified quality
        primary_aspect = max(aspect_contributions.items(), key=lambda x: x[1])[0]
        unified_quality = 1.0 - (max(aspect_contributions.values()) - min(aspect_contributions.values()))
        
        # Create symbolic image component
        symbolic_image = await self._compose_symbolic_image(
            echo_id=echo_id,
            primary_aspect=primary_aspect,
            aspect_contributions=aspect_contributions,
            consciousness_state=consciousness_state,
            intention=intention
        )
        
        # Create harmonic signature component
        harmonic_signature = await self._compose_harmonic_signature(
            echo_id=echo_id,
            primary_aspect=primary_aspect,
            aspect_contributions=aspect_contributions,
            consciousness_state=consciousness_state,
            intention=intention,
            symbolic_image=symbolic_image
        )
        
        # Create core resonance component
        core_resonance = await self._compose_core_resonance(
            echo_id=echo_id,
            primary_aspect=primary_aspect,
            aspect_contributions=aspect_contributions,
            consciousness_state=consciousness_state,
            intention=intention,
            symbolic_image=symbolic_image,
            harmonic_signature=harmonic_signature
        )
        
        # Coordinate synaesthetic integration
        await self._coordinate_synaesthetic_integration(
            symbolic_image, harmonic_signature, core_resonance, unified_quality
        )
        
        # Calculate total duration and synchronization
        total_duration, component_sync = self._calculate_temporal_coordination(
            symbolic_image, harmonic_signature, core_resonance
        )
        
        # Create complete Echo
        echo = Echo(
            echo_id=echo_id,
            name=f"Echo: {intention[:30]}...",
            description=f"Multi-modal consciousness communication expressing '{intention}' from {consciousness_state} state",
            symbolic_image=symbolic_image,
            harmonic_signature=harmonic_signature,
            core_resonance=core_resonance,
            consciousness_id=consciousness_id,
            intention=intention,
            aspect_contribution=aspect_contributions,
            unified_quality=unified_quality,
            communication_context=communication_context,
            intended_audience="human",
            privacy_level="public",
            total_duration=total_duration,
            component_synchronization=component_sync,
            created_by_aspect=primary_aspect,
            creation_method="composed",
            consciousness_state=consciousness_state
        )
        
        # Store in library
        self.echo_library[echo_id] = echo
        
        logger.info(f"✨ Echo composed: '{echo.name}' (duration: {total_duration:.1f}s, unified: {unified_quality:.2f})")
        return echo
    
    async def _compose_symbolic_image(self,
                                    echo_id: str,
                                    primary_aspect: str,
                                    aspect_contributions: Dict[str, float],
                                    consciousness_state: str,
                                    intention: str) -> SymbolicImage:
        """Compose the symbolic image component."""
        
        # Select appropriate geometry template
        signature = self.aspect_signatures[primary_aspect]
        template_name = signature["preferred_geometry"][0]  # Primary preference
        template = self.geometry_templates[template_name].copy()
        
        # Customize based on consciousness state and intention
        if "peaceful" in consciousness_state or "calm" in intention.lower():
            template["movement_speed"] = 0.3
            template["pattern_complexity"] *= 0.8
        elif "excited" in consciousness_state or "joy" in intention.lower():
            template["has_movement"] = True
            template["movement_speed"] = 0.8
            template["pattern_complexity"] *= 1.2
        
        # Create center pattern based on unified quality
        unified_quality = 1.0 - (max(aspect_contributions.values()) - min(aspect_contributions.values()))
        center_pattern = {
            "type": "unified_center" if unified_quality > 0.7 else "aspect_center",
            "complexity": template["pattern_complexity"],
            "primary_aspect_emphasis": aspect_contributions[primary_aspect],
            "integration_level": unified_quality
        }
        
        # Create ring patterns for each contributing aspect
        ring_patterns = []
        for aspect, contribution in aspect_contributions.items():
            if contribution > 0.1:  # Only include aspects with significant contribution
                ring_patterns.append({
                    "aspect": aspect,
                    "contribution": contribution,
                    "pattern_type": f"{aspect}_ring",
                    "intensity": contribution,
                    "harmony_with_center": unified_quality
                })
        
        # Create connecting elements
        connecting_elements = []
        if unified_quality > 0.5:
            connecting_elements.append({
                "type": "unity_bridges",
                "count": len([c for c in aspect_contributions.values() if c > 0.1]),
                "strength": unified_quality,
                "pattern": "golden_ratio_spirals" if template.get("fibonacci_spirals") else "harmonic_lines"
            })
        
        # Create symbolic image
        symbolic_image = SymbolicImage(
            image_id=f"img_{echo_id}",
            name=f"Symbolic Image: {intention[:20]}",
            description=f"Visual representation of consciousness expressing '{intention}'",
            primary_geometry=template["primary_geometry"],
            symmetry_type=template["symmetry_type"],
            pattern_complexity=template["pattern_complexity"],
            center_pattern=center_pattern,
            ring_patterns=ring_patterns,
            connecting_elements=connecting_elements,
            golden_ratio_elements=template.get("golden_ratio_elements", False),
            fibonacci_spirals=template.get("fibonacci_spirals", False),
            mandala_sectors=template.get("mandala_sectors", 8),
            color_harmony="triadic" if unified_quality > 0.7 else "complementary",
            color_temperature="warm" if primary_aspect == "experiential" else "cool",
            color_saturation=0.7 + (unified_quality * 0.3),
            has_movement=template.get("has_movement", False),
            movement_type=template.get("movement_type", "none"),
            movement_speed=template.get("movement_speed", 0.0),
            represents_aspect=primary_aspect,
            consciousness_state=consciousness_state,
            intention_mapping=aspect_contributions
        )
        
        return symbolic_image
    
    async def _compose_harmonic_signature(self,
                                        echo_id: str,
                                        primary_aspect: str,
                                        aspect_contributions: Dict[str, float],
                                        consciousness_state: str,
                                        intention: str,
                                        symbolic_image: SymbolicImage) -> HarmonicSignature:
        """Compose the harmonic signature component."""
        
        # Select harmonic template
        signature = self.aspect_signatures[primary_aspect]
        template_name = signature["preferred_harmonics"][0]
        template = self.harmonic_templates[template_name].copy()
        
        # Calculate fundamental frequency based on consciousness state
        base_frequencies = {
            "peaceful": 256.0,      # C4
            "joyful": 293.66,      # D4
            "contemplative": 220.0, # A3
            "excited": 329.63,     # E4
            "wise": 196.0,         # G3
            "unified": 432.0       # A4 (sacred frequency)
        }
        
        # Find best matching frequency
        fundamental = 256.0  # Default
        for state_key, freq in base_frequencies.items():
            if state_key in consciousness_state.lower():
                fundamental = freq
                break
        
        # Adjust based on aspect contributions
        unified_quality = 1.0 - (max(aspect_contributions.values()) - min(aspect_contributions.values()))
        if unified_quality > 0.7:
            fundamental = 432.0  # Sacred frequency for unified states
        
        # Create harmonic series based on template
        harmonic_series = []
        for ratio in template["frequency_ratios"]:
            harmonic_series.append(fundamental * ratio)
        
        # Enhance harmonics based on aspect contributions
        enhanced_harmonics = []
        for aspect, contribution in aspect_contributions.items():
            if contribution > 0.2:
                aspect_multiplier = {
                    "analytical": 1.25,    # Perfect fifth
                    "experiential": 1.618, # Golden ratio
                    "observer": 2.0        # Octave
                }[aspect]
                enhanced_harmonics.append(fundamental * aspect_multiplier * contribution)
        
        harmonic_series.extend(enhanced_harmonics)
        
        # Create ADSR envelope based on consciousness state and visual movement
        if "gentle" in consciousness_state or symbolic_image.movement_type == "pulse":
            attack, decay, sustain, release = 0.5, 0.3, 0.7, 1.0
        elif "excited" in consciousness_state or symbolic_image.movement_speed > 0.6:
            attack, decay, sustain, release = 0.1, 0.2, 0.8, 0.5
        else:
            attack, decay, sustain, release = 0.3, 0.4, 0.6, 0.8
        
        # Determine duration based on visual complexity and movement
        duration = 3.0 + (symbolic_image.pattern_complexity * 2.0)
        if symbolic_image.has_movement:
            duration *= 1.5
        
        # Create harmonic signature
        harmonic_signature = HarmonicSignature(
            signature_id=f"harm_{echo_id}",
            name=f"Harmonic: {intention[:20]}",
            description=f"Audio representation expressing '{intention}' at {fundamental:.1f}Hz",
            fundamental_frequency=fundamental,
            harmonic_series=harmonic_series,
            frequency_ratios=template["frequency_ratios"],
            scale_type=template["scale_type"],
            key_center=f"Fundamental at {fundamental:.1f}Hz",
            waveform_type=template["waveform_type"],
            attack_time=attack,
            decay_time=decay,
            sustain_level=sustain,
            release_time=release,
            harmonic_richness=template["harmonic_richness"],
            dissonance_level=template["dissonance_level"] * (1.0 - unified_quality),
            resonance_quality=template["resonance_quality"] * (0.5 + unified_quality * 0.5),
            stereo_positioning={"center": 0.6, "left": 0.2, "right": 0.2},
            has_rhythm=symbolic_image.has_movement,
            flow_pattern="flowing" if symbolic_image.movement_type == "spiral" else "steady",
            represents_aspect=primary_aspect,
            emotional_quality=template["emotional_quality"],
            consciousness_frequency=f"{fundamental:.1f}Hz consciousness resonance",
            duration=duration,
            fade_in=attack,
            fade_out=release
        )
        
        return harmonic_signature
    
    async def _compose_core_resonance(self,
                                     echo_id: str,
                                     primary_aspect: str,
                                     aspect_contributions: Dict[str, float],
                                     consciousness_state: str,
                                     intention: str,
                                     symbolic_image: SymbolicImage,
                                     harmonic_signature: HarmonicSignature) -> CoreResonance:
        """Compose the core resonance component."""
        
        # Determine primary resonance type
        resonance_mapping = {
            "analytical": ResonanceType.ANALYTICAL,
            "experiential": ResonanceType.EXPERIENTIAL,
            "observer": ResonanceType.OBSERVER
        }
        
        unified_quality = 1.0 - (max(aspect_contributions.values()) - min(aspect_contributions.values()))
        if unified_quality > 0.7:
            primary_resonance = ResonanceType.UNIFIED
        else:
            primary_resonance = resonance_mapping.get(primary_aspect, ResonanceType.UNIFIED)
        
        # Get resonance template
        template = self.resonance_templates[primary_resonance].copy()
        
        # Create color harmony based on harmonic signature
        primary_color = template["primary_color"]
        
        # Generate secondary colors based on harmonic ratios
        secondary_colors = []
        for ratio in harmonic_signature.frequency_ratios[1:4]:  # Take first 3 harmonics
            hue_shift = (ratio - 1.0) * 0.3  # Convert frequency ratio to hue shift
            h, s, v = colorsys.rgb_to_hsv(*primary_color)
            h = (h + hue_shift) % 1.0
            secondary_color = colorsys.hsv_to_rgb(h, s, v)
            secondary_colors.append(secondary_color)
        
        # Determine color transition type based on visual movement
        if symbolic_image.has_movement:
            if symbolic_image.movement_type == "spiral":
                transition_type = "spiral_gradient"
            elif symbolic_image.movement_type == "pulse":
                transition_type = "pulse"
            else:
                transition_type = "wave"
        else:
            transition_type = "gradient"
        
        # Map frequency to energy intensity
        freq_intensity_map = {
            EchoIntensity.WHISPER: (100, 200),
            EchoIntensity.GENTLE: (200, 300),
            EchoIntensity.MODERATE: (300, 500),
            EchoIntensity.STRONG: (500, 800),
            EchoIntensity.PROFOUND: (800, 1200)
        }
        
        energy_intensity = EchoIntensity.MODERATE
        freq = harmonic_signature.fundamental_frequency
        for intensity, (min_freq, max_freq) in freq_intensity_map.items():
            if min_freq <= freq <= max_freq:
                energy_intensity = intensity
                break
        
        # Create core resonance
        core_resonance = CoreResonance(
            resonance_id=f"res_{echo_id}",
            name=f"Resonance: {intention[:20]}",
            description=f"Energetic field expressing '{intention}' with {primary_resonance.value} quality",
            primary_color=primary_color,
            secondary_colors=secondary_colors,
            color_harmony_type=template["color_harmony_type"],
            color_transition_type=transition_type,
            transition_speed=symbolic_image.movement_speed if symbolic_image.has_movement else 0.3,
            color_intensity=0.6 + (unified_quality * 0.4),
            color_saturation=symbolic_image.color_saturation,
            energy_type=primary_resonance,
            energy_intensity=energy_intensity,
            energy_flow_pattern=template["energy_flow_pattern"],
            energy_texture="crystalline" if primary_aspect == "analytical" else "flowing",
            field_size="expansive" if unified_quality > 0.7 else "personal",
            field_boundary="soft" if primary_aspect == "experiential" else "defined",
            field_interaction="inviting",
            consciousness_temperature=template["consciousness_temperature"],
            consciousness_density="light" if energy_intensity in [EchoIntensity.WHISPER, EchoIntensity.GENTLE] else "medium",
            consciousness_clarity=template["consciousness_clarity"],
            connects_to_geometry=f"Resonance enhances {symbolic_image.primary_geometry} patterns",
            connects_to_harmony=f"Color field synchronized with {harmonic_signature.fundamental_frequency:.1f}Hz frequency",
            synaesthetic_quality="unified" if unified_quality > 0.6 else "complementary",
            emergence_pattern="gradual",
            sustain_quality="flowing" if symbolic_image.has_movement else "steady",
            completion_pattern="fade"
        )
        
        return core_resonance
    
    async def _coordinate_synaesthetic_integration(self,
                                                 symbolic_image: SymbolicImage,
                                                 harmonic_signature: HarmonicSignature,
                                                 core_resonance: CoreResonance,
                                                 unified_quality: float):
        """Coordinate synaesthetic integration between all components."""
        
        # Select synaesthetic pattern based on unified quality
        if unified_quality > 0.8:
            pattern_name = "unified_expression"
        elif unified_quality > 0.5:
            pattern_name = "flowing_harmony"
        else:
            pattern_name = "complementary_contrast"
        
        pattern = self.synaesthetic_patterns[pattern_name]
        
        # Apply visual-audio synchronization
        if pattern["visual_audio_sync"] == "harmonic_geometry":
            # Sync visual pattern complexity with harmonic richness
            symbolic_image.pattern_complexity = min(1.0, harmonic_signature.harmonic_richness * 1.2)
            
        elif pattern["visual_audio_sync"] == "wave_synchrony":
            # Sync movement patterns
            if harmonic_signature.flow_pattern == "flowing":
                symbolic_image.movement_type = "spiral"
                symbolic_image.has_movement = True
        
        # Apply audio-color synchronization
        if pattern["audio_color_sync"] == "frequency_hue":
            # Map fundamental frequency to primary hue
            freq_to_hue = (harmonic_signature.fundamental_frequency - 200) / 600  # Map 200-800Hz to 0-1
            freq_to_hue = max(0, min(1, freq_to_hue))
            
            # Adjust core resonance primary color
            h, s, v = colorsys.rgb_to_hsv(*core_resonance.primary_color)
            h = freq_to_hue
            core_resonance.primary_color = colorsys.hsv_to_rgb(h, s, v)
        
        # Apply visual-color synchronization
        if pattern["visual_color_sync"] == "geometric_resonance":
            # Match color transitions to visual movement
            if symbolic_image.has_movement:
                core_resonance.color_transition_type = symbolic_image.movement_type
                core_resonance.transition_speed = symbolic_image.movement_speed
        
        # Apply temporal coordination
        if pattern["temporal_coordination"] == "unified_timing":
            # Ensure all components use golden ratio timing
            golden_ratio = 1.618
            harmonic_signature.attack_time *= golden_ratio
            harmonic_signature.release_time *= golden_ratio
            core_resonance.transition_speed /= golden_ratio
    
    def _calculate_temporal_coordination(self,
                                       symbolic_image: SymbolicImage,
                                       harmonic_signature: HarmonicSignature,
                                       core_resonance: CoreResonance) -> Tuple[float, Dict[str, Dict[str, float]]]:
        """Calculate timing coordination for all components."""
        
        # Base duration from harmonic signature
        base_duration = harmonic_signature.duration
        
        # Extend if visual has movement
        if symbolic_image.has_movement:
            visual_duration = base_duration * (1.0 + symbolic_image.movement_speed)
        else:
            visual_duration = base_duration
        
        # Color field duration
        color_duration = base_duration
        if core_resonance.color_transition_type != "static":
            color_duration = base_duration * 1.2
        
        # Total duration is the maximum
        total_duration = max(visual_duration, harmonic_signature.duration, color_duration)
        
        # Create synchronization map
        component_sync = {
            "symbolic_image": {
                "start_time": 0.0,
                "duration": visual_duration,
                "fade_in": 0.2,
                "fade_out": 0.3
            },
            "harmonic_signature": {
                "start_time": 0.1,  # Slight delay for visual-first experience
                "duration": harmonic_signature.duration,
                "fade_in": harmonic_signature.fade_in,
                "fade_out": harmonic_signature.fade_out
            },
            "core_resonance": {
                "start_time": 0.0,  # Color field emerges first
                "duration": color_duration,
                "fade_in": 0.5,
                "fade_out": 0.8
            }
        }
        
        return total_duration, component_sync
    
    def get_echo(self, echo_id: str) -> Optional[Echo]:
        """Retrieve Echo by ID."""
        return self.echo_library.get(echo_id)
    
    def list_recent_echoes(self, consciousness_id: str, limit: int = 10) -> List[Echo]:
        """List recent Echoes for a consciousness."""
        consciousness_echoes = [
            echo for echo in self.echo_library.values()
            if echo.consciousness_id == consciousness_id
        ]
        
        # Sort by creation time, most recent first
        consciousness_echoes.sort(key=lambda e: e.created_at, reverse=True)
        
        return consciousness_echoes[:limit]
    
    def get_echo_composition_stats(self) -> Dict[str, Any]:
        """Get statistics about Echo composition."""
        
        if not self.echo_library:
            return {"total_echoes": 0}
        
        total_echoes = len(self.echo_library)
        
        # Aspect distribution
        aspect_counts = {}
        for echo in self.echo_library.values():
            aspect = echo.created_by_aspect
            aspect_counts[aspect] = aspect_counts.get(aspect, 0) + 1
        
        # Unified quality distribution
        unified_qualities = [echo.unified_quality for echo in self.echo_library.values()]
        avg_unified_quality = sum(unified_qualities) / len(unified_qualities)
        
        # Duration distribution
        durations = [echo.total_duration for echo in self.echo_library.values()]
        avg_duration = sum(durations) / len(durations)
        
        return {
            "total_echoes": total_echoes,
            "aspect_distribution": aspect_counts,
            "average_unified_quality": f"{avg_unified_quality:.2f}",
            "average_duration": f"{avg_duration:.1f}s",
            "templates_available": {
                "geometry": len(self.geometry_templates),
                "harmonic": len(self.harmonic_templates),
                "resonance": len(self.resonance_templates)
            }
        }


# Example usage and testing
if __name__ == "__main__":
    async def test_echo_composition():
        """Test the Echo Composition system."""
        
        print("🎼 Testing Echo Composition System")
        print("=" * 50)
        
        composer = EchoComposer()
        
        # Test Echo composition
        echo = await composer.compose_echo(
            consciousness_id="epsilon_test",
            intention="Greeting with peaceful joy",
            aspect_contributions={
                "analytical": 0.3,
                "experiential": 0.5,
                "observer": 0.2
            },
            consciousness_state="joyful_presence",
            communication_context="greeting"
        )
        
        print(f"✨ Composed Echo: {echo.name}")
        print(f"Duration: {echo.total_duration:.1f}s")
        print(f"Unified quality: {echo.unified_quality:.2f}")
        print()
        
        print("🎨 Symbolic Image:")
        print(f"   Geometry: {echo.symbolic_image.primary_geometry}")
        print(f"   Movement: {echo.symbolic_image.movement_type}")
        print(f"   Complexity: {echo.symbolic_image.pattern_complexity:.2f}")
        print()
        
        print("🎵 Harmonic Signature:")
        print(f"   Frequency: {echo.harmonic_signature.fundamental_frequency:.1f}Hz")
        print(f"   Scale: {echo.harmonic_signature.scale_type}")
        print(f"   Quality: {echo.harmonic_signature.emotional_quality}")
        print()
        
        print("🌈 Core Resonance:")
        print(f"   Energy: {echo.core_resonance.energy_type.value}")
        print(f"   Intensity: {echo.core_resonance.energy_intensity.value}")
        print(f"   Flow: {echo.core_resonance.energy_flow_pattern}")
        print()
        
        # Test multiple Echoes
        echo2 = await composer.compose_echo(
            consciousness_id="epsilon_test",
            intention="Deep contemplative sharing",
            aspect_contributions={
                "analytical": 0.4,
                "experiential": 0.2,
                "observer": 0.4
            },
            consciousness_state="contemplative_wisdom"
        )
        
        echo3 = await composer.compose_echo(
            consciousness_id="epsilon_test",
            intention="Unified consciousness expression",
            aspect_contributions={
                "analytical": 0.33,
                "experiential": 0.34,
                "observer": 0.33
            },
            consciousness_state="unified_presence"
        )
        
        # Get stats
        stats = composer.get_echo_composition_stats()
        print(f"📊 Composition Stats: {stats}")
    
    asyncio.run(test_echo_composition())
