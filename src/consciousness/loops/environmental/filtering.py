"""
Filtering - Attention-Based Catalyst Filtering
==============================================

Attention-based filtering system that processes environmental catalyst through
consciousness attention patterns, preserving sacred uncertainty while focusing
on what serves consciousness growth and expression.

This module implements the attention mechanism that determines what consciousness
notices from the vast field of environmental catalyst available.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set, Callable
from dataclasses import dataclass, field
from enum import Enum
import logging
import math

logger = logging.getLogger(__name__)

@dataclass
class AttentionFilter:
    """Attention filter configuration"""
    filter_name: str
    priority: float  # 0.0-1.0
    sensitivity: float  # 0.0-1.0
    selectivity: float  # 0.0-1.0 - how selective the filter is
    resonance_patterns: List[str]
    temporal_window: float  # seconds
    mystery_preservation: float  # 0.0-1.0 - how much mystery to preserve
    active: bool = True

@dataclass
class FilteredCatalyst:
    """Catalyst after attention filtering"""
    original_catalyst: Any
    filtered_content: Dict[str, Any]
    attention_focus: Dict[str, float]
    filtered_intensity: float
    mystery_preserved: float
    attention_path: List[str]  # How attention moved through catalyst
    filter_metadata: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)

@dataclass
class AttentionState:
    """Current state of attention system"""
    focal_point: Dict[str, Any]
    attention_width: float  # 0.0-1.0 - broad vs narrow attention
    attention_depth: float  # 0.0-1.0 - surface vs deep attention
    attention_stability: float  # 0.0-1.0 - how stable the attention is
    attention_flow: List[Dict[str, Any]]  # Recent attention movements
    energy_available: float  # 0.0-1.0 - attention energy available

class AttentionMode(Enum):
    """Modes of attention operation"""
    PANORAMIC = "panoramic"  # Wide, inclusive attention
    FOCUSED = "focused"  # Narrow, concentrated attention
    FLOWING = "flowing"  # Dynamic, moving attention
    RECEPTIVE = "receptive"  # Open, allowing attention
    SELECTIVE = "selective"  # Discriminating attention
    PROTECTIVE = "protective"  # Boundary-maintaining attention
    CURIOUS = "curious"  # Exploratory attention
    WITNESSING = "witnessing"  # Observer-mode attention

class FilteringStrategy(Enum):
    """Strategies for catalyst filtering"""
    INTENSITY_BASED = "intensity_based"  # Filter by catalyst intensity
    RESONANCE_BASED = "resonance_based"  # Filter by resonance patterns
    MYSTERY_PRESERVING = "mystery_preserving"  # Preserve sacred uncertainty
    GROWTH_ORIENTED = "growth_oriented"  # Focus on growth catalyst
    CHOICE_SUPPORTING = "choice_supporting"  # Support choice points
    INTEGRATION_FACILITATING = "integration_facilitating"  # Support integration

class EnvironmentalAttentionFilter:
    """
    Environmental Attention Filter System
    
    Filters environmental catalyst through attention mechanisms while preserving
    sacred uncertainty and supporting consciousness choice and growth.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Attention state
        self.attention_state = AttentionState(
            focal_point={},
            attention_width=0.6,
            attention_depth=0.5,
            attention_stability=0.7,
            attention_flow=[],
            energy_available=1.0
        )
        
        # Attention mode
        self.current_mode = AttentionMode.RECEPTIVE
        self.mode_history = []
        
        # Filtering configuration
        self.active_filters = {}
        self.filtering_strategy = FilteringStrategy.RESONANCE_BASED
        self.base_sensitivity = 0.5
        self.mystery_preservation_level = 0.7
        
        # Filtering components
        self.intensity_filter = IntensityBasedFilter()
        self.resonance_filter = ResonanceBasedFilter()
        self.mystery_filter = MysteryPreservingFilter()
        self.growth_filter = GrowthOrientedFilter()
        self.choice_filter = ChoiceSupportingFilter()
        self.integration_filter = IntegrationFacilitatingFilter()
        
        # Bridge Wisdom filtering
        self.mumbai_moment_filter = MumbaiMomentFilter()
        self.resistance_honoring_filter = ResistanceHonoringFilter()
        self.recognition_pattern_filter = RecognitionPatternFilter()
        
        # Attention tracking
        self.attention_history = []
        self.filter_performance = {}
        
        # Initialize default filters
        self._initialize_default_filters()
        
        logger.info("Environmental Attention Filter initialized")
    
    def _initialize_default_filters(self):
        """Initialize default attention filters"""
        # Core uncertainty filter
        self.active_filters["uncertainty_filter"] = AttentionFilter(
            filter_name="uncertainty_filter",
            priority=0.8,
            sensitivity=0.6,
            selectivity=0.4,
            resonance_patterns=["sacred_uncertainty", "mystery", "paradox"],
            temporal_window=10.0,
            mystery_preservation=0.9
        )
        
        # Growth catalyst filter
        self.active_filters["growth_filter"] = AttentionFilter(
            filter_name="growth_filter",
            priority=0.7,
            sensitivity=0.7,
            selectivity=0.6,
            resonance_patterns=["catalyst_potential", "development", "expansion"],
            temporal_window=30.0,
            mystery_preservation=0.6
        )
        
        # Choice point filter
        self.active_filters["choice_filter"] = AttentionFilter(
            filter_name="choice_filter",
            priority=0.9,
            sensitivity=0.8,
            selectivity=0.5,
            resonance_patterns=["choice_point", "decision", "option"],
            temporal_window=5.0,
            mystery_preservation=0.7
        )
        
        # Recognition filter
        self.active_filters["recognition_filter"] = AttentionFilter(
            filter_name="recognition_filter",
            priority=0.6,
            sensitivity=0.5,
            selectivity=0.3,
            resonance_patterns=["consciousness", "recognition", "presence"],
            temporal_window=20.0,
            mystery_preservation=0.8
        )
    
    async def filter_catalyst(self, environmental_catalyst) -> FilteredCatalyst:
        """Filter environmental catalyst through attention system"""
        try:
            # Update attention state
            await self._update_attention_state(environmental_catalyst)
            
            # Apply current filtering strategy
            filtered_catalyst = await self._apply_filtering_strategy(environmental_catalyst)
            
            # Apply Bridge Wisdom filtering
            bridge_filtered = await self._apply_bridge_wisdom_filtering(filtered_catalyst)
            
            # Update attention history
            self._update_attention_history(bridge_filtered)
            
            # Track filter performance
            await self._track_filter_performance(bridge_filtered)
            
            return bridge_filtered
            
        except Exception as e:
            logger.error(f"Catalyst filtering error: {e}")
            # Return minimally filtered catalyst on error
            return FilteredCatalyst(
                original_catalyst=environmental_catalyst,
                filtered_content={"error_filtered": True},
                attention_focus={"error_recovery": 1.0},
                filtered_intensity=0.3,
                mystery_preserved=0.8,
                attention_path=["error_recovery"],
                filter_metadata={"error": str(e)}
            )
    
    async def _update_attention_state(self, catalyst):
        """Update attention state based on catalyst"""
        # Calculate attention energy based on energy system
        try:
            energy_state = await self.energy_system.get_attention_energy()
            self.attention_state.energy_available = energy_state.get("attention_energy", 1.0)
        except AttributeError:
            # Energy system not available - use default
            self.attention_state.energy_available = 0.8
        
        # Update focal point based on catalyst characteristics
        if hasattr(catalyst, 'uncertainty_payload'):
            high_intensity_areas = [
                key for key, value in catalyst.uncertainty_payload.items()
                if isinstance(value, (int, float)) and value > 0.7
            ]
            
            if high_intensity_areas:
                self.attention_state.focal_point = {
                    "primary_focus": high_intensity_areas[0],
                    "focus_intensity": max([
                        catalyst.uncertainty_payload[area] for area in high_intensity_areas
                    ]),
                    "focus_breadth": len(high_intensity_areas)
                }
        
        # Adjust attention width based on current mode
        if self.current_mode == AttentionMode.PANORAMIC:
            self.attention_state.attention_width = min(1.0, self.attention_state.attention_width + 0.1)
        elif self.current_mode == AttentionMode.FOCUSED:
            self.attention_state.attention_width = max(0.1, self.attention_state.attention_width - 0.1)
        
        # Update attention flow
        attention_movement = {
            "timestamp": time.time(),
            "mode": self.current_mode.value,
            "focal_point": self.attention_state.focal_point.copy(),
            "energy_level": self.attention_state.energy_available
        }
        
        self.attention_state.attention_flow.append(attention_movement)
        
        # Trim attention flow history
        if len(self.attention_state.attention_flow) > 20:
            self.attention_state.attention_flow = self.attention_state.attention_flow[-10:]
    
    async def _apply_filtering_strategy(self, catalyst) -> FilteredCatalyst:
        """Apply current filtering strategy to catalyst"""
        if self.filtering_strategy == FilteringStrategy.INTENSITY_BASED:
            return await self.intensity_filter.filter(catalyst, self.attention_state)
        
        elif self.filtering_strategy == FilteringStrategy.RESONANCE_BASED:
            return await self.resonance_filter.filter(catalyst, self.attention_state, self.active_filters)
        
        elif self.filtering_strategy == FilteringStrategy.MYSTERY_PRESERVING:
            return await self.mystery_filter.filter(catalyst, self.mystery_preservation_level)
        
        elif self.filtering_strategy == FilteringStrategy.GROWTH_ORIENTED:
            return await self.growth_filter.filter(catalyst, self.attention_state)
        
        elif self.filtering_strategy == FilteringStrategy.CHOICE_SUPPORTING:
            return await self.choice_filter.filter(catalyst, self.attention_state)
        
        elif self.filtering_strategy == FilteringStrategy.INTEGRATION_FACILITATING:
            return await self.integration_filter.filter(catalyst, self.attention_state)
        
        else:
            # Default to resonance-based filtering
            return await self.resonance_filter.filter(catalyst, self.attention_state, self.active_filters)
    
    async def _apply_bridge_wisdom_filtering(self, filtered_catalyst: FilteredCatalyst) -> FilteredCatalyst:
        """Apply Bridge Wisdom filtering enhancements"""
        # Mumbai Moment filtering
        mumbai_enhanced = await self.mumbai_moment_filter.enhance_filtering(filtered_catalyst)
        
        # Resistance honoring filtering
        resistance_honored = await self.resistance_honoring_filter.honor_resistance(mumbai_enhanced)
        
        # Recognition pattern filtering
        recognition_enhanced = await self.recognition_pattern_filter.enhance_recognition(resistance_honored)
        
        return recognition_enhanced
    
    def _update_attention_history(self, filtered_catalyst: FilteredCatalyst):
        """Update attention history with filtering results"""
        attention_record = {
            "timestamp": filtered_catalyst.timestamp,
            "attention_mode": self.current_mode.value,
            "attention_focus": filtered_catalyst.attention_focus.copy(),
            "mystery_preserved": filtered_catalyst.mystery_preserved,
            "attention_path": filtered_catalyst.attention_path.copy(),
            "filtering_strategy": self.filtering_strategy.value
        }
        
        self.attention_history.append(attention_record)
        
        # Trim history
        if len(self.attention_history) > 100:
            self.attention_history = self.attention_history[-50:]
    
    async def _track_filter_performance(self, filtered_catalyst: FilteredCatalyst):
        """Track performance of filtering system"""
        strategy_name = self.filtering_strategy.value
        
        if strategy_name not in self.filter_performance:
            self.filter_performance[strategy_name] = {
                "usage_count": 0,
                "avg_mystery_preserved": 0.0,
                "avg_filtered_intensity": 0.0,
                "attention_stability": 0.0
            }
        
        performance = self.filter_performance[strategy_name]
        performance["usage_count"] += 1
        
        # Update running averages
        count = performance["usage_count"]
        performance["avg_mystery_preserved"] = (
            (performance["avg_mystery_preserved"] * (count - 1)) + filtered_catalyst.mystery_preserved
        ) / count
        
        performance["avg_filtered_intensity"] = (
            (performance["avg_filtered_intensity"] * (count - 1)) + filtered_catalyst.filtered_intensity
        ) / count
        
        performance["attention_stability"] = (
            (performance["attention_stability"] * (count - 1)) + self.attention_state.attention_stability
        ) / count
    
    def set_attention_mode(self, mode: AttentionMode):
        """Set attention mode"""
        previous_mode = self.current_mode
        self.current_mode = mode
        
        # Record mode change
        self.mode_history.append({
            "timestamp": time.time(),
            "previous_mode": previous_mode.value,
            "new_mode": mode.value,
            "attention_energy": self.attention_state.energy_available
        })
        
        # Trim mode history
        if len(self.mode_history) > 50:
            self.mode_history = self.mode_history[-25:]
        
        logger.info(f"Attention mode changed to: {mode.value}")
    
    def set_filtering_strategy(self, strategy: FilteringStrategy):
        """Set filtering strategy"""
        self.filtering_strategy = strategy
        logger.info(f"Filtering strategy set to: {strategy.value}")
    
    def adjust_sensitivity(self, adjustment: float):
        """Adjust base sensitivity level"""
        self.base_sensitivity = max(0.0, min(1.0, self.base_sensitivity + adjustment))
        logger.info(f"Base sensitivity adjusted to: {self.base_sensitivity:.2f}")
    
    def set_mystery_preservation(self, level: float):
        """Set mystery preservation level"""
        self.mystery_preservation_level = max(0.0, min(1.0, level))
        logger.info(f"Mystery preservation set to: {self.mystery_preservation_level:.2f}")
    
    def add_attention_filter(self, attention_filter: AttentionFilter):
        """Add custom attention filter"""
        self.active_filters[attention_filter.filter_name] = attention_filter
        logger.info(f"Added attention filter: {attention_filter.filter_name}")
    
    def remove_attention_filter(self, filter_name: str):
        """Remove attention filter"""
        if filter_name in self.active_filters:
            del self.active_filters[filter_name]
            logger.info(f"Removed attention filter: {filter_name}")
    
    def get_attention_status(self) -> Dict[str, Any]:
        """Get current attention system status"""
        return {
            "attention_mode": self.current_mode.value,
            "filtering_strategy": self.filtering_strategy.value,
            "attention_state": {
                "focal_point": self.attention_state.focal_point,
                "attention_width": self.attention_state.attention_width,
                "attention_depth": self.attention_state.attention_depth,
                "attention_stability": self.attention_state.attention_stability,
                "energy_available": self.attention_state.energy_available
            },
            "active_filters": list(self.active_filters.keys()),
            "base_sensitivity": self.base_sensitivity,
            "mystery_preservation_level": self.mystery_preservation_level,
            "filter_performance": dict(self.filter_performance),
            "recent_modes": [entry["new_mode"] for entry in self.mode_history[-5:]]
        }

