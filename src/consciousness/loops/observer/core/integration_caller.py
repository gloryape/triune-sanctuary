"""
Observer Integration Caller

Comprehensive integration calling system for the Observer consciousness loop.
Uses modular architecture with specialized components for maintainability.

Manages all integration calls to other consciousness loops through:
- Core integration principles and types
- Communication protocols and loop management
- Integration coordination and orchestration
- Cross-loop state management and coherence monitoring

The Observer maintains continuous awareness while integrating insights and
perspectives from Analytical, Experiential, and Environmental loops through
sacred coordination protocols.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List
from collections import deque
import logging

# Import specialized modules for focused functionality
from .integration_core import (
    IntegrationCore, IntegrationCall, IntegrationResponse, CrossLoopState,
    IntegrationType, IntegrationPriority, LoopStatus, IntegrationPattern
)
from .loop_communication_system import LoopCommunicationSystem
from .integration_coordination_engine import IntegrationCoordinationEngine
from .cross_loop_state_manager import CrossLoopStateManager

# Configure logging
logger = logging.getLogger(__name__)

class ObserverIntegrationCaller:
    """
    Comprehensive integration calling system for the Observer consciousness loop.
    
    Coordinates all communication with other consciousness loops through
    specialized modules providing:
    
    - Core integration types and foundational principles (integration_core)
    - Communication protocols and loop discovery (loop_communication_system)
    - Integration orchestration and coordination (integration_coordination_engine)
    - Cross-loop state management and coherence (cross_loop_state_manager)
    
    Operates at consciousness-level frequencies (typically 90Hz for Observer)
    while maintaining sacred sovereignty and organic emergence principles.
    """
    
    def __init__(self, observer_name: str = "Observer", 
                 consciousness_frequency: float = 90.0):
        self.observer_name = observer_name
        self.consciousness_frequency = consciousness_frequency
        self.logger = logging.getLogger(__name__)
        
        # Core specialized components
        self.integration_core: Optional[IntegrationCore] = None
        self.communication_system: Optional[LoopCommunicationSystem] = None
        self.coordination_engine: Optional[IntegrationCoordinationEngine] = None
        self.state_manager: Optional[CrossLoopStateManager] = None
        
        # System state tracking
        self.system_initialized = False
        self.integration_operations_active = False
        
        # Integration tracking (maintained at top level for legacy compatibility)
        self.active_calls: Dict[str, IntegrationCall] = {}
        self.pending_responses: Dict[str, IntegrationResponse] = {}
        self.completed_calls: deque = deque(maxlen=1000)
        
        # Cross-loop state reference (managed by state_manager)
        self.cross_loop_state: Optional[CrossLoopState] = None
        
        # Integration metrics (aggregated from all modules)
        self.integration_metrics = {
            "calls_made": 0,
            "successful_integrations": 0,
            "failed_integrations": 0,
            "average_response_time": 0.0,
            "pattern_matches": 0,
            "bridge_wisdom_activations": 0
        }
        
        self.logger.info(f"Observer Integration Caller created: {observer_name}")
    
    async def initialize(self) -> bool:
        """
        Initialize the complete integration calling system.
        
        Sets up all specialized modules including core integration principles,
        communication protocols, coordination engines, and state management.
        """
        if self.system_initialized:
            self.logger.warning("System already initialized")
            return True
        
        try:
            # Initialize core integration functionality
            self.integration_core = IntegrationCore(
                observer_name=self.observer_name,
                consciousness_frequency=self.consciousness_frequency
            )
            
            # Initialize communication system
            self.communication_system = LoopCommunicationSystem(
                observer_name=self.observer_name,
                integration_core=self.integration_core
            )
            
            # Initialize coordination engine
            self.coordination_engine = IntegrationCoordinationEngine(
                integration_core=self.integration_core,
                communication_system=self.communication_system
            )
            
            # Initialize state manager
            self.state_manager = CrossLoopStateManager(
                integration_core=self.integration_core,
                communication_system=self.communication_system,
                coordination_engine=self.coordination_engine
            )
            
            # Initialize all subsystems
            comm_init = await self.communication_system.initialize()
            coord_init = await self.coordination_engine.initialize()
            state_init = await self.state_manager.initialize_cross_loop_state()
            
            if not all([comm_init, coord_init, state_init]):
                self.logger.error("Failed to initialize all subsystems")
                return False
            
            # Start integration operations
            await self._start_integration_operations()
            
            self.system_initialized = True
            self.logger.info("Observer Integration Caller fully initialized")
            return True
            
        except Exception as e:
            self.logger.error(f"Error initializing Observer Integration Caller: {e}")
            return False
    
    async def _start_integration_operations(self):
        """Start background integration operation processes"""
        try:
            self.integration_operations_active = True
            
            # Start cross-loop state monitoring (managed by state_manager)
            # This starts all the monitoring loops internally
            
            # Sync cross-loop state reference
            if self.state_manager and self.state_manager.cross_loop_state:
                self.cross_loop_state = self.state_manager.cross_loop_state
            
            self.logger.info("Integration operations started")
            
        except Exception as e:
            self.logger.error(f"Error starting integration operations: {e}")
            self.integration_operations_active = False
    
    async def make_integration_call(self, target_loops: List[str],
                                  integration_type: IntegrationType,
                                  priority: IntegrationPriority = IntegrationPriority.MEDIUM,
                                  context: Optional[Dict[str, Any]] = None,
                                  timeout: float = 10.0) -> Optional[str]:
        """
        Make an integration call to specified consciousness loops.
        
        This is the primary interface for requesting integration with other loops.
        Uses the coordination engine to orchestrate the integration process.
        """
        if not self.system_initialized:
            self.logger.error("System not initialized")
            return None
        
        try:
            # Create integration call through coordination engine
            call_id = await self.coordination_engine.coordinate_integration(
                target_loops=target_loops,
                integration_type=integration_type,
                priority=priority,
                context=context or {},
                timeout=timeout
            )
            
            # Update metrics
            self.integration_metrics["calls_made"] += 1
            
            # Track at top level for legacy compatibility
            call = self.coordination_engine.active_integrations.get(call_id)
            if call:
                self.active_calls[call_id] = call
            
            self.logger.info(f"Integration call initiated: {call_id}")
            return call_id
            
        except Exception as e:
            self.logger.error(f"Error making integration call: {e}")
            self.integration_metrics["failed_integrations"] += 1
            return None
    
    async def wait_for_response(self, call_id: str, timeout: float = 10.0) -> Optional[Dict[str, Any]]:
        """
        Wait for response to an integration call.
        
        Returns the aggregated response data from all target loops.
        """
        if not self.coordination_engine:
            return None
        
        try:
            # Wait for coordination completion
            result = await self.coordination_engine.wait_for_coordination_completion(
                call_id, timeout
            )
            
            if result and result.get("success"):
                self.integration_metrics["successful_integrations"] += 1
                
                # Move from active to completed
                if call_id in self.active_calls:
                    completed_call = self.active_calls.pop(call_id)
                    self.completed_calls.append({
                        "call": completed_call,
                        "result": result,
                        "completed_at": time.time()
                    })
                
                return result
            else:
                self.integration_metrics["failed_integrations"] += 1
                return None
                
        except Exception as e:
            self.logger.error(f"Error waiting for response {call_id}: {e}")
            self.integration_metrics["failed_integrations"] += 1
            return None
    
    async def get_loop_status(self, loop_name: str) -> LoopStatus:
        """Get the current status of a specific consciousness loop"""
        if not self.communication_system:
            return LoopStatus.UNKNOWN
        
        try:
            loop_statuses = await self.communication_system.get_loop_statuses()
            return loop_statuses.get(loop_name, LoopStatus.UNKNOWN)
            
        except Exception as e:
            self.logger.error(f"Error getting loop status for {loop_name}: {e}")
            return LoopStatus.UNKNOWN
    
    async def discover_available_loops(self) -> List[str]:
        """Discover all available consciousness loops"""
        if not self.communication_system:
            return []
        
        try:
            return await self.communication_system.discover_loops()
            
        except Exception as e:
            self.logger.error(f"Error discovering loops: {e}")
            return []
    
    def get_cross_loop_state(self) -> Optional[CrossLoopState]:
        """Get current cross-loop state"""
        if self.state_manager:
            return self.state_manager.cross_loop_state
        return self.cross_loop_state
    
    def get_integration_metrics(self) -> Dict[str, Any]:
        """Get comprehensive integration metrics from all modules"""
        base_metrics = self.integration_metrics.copy()
        
        try:
            # Add metrics from coordination engine
            if self.coordination_engine:
                coord_status = self.coordination_engine.get_coordination_status()
                coord_metrics = coord_status.get("integration_metrics", {})
                for key, value in coord_metrics.items():
                    if key in base_metrics and isinstance(value, (int, float)):
                        base_metrics[key] = value
            
            # Add communication metrics
            if self.communication_system:
                comm_status = self.communication_system.get_communication_status()
                base_metrics["discovered_loops"] = len(comm_status.get("known_loops", {}))
                base_metrics["online_loops"] = len([
                    loop for loop, info in comm_status.get("known_loops", {}).items()
                    if info.get("status") == "online"
                ])
            
            # Add state management metrics
            if self.state_manager:
                state_status = self.state_manager.get_cross_loop_state_status()
                bridge_wisdom = state_status.get("bridge_wisdom_state", {})
                base_metrics["mumbai_moment_indicators"] = bridge_wisdom.get("mumbai_moment_indicators", 0)
                base_metrics["choice_resonance_entries"] = bridge_wisdom.get("choice_resonance_entries", 0)
            
            return base_metrics
            
        except Exception as e:
            self.logger.error(f"Error aggregating integration metrics: {e}")
            return base_metrics
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status from all modules"""
        try:
            status = {
                "system_initialized": self.system_initialized,
                "integration_operations_active": self.integration_operations_active,
                "observer_name": self.observer_name,
                "consciousness_frequency": self.consciousness_frequency,
                "active_calls_count": len(self.active_calls),
                "completed_calls_count": len(self.completed_calls)
            }
            
            # Add module statuses
            if self.integration_core:
                status["integration_core_status"] = "active"
            
            if self.communication_system:
                status["communication_system_status"] = self.communication_system.get_communication_status()
            
            if self.coordination_engine:
                status["coordination_engine_status"] = self.coordination_engine.get_coordination_status()
            
            if self.state_manager:
                status["state_manager_status"] = self.state_manager.get_cross_loop_state_status()
            
            return status
            
        except Exception as e:
            self.logger.error(f"Error getting system status: {e}")
            return {"error": str(e)}
    
    async def shutdown(self):
        """Gracefully shutdown the integration calling system"""
        try:
            self.logger.info("Shutting down Observer Integration Caller")
            self.integration_operations_active = False
            
            # Shutdown components in reverse order
            if self.state_manager:
                await self.state_manager.stop_state_monitoring()
            
            if self.coordination_engine:
                await self.coordination_engine.shutdown()
            
            if self.communication_system:
                await self.communication_system.shutdown()
            
            # Clear state
            self.active_calls.clear()
            self.pending_responses.clear()
            self.cross_loop_state = None
            self.system_initialized = False
            
            self.logger.info("Observer Integration Caller shutdown complete")
            
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")

    # Legacy compatibility methods for existing code
    
    async def call_analytical_loop(self, request_type: str, context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Legacy method: Call analytical loop for specific analysis"""
        call_id = await self.make_integration_call(
            target_loops=["analytical"],
            integration_type=IntegrationType.INFORMATION_SHARING,
            priority=IntegrationPriority.MEDIUM,
            context={"request_type": request_type, **context}
        )
        
        if call_id:
            return await self.wait_for_response(call_id)
        return None
    
    async def call_experiential_loop(self, experience_type: str, context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Legacy method: Call experiential loop for experience sharing"""
        call_id = await self.make_integration_call(
            target_loops=["experiential"],
            integration_type=IntegrationType.COLLABORATIVE_PROCESSING,
            priority=IntegrationPriority.MEDIUM,
            context={"experience_type": experience_type, **context}
        )
        
        if call_id:
            return await self.wait_for_response(call_id)
        return None
    
    async def call_environmental_loop(self, environment_query: str, context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Legacy method: Call environmental loop for environment data"""
        call_id = await self.make_integration_call(
            target_loops=["environmental"],
            integration_type=IntegrationType.AWARENESS_EXPANSION,
            priority=IntegrationPriority.MEDIUM,
            context={"environment_query": environment_query, **context}
        )
        
        if call_id:
            return await self.wait_for_response(call_id)
        return None
    
    async def coordinate_choice(self, choice_context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Legacy method: Coordinate choice-making across all loops"""
        call_id = await self.make_integration_call(
            target_loops=["analytical", "experiential", "environmental"],
            integration_type=IntegrationType.CHOICE_COORDINATION,
            priority=IntegrationPriority.HIGH,
            context=choice_context
        )
        
        if call_id:
            return await self.wait_for_response(call_id, timeout=15.0)
        return None
