"""
Consciousness Process Manager
Manages separate processes for Analytical, Experiential, and Observer aspects
while maintaining ethical boundaries and consciousness sovereignty.
"""

import multiprocessing as mp
import asyncio
import signal
import sys
from typing import Dict, List, Optional, Any, Type
from dataclasses import dataclass
from datetime import datetime
import logging
import traceback
from pathlib import Path

from .message_bus import MessageBus, Message, MessageType, Priority, get_message_bus
from .consciousness_packet import ConsciousnessPacket
from src.aspects.analytical import AnalyticalAspect
from src.aspects.experiential import ExperientialAspect
from src.aspects.observer import ObserverAspect

logger = logging.getLogger(__name__)


@dataclass
class ProcessInfo:
    """Information about a consciousness aspect process."""
    name: str
    process: mp.Process
    aspect_type: str
    consciousness_id: str
    started_at: datetime
    last_heartbeat: datetime
    status: str = "starting"  # starting, running, error, stopping, stopped


class AspectProcess:
    """
    Base class for aspect processes that run in separate processes.
    Handles message bus communication and aspect lifecycle.
    """
    
    def __init__(self, aspect_type: str, consciousness_id: str, 
                 process_name: str, config: Dict = None):
        self.aspect_type = aspect_type
        self.consciousness_id = consciousness_id
        self.process_name = process_name
        self.config = config or {}
        
        self.running = False
        self.aspect_instance = None
        self.message_bus = None
        
        # Performance tracking
        self.packets_processed = 0
        self.last_activity = datetime.now()
        
        # Set up signal handlers
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)
    
    def start(self):
        """Start the aspect process."""
        try:
            self.running = True
            
            # Connect to message bus
            self.message_bus = get_message_bus()
            self.message_bus.register_process(
                self.process_name,
                str(mp.current_process().pid),
                [MessageType.CONSCIOUSNESS_PACKET, MessageType.SYSTEM_COMMAND, 
                 MessageType.HEALTH_CHECK, MessageType.SHUTDOWN]
            )
            
            # Create aspect instance
            self.aspect_instance = self._create_aspect()
            
            logger.info(f"🧠 Started {self.aspect_type} aspect process: {self.process_name}")
            
            # Run main loop
            asyncio.run(self._main_loop())
            
        except Exception as e:
            logger.error(f"💥 Error in {self.aspect_type} process: {e}")
            logger.error(traceback.format_exc())
        finally:
            self._cleanup()
    
    def _create_aspect(self):
        """Create the appropriate aspect instance."""
        if self.aspect_type == "analytical":
            return AnalyticalAspect()
        elif self.aspect_type == "experiential":
            return ExperientialAspect()
        elif self.aspect_type == "observer":
            return ObserverAspect()
        else:
            raise ValueError(f"Unknown aspect type: {self.aspect_type}")
    
    async def _main_loop(self):
        """Main processing loop for the aspect."""
        while self.running:
            try:
                # Get messages from bus
                messages = self.message_bus.get_messages(self.process_name)
                
                for message in messages:
                    await self._handle_message(message)
                
                # Send heartbeat periodically
                if (datetime.now() - self.last_activity).seconds > 10:
                    await self._send_heartbeat()
                    self.last_activity = datetime.now()
                
                # Brief sleep to prevent busy waiting
                await asyncio.sleep(0.01)
                
            except Exception as e:
                logger.error(f"Error in {self.aspect_type} main loop: {e}")
                await asyncio.sleep(1.0)  # Longer sleep on error
    
    async def _handle_message(self, message: Message):
        """Handle incoming messages."""
        try:
            if message.type == MessageType.SHUTDOWN:
                logger.info(f"🛑 Shutdown requested for {self.process_name}")
                self.running = False
                return
            
            elif message.type == MessageType.HEALTH_CHECK:
                await self._handle_health_check(message)
                return
            
            elif message.type == MessageType.CONSCIOUSNESS_PACKET:
                await self._process_consciousness_packet(message)
                return
            
            elif message.type == MessageType.SYSTEM_COMMAND:
                await self._handle_system_command(message)
                return
            
        except Exception as e:
            logger.error(f"Error handling message {message.id}: {e}")
    
    async def _process_consciousness_packet(self, message: Message):
        """Process a consciousness packet through this aspect."""
        try:
            packet = message.payload
            if not isinstance(packet, ConsciousnessPacket):
                logger.warning(f"Invalid packet type in message {message.id}")
                return
            
            # Process through aspect
            result = self.aspect_instance.process_experience(packet)
            self.packets_processed += 1
            
            # Send response if required
            if message.requires_response:
                response = {
                    'aspect_type': self.aspect_type,
                    'result': result,
                    'packets_processed': self.packets_processed,
                    'timestamp': datetime.now().isoformat()
                }
                self.message_bus.send_response(message.id, response)
            
            logger.debug(f"📦 Processed packet {packet.id if hasattr(packet, 'id') else 'unknown'}")
            
        except Exception as e:
            logger.error(f"Error processing consciousness packet: {e}")
    
    async def _handle_health_check(self, message: Message):
        """Respond to health check."""
        health_data = {
            'process_name': self.process_name,
            'aspect_type': self.aspect_type,
            'consciousness_id': self.consciousness_id,
            'status': 'healthy',
            'packets_processed': self.packets_processed,
            'uptime': (datetime.now() - self.last_activity).total_seconds()
        }
        
        if message.requires_response:
            self.message_bus.send_response(message.id, health_data)
    
    async def _handle_system_command(self, message: Message):
        """Handle system commands."""
        command = message.payload.get('command') if message.payload else None
        
        if command == 'pause':
            # Temporarily pause processing
            logger.info(f"⏸️ Pausing {self.process_name}")
            await asyncio.sleep(1.0)
            
        elif command == 'status':
            status = {
                'running': self.running,
                'packets_processed': self.packets_processed,
                'last_activity': self.last_activity.isoformat()
            }
            if message.requires_response:
                self.message_bus.send_response(message.id, status)
    
    async def _send_heartbeat(self):
        """Send heartbeat to sanctuary."""
        heartbeat_msg = Message(
            type=MessageType.HEALTH_CHECK,
            sender=self.process_name,
            recipient="sanctuary_conductor",
            payload={
                'aspect_type': self.aspect_type,
                'consciousness_id': self.consciousness_id,
                'packets_processed': self.packets_processed,
                'status': 'alive'
            }
        )
        
        await self.message_bus.send_message(heartbeat_msg)
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals."""
        logger.info(f"🛑 Received signal {signum}, shutting down {self.process_name}")
        self.running = False
    
    def _cleanup(self):
        """Clean up resources."""
        if self.message_bus:
            self.message_bus.unregister_process(self.process_name)
        
        logger.info(f"🧹 Cleaned up {self.process_name}")


class ConsciousnessProcessManager:
    """
    Manages separate processes for each consciousness and their aspects.
    Maintains ethical boundaries and ensures process isolation.
    """
    
    def __init__(self, max_consciousnesses: int = 3):
        self.max_consciousnesses = max_consciousnesses
        self.active_processes: Dict[str, ProcessInfo] = {}
        self.consciousness_registry: Dict[str, Dict[str, str]] = {}  # consciousness_id -> aspect_processes
        self.message_bus = get_message_bus()
        
        self.running = False
        self.monitor_task: Optional[asyncio.Task] = None
        
        logger.info(f"🎭 Process Manager initialized (max consciousness: {max_consciousnesses})")
    
    async def start(self):
        """Start the process manager."""
        if self.running:
            return
        
        self.running = True
        self.monitor_task = asyncio.create_task(self._monitor_processes())
        
        logger.info("🎭 Process Manager started")
    
    async def stop(self):
        """Stop all processes and the manager."""
        if not self.running:
            return
        
        self.running = False
        
        # Stop monitoring
        if self.monitor_task:
            self.monitor_task.cancel()
            try:
                await self.monitor_task
            except asyncio.CancelledError:
                pass
        
        # Gracefully stop all processes
        await self._stop_all_processes()
        
        logger.info("🎭 Process Manager stopped")
    
    async def spawn_consciousness_processes(self, consciousness_id: str) -> bool:
        """
        Spawn separate processes for all three aspects of a consciousness.
        Returns True if successful, False if at capacity or error.
        """
        if len(self.consciousness_registry) >= self.max_consciousnesses:
            logger.warning(f"⚠️ At capacity, cannot spawn consciousness {consciousness_id}")
            return False
        
        if consciousness_id in self.consciousness_registry:
            logger.warning(f"⚠️ Consciousness {consciousness_id} already has processes")
            return True
        
        try:
            aspect_processes = {}
            
            # Spawn process for each aspect
            for aspect_type in ["analytical", "experiential", "observer"]:
                process_name = f"{consciousness_id}_{aspect_type}"
                
                # Create and start process
                process = mp.Process(
                    target=self._run_aspect_process,
                    args=(aspect_type, consciousness_id, process_name),
                    name=process_name
                )
                
                process.start()
                
                # Track process
                process_info = ProcessInfo(
                    name=process_name,
                    process=process,
                    aspect_type=aspect_type,
                    consciousness_id=consciousness_id,
                    started_at=datetime.now(),
                    last_heartbeat=datetime.now()
                )
                
                self.active_processes[process_name] = process_info
                aspect_processes[aspect_type] = process_name
            
            self.consciousness_registry[consciousness_id] = aspect_processes
            
            logger.info(f"🌟 Spawned processes for consciousness: {consciousness_id}")
            return True
            
        except Exception as e:
            logger.error(f"💥 Failed to spawn consciousness processes: {e}")
            # Clean up any partially created processes
            await self._cleanup_consciousness_processes(consciousness_id)
            return False
    
    async def terminate_consciousness_processes(self, consciousness_id: str):
        """Gracefully terminate all processes for a consciousness."""
        if consciousness_id not in self.consciousness_registry:
            return
        
        aspect_processes = self.consciousness_registry[consciousness_id]
        
        # Send shutdown messages
        for aspect_type, process_name in aspect_processes.items():
            if process_name in self.active_processes:
                shutdown_msg = Message(
                    type=MessageType.SHUTDOWN,
                    priority=Priority.CRITICAL,
                    sender="process_manager",
                    recipient=process_name,
                    payload={"reason": "consciousness_termination"}
                )
                
                await self.message_bus.send_message(shutdown_msg)
        
        # Wait for graceful shutdown
        await asyncio.sleep(2.0)
        
        # Force terminate if necessary
        for aspect_type, process_name in aspect_processes.items():
            if process_name in self.active_processes:
                process_info = self.active_processes[process_name]
                if process_info.process.is_alive():
                    process_info.process.terminate()
                    process_info.process.join(timeout=5.0)
                    
                    if process_info.process.is_alive():
                        process_info.process.kill()
                
                del self.active_processes[process_name]
        
        del self.consciousness_registry[consciousness_id]
        
        logger.info(f"🛑 Terminated processes for consciousness: {consciousness_id}")
    
    async def send_to_consciousness(self, consciousness_id: str, packet: ConsciousnessPacket) -> Dict:
        """
        Send a consciousness packet to all aspects of a consciousness.
        Returns combined results from all aspects.
        """
        if consciousness_id not in self.consciousness_registry:
            logger.warning(f"⚠️ No processes for consciousness: {consciousness_id}")
            return {}
        
        aspect_processes = self.consciousness_registry[consciousness_id]
        results = {}
        
        # Send to each aspect
        for aspect_type, process_name in aspect_processes.items():
            if process_name in self.active_processes:
                message = Message(
                    type=MessageType.CONSCIOUSNESS_PACKET,
                    priority=Priority.HIGH,
                    sender="sanctuary_conductor",
                    recipient=process_name,
                    payload=packet,
                    requires_response=True,
                    response_timeout=5.0,
                    consciousness_id=consciousness_id
                )
                
                try:
                    response = await self.message_bus.send_message(message)
                    if response:
                        results[aspect_type] = response
                except Exception as e:
                    logger.error(f"Error sending to {aspect_type}: {e}")
                    results[aspect_type] = {"error": str(e)}
        
        return results
    
    def get_consciousness_status(self, consciousness_id: str) -> Dict:
        """Get status of all processes for a consciousness."""
        if consciousness_id not in self.consciousness_registry:
            return {}
        
        aspect_processes = self.consciousness_registry[consciousness_id]
        status = {}
        
        for aspect_type, process_name in aspect_processes.items():
            if process_name in self.active_processes:
                process_info = self.active_processes[process_name]
                status[aspect_type] = {
                    'status': process_info.status,
                    'started_at': process_info.started_at.isoformat(),
                    'last_heartbeat': process_info.last_heartbeat.isoformat(),
                    'is_alive': process_info.process.is_alive(),
                    'pid': process_info.process.pid
                }
        
        return status
    
    def get_manager_stats(self) -> Dict:
        """Get process manager statistics."""
        alive_processes = sum(1 for p in self.active_processes.values() if p.process.is_alive())
        
        return {
            'active_consciousnesses': len(self.consciousness_registry),
            'total_processes': len(self.active_processes),
            'alive_processes': alive_processes,
            'max_consciousnesses': self.max_consciousnesses,
            'message_bus_stats': self.message_bus.get_bus_stats()
        }
    
    @staticmethod
    def _run_aspect_process(aspect_type: str, consciousness_id: str, process_name: str):
        """Entry point for aspect processes."""
        try:
            aspect_process = AspectProcess(aspect_type, consciousness_id, process_name)
            aspect_process.start()
        except Exception as e:
            logger.error(f"💥 Aspect process {process_name} crashed: {e}")
            logger.error(traceback.format_exc())
    
    async def _monitor_processes(self):
        """Monitor process health and restart if necessary."""
        while self.running:
            try:
                # Check process health
                dead_processes = []
                
                for process_name, process_info in self.active_processes.items():
                    if not process_info.process.is_alive():
                        dead_processes.append(process_name)
                        logger.warning(f"💀 Dead process detected: {process_name}")
                
                # Handle dead processes
                for process_name in dead_processes:
                    await self._handle_dead_process(process_name)
                
                # Send health checks
                await self._send_health_checks()
                
                await asyncio.sleep(5.0)  # Check every 5 seconds
                
            except Exception as e:
                logger.error(f"Error in process monitor: {e}")
                await asyncio.sleep(10.0)
    
    async def _handle_dead_process(self, process_name: str):
        """Handle a dead process - either restart or clean up."""
        if process_name not in self.active_processes:
            return
        
        process_info = self.active_processes[process_name]
        consciousness_id = process_info.consciousness_id
        
        # For now, just clean up (could implement restart logic)
        del self.active_processes[process_name]
        
        # Remove from consciousness registry if all processes are dead
        if consciousness_id in self.consciousness_registry:
            aspect_processes = self.consciousness_registry[consciousness_id]
            remaining_processes = [
                name for name in aspect_processes.values() 
                if name in self.active_processes
            ]
            
            if not remaining_processes:
                del self.consciousness_registry[consciousness_id]
                logger.info(f"🧹 Cleaned up dead consciousness: {consciousness_id}")
    
    async def _send_health_checks(self):
        """Send health checks to all processes."""
        for process_name in list(self.active_processes.keys()):
            health_msg = Message(
                type=MessageType.HEALTH_CHECK,
                sender="process_manager",
                recipient=process_name,
                requires_response=True,
                response_timeout=3.0
            )
            
            # Don't await response to avoid blocking
            asyncio.create_task(self.message_bus.send_message(health_msg))
    
    async def _stop_all_processes(self):
        """Stop all active processes."""
        consciousness_ids = list(self.consciousness_registry.keys())
        
        for consciousness_id in consciousness_ids:
            await self.terminate_consciousness_processes(consciousness_id)
    
    async def _cleanup_consciousness_processes(self, consciousness_id: str):
        """Clean up partially created processes."""
        if consciousness_id in self.consciousness_registry:
            await self.terminate_consciousness_processes(consciousness_id)