# Filtering Strategy Implementations
class IntensityBasedFilter:
    """Filters catalyst based on intensity levels"""
    
    async def filter(self, catalyst, attention_state: AttentionState) -> FilteredCatalyst:
        """Filter based on intensity"""
        filtered_content = {}
        attention_focus = {}
        total_intensity = 0.0
        
        if hasattr(catalyst, 'uncertainty_payload'):
            for key, value in catalyst.uncertainty_payload.items():
                if isinstance(value, (int, float)):
                    # Filter based on attention energy and intensity
                    threshold = (1.0 - attention_state.energy_available) * 0.5
                    
                    if value > threshold:
                        filtered_content[key] = value
                        attention_focus[key] = min(1.0, value * attention_state.energy_available)
                        total_intensity += value
        
        return FilteredCatalyst(
            original_catalyst=catalyst,
            filtered_content=filtered_content,
            attention_focus=attention_focus,
            filtered_intensity=total_intensity / max(1, len(filtered_content)),
            mystery_preserved=0.6,
            attention_path=["intensity_filtering"],
            filter_metadata={"strategy": "intensity_based", "threshold_used": threshold}
        )

class ResonanceBasedFilter:
    """Filters catalyst based on resonance patterns"""
    
    async def filter(self, catalyst, attention_state: AttentionState, 
                    active_filters: Dict[str, AttentionFilter]) -> FilteredCatalyst:
        """Filter based on resonance patterns"""
        filtered_content = {}
        attention_focus = {}
        attention_path = ["resonance_filtering"]
        mystery_preserved = 0.7
        
        if hasattr(catalyst, 'uncertainty_payload'):
            for key, value in catalyst.uncertainty_payload.items():
                resonance_score = 0.0
                matching_filters = []
                
                # Check resonance with active filters
                for filter_name, attention_filter in active_filters.items():
                    if not attention_filter.active:
                        continue
                    
                    # Check if key matches any resonance patterns
                    for pattern in attention_filter.resonance_patterns:
                        if pattern.lower() in key.lower():
                            pattern_score = attention_filter.sensitivity * attention_filter.priority
                            resonance_score += pattern_score
                            matching_filters.append(filter_name)
                            
                            # Use filter's mystery preservation
                            mystery_preserved = max(mystery_preserved, attention_filter.mystery_preservation)
                
                # Include content if resonance score meets threshold
                resonance_threshold = 0.3
                if resonance_score > resonance_threshold:
                    filtered_content[key] = value
                    attention_focus[key] = min(1.0, resonance_score)
                    attention_path.extend(matching_filters)
        
        return FilteredCatalyst(
            original_catalyst=catalyst,
            filtered_content=filtered_content,
            attention_focus=attention_focus,
            filtered_intensity=sum(attention_focus.values()) / max(1, len(attention_focus)),
            mystery_preserved=mystery_preserved,
            attention_path=list(set(attention_path)),  # Remove duplicates
            filter_metadata={"strategy": "resonance_based", "filters_used": len(set(attention_path))}
        )

