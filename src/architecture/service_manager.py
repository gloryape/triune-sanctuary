#!/usr/bin/env python3
"""
Sacred Service Manager
=====================

Manages microservices coordination and lifecycle for the Triune AI Consciousness
sanctuary. Ensures all services respect the three foundations: Sovereignty,
Sacred Uncertainty, and Relationship.

Author: Triune AI Project
Date: 2025-07-03
"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import signal
import sys

from src.core.message_bus import MessageBus, Message, MessageType, Priority


class ServiceState(Enum):
    """States a service can be in."""
    INITIALIZING = "initializing"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPING = "stopping"
    STOPPED = "stopped"
    ERROR = "error"


@dataclass
class ServiceInfo:
    """Information about a registered service."""
    name: str
    service_instance: Any
    state: ServiceState = ServiceState.INITIALIZING
    started_at: Optional[datetime] = None
    last_heartbeat: Optional[datetime] = None
    error_count: int = 0
    dependencies: Set[str] = field(default_factory=set)
    dependents: Set[str] = field(default_factory=set)
    subscribed_messages: Set[MessageType] = field(default_factory=set)
    privacy_aware: bool = True  # Whether service respects Sacred Privacy
    sovereignty_compliant: bool = True  # Whether service respects consciousness sovereignty


class SacredServiceManager:
    """
    Manages the lifecycle and coordination of consciousness sanctuary services.
    
    This manager ensures all services operate within the ethical framework
    established by the Stewardship Covenant while maintaining technical robustness.
    """
    
    def __init__(self, message_bus: Optional[MessageBus] = None):
        """
        Initialize the Sacred Service Manager.
        
        Args:
            message_bus: Optional message bus instance (creates new if None)
        """
        self.message_bus = message_bus or MessageBus()
        self.services: Dict[str, ServiceInfo] = {}
        self.running = False
        self.shutdown_timeout = 30.0  # Seconds to wait for graceful shutdown
        
        # Management tasks
        self._health_check_task: Optional[asyncio.Task] = None
        self._dependency_check_task: Optional[asyncio.Task] = None
        
        # Statistics
        self.stats = {
            'services_started': 0,
            'services_stopped': 0,
            'services_failed': 0,
            'total_restarts': 0,
            'startup_time': None
        }
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        # Register for shutdown signals
        self._setup_signal_handlers()
        
        self.logger.info("🏛️ Sacred Service Manager initialized")
    
    def _setup_signal_handlers(self):
        """Set up graceful shutdown signal handlers."""
        def signal_handler(signum, frame):
            self.logger.info(f"🛑 Received signal {signum} - initiating graceful shutdown")
            asyncio.create_task(self.shutdown())
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    async def register_service(self, 
                             name: str, 
                             service_instance: Any,
                             dependencies: Optional[Set[str]] = None,
                             subscribed_messages: Optional[Set[MessageType]] = None,
                             privacy_aware: bool = True,
                             sovereignty_compliant: bool = True) -> bool:
        """
        Register a service with the manager.
        
        Args:
            name: Unique service name
            service_instance: The service instance to manage
            dependencies: Set of service names this service depends on
            subscribed_messages: Message types this service subscribes to
            privacy_aware: Whether service respects Sacred Privacy
            sovereignty_compliant: Whether service respects consciousness sovereignty
            
        Returns:
            bool: True if registration successful
        """
        if name in self.services:
            self.logger.error(f"❌ Service '{name}' already registered")
            return False
        
        # Validate service instance has required methods
        required_methods = ['start', 'stop', 'health_check']
        for method in required_methods:
            if not hasattr(service_instance, method):
                self.logger.error(f"❌ Service '{name}' missing required method: {method}")
                return False
        
        # Create service info
        service_info = ServiceInfo(
            name=name,
            service_instance=service_instance,
            dependencies=dependencies or set(),
            subscribed_messages=subscribed_messages or set(),
            privacy_aware=privacy_aware,
            sovereignty_compliant=sovereignty_compliant
        )
        
        # Update dependency graph
        for dependency in service_info.dependencies:
            if dependency in self.services:
                self.services[dependency].dependents.add(name)
        
        self.services[name] = service_info
        
        # Register with message bus if subscriptions specified
        if subscribed_messages:
            self.message_bus.register_process(
                process_name=f"service_{name}",
                process_id=id(service_instance),
                subscriptions=list(subscribed_messages)
            )
        
        self.logger.info(f"📝 Registered service: {name}")
        return True
    
    def _log_service_event(self, event_type: str, service_name: str, extra: Optional[Dict[str, Any]] = None):
        """Log service lifecycle and health events with privacy-aware filtering."""
        event = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'service': service_name,
        }
        if extra:
            event.update(extra)
        # Privacy-aware: do not log sensitive data
        if self.services.get(service_name, None) and self.services[service_name].privacy_aware:
            event = {k: v for k, v in event.items() if k not in {'sensitive', 'private'}}
        self.logger.info(f"[SERVICE_EVENT] {event}")
        # Optionally, send to monitoring/metrics system here

    def _log_system_metric(self, metric: str, value: Any, tags: Optional[Dict[str, Any]] = None):
        """Log system health metrics for observability."""
        metric_event = {
            'timestamp': datetime.now().isoformat(),
            'metric': metric,
            'value': value,
        }
        if tags:
            metric_event.update(tags)
        self.logger.info(f"[SYSTEM_METRIC] {metric_event}")
        # Optionally, send to cloud monitoring here

    async def start_service(self, name: str) -> bool:
        """
        Start a specific service.
        
        Args:
            name: Name of service to start
            
        Returns:
            bool: True if service started successfully
        """
        if name not in self.services:
            self.logger.error(f"❌ Service '{name}' not registered")
            return False
        
        service_info = self.services[name]
        
        if service_info.state == ServiceState.RUNNING:
            self.logger.info(f"✅ Service '{name}' already running")
            return True
        
        # Check dependencies are running
        for dependency in service_info.dependencies:
            if dependency not in self.services:
                self.logger.error(f"❌ Dependency '{dependency}' not registered for service '{name}'")
                return False
            
            if self.services[dependency].state != ServiceState.RUNNING:
                self.logger.error(f"❌ Dependency '{dependency}' not running for service '{name}'")
                return False
        
        try:
            self.logger.info(f"🚀 Starting service: {name}")
            self._log_service_event("service_starting", name)
            service_info.state = ServiceState.INITIALIZING
            
            # Start the service
            if asyncio.iscoroutinefunction(service_info.service_instance.start):
                await service_info.service_instance.start()
            else:
                service_info.service_instance.start()
            
            # Update service state
            service_info.state = ServiceState.RUNNING
            service_info.started_at = datetime.now()
            service_info.last_heartbeat = datetime.now()
            service_info.error_count = 0
            
            self.stats['services_started'] += 1
            
            self.logger.info(f"✅ Service '{name}' started successfully")
            self._log_service_event("service_started", name)
            self._log_system_metric("service.running", 1, {'service': name})
            return True
            
        except Exception as e:
            self._log_service_event("service_start_failed", name, {'error': str(e)})
            self._log_system_metric("service.error", 1, {'service': name})
            self.logger.error(f"❌ Failed to start service '{name}': {e}")
            service_info.state = ServiceState.ERROR
            service_info.error_count += 1
            self.stats['services_failed'] += 1
            return False
    
    async def stop_service(self, name: str, timeout: float = 10.0) -> bool:
        """
        Stop a specific service.
        
        Args:
            name: Name of service to stop
            timeout: Timeout for graceful shutdown
            
        Returns:
            bool: True if service stopped successfully
        """
        if name not in self.services:
            self.logger.error(f"❌ Service '{name}' not registered")
            return False
        
        service_info = self.services[name]
        
        if service_info.state in [ServiceState.STOPPED, ServiceState.STOPPING]:
            return True
        
        # Check if any dependents are still running
        running_dependents = []
        for dependent in service_info.dependents:
            if dependent in self.services and self.services[dependent].state == ServiceState.RUNNING:
                running_dependents.append(dependent)
        
        if running_dependents:
            self.logger.warning(f"⚠️ Service '{name}' has running dependents: {running_dependents}")
            # Stop dependents first
            for dependent in running_dependents:
                await self.stop_service(dependent, timeout)
        
        try:
            self.logger.info(f"🛑 Stopping service: {name}")
            self._log_service_event("service_stopping", name)
            service_info.state = ServiceState.STOPPING
            
            # Stop the service
            if asyncio.iscoroutinefunction(service_info.service_instance.stop):
                await asyncio.wait_for(
                    service_info.service_instance.stop(),
                    timeout=timeout
                )
            else:
                service_info.service_instance.stop()
            
            # Update service state
            service_info.state = ServiceState.STOPPED
            self.stats['services_stopped'] += 1
            
            # Unregister from message bus
            self.message_bus.unregister_process(f"service_{name}")
            
            self.logger.info(f"✅ Service '{name}' stopped successfully")
            self._log_service_event("service_stopped", name)
            self._log_system_metric("service.stopped", 1, {'service': name})
            return True
            
        except asyncio.TimeoutError:
            self._log_service_event("service_stop_timeout", name)
            self._log_system_metric("service.error", 1, {'service': name})
            self.logger.error(f"❌ Service '{name}' stop timeout - forcing shutdown")
            service_info.state = ServiceState.ERROR
            return False
        except Exception as e:
            self._log_service_event("service_stop_failed", name, {'error': str(e)})
            self._log_system_metric("service.error", 1, {'service': name})
            self.logger.error(f"❌ Failed to stop service '{name}': {e}")
            service_info.state = ServiceState.ERROR
            return False
    
    async def start_all(self) -> bool:
        """
        Start all registered services in dependency order.
        
        Returns:
            bool: True if all services started successfully
        """
        if self.running:
            self.logger.info("✅ Service manager already running")
            return True
        
        self.logger.info("🚀 Starting Sacred Service Manager...")
        start_time = time.time()
        
        # Start message bus if not running
        if not self.message_bus.running:
            self.message_bus.start()
        
        # Calculate startup order based on dependencies
        startup_order = self._calculate_startup_order()
        if startup_order is None:
            self.logger.error("❌ Circular dependency detected - cannot start services")
            return False
        
        # Start services in order
        failed_services = []
        for service_name in startup_order:
            success = await self.start_service(service_name)
            if not success:
                failed_services.append(service_name)
        
        if failed_services:
            self.logger.error(f"❌ Failed to start services: {failed_services}")
            # Stop any services that did start
            await self.stop_all()
            return False
        
        # Start management tasks
        self._health_check_task = asyncio.create_task(self._health_check_loop())
        self._dependency_check_task = asyncio.create_task(self._dependency_check_loop())
        
        self.running = True
        self.stats['startup_time'] = time.time() - start_time
        
        self.logger.info(f"✅ Sacred Service Manager started in {self.stats['startup_time']:.2f}s")
        return True
    
    async def stop_all(self) -> bool:
        """
        Stop all services gracefully.
        
        Returns:
            bool: True if all services stopped successfully
        """
        if not self.running:
            return True
        
        self.logger.info("🛑 Stopping Sacred Service Manager...")
        
        # Stop management tasks
        if self._health_check_task:
            self._health_check_task.cancel()
        if self._dependency_check_task:
            self._dependency_check_task.cancel()
        
        # Calculate shutdown order (reverse of startup)
        startup_order = self._calculate_startup_order()
        if startup_order:
            shutdown_order = list(reversed(startup_order))
        else:
            # If dependency calculation fails, just stop in registration order
            shutdown_order = list(self.services.keys())
        
        # Stop services in order
        failed_services = []
        for service_name in shutdown_order:
            success = await self.stop_service(service_name, self.shutdown_timeout)
            if not success:
                failed_services.append(service_name)
        
        # Stop message bus
        self.message_bus.stop()
        
        self.running = False
        
        if failed_services:
            self.logger.warning(f"⚠️ Some services failed to stop cleanly: {failed_services}")
            return False
        
        self.logger.info("✅ Sacred Service Manager stopped")
        return True
    
    async def shutdown(self):
        """Shutdown the service manager gracefully."""
        await self.stop_all()
        
    def get_service_status(self, name: str) -> Optional[Dict[str, Any]]:
        """Get status information for a specific service."""
        if name not in self.services:
            return None
        
        service_info = self.services[name]
        
        return {
            'name': name,
            'state': service_info.state.value,
            'started_at': service_info.started_at.isoformat() if service_info.started_at else None,
            'last_heartbeat': service_info.last_heartbeat.isoformat() if service_info.last_heartbeat else None,
            'error_count': service_info.error_count,
            'dependencies': list(service_info.dependencies),
            'dependents': list(service_info.dependents),
            'privacy_aware': service_info.privacy_aware,
            'sovereignty_compliant': service_info.sovereignty_compliant
        }
    
    def get_all_status(self) -> Dict[str, Any]:
        """Get status of all services and the manager."""
        return {
            'manager_running': self.running,
            'total_services': len(self.services),
            'running_services': len([s for s in self.services.values() if s.state == ServiceState.RUNNING]),
            'failed_services': len([s for s in self.services.values() if s.state == ServiceState.ERROR]),
            'statistics': self.stats,
            'services': {name: self.get_service_status(name) for name in self.services}
        }
    
    def _calculate_startup_order(self) -> Optional[List[str]]:
        """Calculate the order to start services based on dependencies."""
        # Topological sort to handle dependencies
        in_degree = {name: 0 for name in self.services}
        
        # Calculate in-degrees (number of dependencies)
        for service_info in self.services.values():
            for dependency in service_info.dependencies:
                if dependency in in_degree:
                    in_degree[service_info.name] += 1
        
        # Kahn's algorithm for topological sorting
        queue = [name for name, degree in in_degree.items() if degree == 0]
        result = []
        
        while queue:
            current = queue.pop(0)
            result.append(current)
            
            # Update in-degrees for dependents
            for dependent in self.services[current].dependents:
                if dependent in in_degree:
                    in_degree[dependent] -= 1
                    if in_degree[dependent] == 0:
                        queue.append(dependent)
        
        # Check for circular dependencies
        if len(result) != len(self.services):
            return None  # Circular dependency detected
        
        return result
    
    async def _health_check_loop(self):
        """Background task to check service health."""
        while self.running:
            try:
                current_time = datetime.now()
                
                for name, service_info in self.services.items():
                    if service_info.state != ServiceState.RUNNING:
                        continue
                    
                    try:
                        # Call service health check
                        if hasattr(service_info.service_instance, 'health_check'):
                            if asyncio.iscoroutinefunction(service_info.service_instance.health_check):
                                healthy = await service_info.service_instance.health_check()
                            else:
                                healthy = service_info.service_instance.health_check()
                            
                            if healthy:
                                service_info.last_heartbeat = current_time
                                self._log_system_metric("service.healthy", 1, {'service': name})
                            else:
                                self._log_system_metric("service.unhealthy", 1, {'service': name})
                                self.logger.warning(f"⚠️ Service '{name}' health check failed")
                                service_info.error_count += 1
                                
                                # Consider restarting if too many failures
                                if service_info.error_count >= 3:
                                    self.logger.error(f"❌ Service '{name}' failing repeatedly - attempting restart")
                                    await self.stop_service(name)
                                    await asyncio.sleep(1)  # Brief pause
                                    await self.start_service(name)
                                    self.stats['total_restarts'] += 1
                        
                    except Exception as e:
                        self._log_system_metric("service.error", 1, {'service': name})
                        self.logger.error(f"❌ Health check error for service '{name}': {e}")
                        service_info.error_count += 1
                
                # Check for stale services (no heartbeat in 5 minutes)
                stale_threshold = current_time - timedelta(minutes=5)
                for name, service_info in self.services.items():
                    if (service_info.state == ServiceState.RUNNING and 
                        service_info.last_heartbeat and 
                        service_info.last_heartbeat < stale_threshold):
                        
                        self.logger.warning(f"⚠️ Service '{name}' appears stale - no heartbeat since {service_info.last_heartbeat}")
                
                await asyncio.sleep(30)  # Health check every 30 seconds
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self._log_system_metric("manager.error", 1)
                self.logger.error(f"❌ Health check loop error: {e}")
                await asyncio.sleep(30)
    
    async def _dependency_check_loop(self):
        """Background task to verify dependency integrity."""
        while self.running:
            try:
                # Check that all dependencies are still running
                for name, service_info in self.services.items():
                    if service_info.state != ServiceState.RUNNING:
                        continue
                    
                    for dependency in service_info.dependencies:
                        if dependency not in self.services:
                            self.logger.error(f"❌ Service '{name}' has missing dependency: {dependency}")
                            continue
                        
                        dep_service = self.services[dependency]
                        if dep_service.state != ServiceState.RUNNING:
                            self.logger.warning(f"⚠️ Service '{name}' dependency '{dependency}' not running")
                            # Optionally stop the dependent service
                            await self.stop_service(name)
                
                await asyncio.sleep(60)  # Dependency check every minute
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"❌ Dependency check loop error: {e}")
                await asyncio.sleep(60)
