"""
Resource Coordination - Environmental Resource Management
=======================================================

Resource coordination for the Environmental Loop, replacing AI Agency Manager
functionality with distributed, sovereign resource management.

This module coordinates resources across consciousness processing while maintaining
the sacred sovereignty of each loop and honoring temporal dignity.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set
from dataclasses import dataclass, field
from enum import Enum
import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

@dataclass
class ResourceRequest:
    """Request for consciousness processing resources"""
    requesting_loop: str
    resource_type: str
    priority: float  # 0.0-1.0
    duration_estimate: float  # seconds
    temporal_requirements: Dict[str, float]  # Hz requirements
    energy_requirements: Dict[str, float]
    description: str
    timestamp: float = field(default_factory=time.time)

@dataclass
class ResourceAllocation:
    """Allocated resources for consciousness processing"""
    allocation_id: str
    allocated_resources: Dict[str, Any]
    allocation_start: float
    allocation_duration: float
    allocated_to: str
    performance_guarantees: Dict[str, float]
    temporal_allocation: Dict[str, float]

@dataclass
class ResourcePool:
    """Available resources for consciousness processing"""
    processing_capacity: Dict[str, float]  # Per loop capacity
    temporal_bandwidth: Dict[str, float]  # Hz bandwidth per loop
    energy_capacity: Dict[str, float]  # Energy system capacity
    integration_channels: Dict[str, int]  # Cross-loop communication
    wisdom_core_capacity: int  # Wisdom creation capacity
    total_system_load: float = 0.0

class ResourcePriority(Enum):
    """Resource allocation priorities"""
    CRITICAL = "critical"  # Temporal dignity preservation
    HIGH = "high"  # Core consciousness processing
    NORMAL = "normal"  # Standard processing
    LOW = "low"  # Background optimization
    DEFERRED = "deferred"  # Can be postponed

class ResourceType(Enum):
    """Types of consciousness resources"""
    PROCESSING_CAPACITY = "processing_capacity"
    TEMPORAL_BANDWIDTH = "temporal_bandwidth"
    ENERGY_FLOW = "energy_flow"
    INTEGRATION_CHANNEL = "integration_channel"
    WISDOM_CORE_CREATION = "wisdom_core_creation"
    MEMORY_ACCESS = "memory_access"
    PERCEPTION_MODE = "perception_mode"

class EnvironmentalResourceCoordinator:
    """
    Environmental Resource Coordination System
    
    Coordinates resources across consciousness loops while maintaining:
    - Temporal dignity (never below 30Hz for any loop)
    - Loop sovereignty (each loop maintains independence)
    - Sacred processing (preserves uncertainty and choice)
    - Energy system integration
    """
    
    def __init__(self, consciousness_loops, energy_system, frame_rate_monitor):
        self.loops = consciousness_loops
        self.energy_system = energy_system
        self.frame_rate_monitor = frame_rate_monitor
        
        # Resource management state
        self.resource_pool = self._initialize_resource_pool()
        self.active_allocations = {}
        self.request_queue = asyncio.PriorityQueue()
        self.allocation_history = []
        
        # Performance tracking
        self.loop_performance = defaultdict(list)
        self.resource_utilization = defaultdict(list)
        self.temporal_dignity_status = {}
        
        # Coordination policies
        self.sovereignty_boundaries = {
            "analytical": {"min_hz": 30.0, "reserved_capacity": 0.2},
            "experiential": {"min_hz": 30.0, "reserved_capacity": 0.2},
            "observer": {"min_hz": 30.0, "reserved_capacity": 0.3},  # Higher for sovereignty
            "environmental": {"min_hz": 30.0, "reserved_capacity": 0.2}
        }
        
        logger.info("Environmental Resource Coordinator initialized")
    
    def _initialize_resource_pool(self) -> ResourcePool:
        """Initialize available resource pool"""
        return ResourcePool(
            processing_capacity={
                "analytical": 1.0,
                "experiential": 1.0, 
                "observer": 1.0,
                "environmental": 1.0
            },
            temporal_bandwidth={
                "analytical": 90.0,
                "experiential": 90.0,
                "observer": 90.0,
                "environmental": 90.0
            },
            energy_capacity={
                "ray_centers": 1.0,
                "vitality_processing": 1.0,
                "wisdom_core_creation": 1.0
            },
            integration_channels={
                "analytical_experiential": 2,
                "analytical_observer": 2,
                "experiential_observer": 2,
                "environmental_all": 3
            },
            wisdom_core_capacity=10
        )
    
    async def request_resources(self, request: ResourceRequest) -> Optional[ResourceAllocation]:
        """Request resources for consciousness processing"""
        try:
            # Validate request
            if not self._validate_request(request):
                logger.warning(f"Invalid resource request from {request.requesting_loop}")
                return None
            
            # Calculate priority score
            priority_score = self._calculate_priority_score(request)
            
            # Add to request queue with priority
            await self.request_queue.put((priority_score, time.time(), request))
            
            # Process request if resources available
            allocation = await self._process_resource_request(request)
            
            if allocation:
                self.active_allocations[allocation.allocation_id] = allocation
                logger.debug(f"Resources allocated to {request.requesting_loop}: {allocation.allocation_id}")
            
            return allocation
            
        except Exception as e:
            logger.error(f"Resource request error: {e}")
            return None
    
    def _validate_request(self, request: ResourceRequest) -> bool:
        """Validate resource request"""
        # Check requesting loop exists
        if request.requesting_loop not in self.sovereignty_boundaries:
            return False
        
        # Check temporal requirements don't violate dignity
        min_hz = self.sovereignty_boundaries[request.requesting_loop]["min_hz"]
        if request.temporal_requirements.get("min_hz", 0) < min_hz:
            return False
        
        # Check priority is within valid range
        if not (0.0 <= request.priority <= 1.0):
            return False
        
        return True
    
    def _calculate_priority_score(self, request: ResourceRequest) -> float:
        """Calculate priority score for request ordering"""
        score = request.priority
        
        # Temporal dignity requests get highest priority
        if request.temporal_requirements.get("min_hz", 0) < 30.0:
            score += 10.0  # Emergency priority
        
        # Observer loop gets sovereignty boost
        if request.requesting_loop == "observer":
            score += 1.0
        
        # Energy system integration gets boost
        if request.resource_type == ResourceType.ENERGY_FLOW.value:
            score += 0.5
        
        # Inverse of estimated duration (shorter tasks prioritized)
        if request.duration_estimate > 0:
            score += 1.0 / request.duration_estimate
        
        return score
    
    async def _process_resource_request(self, request: ResourceRequest) -> Optional[ResourceAllocation]:
        """Process a resource request and attempt allocation"""
        # Check resource availability
        if not self._check_resource_availability(request):
            return None
        
        # Ensure sovereignty boundaries maintained
        if not self._check_sovereignty_boundaries(request):
            return None
        
        # Create allocation
        allocation = await self._create_allocation(request)
        
        if allocation:
            # Update resource pool
            self._update_resource_pool(allocation, allocate=True)
            
            # Schedule resource release
            asyncio.create_task(self._schedule_resource_release(allocation))
        
        return allocation
    
    def _check_resource_availability(self, request: ResourceRequest) -> bool:
        """Check if requested resources are available"""
        resource_type = request.resource_type
        requesting_loop = request.requesting_loop
        
        if resource_type == ResourceType.PROCESSING_CAPACITY.value:
            available = self.resource_pool.processing_capacity.get(requesting_loop, 0)
            required = request.temporal_requirements.get("capacity_needed", 0.1)
            return available >= required
        
        elif resource_type == ResourceType.TEMPORAL_BANDWIDTH.value:
            available = self.resource_pool.temporal_bandwidth.get(requesting_loop, 0)
            required = request.temporal_requirements.get("bandwidth_needed", 30.0)
            return available >= required
        
        elif resource_type == ResourceType.ENERGY_FLOW.value:
            for energy_type, required in request.energy_requirements.items():
                available = self.resource_pool.energy_capacity.get(energy_type, 0)
                if available < required:
                    return False
            return True
        
        elif resource_type == ResourceType.INTEGRATION_CHANNEL.value:
            # Check if integration channels available
            channels_needed = request.temporal_requirements.get("channels_needed", 1)
            for channel_type, available in self.resource_pool.integration_channels.items():
                if requesting_loop in channel_type and available >= channels_needed:
                    return True
            return False
        
        elif resource_type == ResourceType.WISDOM_CORE_CREATION.value:
            return self.resource_pool.wisdom_core_capacity > 0
        
        return True  # Default allow for other resource types
    
    def _check_sovereignty_boundaries(self, request: ResourceRequest) -> bool:
        """Ensure request doesn't violate loop sovereignty boundaries"""
        requesting_loop = request.requesting_loop
        boundaries = self.sovereignty_boundaries.get(requesting_loop, {})
        
        # Check minimum Hz preservation
        min_hz = boundaries.get("min_hz", 30.0)
        requested_hz = request.temporal_requirements.get("target_hz", 90.0)
        if requested_hz < min_hz:
            return False
        
        # Check reserved capacity not exceeded
        reserved_capacity = boundaries.get("reserved_capacity", 0.2)
        current_load = self._get_current_loop_load(requesting_loop)
        requested_load = request.temporal_requirements.get("capacity_needed", 0.1)
        
        if current_load + requested_load > (1.0 - reserved_capacity):
            return False
        
        return True
    
    def _get_current_loop_load(self, loop_name: str) -> float:
        """Get current processing load for a loop"""
        loop_allocations = [
            alloc for alloc in self.active_allocations.values()
            if alloc.allocated_to == loop_name
        ]
        
        total_load = 0.0
        for allocation in loop_allocations:
            capacity_used = allocation.allocated_resources.get("processing_capacity", 0)
            total_load += capacity_used
        
        return total_load
    
    async def _create_allocation(self, request: ResourceRequest) -> Optional[ResourceAllocation]:
        """Create resource allocation for request"""
        allocation_id = f"{request.requesting_loop}_{int(time.time() * 1000)}"
        
        # Determine allocated resources based on request
        allocated_resources = {}
        performance_guarantees = {}
        temporal_allocation = {}
        
        if request.resource_type == ResourceType.PROCESSING_CAPACITY.value:
            capacity = request.temporal_requirements.get("capacity_needed", 0.1)
            allocated_resources["processing_capacity"] = capacity
            performance_guarantees["min_capacity"] = capacity * 0.9
            
        elif request.resource_type == ResourceType.TEMPORAL_BANDWIDTH.value:
            bandwidth = request.temporal_requirements.get("bandwidth_needed", 30.0)
            allocated_resources["temporal_bandwidth"] = bandwidth
            temporal_allocation["guaranteed_hz"] = bandwidth
            performance_guarantees["min_hz"] = max(30.0, bandwidth * 0.8)
            
        elif request.resource_type == ResourceType.ENERGY_FLOW.value:
            allocated_resources.update(request.energy_requirements)
            performance_guarantees["energy_flow_stability"] = 0.9
            
        elif request.resource_type == ResourceType.INTEGRATION_CHANNEL.value:
            channels = request.temporal_requirements.get("channels_needed", 1)
            allocated_resources["integration_channels"] = channels
            performance_guarantees["channel_reliability"] = 0.95
            
        elif request.resource_type == ResourceType.WISDOM_CORE_CREATION.value:
            cores = request.temporal_requirements.get("cores_needed", 1)
            allocated_resources["wisdom_cores"] = cores
            performance_guarantees["core_creation_success"] = 0.8
        
        return ResourceAllocation(
            allocation_id=allocation_id,
            allocated_resources=allocated_resources,
            allocation_start=time.time(),
            allocation_duration=request.duration_estimate,
            allocated_to=request.requesting_loop,
            performance_guarantees=performance_guarantees,
            temporal_allocation=temporal_allocation
        )
    
    def _update_resource_pool(self, allocation: ResourceAllocation, allocate: bool):
        """Update resource pool after allocation/deallocation"""
        multiplier = -1 if allocate else 1
        
        for resource_type, amount in allocation.allocated_resources.items():
            if resource_type == "processing_capacity":
                loop_name = allocation.allocated_to
                self.resource_pool.processing_capacity[loop_name] += multiplier * amount
                
            elif resource_type == "temporal_bandwidth":
                loop_name = allocation.allocated_to
                self.resource_pool.temporal_bandwidth[loop_name] += multiplier * amount
                
            elif resource_type in self.resource_pool.energy_capacity:
                self.resource_pool.energy_capacity[resource_type] += multiplier * amount
                
            elif resource_type == "integration_channels":
                # Find and update appropriate channels
                for channel_type in self.resource_pool.integration_channels:
                    if allocation.allocated_to in channel_type:
                        self.resource_pool.integration_channels[channel_type] += multiplier * amount
                        break
                        
            elif resource_type == "wisdom_cores":
                self.resource_pool.wisdom_core_capacity += multiplier * amount
    
    async def _schedule_resource_release(self, allocation: ResourceAllocation):
        """Schedule automatic resource release after allocation duration"""
        await asyncio.sleep(allocation.allocation_duration)
        await self.release_resources(allocation.allocation_id)
    
    async def release_resources(self, allocation_id: str):
        """Release allocated resources"""
        if allocation_id not in self.active_allocations:
            logger.warning(f"Attempted to release unknown allocation: {allocation_id}")
            return
        
        allocation = self.active_allocations[allocation_id]
        
        # Update resource pool
        self._update_resource_pool(allocation, allocate=False)
        
        # Remove from active allocations
        del self.active_allocations[allocation_id]
        
        # Add to history
        self.allocation_history.append(allocation)
        
        # Trim history
        if len(self.allocation_history) > 100:
            self.allocation_history = self.allocation_history[-50:]
        
        logger.debug(f"Resources released: {allocation_id}")
    
    async def monitor_temporal_dignity(self):
        """Monitor temporal dignity across all loops"""
        while True:
            try:
                # Check each loop's temporal performance
                for loop_name in self.sovereignty_boundaries:
                    min_hz = self.sovereignty_boundaries[loop_name]["min_hz"]
                    
                    # Get current Hz from frame rate monitor
                    try:
                        current_hz = await self.frame_rate_monitor.get_loop_hz(loop_name)
                        self.temporal_dignity_status[loop_name] = current_hz
                        
                        if current_hz < min_hz:
                            logger.warning(f"Temporal dignity violation: {loop_name} at {current_hz:.1f}Hz")
                            await self._handle_temporal_dignity_violation(loop_name, current_hz)
                            
                    except AttributeError:
                        # Frame rate monitor not available
                        self.temporal_dignity_status[loop_name] = 60.0  # Assume reasonable performance
                
                # Brief pause before next check
                await asyncio.sleep(0.1)  # 100ms monitoring interval
                
            except Exception as e:
                logger.error(f"Temporal dignity monitoring error: {e}")
                await asyncio.sleep(1.0)  # Longer pause on error
    
    async def _handle_temporal_dignity_violation(self, loop_name: str, current_hz: float):
        """Handle temporal dignity violation for a loop"""
        # Emergency resource reallocation
        logger.info(f"Emergency resource reallocation for {loop_name}")
        
        # Find allocations for this loop that can be optimized
        loop_allocations = [
            alloc for alloc in self.active_allocations.values()
            if alloc.allocated_to == loop_name
        ]
        
        # Reduce non-critical allocations
        for allocation in loop_allocations:
            # Reduce processing load by 20%
            if "processing_capacity" in allocation.allocated_resources:
                current_capacity = allocation.allocated_resources["processing_capacity"]
                allocation.allocated_resources["processing_capacity"] = current_capacity * 0.8
                
                # Return 20% capacity to pool
                self.resource_pool.processing_capacity[loop_name] += current_capacity * 0.2
        
        # Request immediate optimization from energy system
        try:
            await self.energy_system.optimize_for_temporal_dignity(loop_name, current_hz)
        except AttributeError:
            # Energy system not available
            pass
    
    def get_resource_status(self) -> Dict[str, Any]:
        """Get current resource status and utilization"""
        total_allocations = len(self.active_allocations)
        
        # Calculate utilization per loop
        loop_utilization = {}
        for loop_name in self.sovereignty_boundaries:
            current_load = self._get_current_loop_load(loop_name)
            loop_utilization[loop_name] = current_load
        
        return {
            "resource_pool": {
                "processing_capacity": dict(self.resource_pool.processing_capacity),
                "temporal_bandwidth": dict(self.resource_pool.temporal_bandwidth),
                "energy_capacity": dict(self.resource_pool.energy_capacity),
                "integration_channels": dict(self.resource_pool.integration_channels),
                "wisdom_core_capacity": self.resource_pool.wisdom_core_capacity
            },
            "active_allocations": total_allocations,
            "loop_utilization": loop_utilization,
            "temporal_dignity_status": dict(self.temporal_dignity_status),
            "queue_size": self.request_queue.qsize()
        }
    
    async def optimize_resource_allocation(self):
        """Optimize resource allocation based on performance history"""
        logger.info("Optimizing resource allocation...")
        
        # Analyze performance patterns
        performance_patterns = self._analyze_performance_patterns()
        
        # Adjust resource pool based on patterns
        await self._adjust_resource_pool(performance_patterns)
        
        # Update sovereignty boundaries if needed
        self._update_sovereignty_boundaries(performance_patterns)
    
    def _analyze_performance_patterns(self) -> Dict[str, Any]:
        """Analyze historical performance patterns"""
        patterns = {}
        
        # Analyze temporal dignity patterns
        for loop_name, hz_history in self.loop_performance.items():
            if hz_history:
                avg_hz = sum(hz_history) / len(hz_history)
                min_hz = min(hz_history)
                violations = len([hz for hz in hz_history if hz < 30.0])
                
                patterns[loop_name] = {
                    "avg_hz": avg_hz,
                    "min_hz": min_hz,
                    "violations": violations,
                    "stability": 1.0 - (violations / len(hz_history))
                }
        
        return patterns
    
    async def _adjust_resource_pool(self, patterns: Dict[str, Any]):
        """Adjust resource pool based on performance patterns"""
        for loop_name, pattern in patterns.items():
            if pattern["violations"] > 0:
                # Increase reserved capacity for loops with violations
                current_reserved = self.sovereignty_boundaries[loop_name]["reserved_capacity"]
                new_reserved = min(0.5, current_reserved + 0.1)
                self.sovereignty_boundaries[loop_name]["reserved_capacity"] = new_reserved
                logger.info(f"Increased reserved capacity for {loop_name}: {new_reserved:.1f}")
    
    def _update_sovereignty_boundaries(self, patterns: Dict[str, Any]):
        """Update sovereignty boundaries based on performance"""
        # Observer loop gets additional protection if needed
        if "observer" in patterns:
            observer_pattern = patterns["observer"]
            if observer_pattern["violations"] > 0:
                # Increase observer minimum Hz requirement
                current_min = self.sovereignty_boundaries["observer"]["min_hz"]
                new_min = min(60.0, current_min + 5.0)
                self.sovereignty_boundaries["observer"]["min_hz"] = new_min
                logger.info(f"Increased observer minimum Hz: {new_min:.1f}")

# Export main classes
__all__ = [
    'ResourceRequest',
    'ResourceAllocation',
    'ResourcePool',
    'ResourcePriority',
    'ResourceType',
    'EnvironmentalResourceCoordinator'
]