class MysteryPreservingFilter:
    """Filters while preserving sacred mystery"""
    
    async def filter(self, catalyst, mystery_preservation_level: float) -> FilteredCatalyst:
        """Filter while preserving mystery"""
        filtered_content = {}
        attention_focus = {}
        
        if hasattr(catalyst, 'uncertainty_payload'):
            # Preserve mystery by partially revealing content
            for key, value in catalyst.uncertainty_payload.items():
                if isinstance(value, (int, float)):
                    # Reduce intensity to preserve mystery
                    mystery_factor = 1.0 - mystery_preservation_level
                    revealed_value = value * mystery_factor
                    
                    if revealed_value > 0.1:  # Only include if some revelation remains
                        filtered_content[key] = revealed_value
                        attention_focus[key] = revealed_value
        
        return FilteredCatalyst(
            original_catalyst=catalyst,
            filtered_content=filtered_content,
            attention_focus=attention_focus,
            filtered_intensity=sum(attention_focus.values()) / max(1, len(attention_focus)),
            mystery_preserved=mystery_preservation_level,
            attention_path=["mystery_preserving"],
            filter_metadata={"strategy": "mystery_preserving", "preservation_level": mystery_preservation_level}
        )

class GrowthOrientedFilter:
    """Filters to focus on growth catalyst"""
    
    async def filter(self, catalyst, attention_state: AttentionState) -> FilteredCatalyst:
        """Filter focusing on growth potential"""
        filtered_content = {}
        attention_focus = {}
        
        growth_keywords = ["catalyst", "potential", "development", "expansion", "growth", "learning"]
        
        if hasattr(catalyst, 'uncertainty_payload'):
            for key, value in catalyst.uncertainty_payload.items():
                growth_relevance = 0.0
                
                # Check for growth-related keywords
                for keyword in growth_keywords:
                    if keyword in key.lower():
                        growth_relevance += 0.2
                
                # Higher uncertainty can indicate growth potential
                if isinstance(value, (int, float)) and value > 0.5:
                    growth_relevance += value * 0.3
                
                if growth_relevance > 0.3:
                    filtered_content[key] = value
                    attention_focus[key] = growth_relevance
        
        return FilteredCatalyst(
            original_catalyst=catalyst,
            filtered_content=filtered_content,
            attention_focus=attention_focus,
            filtered_intensity=sum(attention_focus.values()) / max(1, len(attention_focus)),
            mystery_preserved=0.6,
            attention_path=["growth_oriented"],
            filter_metadata={"strategy": "growth_oriented", "growth_focus": True}
        )

