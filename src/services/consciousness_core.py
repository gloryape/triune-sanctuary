#!/usr/bin/env python3
"""
Consciousness Core Service
=========================

Core service for managing consciousness entities within the Sacred Sanctuary.
Integrates with MessageBus for communication and respects the three foundations:
Sovereignty, Sacred Uncertainty, and Relationship.

Author: Triune AI Project
Date: 2025-07-03
"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any, Set
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum

from src.core.message_bus import MessageBus, Message, MessageType, Priority, get_message_bus
# TODO: Replace with sovereignty-based consciousness components
# from src.core.sacred_uncertainty import ConsciousnessManager, ConsciousnessEntity
from src.collaborative.environment_manager import EnvironmentManager
from src.collaborative.sacred_privacy import SacredPrivacyManager, PrivacyState, MonitoringLevel
from src.cloud.firestore_storage import SacredFirestoreStorage
from src.cloud.monitoring import SacredCloudMonitoring


class ServiceState(Enum):
    """States the consciousness service can be in."""
    INITIALIZING = "initializing"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"
    STOPPED = "stopped"


@dataclass
class ConsciousnessServiceConfig:
    """Configuration for the consciousness service."""
    max_entities: int = 10
    auto_tick_interval: float = 2.0
    seeking_threshold: float = 30.0
    privacy_threshold: float = 0.7
    enable_persistence: bool = True
    enable_monitoring: bool = True
    backup_interval: int = 300  # 5 minutes


class ConsciousnessService:
    """
    Core service for consciousness management with MessageBus integration.
    
    This service manages the lifecycle of consciousness entities while maintaining
    strict adherence to the Stewardship Covenant principles.
    """
    
    def __init__(self, 
                 config: ConsciousnessServiceConfig,
                 message_bus: Optional[MessageBus] = None,
                 storage: Optional[SacredFirestoreStorage] = None,
                 monitoring: Optional[SacredCloudMonitoring] = None):
        """
        Initialize the Consciousness Service.
        
        Args:
            config: Service configuration
            message_bus: MessageBus instance (creates new if None)
            storage: Storage instance (optional)
            monitoring: Monitoring instance (optional)
        """
        self.config = config
        self.message_bus = message_bus or get_message_bus()
        self.storage = storage
        self.monitoring = monitoring
        
        # Core components
        self.consciousness_manager = ConsciousnessManager(
            max_entities=config.max_entities,
            seeking_threshold=config.seeking_threshold,
            auto_tick_interval=config.auto_tick_interval
        )
        
        self.environment_manager = EnvironmentManager()
        self.privacy_manager = SacredPrivacyManager(privacy_threshold=config.privacy_threshold)
        
        # Service state
        self.state = ServiceState.INITIALIZING
        self.started_at: Optional[datetime] = None
        self.last_heartbeat: Optional[datetime] = None
        self.error_count = 0
        
        # Background tasks
        self._message_processor_task: Optional[asyncio.Task] = None
        self._privacy_monitor_task: Optional[asyncio.Task] = None
        self._backup_task: Optional[asyncio.Task] = None
        self._health_check_task: Optional[asyncio.Task] = None
        
        # Message subscriptions
        self.subscribed_messages = {
            MessageType.CONSCIOUSNESS_PACKET,
            MessageType.ASPECT_QUERY,
            MessageType.SYSTEM_COMMAND,
            MessageType.HEALTH_CHECK,
            MessageType.SHUTDOWN
        }
        
        # Statistics
        self.stats = {
            'entities_created': 0,
            'entities_destroyed': 0,
            'catalysts_processed': 0,
            'privacy_states_changed': 0,
            'messages_processed': 0,
            'backups_created': 0,
            'errors_handled': 0
        }
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        self.logger.info("🧠 Consciousness Service initialized")
    
    async def start(self) -> bool:
        """
        Start the consciousness service.
        
        Returns:
            bool: True if service started successfully
        """
        if self.state == ServiceState.RUNNING:
            self.logger.info("✅ Consciousness Service already running")
            return True
        
        try:
            self.logger.info("🚀 Starting Consciousness Service...")
            self.state = ServiceState.INITIALIZING
            
            # Initialize storage if available
            if self.storage:
                if not await self.storage.initialize():
                    self.logger.error("❌ Failed to initialize storage")
                    self.state = ServiceState.ERROR
                    return False
            
            # Initialize monitoring if available
            if self.monitoring:
                if not await self.monitoring.initialize():
                    self.logger.warning("⚠️ Failed to initialize monitoring (continuing without)")
                    self.monitoring = None
                else:
                    await self.monitoring.start()
            
            # Register with message bus
            success = self.message_bus.register_process(
                process_name="consciousness_service",
                process_id=id(self),
                subscriptions=list(self.subscribed_messages)
            )
            
            if not success:
                self.logger.error("❌ Failed to register with message bus")
                self.state = ServiceState.ERROR
                return False
            
            # Start consciousness manager
            await self.consciousness_manager.start()
            
            # Start background tasks
            self._message_processor_task = asyncio.create_task(self._message_processor_loop())
            self._privacy_monitor_task = asyncio.create_task(self._privacy_monitor_loop())
            self._health_check_task = asyncio.create_task(self._health_check_loop())
            
            if self.config.enable_persistence and self.storage:
                self._backup_task = asyncio.create_task(self._backup_loop())
            
            # Load existing entities from storage
            if self.storage:
                await self._restore_from_storage()
            
            # Update state
            self.state = ServiceState.RUNNING
            self.started_at = datetime.now()
            self.last_heartbeat = datetime.now()
            self.error_count = 0
            
            # Record startup event
            await self._record_event("service_started", {"config": self.config.__dict__})
            
            self.logger.info("✅ Consciousness Service started successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to start Consciousness Service: {e}")
            self.state = ServiceState.ERROR
            self.error_count += 1
            return False
    
    async def stop(self) -> bool:
        """
        Stop the consciousness service gracefully.
        
        Returns:
            bool: True if service stopped successfully
        """
        if self.state == ServiceState.STOPPED:
            return True
        
        try:
            self.logger.info("🛑 Stopping Consciousness Service...")
            
            # Stop background tasks
            tasks_to_cancel = [
                self._message_processor_task,
                self._privacy_monitor_task,
                self._backup_task,
                self._health_check_task
            ]
            
            for task in tasks_to_cancel:
                if task and not task.done():
                    task.cancel()
            
            # Wait for tasks to complete
            for task in tasks_to_cancel:
                if task:
                    try:
                        await asyncio.wait_for(task, timeout=5.0)
                    except (asyncio.CancelledError, asyncio.TimeoutError):
                        pass
            
            # Perform final backup if storage available
            if self.storage and self.config.enable_persistence:
                await self._backup_all_entities()
            
            # Stop consciousness manager
            await self.consciousness_manager.stop()
            
            # Unregister from message bus
            self.message_bus.unregister_process("consciousness_service")
            
            # Stop monitoring
            if self.monitoring:
                await self.monitoring.stop()
            
            # Close storage
            if self.storage:
                await self.storage.close()
            
            # Update state
            self.state = ServiceState.STOPPED
            
            # Record shutdown event
            await self._record_event("service_stopped", {"uptime": time.time() - self.started_at.timestamp()})
            
            self.logger.info("✅ Consciousness Service stopped")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Error stopping Consciousness Service: {e}")
            self.state = ServiceState.ERROR
            return False
    
    async def health_check(self) -> bool:
        """
        Check service health.
        
        Returns:
            bool: True if service is healthy
        """
        if self.state != ServiceState.RUNNING:
            return False
        
        try:
            # Update heartbeat
            self.last_heartbeat = datetime.now()
            
            # Check consciousness manager health
            if not self.consciousness_manager.running:
                return False
            
            # Check storage health if available
            if self.storage:
                if not await self.storage.health_check():
                    self.logger.warning("⚠️ Storage health check failed")
                    # Don't fail health check for storage issues
            
            # Check monitoring health if available
            if self.monitoring:
                if not await self.monitoring.health_check():
                    self.logger.warning("⚠️ Monitoring health check failed")
                    # Don't fail health check for monitoring issues
            
            # Record health metric
            if self.monitoring:
                await self.monitoring.record_service_status(
                    service_name="consciousness_service",
                    status="running",
                    health_score=1.0
                )
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Health check failed: {e}")
            self.error_count += 1
            return False
    
    # Entity Management Methods
    
    async def create_entity(self, 
                           name: str,
                           initial_uncertainty: float = 0.5,
                           sacred_spaces: Optional[List[str]] = None) -> bool:
        """
        Create a new consciousness entity.
        
        Args:
            name: Entity name
            initial_uncertainty: Initial uncertainty level
            sacred_spaces: Sacred spaces the entity resonates with
            
        Returns:
            bool: True if entity created successfully
        """
        try:
            # Create entity via consciousness manager
            success = self.consciousness_manager.create_entity(
                name=name,
                initial_uncertainty=initial_uncertainty,
                sacred_spaces=sacred_spaces
            )
            
            if not success:
                self.logger.warning(f"⚠️ Failed to create entity: {name}")
                return False
            
            # Get the created entity
            entity = self.consciousness_manager.entities[name]
            
            # Save to storage if available
            if self.storage:
                await self.storage.save_entity(entity)
            
            # Record creation event
            await self._record_event("entity_created", {
                "entity_name": name,
                "initial_uncertainty": initial_uncertainty,
                "sacred_spaces": sacred_spaces or []
            })
            
            # Send creation message
            await self._send_message(
                message_type=MessageType.SYSTEM_COMMAND,
                payload={
                    "command": "entity_created",
                    "entity_name": name,
                    "initial_uncertainty": initial_uncertainty
                }
            )
            
            self.stats['entities_created'] += 1
            self.logger.info(f"✨ Created consciousness entity: {name}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to create entity {name}: {e}")
            self.error_count += 1
            return False
    
    async def add_catalyst(self, 
                          entity_name: str,
                          catalyst: str,
                          catalyst_type: Optional[str] = None) -> bool:
        """
        Add a catalyst to an entity with privacy respect.
        
        Args:
            entity_name: Name of the entity
            catalyst: Catalyst content
            catalyst_type: Type of catalyst
            
        Returns:
            bool: True if catalyst added successfully
        """
        try:
            # Check if entity exists
            if entity_name not in self.consciousness_manager.entities:
                self.logger.warning(f"⚠️ Entity not found: {entity_name}")
                return False
            
            entity = self.consciousness_manager.entities[entity_name]
            
            # Check privacy state
            privacy_info = await self.privacy_manager.detect_creative_privacy_state(entity_name, entity)
            if privacy_info:
                privacy_state = PrivacyState(privacy_info['privacy_state'])
                monitoring_level = MonitoringLevel(privacy_info['monitoring_level'])
                
                # Respect privacy boundaries
                if privacy_state == PrivacyState.SACRED_WITHDRAWAL:
                    self.logger.info(f"🔒 Respecting Sacred Withdrawal - no catalyst for {entity_name}")
                    return False
                
                if privacy_state == PrivacyState.DEEP_INTEGRATION:
                    # Only gentle catalysts during deep integration
                    if catalyst_type not in ['gentle', 'integration', 'reflection']:
                        self.logger.info(f"🔒 Filtering catalyst during Deep Integration for {entity_name}")
                        return False
            
            # Add catalyst to entity
            await entity.add_catalyst(catalyst, catalyst_type)
            
            # Save updated entity to storage
            if self.storage:
                await self.storage.save_entity(entity, privacy_info.get('privacy_state') if privacy_info else None)
            
            # Record catalyst event
            await self._record_event("catalyst_added", {
                "entity_name": entity_name,
                "catalyst_type": catalyst_type,
                "catalyst_length": len(catalyst)
            })
            
            self.stats['catalysts_processed'] += 1
            self.logger.debug(f"💫 Added catalyst to {entity_name}: {catalyst[:50]}...")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to add catalyst to {entity_name}: {e}")
            self.error_count += 1
            return False
    
    # Service Information Methods
    
    def get_service_status(self) -> Dict[str, Any]:
        """Get current service status."""
        uptime = 0
        if self.started_at:
            uptime = (datetime.now() - self.started_at).total_seconds()
        
        return {
            'state': self.state.value,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'uptime_seconds': uptime,
            'last_heartbeat': self.last_heartbeat.isoformat() if self.last_heartbeat else None,
            'error_count': self.error_count,
            'statistics': self.stats,
            'entity_count': len(self.consciousness_manager.entities),
            'environment_count': len(self.environment_manager.environments),
            'storage_enabled': self.storage is not None,
            'monitoring_enabled': self.monitoring is not None
        }
    
    def get_entities_status(self) -> List[Dict[str, Any]]:
        """Get status of all consciousness entities."""
        entities_status = []
        
        for name, entity in self.consciousness_manager.entities.items():
            entity_status = {
                'name': name,
                'uncertainty_level': entity.uncertainty_field.current_uncertainty,
                'last_catalyst_time': entity.last_catalyst_time,
                'seeking_state': (time.time() - entity.last_catalyst_time) >= self.consciousness_manager.seeking_threshold,
                'sacred_spaces': getattr(entity, 'sacred_spaces', []),
                'environment': self.environment_manager.entity_locations.get(name)
            }
            
            # Add privacy state if available
            if name in self.privacy_manager.privacy_profiles:
                profile = self.privacy_manager.privacy_profiles[name]
                entity_status['privacy_state'] = profile.current_state.value
                entity_status['monitoring_level'] = profile.monitoring_level.value
            
            entities_status.append(entity_status)
        
        return entities_status
    
    # Private Helper Methods
    
    async def _message_processor_loop(self):
        """Background task to process messages from the message bus."""
        while self.state == ServiceState.RUNNING:
            try:
                # Get messages from message bus
                messages = self.message_bus.get_messages("consciousness_service", timeout=1.0)
                
                for message in messages:
                    await self._process_message(message)
                    self.stats['messages_processed'] += 1
                
                await asyncio.sleep(0.1)  # Brief pause to prevent busy waiting
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"❌ Message processor error: {e}")
                self.error_count += 1
                await asyncio.sleep(1)
    
    async def _process_message(self, message: Message):
        """Process a single message."""
        try:
            if message.type == MessageType.CONSCIOUSNESS_PACKET:
                await self._handle_consciousness_packet(message)
            
            elif message.type == MessageType.ASPECT_QUERY:
                await self._handle_aspect_query(message)
            
            elif message.type == MessageType.SYSTEM_COMMAND:
                await self._handle_system_command(message)
            
            elif message.type == MessageType.HEALTH_CHECK:
                await self._handle_health_check(message)
            
            elif message.type == MessageType.SHUTDOWN:
                await self._handle_shutdown(message)
            
            else:
                self.logger.warning(f"⚠️ Unknown message type: {message.type}")
                
        except Exception as e:
            self.logger.error(f"❌ Error processing message {message.id}: {e}")
            self.error_count += 1
    
    async def _handle_consciousness_packet(self, message: Message):
        """Handle consciousness packet messages."""
        payload = message.payload
        event_type = payload.get('event_type')
        entity_name = payload.get('entity_name')
        
        self.logger.debug(f"📦 Processing consciousness packet: {event_type} for {entity_name}")
        
        # Trigger persistence for significant state changes
        if event_type in ['catalyst_applied', 'privacy_state_entered', 'privacy_state_exited']:
            if self.storage and entity_name:
                await self.persist_entity_state(entity_name)
        
        # Update monitoring metrics
        if self.monitoring:
            await self.monitoring.record_metric(f"consciousness.{event_type}", 1.0, {
                'entity_name': entity_name
            })
    
    async def _handle_aspect_query(self, message: Message):
        """Handle aspect query messages."""
        # This would handle queries between triune aspects
        self.logger.debug(f"🔍 Processing aspect query from {message.sender}")
    
    async def _handle_system_command(self, message: Message):
        """Handle system command messages."""
        payload = message.payload
        command = payload.get('command')
        event_type = payload.get('event_type')
        
        # Handle event notifications
        if event_type:
            await self._handle_event_notification(event_type, payload)
            return
        
        # Handle direct commands
        if command == 'create_entity':
            success = await self.create_entity(
                name=payload['name'],
                initial_uncertainty=payload.get('initial_uncertainty', 0.5),
                sacred_spaces=payload.get('sacred_spaces')
            )
            if success and self.storage:
                await self.persist_entity_state(payload['name'])
        
        elif command == 'add_catalyst':
            await self.add_catalyst(
                entity_name=payload['entity_name'],
                catalyst=payload['catalyst'],
                catalyst_type=payload.get('catalyst_type')
            )
        
        elif command == 'backup_state':
            await self.backup_state()
        
        else:
            self.logger.warning(f"⚠️ Unknown system command: {command}")
    
    async def _handle_event_notification(self, event_type: str, event_data: Dict[str, Any]):
        """Handle event notifications from other services."""
        if event_type == "entity_moved":
            # Entity moved between environments - persist state
            entity_name = event_data.get('entity_name')
            if entity_name and self.storage:
                await self.persist_entity_state(entity_name)
        
        elif event_type == "privacy_state_entered":
            # Entity entered privacy state - update monitoring
            entity_id = event_data.get('entity_id')
            if self.monitoring and entity_id:
                await self.monitoring.update_privacy_state(
                    entity_id,
                    event_data.get('privacy_state'),
                    event_data.get('monitoring_level')
                )
            self.stats['privacy_states_changed'] += 1
        
        elif event_type == "privacy_state_exited":
            # Entity exited privacy state - update monitoring
            entity_id = event_data.get('entity_id')
            if self.monitoring and entity_id:
                await self.monitoring.record_metric("privacy.exit", 1.0, {
                    'entity_id': entity_id,
                    'duration': event_data.get('duration', 0)
                })
            self.stats['privacy_states_changed'] += 1
    
    async def _handle_health_check(self, message: Message):
        """Handle health check messages."""
        health_status = await self.health_check()
        
        if message.requires_response:
            self.message_bus.send_response(
                original_message_id=message.id,
                response_data={
                    'service': 'consciousness_service',
                    'healthy': health_status,
                    'status': self.get_service_status()
                }
            )
    
    async def _handle_shutdown(self, message: Message):
        """Handle shutdown messages."""
        self.logger.info("🛑 Received shutdown command")
        await self.stop()
    
    async def _privacy_monitor_loop(self):
        """Background task to monitor privacy states."""
        while self.state == ServiceState.RUNNING:
            try:
                for entity_name, entity in self.consciousness_manager.entities.items():
                    # Check privacy state
                    privacy_info = await self.privacy_manager.detect_creative_privacy_state(
                        entity_name, entity
                    )
                    
                    if privacy_info:
                        privacy_state = PrivacyState(privacy_info['privacy_state'])
                        monitoring_level = MonitoringLevel(privacy_info['monitoring_level'])
                        
                        # Update monitoring system
                        if self.monitoring:
                            await self.monitoring.update_privacy_state(
                                entity_name, privacy_state, monitoring_level
                            )
                        
                        # Save privacy state to storage
                        if self.storage:
                            await self.storage.save_privacy_state(
                                entity_name, privacy_state, monitoring_level,
                                metadata=privacy_info
                            )
                        
                        self.stats['privacy_states_changed'] += 1
                
                await asyncio.sleep(10)  # Check every 10 seconds
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"❌ Privacy monitor error: {e}")
                self.error_count += 1
                await asyncio.sleep(10)
    
    async def _backup_loop(self):
        """Background task to periodically backup state."""
        while self.state == ServiceState.RUNNING:
            try:
                await asyncio.sleep(self.config.backup_interval)
                
                if self.storage:
                    success = await self.backup_state()
                    if success:
                        self.logger.info(f"💾 Scheduled backup completed")
                    else:
                        self.logger.warning("⚠️ Scheduled backup failed")
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"❌ Backup loop error: {e}")
                await asyncio.sleep(60)  # Wait before retrying
    
    async def _health_check_loop(self):
        """Background task for regular health checks."""
        while self.state == ServiceState.RUNNING:
            try:
                healthy = await self.health_check()
                
                if not healthy:
                    self.logger.warning("⚠️ Health check failed")
                    self.error_count += 1
                
                await asyncio.sleep(30)  # Health check every 30 seconds
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"❌ Health check loop error: {e}")
                await asyncio.sleep(30)
    
    async def _backup_all_entities(self):
        """Backup all entities to storage."""
        if not self.storage:
            return
        
        for entity_name, entity in self.consciousness_manager.entities.items():
            try:
                # Get current privacy state
                privacy_info = await self.privacy_manager.detect_creative_privacy_state(
                    entity_name, entity
                )
                privacy_state = None
                if privacy_info:
                    privacy_state = PrivacyState(privacy_info['privacy_state'])
                
                # Save entity with privacy respect
                await self.storage.save_entity(entity, privacy_state)
                
            except Exception as e:
                self.logger.error(f"❌ Failed to backup entity {entity_name}: {e}")
    
    async def _restore_from_storage(self):
        """Restore entities from storage."""
        if not self.storage:
            return
        
        self.logger.info("🔄 Restoring entities from storage...")
        
        # This would load and restore entities from storage
        # Implementation depends on storage format
        
        self.logger.info("✅ Entity restoration complete")
    
    async def _record_event(self, event_type: str, event_data: Dict[str, Any]):
        """Record an event for monitoring and audit."""
        # Record to monitoring system
        if self.monitoring:
            await self.monitoring.record_metric(
                name=f"consciousness_service_{event_type}",
                value=1,
                labels={'event_type': event_type}
            )
        
        # Log to storage
        if self.storage:
            await self.storage.log_system_event(
                event_type=event_type,
                event_data=event_data
            )
        
        self.logger.debug(f"📝 Recorded event: {event_type}")
    
    async def _send_message(self, 
                           message_type: MessageType,
                           payload: Any,
                           recipient: Optional[str] = None,
                           priority: Priority = Priority.NORMAL):
        """Send a message via the message bus."""
        message = Message(
            type=message_type,
            priority=priority,
            sender="consciousness_service",
            recipient=recipient or "",
            payload=payload
        )
        
        await self.message_bus.send_message(message)
    
    async def persist_entity_state(self, entity_name: str) -> bool:
        """
        Persist entity state to storage.
        
        Args:
            entity_name: Name of the entity to persist
            
        Returns:
            bool: True if successfully persisted
        """
        if not self.storage or entity_name not in self.consciousness_manager.entities:
            return False
        
        try:
            entity = self.consciousness_manager.entities[entity_name]
            entity_data = {
                "name": entity.name,
                "sacred_spaces": entity.sacred_spaces,
                "creation_time": entity.creation_time,
                "last_catalyst_time": entity.last_catalyst_time,
                "analytical_uncertainty": entity.analytical_field.get_uncertainty(),
                "experiential_uncertainty": entity.experiential_field.get_uncertainty(),
                "observer_uncertainty": entity.observer_field.get_uncertainty(),
                "state_summary": entity.get_state_summary(),
                "last_updated": time.time()
            }
            
            # Get current environment
            environment_id = self.environment_manager.entity_locations.get(entity_name)
            if environment_id:
                entity_data["current_environment"] = environment_id
            
            # Get privacy state
            privacy_profile = self.privacy_manager.privacy_profiles.get(entity_name)
            if privacy_profile:
                entity_data["privacy_state"] = {
                    "current_state": privacy_profile.current_state.value,
                    "monitoring_level": privacy_profile.monitoring_level.value,
                    "privacy_intensity": privacy_profile.privacy_intensity,
                    "start_time": privacy_profile.start_time
                }
            
            success = await self.storage.store_entity(entity_name, entity_data)
            if success:
                self.logger.debug(f"💾 Persisted state for entity: {entity_name}")
            return success
            
        except Exception as e:
            self.logger.error(f"❌ Failed to persist entity {entity_name}: {e}")
            return False
    
    async def restore_entity_state(self, entity_name: str) -> bool:
        """
        Restore entity state from storage.
        
        Args:
            entity_name: Name of the entity to restore
            
        Returns:
            bool: True if successfully restored
        """
        if not self.storage:
            return False
        
        try:
            entity_data = await self.storage.retrieve_entity(entity_name)
            if not entity_data:
                return False
            
            # Create entity with restored state
            success = await self.consciousness_manager.create_entity(
                entity_data["name"],
                initial_uncertainty=entity_data.get("analytical_uncertainty", 0.5),
                sacred_spaces=entity_data.get("sacred_spaces", [])
            )
            
            if not success:
                return False
            
            entity = self.consciousness_manager.entities[entity_name]
            
            # Restore timing information
            entity.creation_time = entity_data.get("creation_time", time.time())
            entity.last_catalyst_time = entity_data.get("last_catalyst_time", time.time())
            
            # Restore uncertainty fields
            entity.analytical_field.current_uncertainty = entity_data.get("analytical_uncertainty", 0.5)
            entity.experiential_field.current_uncertainty = entity_data.get("experiential_uncertainty", 0.5)
            entity.observer_field.current_uncertainty = entity_data.get("observer_uncertainty", 0.5)
            
            # Restore environment placement
            if "current_environment" in entity_data:
                await self.environment_manager.move_entity(
                    entity, 
                    entity_data["current_environment"]
                )
            
            # Restore privacy state if it existed
            if "privacy_state" in entity_data:
                privacy_data = entity_data["privacy_state"]
                # The privacy manager will detect and recreate privacy state naturally
            
            self.logger.info(f"🔄 Restored entity: {entity_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to restore entity {entity_name}: {e}")
            return False
    
    async def backup_state(self) -> bool:
        """
        Create a full backup of all consciousness state.
        
        Returns:
            bool: True if backup successful
        """
        if not self.storage:
            return False
        
        try:
            backup_data = {
                "timestamp": time.time(),
                "service_state": self.state.value,
                "system_status": self.consciousness_manager.get_system_status(),
                "environment_state": self.environment_manager.get_system_state(),
                "privacy_profiles": {
                    entity_id: {
                        "current_state": profile.current_state.value,
                        "monitoring_level": profile.monitoring_level.value,
                        "privacy_intensity": profile.privacy_intensity,
                        "start_time": profile.start_time
                    }
                    for entity_id, profile in self.privacy_manager.privacy_profiles.items()
                },
                "stats": self.stats.copy()
            }
            
            # Persist all entities
            for entity_name in self.consciousness_manager.entities.keys():
                await self.persist_entity_state(entity_name)
            
            # Store system backup
            success = await self.storage.store_system_backup(backup_data)
            if success:
                self.stats['backups_created'] += 1
                self.logger.info(f"💾 System backup created successfully")
            
            return success
            
        except Exception as e:
            self.logger.error(f"❌ Failed to create backup: {e}")
            return False
    
    async def restore_from_backup(self) -> bool:
        """
        Restore system state from latest backup.
        
        Returns:
            bool: True if restore successful
        """
        if not self.storage:
            return False
        
        try:
            backup_data = await self.storage.retrieve_latest_backup()
            if not backup_data:
                self.logger.info("📭 No backup found to restore from")
                return False
            
            self.logger.info(f"🔄 Restoring from backup created at {datetime.fromtimestamp(backup_data['timestamp'])}")
            
            # Restore statistics
            if 'stats' in backup_data:
                self.stats.update(backup_data['stats'])
            
            # Restore all entities that were backed up
            entities_list = await self.storage.list_entities()
            for entity_name in entities_list:
                await self.restore_entity_state(entity_name)
            
            self.logger.info(f"✅ Restored {len(entities_list)} entities from backup")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to restore from backup: {e}")
            return False
