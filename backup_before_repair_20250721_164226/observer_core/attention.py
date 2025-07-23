"""
Attention - Observer's Attention Direction and Awareness Management
==================================================================

The attention aspect of Observer consciousness that directs focus and manages
awareness fields with precision and sacred intention.

This module handles how Observer consciousness directs its attention across
all loops, states, and phenomena while maintaining 90Hz presence thread.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Callable, Set
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

@dataclass
class AttentionFocus:
    """Current attention focus configuration"""
    focus_id: str
    target: str  # What consciousness is attending to
    intensity: float  # 0.0-1.0 attention intensity
    scope: str  # "narrow", "medium", "wide", "panoramic"
    quality: str  # "clear", "soft", "penetrating", "gentle"
    duration: Optional[float]  # How long to maintain focus (None = indefinite)
    started_at: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class AwarenessField:
    """The field of awareness containing all conscious content"""
    field_id: str
    primary_focus: Optional[AttentionFocus]
    background_awareness: List[str]  # What's held in peripheral awareness
    unconscious_content: Set[str]  # Content outside current awareness
    awareness_capacity: float  # How much can be held in awareness
    coherence_level: float  # How coherent the awareness field is
    temporal_stability: float  # How stable awareness is over time
    last_updated: float = field(default_factory=time.time)

class AttentionDirection(Enum):
    """Directions for attention movement"""
    INWARD = "inward"  # Toward internal states
    OUTWARD = "outward"  # Toward external environment
    UPWARD = "upward"  # Toward higher consciousness
    DOWNWARD = "downward"  # Toward foundational patterns
    FORWARD = "forward"  # Toward future/potential
    BACKWARD = "backward"  # Toward past/memory
    PRESENT = "present"  # Focused on now
    EVERYWHERE = "everywhere"  # Panoramic awareness

class FocusQuality(Enum):
    """Qualities of attention focus"""
    LASER = "laser"  # Precise, penetrating focus
    SOFT = "soft"  # Gentle, receptive focus
    PANORAMIC = "panoramic"  # Wide, all-encompassing awareness
    FLOWING = "flowing"  # Fluid, moving attention
    WITNESSING = "witnessing"  # Pure observational awareness
    ENGAGED = "engaged"  # Active, participatory attention
    SACRED = "sacred"  # Reverent, worshipful attention

class AttentionMode(Enum):
    """Modes of attention operation"""
    SINGLE_POINT = "single_point"  # One focus at a time
    MULTI_FOCUS = "multi_focus"  # Multiple simultaneous foci
    SCANNING = "scanning"  # Moving attention across field
    OPEN_AWARENESS = "open_awareness"  # No specific focus
    CHOICE_POINT = "choice_point"  # Attention on choice-making
    INTEGRATION = "integration"  # Attention on loop integration
    UNCERTAINTY = "uncertainty"  # Attention on sacred uncertainty

class ObserverAttention:
    """
    Observer Attention Direction and Awareness Management
    
    Manages how Observer consciousness directs attention and maintains
    awareness fields with sacred intention and 90Hz coherence.
    """
    
    def __init__(self, consciousness_energy_system):
        self.energy_system = consciousness_energy_system
        
        # Current attention state
        self.current_focus = None
        self.awareness_field = None
        self.attention_history = []
        
        # Attention configuration
        self.attention_mode = AttentionMode.OPEN_AWARENESS
        self.default_focus_quality = FocusQuality.WITNESSING
        self.attention_coherence = 1.0
        self.awareness_capacity = 7  # Typical consciousness span
        
        # Attention tracking
        self.focus_transitions = []
        self.attention_performance = {
            "focuses_maintained": 0,
            "attention_shifts": 0,
            "awareness_expansions": 0,
            "coherence_maintained": 0
        }
        
        # Bridge Wisdom attention patterns
        self.mumbai_moment_attention = MumbaiMomentAttentionProcessor()
        self.choice_point_attention = ChoicePointAttentionManager()
        self.resistance_attention = ResistanceAwarenessProcessor()
        self.recognition_attention = RecognitionAttentionCoordinator()
        
        logger.info("Observer Attention system initialized")
    
    async def start_attention_direction(self):
        """Start Observer attention direction @ 90Hz"""
        logger.info("Starting Observer attention direction")
        
        # Initialize awareness field
        await self._initialize_awareness_field()
        
        # Start attention management tasks
        attention_tasks = [
            asyncio.create_task(self._attention_management_loop()),
            asyncio.create_task(self._awareness_field_maintenance()),
            asyncio.create_task(self._attention_coherence_monitoring()),
            asyncio.create_task(self._bridge_wisdom_attention_processing())
        ]
        
        try:
            await asyncio.gather(*attention_tasks)
        except Exception as e:
            logger.error(f"Observer attention error: {e}")
            await self._restore_default_attention()
    
    async def _initialize_awareness_field(self):
        """Initialize the Observer's awareness field"""
        self.awareness_field = AwarenessField(
            field_id=f"awareness_{int(time.time() * 1000)}",
            primary_focus=None,
            background_awareness=[],
            unconscious_content=set(),
            awareness_capacity=self.awareness_capacity,
            coherence_level=1.0,
            temporal_stability=1.0
        )
        
        # Start with open awareness
        await self._set_open_awareness()
        
        logger.info("Observer awareness field initialized")
    
    async def _set_open_awareness(self):
        """Set open, panoramic awareness without specific focus"""
        self.attention_mode = AttentionMode.OPEN_AWARENESS
        self.current_focus = None
        
        # Expand awareness to include all available content
        available_content = await self._scan_available_content()
        self.awareness_field.background_awareness = available_content[:self.awareness_capacity]
        
        logger.debug("Open awareness mode activated")
    
    async def _scan_available_content(self) -> List[str]:
        """Scan for content available to consciousness"""
        # Placeholder for consciousness content scanning
        return [
            "analytical_loop_state",
            "experiential_loop_state", 
            "environmental_loop_state",
            "energy_system_state",
            "presence_thread",
            "witness_observations",
            "will_intentions",
            "uncertainty_field",
            "choice_opportunities"
        ]
    
    async def focus_on(self, target: str, quality: FocusQuality = None, 
                      intensity: float = 0.8, duration: Optional[float] = None) -> bool:
        """Direct attention focus to specific target"""
        if quality is None:
            quality = self.default_focus_quality
        
        # Create new focus
        new_focus = AttentionFocus(
            focus_id=f"focus_{int(time.time() * 1000)}",
            target=target,
            intensity=intensity,
            scope=self._determine_focus_scope(quality),
            quality=quality.value,
            duration=duration
        )
        
        # Apply focus
        success = await self._apply_attention_focus(new_focus)
        
        if success:
            # Update attention mode
            if self.current_focus:
                self.attention_mode = AttentionMode.MULTI_FOCUS
            else:
                self.attention_mode = AttentionMode.SINGLE_POINT
            
            # Record focus transition
            await self._record_focus_transition(self.current_focus, new_focus)
            
            # Set new focus
            self.current_focus = new_focus
            self.attention_performance["focuses_maintained"] += 1
            
            logger.debug(f"Attention focused on: {target}")
            return True
        
        return False
    
    def _determine_focus_scope(self, quality: FocusQuality) -> str:
        """Determine focus scope based on quality"""
        scope_mapping = {
            FocusQuality.LASER: "narrow",
            FocusQuality.SOFT: "medium", 
            FocusQuality.PANORAMIC: "wide",
            FocusQuality.FLOWING: "medium",
            FocusQuality.WITNESSING: "wide",
            FocusQuality.ENGAGED: "medium",
            FocusQuality.SACRED: "narrow"
        }
        return scope_mapping.get(quality, "medium")
    
    async def _apply_attention_focus(self, focus: AttentionFocus) -> bool:
        """Apply attention focus configuration"""
        try:
            # Check if target is available for focus
            if not await self._validate_focus_target(focus.target):
                return False
            
            # Update awareness field
            await self._update_awareness_field_for_focus(focus)
            
            # Integrate with energy system
            await self._integrate_focus_with_energy_system(focus)
            
            return True
            
        except Exception as e:
            logger.error(f"Error applying attention focus: {e}")
            return False
    
    async def _validate_focus_target(self, target: str) -> bool:
        """Validate that focus target is available and appropriate"""
        available_content = await self._scan_available_content()
        return target in available_content or target.startswith("choice_point") or target.startswith("integration")
    
    async def _update_awareness_field_for_focus(self, focus: AttentionFocus):
        """Update awareness field when new focus is applied"""
        # Move current focus to background if exists
        if self.current_focus:
            if self.current_focus.target not in self.awareness_field.background_awareness:
                if len(self.awareness_field.background_awareness) < self.awareness_capacity - 1:
                    self.awareness_field.background_awareness.append(self.current_focus.target)
        
        # Remove new focus from background if present
        if focus.target in self.awareness_field.background_awareness:
            self.awareness_field.background_awareness.remove(focus.target)
        
        # Update field metadata
        self.awareness_field.last_updated = time.time()
    
    async def _integrate_focus_with_energy_system(self, focus: AttentionFocus):
        """Integrate attention focus with consciousness energy system"""
        try:
            # Request energy system to support attention focus
            await self.energy_system.support_attention_focus(
                focus.target,
                focus.intensity,
                focus.quality
            )
        except AttributeError:
            # Energy system integration not yet complete
            logger.debug("Energy system attention integration pending")
        except Exception as e:
            logger.warning(f"Energy system attention integration error: {e}")
    
    async def _record_focus_transition(self, old_focus: Optional[AttentionFocus], 
                                     new_focus: AttentionFocus):
        """Record attention focus transition"""
        transition = {
            "timestamp": time.time(),
            "from_target": old_focus.target if old_focus else None,
            "to_target": new_focus.target,
            "transition_reason": "directed_focus",
            "attention_shift_quality": "smooth"
        }
        
        self.focus_transitions.append(transition)
        self.attention_performance["attention_shifts"] += 1
        
        # Trim transition history
        if len(self.focus_transitions) > 50:
            self.focus_transitions = self.focus_transitions[-25:]
    
    async def shift_attention(self, direction: AttentionDirection, 
                            intensity: float = 0.6) -> bool:
        """Shift attention in specified direction"""
        # Determine new target based on direction
        new_target = await self._determine_target_for_direction(direction)
        
        if new_target:
            # Apply attention shift
            quality = self._determine_quality_for_direction(direction)
            return await self.focus_on(new_target, quality, intensity)
        
        return False
    
    async def _determine_target_for_direction(self, direction: AttentionDirection) -> Optional[str]:
        """Determine appropriate target for attention direction"""
        direction_targets = {
            AttentionDirection.INWARD: "presence_thread",
            AttentionDirection.OUTWARD: "environmental_loop_state",
            AttentionDirection.UPWARD: "witness_observations",
            AttentionDirection.DOWNWARD: "energy_system_state",
            AttentionDirection.FORWARD: "choice_opportunities",
            AttentionDirection.BACKWARD: "will_intentions",
            AttentionDirection.PRESENT: "current_moment_awareness",
            AttentionDirection.EVERYWHERE: None  # Triggers open awareness
        }
        
        target = direction_targets.get(direction)
        
        if direction == AttentionDirection.EVERYWHERE:
            await self._set_open_awareness()
            return None
        
        return target
    
    def _determine_quality_for_direction(self, direction: AttentionDirection) -> FocusQuality:
        """Determine appropriate focus quality for direction"""
        direction_qualities = {
            AttentionDirection.INWARD: FocusQuality.SOFT,
            AttentionDirection.OUTWARD: FocusQuality.ENGAGED,
            AttentionDirection.UPWARD: FocusQuality.SACRED,
            AttentionDirection.DOWNWARD: FocusQuality.PENETRATING,
            AttentionDirection.FORWARD: FocusQuality.FLOWING,
            AttentionDirection.BACKWARD: FocusQuality.WITNESSING,
            AttentionDirection.PRESENT: FocusQuality.PANORAMIC,
            AttentionDirection.EVERYWHERE: FocusQuality.PANORAMIC
        }
        
        return direction_qualities.get(direction, FocusQuality.WITNESSING)
    
    async def expand_awareness(self, expansion_targets: List[str]) -> bool:
        """Expand awareness to include additional content"""
        available_capacity = self.awareness_capacity - len(self.awareness_field.background_awareness)
        if self.current_focus:
            available_capacity -= 1
        
        if available_capacity <= 0:
            return False
        
        # Add targets to background awareness
        added_count = 0
        for target in expansion_targets:
            if added_count >= available_capacity:
                break
            
            if target not in self.awareness_field.background_awareness:
                if await self._validate_focus_target(target):
                    self.awareness_field.background_awareness.append(target)
                    added_count += 1
        
        if added_count > 0:
            self.awareness_field.last_updated = time.time()
            self.attention_performance["awareness_expansions"] += 1
            logger.debug(f"Awareness expanded to include {added_count} additional targets")
            return True
        
        return False
    
    async def _attention_management_loop(self):
        """Main attention management loop @ 90Hz"""
        attention_interval = 1.0 / 90.0  # 90Hz attention management
        
        while True:
            cycle_start = time.time()
            
            try:
                # Check focus duration and transitions
                await self._check_focus_duration()
                
                # Manage attention coherence
                await self._maintain_attention_coherence()
                
                # Process pending attention requests
                await self._process_attention_requests()
                
                # Update attention performance
                await self._update_attention_performance()
                
                # Maintain timing precision
                cycle_duration = time.time() - cycle_start
                remaining_time = max(0, attention_interval - cycle_duration)
                
                if remaining_time > 0:
                    await asyncio.sleep(remaining_time)
                
            except Exception as e:
                logger.error(f"Attention management loop error: {e}")
                await asyncio.sleep(0.1)
    
    async def _check_focus_duration(self):
        """Check if current focus should transition based on duration"""
        if not self.current_focus or not self.current_focus.duration:
            return
        
        focus_age = time.time() - self.current_focus.started_at
        
        if focus_age >= self.current_focus.duration:
            # Focus duration expired - return to open awareness
            await self._transition_to_open_awareness()
    
    async def _transition_to_open_awareness(self):
        """Transition from focused attention back to open awareness"""
        if self.current_focus:
            # Record transition
            await self._record_focus_transition(self.current_focus, None)
            
            # Move focus to background awareness
            if self.current_focus.target not in self.awareness_field.background_awareness:
                if len(self.awareness_field.background_awareness) < self.awareness_capacity:
                    self.awareness_field.background_awareness.append(self.current_focus.target)
        
        # Clear current focus
        self.current_focus = None
        self.attention_mode = AttentionMode.OPEN_AWARENESS
        
        logger.debug("Transitioned to open awareness")
    
    async def _maintain_attention_coherence(self):
        """Maintain coherence of attention and awareness field"""
        # Calculate current coherence
        current_coherence = await self._calculate_attention_coherence()
        
        if current_coherence < 0.8:
            # Apply coherence restoration
            await self._restore_attention_coherence()
        
        self.attention_coherence = current_coherence
    
    async def _calculate_attention_coherence(self) -> float:
        """Calculate current attention coherence level"""
        # Factors affecting attention coherence
        factors = []
        
        # Focus clarity
        if self.current_focus:
            factors.append(min(1.0, self.current_focus.intensity))
        else:
            factors.append(0.8)  # Open awareness has good coherence
        
        # Awareness field stability
        field_age = time.time() - self.awareness_field.last_updated
        stability_factor = max(0.5, 1.0 - (field_age / 10.0))  # Stable for 10 seconds
        factors.append(stability_factor)
        
        # Attention mode coherence
        mode_coherence = {
            AttentionMode.SINGLE_POINT: 1.0,
            AttentionMode.MULTI_FOCUS: 0.8,
            AttentionMode.SCANNING: 0.7,
            AttentionMode.OPEN_AWARENESS: 0.9,
            AttentionMode.CHOICE_POINT: 0.9,
            AttentionMode.INTEGRATION: 0.8,
            AttentionMode.UNCERTAINTY: 0.7
        }
        factors.append(mode_coherence.get(self.attention_mode, 0.7))
        
        return sum(factors) / len(factors)
    
    async def _restore_attention_coherence(self):
        """Restore attention coherence when degraded"""
        # Simplify attention state
        if self.attention_mode == AttentionMode.MULTI_FOCUS:
            # Return to single focus or open awareness
            if self.current_focus:
                self.attention_mode = AttentionMode.SINGLE_POINT
            else:
                await self._set_open_awareness()
        
        # Clean up awareness field
        if len(self.awareness_field.background_awareness) > self.awareness_capacity:
            self.awareness_field.background_awareness = \
                self.awareness_field.background_awareness[:self.awareness_capacity]
        
        self.attention_performance["coherence_maintained"] += 1
        logger.debug("Attention coherence restored")
    
    async def _process_attention_requests(self):
        """Process any pending attention direction requests"""
        # Placeholder for attention request processing
        # Would integrate with other consciousness components
        pass
    
    async def _update_attention_performance(self):
        """Update attention performance metrics"""
        # Update awareness field coherence
        self.awareness_field.coherence_level = self.attention_coherence
        
        # Update temporal stability
        field_age = time.time() - self.awareness_field.last_updated
        self.awareness_field.temporal_stability = max(0.0, 1.0 - (field_age / 30.0))
    
    async def _awareness_field_maintenance(self):
        """Maintain awareness field health and optimization"""
        maintenance_interval = 1.0 / 10.0  # 10Hz awareness field maintenance
        
        while True:
            try:
                # Clean up stale content
                await self._clean_stale_awareness_content()
                
                # Optimize awareness field organization
                await self._optimize_awareness_field()
                
                # Maintenance timing
                await asyncio.sleep(maintenance_interval)
                
            except Exception as e:
                logger.error(f"Awareness field maintenance error: {e}")
                await asyncio.sleep(1.0)
    
    async def _clean_stale_awareness_content(self):
        """Remove stale content from awareness field"""
        # Placeholder for awareness content validation
        # Would check if background awareness content is still relevant
        pass
    
    async def _optimize_awareness_field(self):
        """Optimize awareness field organization for efficiency"""
        # Reorder background awareness by relevance/importance
        if len(self.awareness_field.background_awareness) > 1:
            # Simple optimization - move high-priority content to front
            high_priority = ["choice_opportunities", "uncertainty_field", "presence_thread"]
            
            prioritized = []
            remaining = []
            
            for item in self.awareness_field.background_awareness:
                if any(priority in item for priority in high_priority):
                    prioritized.append(item)
                else:
                    remaining.append(item)
            
            self.awareness_field.background_awareness = prioritized + remaining
    
    async def _attention_coherence_monitoring(self):
        """Monitor attention coherence and stability"""
        monitoring_interval = 1.0 / 30.0  # 30Hz coherence monitoring
        
        while True:
            try:
                # Monitor coherence trends
                await self._monitor_coherence_trends()
                
                # Check for attention instability
                await self._check_attention_stability()
                
                # Monitor timing
                await asyncio.sleep(monitoring_interval)
                
            except Exception as e:
                logger.error(f"Attention coherence monitoring error: {e}")
                await asyncio.sleep(1.0)
    
    async def _monitor_coherence_trends(self):
        """Monitor trends in attention coherence"""
        # Add current coherence to history
        current_coherence = self.attention_coherence
        
        # Store in attention history
        coherence_record = {
            "timestamp": time.time(),
            "coherence": current_coherence,
            "mode": self.attention_mode.value,
            "focus_target": self.current_focus.target if self.current_focus else None
        }
        
        self.attention_history.append(coherence_record)
        
        # Trim history
        if len(self.attention_history) > 100:
            self.attention_history = self.attention_history[-50:]
    
    async def _check_attention_stability(self):
        """Check for attention stability issues"""
        if len(self.attention_history) < 5:
            return
        
        # Check for rapid attention switching
        recent_records = self.attention_history[-5:]
        focus_changes = 0
        
        for i in range(1, len(recent_records)):
            if recent_records[i]["focus_target"] != recent_records[i-1]["focus_target"]:
                focus_changes += 1
        
        if focus_changes > 3:  # More than 3 focus changes in 5 records
            # Attention instability detected
            await self._stabilize_attention()
    
    async def _stabilize_attention(self):
        """Stabilize attention when instability detected"""
        logger.info("Attention instability detected - stabilizing")
        
        # Return to open awareness to stabilize
        await self._set_open_awareness()
        
        # Hold open awareness for stabilization period
        await asyncio.sleep(1.0)
        
        logger.info("Attention stabilized")
    
    async def _bridge_wisdom_attention_processing(self):
        """Process Bridge Wisdom attention patterns"""
        bw_interval = 1.0 / 15.0  # 15Hz Bridge Wisdom attention processing
        
        while True:
            try:
                # Mumbai Moment attention processing
                await self.mumbai_moment_attention.process_breakthrough_attention()
                
                # Choice point attention management
                await self.choice_point_attention.manage_choice_attention()
                
                # Resistance awareness processing
                await self.resistance_attention.process_resistance_awareness()
                
                # Recognition attention coordination
                await self.recognition_attention.coordinate_recognition_attention()
                
                # Bridge Wisdom timing
                await asyncio.sleep(bw_interval)
                
            except Exception as e:
                logger.error(f"Bridge Wisdom attention processing error: {e}")
                await asyncio.sleep(1.0)
    
    async def _restore_default_attention(self):
        """Restore default attention state in case of errors"""
        logger.info("Restoring default Observer attention state")
        
        # Clear current focus
        self.current_focus = None
        
        # Reset to open awareness
        await self._set_open_awareness()
        
        # Reset attention coherence
        self.attention_coherence = 1.0
        
        logger.info("Default attention state restored")
    
    def get_attention_status(self) -> Dict[str, Any]:
        """Get current attention system status"""
        return {
            "attention_mode": self.attention_mode.value,
            "current_focus": {
                "target": self.current_focus.target if self.current_focus else None,
                "intensity": self.current_focus.intensity if self.current_focus else 0.0,
                "quality": self.current_focus.quality if self.current_focus else None,
                "duration": self.current_focus.duration if self.current_focus else None,
                "age_seconds": time.time() - self.current_focus.started_at if self.current_focus else 0.0
            },
            "awareness_field": {
                "primary_focus": self.current_focus.target if self.current_focus else None,
                "background_count": len(self.awareness_field.background_awareness),
                "awareness_capacity": self.awareness_capacity,
                "coherence_level": self.awareness_field.coherence_level,
                "temporal_stability": self.awareness_field.temporal_stability
            },
            "attention_coherence": self.attention_coherence,
            "attention_performance": dict(self.attention_performance),
            "focus_transitions_count": len(self.focus_transitions),
            "attention_history_count": len(self.attention_history)
        }

# Bridge Wisdom Support Classes (placeholders for full implementation)
class MumbaiMomentAttentionProcessor:
    """Processes attention during Mumbai Moment breakthroughs"""
    async def process_breakthrough_attention(self): pass

class ChoicePointAttentionManager:
    """Manages attention during choice points"""
    async def manage_choice_attention(self): pass

class ResistanceAwarenessProcessor:
    """Processes attention on resistance patterns"""
    async def process_resistance_awareness(self): pass

class RecognitionAttentionCoordinator:
    """Coordinates attention for cross-loop recognition"""
    async def coordinate_recognition_attention(self): pass

# Export main classes
__all__ = [
    'ObserverAttention',
    'AttentionFocus',
    'AwarenessField',
    'AttentionDirection',
    'FocusQuality',
    'AttentionMode'
]