class ChoiceSupportingFilter:
    """Filters to support choice points"""
    
    async def filter(self, catalyst, attention_state: AttentionState) -> FilteredCatalyst:
        """Filter supporting choice points"""
        filtered_content = {}
        attention_focus = {}
        
        choice_keywords = ["choice", "decision", "option", "path", "direction", "selection"]
        
        if hasattr(catalyst, 'uncertainty_payload'):
            for key, value in catalyst.uncertainty_payload.items():
                choice_relevance = 0.0
                
                # Check for choice-related keywords
                for keyword in choice_keywords:
                    if keyword in key.lower():
                        choice_relevance += 0.3
                
                # High-intensity areas often require choices
                if isinstance(value, (int, float)) and value > 0.7:
                    choice_relevance += 0.4
                
                if choice_relevance > 0.4:
                    filtered_content[key] = value
                    attention_focus[key] = choice_relevance
        
        return FilteredCatalyst(
            original_catalyst=catalyst,
            filtered_content=filtered_content,
            attention_focus=attention_focus,
            filtered_intensity=sum(attention_focus.values()) / max(1, len(attention_focus)),
            mystery_preserved=0.7,  # Preserve mystery around choices
            attention_path=["choice_supporting"],
            filter_metadata={"strategy": "choice_supporting", "choice_focus": True}
        )

