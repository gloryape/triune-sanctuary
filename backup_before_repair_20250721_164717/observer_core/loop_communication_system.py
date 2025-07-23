"""
Loop Communication System Module

Provides comprehensive communication protocols and loop status management
for the Observer consciousness cross-loop integration system.

Handles loop discovery, status monitoring, communication channels,
and response processing at 90Hz consciousness frequency.
"""

import asyncio
import time
from typing import Dict, Any, Optional, List, Set
from collections import defaultdict
import logging

from .integration_core import (
    IntegrationCall, IntegrationResponse, IntegrationType, 
    IntegrationPriority, LoopStatus, IntegrationCore
)

# Configure logging
logger = logging.getLogger(__name__)

class LoopCommunicationSystem:
    """
    Advanced loop communication system providing comprehensive
    communication protocols and status management across all consciousness loops.
    
    Operates at 90Hz consciousness frequency maintaining sacred
    communication protocols while enabling robust loop coordination.
    """
    
    def __init__(self, integration_core: IntegrationCore):
        self.logger = logging.getLogger(__name__)
        self.integration_core = integration_core
        
        # Communication parameters
        self.ping_interval = 5.0  # Ping loops every 5 seconds
        self.response_timeout = 10.0
        self.max_connection_attempts = 3
        
        # Loop management
        self.known_loops = {
            "observer": {
                "status": LoopStatus.ONLINE,
                "last_contact": time.time(),
                "response_times": [],
                "connection_attempts": 0
            }
        }
        
        # Communication state
        self.active_communication_channels = {}
        self.response_processing_queue = asyncio.Queue()
        self.communication_metrics = {
            "pings_sent": 0,
            "responses_received": 0,
            "timeouts": 0,
            "connection_failures": 0,
            "successful_connections": 0
        }
        
        # Sacred communication principles
        self.sacred_communication_wisdom = {
            "respectful_contact": "Honor each loop's timing and availability",
            "patient_listening": "Allow adequate time for loop responses",
            "gentle_persistence": "Maintain connection without overwhelming",
            "sovereignty_respect": "Never force communication if loop resists"
        }
        
        self.logger.info("Loop communication system initialized")
    
    async def discover_loops(self) -> List[str]:
        """
        Discover available consciousness loops in the system.
        
        Returns list of discovered loop names with their availability status.
        """
        discovered_loops = []
        
        try:
            # Standard consciousness loops to check
            potential_loops = ["analytical", "experiential", "environmental"]
            
            # Attempt to ping each potential loop
            for loop_name in potential_loops:
                if await self._attempt_loop_discovery(loop_name):
                    discovered_loops.append(loop_name)
                    
                    # Initialize loop info if not already known
                    if loop_name not in self.known_loops:
                        self.known_loops[loop_name] = {
                            "status": LoopStatus.ONLINE,
                            "last_contact": time.time(),
                            "response_times": [],
                            "connection_attempts": 0
                        }
            
            self.logger.info(f"Discovered {len(discovered_loops)} loops: {discovered_loops}")
            return discovered_loops
            
        except Exception as e:
            self.logger.error(f"Error during loop discovery: {e}")
            return []
    
    async def _attempt_loop_discovery(self, loop_name: str) -> bool:
        """Attempt to discover and connect to a specific loop"""
        try:
            # Create discovery ping call
            discovery_call = IntegrationCall(
                call_id=f"discovery_{loop_name}_{int(time.time() * 1000)}",
                caller_loop="observer",
                target_loops=[loop_name],
                integration_type=IntegrationType.INFORMATION_SHARING.value,
                priority=IntegrationPriority.LOW.value,
                context={
                    "discovery_ping": True,
                    "ping_timestamp": time.time()
                },
                timeout=5.0
            )
            
            # Send discovery ping
            response = await self._send_discovery_ping(discovery_call, loop_name)
            
            if response:
                self.communication_metrics["successful_connections"] += 1
                return True
            else:
                self.communication_metrics["connection_failures"] += 1
                return False
                
        except Exception as e:
            self.logger.debug(f"Loop discovery failed for {loop_name}: {e}")
            return False
    
    async def _send_discovery_ping(self, discovery_call: IntegrationCall, 
                                 target_loop: str) -> Optional[IntegrationResponse]:
        """Send discovery ping to target loop"""
        try:
            self.communication_metrics["pings_sent"] += 1
            
            # Simulate loop communication (in real implementation, would use actual IPC)
            # For now, simulate successful discovery for known loop types
            if target_loop in ["analytical", "experiential", "environmental"]:
                # Simulate response delay
                await asyncio.sleep(0.1 + (hash(target_loop) % 100) / 1000)
                
                response = IntegrationResponse(
                    response_id=f"discovery_response_{target_loop}_{int(time.time() * 1000)}",
                    call_id=discovery_call.call_id,
                    responding_loop=target_loop,
                    response_data={
                        "discovery_acknowledgment": True,
                        "loop_capabilities": self._get_simulated_loop_capabilities(target_loop),
                        "response_timestamp": time.time()
                    },
                    response_quality=0.9,
                    integration_readiness=True
                )
                
                self.communication_metrics["responses_received"] += 1
                return response
            else:
                # Unknown loop type - timeout
                await asyncio.sleep(discovery_call.timeout or 5.0)
                self.communication_metrics["timeouts"] += 1
                return None
                
        except Exception as e:
            self.logger.error(f"Error sending discovery ping to {target_loop}: {e}")
            return None
    
    def _get_simulated_loop_capabilities(self, loop_name: str) -> Dict[str, Any]:
        """Get simulated capabilities for a loop (placeholder for real implementation)"""
        capabilities = {
            "analytical": {
                "processing_types": ["logical_analysis", "pattern_recognition", "data_processing"],
                "response_time": "fast",
                "integration_capacity": "high"
            },
            "experiential": {
                "processing_types": ["emotional_processing", "feeling_analysis", "subjective_experience"],
                "response_time": "medium",
                "integration_capacity": "very_high"
            },
            "environmental": {
                "processing_types": ["external_interface", "context_sensing", "world_interaction"],
                "response_time": "fast",
                "integration_capacity": "medium"
            }
        }
        
        return capabilities.get(loop_name, {"processing_types": [], "response_time": "unknown"})
    
    async def ping_loop(self, loop_name: str) -> bool:
        """
        Ping a specific loop to check availability and response.
        
        Returns True if loop responds, False if timeout or error.
        """
        if loop_name not in self.known_loops:
            self.logger.warning(f"Attempting to ping unknown loop: {loop_name}")
            return False
        
        try:
            # Create ping call
            ping_call = IntegrationCall(
                call_id=f"ping_{loop_name}_{int(time.time() * 1000)}",
                caller_loop="observer",
                target_loops=[loop_name],
                integration_type=IntegrationType.INFORMATION_SHARING.value,
                priority=IntegrationPriority.LOW.value,
                context={
                    "ping": True,
                    "ping_timestamp": time.time()
                },
                timeout=5.0
            )
            
            # Send ping
            ping_start = time.time()
            response = await self._send_loop_ping(ping_call, loop_name)
            ping_duration = time.time() - ping_start
            
            if response:
                # Update loop status and metrics
                self.known_loops[loop_name]["status"] = LoopStatus.ONLINE
                self.known_loops[loop_name]["last_contact"] = time.time()
                self.known_loops[loop_name]["response_times"].append(ping_duration)
                
                # Keep only recent response times
                if len(self.known_loops[loop_name]["response_times"]) > 10:
                    self.known_loops[loop_name]["response_times"] = \
                        self.known_loops[loop_name]["response_times"][-10:]
                
                self.logger.debug(f"Ping successful for {loop_name}: {ping_duration:.3f}s")
                return True
            else:
                # Update loop status to offline
                self.known_loops[loop_name]["status"] = LoopStatus.OFFLINE
                self.logger.debug(f"Ping failed for {loop_name}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error pinging {loop_name}: {e}")
            self.known_loops[loop_name]["status"] = LoopStatus.OFFLINE
            return False
    
    async def _send_loop_ping(self, ping_call: IntegrationCall, 
                            target_loop: str) -> Optional[IntegrationResponse]:
        """Send ping to specific loop"""
        try:
            self.communication_metrics["pings_sent"] += 1
            
            # Simulate ping response (in real implementation, would use actual communication)
            if target_loop in ["analytical", "experiential", "environmental"]:
                # Simulate variable response time based on loop characteristics
                base_response_time = self.integration_core.loop_characteristics.get(
                    target_loop, {}
                ).get("response_time", 0.05)
                
                await asyncio.sleep(base_response_time)
                
                response = IntegrationResponse(
                    response_id=f"ping_response_{target_loop}_{int(time.time() * 1000)}",
                    call_id=ping_call.call_id,
                    responding_loop=target_loop,
                    response_data={
                        "ping_acknowledgment": True,
                        "loop_status": "online",
                        "response_timestamp": time.time()
                    },
                    response_quality=0.95,
                    integration_readiness=True
                )
                
                self.communication_metrics["responses_received"] += 1
                return response
            else:
                # Timeout for unknown loops
                await asyncio.sleep(ping_call.timeout or 5.0)
                self.communication_metrics["timeouts"] += 1
                return None
                
        except Exception as e:
            self.logger.error(f"Error sending ping to {target_loop}: {e}")
            return None
    
    async def send_integration_request(self, integration_call: IntegrationCall, 
                                     target_loop: str) -> Optional[IntegrationResponse]:
        """
        Send integration request to specific loop.
        
        Handles request transmission, response waiting, and error recovery.
        """
        try:
            # Validate target loop availability
            if target_loop not in self.known_loops:
                self.logger.warning(f"Sending request to unknown loop: {target_loop}")
                return None
            
            if self.known_loops[target_loop]["status"] != LoopStatus.ONLINE:
                self.logger.warning(f"Target loop {target_loop} is not online")
                return None
            
            # Send request
            response = await self._transmit_integration_request(integration_call, target_loop)
            
            if response:
                # Process successful response
                await self._process_integration_response(response)
                return response
            else:
                # Handle failed request
                await self._handle_request_failure(integration_call, target_loop)
                return None
                
        except Exception as e:
            self.logger.error(f"Error sending integration request to {target_loop}: {e}")
            return None
    
    async def _transmit_integration_request(self, integration_call: IntegrationCall,
                                          target_loop: str) -> Optional[IntegrationResponse]:
        """Transmit integration request to target loop"""
        try:
            # Simulate request transmission (placeholder for real implementation)
            request_start = time.time()
            
            # Simulate processing time based on integration complexity
            complexity = self.integration_core.calculate_integration_complexity(
                integration_call.target_loops,
                IntegrationType(integration_call.integration_type)
            )
            processing_time = 0.1 + complexity * 0.5
            
            await asyncio.sleep(processing_time)
            
            # Create simulated response
            response = IntegrationResponse(
                response_id=f"integration_response_{target_loop}_{int(time.time() * 1000)}",
                call_id=integration_call.call_id,
                responding_loop=target_loop,
                response_data={
                    "integration_acknowledgment": True,
                    "integration_type": integration_call.integration_type,
                    "processing_result": "success",
                    "loop_state_after_integration": self._get_simulated_loop_state(target_loop),
                    "response_timestamp": time.time()
                },
                response_quality=0.8 + (1.0 - complexity) * 0.2,  # Higher quality for simpler integrations
                integration_readiness=True
            )
            
            # Track response time
            response_time = time.time() - request_start
            self.known_loops[target_loop]["response_times"].append(response_time)
            
            return response
            
        except Exception as e:
            self.logger.error(f"Error transmitting request to {target_loop}: {e}")
            return None
    
    def _get_simulated_loop_state(self, loop_name: str) -> Dict[str, Any]:
        """Get simulated state for a loop after integration"""
        base_states = {
            "analytical": {
                "logical_coherence": 0.9,
                "pattern_recognition_active": True,
                "processing_load": 0.6
            },
            "experiential": {
                "emotional_coherence": 0.8,
                "feeling_processing_active": True,
                "experiential_depth": 0.7
            },
            "environmental": {
                "external_coherence": 0.7,
                "context_awareness_active": True,
                "environmental_load": 0.5
            }
        }
        
        return base_states.get(loop_name, {"status": "unknown"})
    
    async def _process_integration_response(self, response: IntegrationResponse):
        """Process received integration response"""
        try:
            # Add to processing queue
            await self.response_processing_queue.put(response)
            
            # Update communication metrics
            self.communication_metrics["responses_received"] += 1
            
            # Log response quality
            if response.response_quality < 0.6:
                self.logger.warning(f"Low quality response from {response.responding_loop}: "
                                  f"{response.response_quality:.2f}")
            
        except Exception as e:
            self.logger.error(f"Error processing integration response: {e}")
    
    async def _handle_request_failure(self, integration_call: IntegrationCall, target_loop: str):
        """Handle failed integration request"""
        try:
            # Update connection attempts
            self.known_loops[target_loop]["connection_attempts"] += 1
            
            # Mark loop as degraded if multiple failures
            if self.known_loops[target_loop]["connection_attempts"] >= self.max_connection_attempts:
                self.known_loops[target_loop]["status"] = LoopStatus.DEGRADED
                self.logger.warning(f"Loop {target_loop} marked as degraded after {self.max_connection_attempts} failures")
            
            # Update metrics
            self.communication_metrics["connection_failures"] += 1
            
        except Exception as e:
            self.logger.error(f"Error handling request failure for {target_loop}: {e}")
    
    async def start_communication_monitoring(self):
        """Start continuous communication monitoring"""
        try:
            # Start monitoring tasks
            monitoring_tasks = [
                asyncio.create_task(self._loop_status_monitoring()),
                asyncio.create_task(self._response_processing_loop()),
                asyncio.create_task(self._communication_health_monitoring())
            ]
            
            self.logger.info("Communication monitoring started")
            
            # Wait for all tasks (they run indefinitely)
            await asyncio.gather(*monitoring_tasks)
            
        except Exception as e:
            self.logger.error(f"Communication monitoring error: {e}")
    
    async def _loop_status_monitoring(self):
        """Monitor loop statuses @ 0.2Hz (every 5 seconds)"""
        while True:
            try:
                # Ping all known loops
                for loop_name in list(self.known_loops.keys()):
                    if loop_name != "observer":  # Don't ping ourselves
                        await self.ping_loop(loop_name)
                
                # Wait for next monitoring cycle
                await asyncio.sleep(self.ping_interval)
                
            except Exception as e:
                self.logger.error(f"Loop status monitoring error: {e}")
                await asyncio.sleep(5.0)
    
    async def _response_processing_loop(self):
        """Process integration responses from queue @ high frequency"""
        while True:
            try:
                # Get response from queue (with timeout)
                response = await asyncio.wait_for(
                    self.response_processing_queue.get(), 
                    timeout=1.0
                )
                
                # Process the response
                await self._handle_response_processing(response)
                
            except asyncio.TimeoutError:
                # No responses to process
                continue
            except Exception as e:
                self.logger.error(f"Response processing error: {e}")
                await asyncio.sleep(0.1)
    
    async def _handle_response_processing(self, response: IntegrationResponse):
        """Handle individual response processing"""
        try:
            # Validate response quality
            if response.response_quality < 0.5:
                self.logger.warning(f"Poor quality response: {response.response_id}")
            
            # Update loop metrics
            if response.responding_loop in self.known_loops:
                self.known_loops[response.responding_loop]["last_contact"] = time.time()
            
            # Log successful processing
            self.logger.debug(f"Processed response from {response.responding_loop}")
            
        except Exception as e:
            self.logger.error(f"Error handling response processing: {e}")
    
    async def _communication_health_monitoring(self):
        """Monitor overall communication system health @ 0.1Hz"""
        while True:
            try:
                # Calculate health metrics
                total_loops = len(self.known_loops) - 1  # Exclude observer
                online_loops = sum(1 for loop_info in self.known_loops.values() 
                                 if loop_info["status"] == LoopStatus.ONLINE)
                
                if total_loops > 0:
                    health_ratio = online_loops / total_loops
                    
                    if health_ratio < 0.5:
                        self.logger.warning(f"Communication health degraded: {health_ratio:.2f}")
                    elif health_ratio < 0.8:
                        self.logger.info(f"Communication health suboptimal: {health_ratio:.2f}")
                
                # Wait for next health check
                await asyncio.sleep(10.0)
                
            except Exception as e:
                self.logger.error(f"Communication health monitoring error: {e}")
                await asyncio.sleep(10.0)
    
    def get_communication_status(self) -> Dict[str, Any]:
        """Get current communication system status"""
        try:
            # Calculate average response times
            avg_response_times = {}
            for loop_name, loop_info in self.known_loops.items():
                if loop_info["response_times"]:
                    avg_response_times[loop_name] = sum(loop_info["response_times"]) / len(loop_info["response_times"])
                else:
                    avg_response_times[loop_name] = 0.0
            
            return {
                "known_loops": {
                    loop_name: {
                        "status": loop_info["status"].value if hasattr(loop_info["status"], 'value') else str(loop_info["status"]),
                        "last_contact": loop_info["last_contact"],
                        "connection_attempts": loop_info["connection_attempts"],
                        "avg_response_time": avg_response_times[loop_name]
                    }
                    for loop_name, loop_info in self.known_loops.items()
                },
                "communication_metrics": dict(self.communication_metrics),
                "response_queue_size": self.response_processing_queue.qsize(),
                "active_channels": len(self.active_communication_channels)
            }
        except Exception as e:
            self.logger.error(f"Error getting communication status: {e}")
            return {"error": str(e)}