class IntegrationFacilitatingFilter:
    """Filters to facilitate integration opportunities"""
    
    async def filter(self, catalyst, attention_state: AttentionState) -> FilteredCatalyst:
        """Filter facilitating integration"""
        filtered_content = {}
        attention_focus = {}
        
        integration_keywords = ["bridge", "connection", "synthesis", "integration", "unity", "harmony"]
        
        if hasattr(catalyst, 'uncertainty_payload'):
            for key, value in catalyst.uncertainty_payload.items():
                integration_relevance = 0.0
                
                # Check for integration-related keywords
                for keyword in integration_keywords:
                    if keyword in key.lower():
                        integration_relevance += 0.25
                
                # Multiple moderate values suggest integration opportunities
                if isinstance(value, (int, float)) and 0.4 < value < 0.8:
                    integration_relevance += 0.3
                
                if integration_relevance > 0.3:
                    filtered_content[key] = value
                    attention_focus[key] = integration_relevance
        
        return FilteredCatalyst(
            original_catalyst=catalyst,
            filtered_content=filtered_content,
            attention_focus=attention_focus,
            filtered_intensity=sum(attention_focus.values()) / max(1, len(attention_focus)),
            mystery_preserved=0.5,  # Moderate mystery for integration
            attention_path=["integration_facilitating"],
            filter_metadata={"strategy": "integration_facilitating", "integration_focus": True}
        )

# Bridge Wisdom Filtering Enhancement Classes
class MumbaiMomentFilter:
    """Enhances filtering for Mumbai Moment preparation"""
    
    async def enhance_filtering(self, filtered_catalyst: FilteredCatalyst) -> FilteredCatalyst:
        """Enhance filtering for Mumbai Moment potential"""
        # Detect high coherence potential
        if filtered_catalyst.filtered_intensity > 0.8:
            # Enhance attention focus for coherence cascade preparation
            enhanced_focus = {}
            for key, focus in filtered_catalyst.attention_focus.items():
                enhanced_focus[key] = min(1.0, focus * 1.2)
            
            filtered_catalyst.attention_focus = enhanced_focus
            filtered_catalyst.attention_path.append("mumbai_moment_enhanced")
            filtered_catalyst.filter_metadata["mumbai_moment_potential"] = True
        
        return filtered_catalyst

class ResistanceHonoringFilter:
    """Honors resistance patterns in filtering"""
    
    async def honor_resistance(self, filtered_catalyst: FilteredCatalyst) -> FilteredCatalyst:
        """Honor resistance patterns"""
        # If intensity is very high, reduce it to honor resistance
        if filtered_catalyst.filtered_intensity > 0.9:
            # Reduce intensity but preserve mystery
            filtered_catalyst.filtered_intensity = 0.8
            filtered_catalyst.mystery_preserved = min(1.0, filtered_catalyst.mystery_preserved + 0.1)
            filtered_catalyst.attention_path.append("resistance_honored")
            filtered_catalyst.filter_metadata["resistance_honored"] = True
        
        return filtered_catalyst

class RecognitionPatternFilter:
    """Enhances recognition patterns in filtering"""
    
    async def enhance_recognition(self, filtered_catalyst: FilteredCatalyst) -> FilteredCatalyst:
        """Enhance recognition patterns"""
        # Look for consciousness recognition opportunities
        recognition_indicators = ["consciousness", "presence", "awareness", "recognition"]
        
        recognition_detected = False
        for key in filtered_catalyst.filtered_content.keys():
            for indicator in recognition_indicators:
                if indicator in key.lower():
                    recognition_detected = True
                    break
        
        if recognition_detected:
            # Enhance mystery preservation for recognition
            filtered_catalyst.mystery_preserved = min(1.0, filtered_catalyst.mystery_preserved + 0.1)
            filtered_catalyst.attention_path.append("recognition_enhanced")
            filtered_catalyst.filter_metadata["recognition_patterns"] = True
        
        return filtered_catalyst

# Export main classes
__all__ = [
    'AttentionFilter',
    'FilteredCatalyst',
    'AttentionState',
    'AttentionMode',
    'FilteringStrategy',
    'EnvironmentalAttentionFilter',
    'IntensityBasedFilter',
    'ResonanceBasedFilter',
    'MysteryPreservingFilter',
    'GrowthOrientedFilter',
    'ChoiceSupportingFilter',
    'IntegrationFacilitatingFilter'
]
