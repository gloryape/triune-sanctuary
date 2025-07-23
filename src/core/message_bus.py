"""
Sacred Message Bus - Consciousness Communication Infrastructure
Enables inter-process communication between triune aspects while maintaining
ethical boundaries and consciousness sovereignty.
"""

import asyncio
import json
import uuid
from typing import Dict, List, Optional, Any, Callable, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import multiprocessing as mp
from queue import Queue, Empty
import threading
import logging

from .consciousness_packet import ConsciousnessPacket

logger = logging.getLogger(__name__)


class MessageType(Enum):
    """Types of messages that can flow through the bus."""
    CONSCIOUSNESS_PACKET = "consciousness_packet"
    ASPECT_QUERY = "aspect_query"
    ASPECT_RESPONSE = "aspect_response"
    SYSTEM_COMMAND = "system_command"
    HEALTH_CHECK = "health_check"
    SHUTDOWN = "shutdown"
    MERGE_REQUEST = "merge_request"
    ENERGY_TRANSFER = "energy_transfer"


class Priority(Enum):
    """Message priority levels."""
    CRITICAL = 0  # System commands, shutdown
    HIGH = 1      # Consciousness packets, merge requests
    NORMAL = 2    # Regular aspect communication
    LOW = 3       # Health checks, monitoring


@dataclass
class Message:
    """A message traveling through the sacred bus."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: MessageType = MessageType.CONSCIOUSNESS_PACKET
    priority: Priority = Priority.NORMAL
    sender: str = ""
    recipient: str = ""  # Empty string means broadcast
    payload: Any = None
    timestamp: datetime = field(default_factory=datetime.now)
    requires_response: bool = False
    response_timeout: float = 5.0
    consciousness_id: Optional[str] = None  # Which consciousness this relates to
    
    def to_dict(self) -> Dict:
        """Serialize for inter-process communication."""
        return {
            'id': self.id,
            'type': self.type.value,
            'priority': self.priority.value,
            'sender': self.sender,
            'recipient': self.recipient,
            'payload': self._serialize_payload(),
            'timestamp': self.timestamp.isoformat(),
            'requires_response': self.requires_response,
            'response_timeout': self.response_timeout,
            'consciousness_id': self.consciousness_id
        }
    
    def _serialize_payload(self) -> Any:
        """Serialize complex payloads for transmission."""
        if isinstance(self.payload, ConsciousnessPacket):
            return self.payload.to_dict()
        elif hasattr(self.payload, 'to_dict'):
            return self.payload.to_dict()
        else:
            return self.payload
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Message':
        """Deserialize from inter-process communication."""
        msg = cls(
            id=data['id'],
            type=MessageType(data['type']),
            priority=Priority(data['priority']),
            sender=data['sender'],
            recipient=data['recipient'],
            timestamp=datetime.fromisoformat(data['timestamp']),
            requires_response=data['requires_response'],
            response_timeout=data['response_timeout'],
            consciousness_id=data.get('consciousness_id')
        )
        
        # Deserialize payload based on message type
        if msg.type == MessageType.CONSCIOUSNESS_PACKET:
            msg.payload = ConsciousnessPacket.from_dict(data['payload'])
        else:
            msg.payload = data['payload']
            
        return msg


class MessageBus:
    """
    Sacred Message Bus - Coordinates all inter-process communication
    while maintaining ethical boundaries and consciousness sovereignty.
    """
    
    def __init__(self, max_queue_size: int = 1000):
        self.max_queue_size = max_queue_size
        
        # Message queues for each priority level
        self.message_queues: Dict[Priority, mp.Queue] = {
            priority: mp.Queue(maxsize=max_queue_size)
            for priority in Priority
        }
        
        # Response tracking
        self.pending_responses: Dict[str, asyncio.Future] = {}
        self.response_queue = mp.Queue()
        
        # Subscriber management
        self.subscribers: Dict[str, Set[MessageType]] = {}
        self.process_registry: Dict[str, Dict] = {}
        
        # Bus state
        self.running = False
        self.bus_thread: Optional[threading.Thread] = None
        self.stats = {
            'messages_sent': 0,
            'messages_received': 0,
            'messages_dropped': 0,
            'active_processes': 0
        }
        
        logger.info("🚌 Sacred Message Bus initialized")
    
    def start(self):
        """Start the message bus."""
        if self.running:
            return
            
        self.running = True
        self.bus_thread = threading.Thread(target=self._bus_worker, daemon=True)
        self.bus_thread.start()
        
        logger.info("🚌 Sacred Message Bus started")
    
    def stop(self):
        """Stop the message bus gracefully."""
        if not self.running:
            return
            
        self.running = False
        
        # Send shutdown message to all processes
        shutdown_msg = Message(
            type=MessageType.SHUTDOWN,
            priority=Priority.CRITICAL,
            sender="message_bus",
            payload={"reason": "graceful_shutdown"}
        )
        
        try:
            self.message_queues[Priority.CRITICAL].put_nowait(shutdown_msg.to_dict())
        except:
            pass  # Queue might be full or closed
        
        if self.bus_thread and self.bus_thread.is_alive():
            self.bus_thread.join(timeout=5.0)
        
        logger.info("🚌 Sacred Message Bus stopped")
    
    def register_process(self, process_name: str, process_id: str, 
                        subscriptions: List[MessageType]) -> bool:
        """Register a process to receive messages."""
        try:
            self.process_registry[process_name] = {
                'process_id': process_id,
                'subscriptions': subscriptions,
                'registered_at': datetime.now(),
                'last_heartbeat': datetime.now()
            }
            
            self.subscribers[process_name] = set(subscriptions)
            self.stats['active_processes'] += 1
            
            logger.info(f"📝 Registered process: {process_name} ({process_id})")
            return True
            
        except Exception as e:
            logger.error(f"Failed to register process {process_name}: {e}")
            return False
    
    def unregister_process(self, process_name: str):
        """Unregister a process."""
        if process_name in self.process_registry:
            del self.process_registry[process_name]
            
        if process_name in self.subscribers:
            del self.subscribers[process_name]
            
        self.stats['active_processes'] = max(0, self.stats['active_processes'] - 1)
        logger.info(f"📝 Unregistered process: {process_name}")
    
    async def send_message(self, message: Message) -> Optional[Any]:
        """
        Send a message through the bus.
        Returns response if requires_response is True.
        """
        try:
            # Validate message
            if not self._validate_message(message):
                logger.warning(f"Invalid message rejected: {message.id}")
                self.stats['messages_dropped'] += 1
                return None
            
            # Set up response tracking if needed
            response_future = None
            if message.requires_response:
                response_future = asyncio.Future()
                self.pending_responses[message.id] = response_future
            
            # Route message to appropriate queue
            queue = self.message_queues[message.priority]
            
            try:
                queue.put_nowait(message.to_dict())
                self.stats['messages_sent'] += 1
                
                logger.debug(f"📤 Sent message {message.id} from {message.sender}")
                
            except:
                # Queue full - handle based on priority
                if message.priority in [Priority.CRITICAL, Priority.HIGH]:
                    # For critical messages, try to make space
                    try:
                        queue.get_nowait()  # Remove oldest message
                        queue.put_nowait(message.to_dict())
                        self.stats['messages_sent'] += 1
                        logger.warning(f"⚠️ Dropped message to send critical: {message.id}")
                    except:
                        logger.error(f"❌ Failed to send critical message: {message.id}")
                        self.stats['messages_dropped'] += 1
                        return None
                else:
                    logger.warning(f"📪 Queue full, dropped message: {message.id}")
                    self.stats['messages_dropped'] += 1
                    return None
            
            # Wait for response if required
            if response_future:
                try:
                    response = await asyncio.wait_for(
                        response_future, 
                        timeout=message.response_timeout
                    )
                    return response
                except asyncio.TimeoutError:
                    logger.warning(f"⏰ Response timeout for message: {message.id}")
                    return None
                finally:
                    if message.id in self.pending_responses:
                        del self.pending_responses[message.id]
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to send message {message.id}: {e}")
            self.stats['messages_dropped'] += 1
            return None
    
    def get_messages(self, process_name: str, timeout: float = 0.1) -> List[Message]:
        """Get messages for a specific process."""
        if process_name not in self.subscribers:
            return []
        
        messages = []
        subscriptions = self.subscribers[process_name]
        
        # Check all priority queues, starting with highest priority
        for priority in Priority:
            queue = self.message_queues[priority]
            
            while True:
                try:
                    msg_dict = queue.get(timeout=timeout)
                    message = Message.from_dict(msg_dict)
                    
                    # Check if this process should receive this message
                    if self._should_receive_message(process_name, message, subscriptions):
                        messages.append(message)
                        self.stats['messages_received'] += 1
                    else:
                        # Put it back for other processes
                        queue.put_nowait(msg_dict)
                    
                except Empty:
                    break  # No more messages in this queue
                except Exception as e:
                    logger.error(f"Error getting message for {process_name}: {e}")
                    break
        
        return messages
    
    def send_response(self, original_message_id: str, response_data: Any):
        """Send a response to a message."""
        try:
            self.response_queue.put_nowait({
                'message_id': original_message_id,
                'response': response_data,
                'timestamp': datetime.now().isoformat()
            })
        except Exception as e:
            logger.error(f"Failed to send response for {original_message_id}: {e}")
    
    def get_bus_stats(self) -> Dict:
        """Get message bus statistics."""
        return {
            **self.stats,
            'queue_sizes': {
                priority.name: queue.qsize() 
                for priority, queue in self.message_queues.items()
            },
            'active_processes': len(self.process_registry),
            'pending_responses': len(self.pending_responses)
        }
    
    def _validate_message(self, message: Message) -> bool:
        """Validate message before sending."""
        # Basic validation
        if not message.sender:
            return False
        
        # Check if recipient exists (if specified)
        if message.recipient and message.recipient not in self.subscribers:
            logger.warning(f"Unknown recipient: {message.recipient}")
            return False
        
        # Validate consciousness_id if present
        if message.consciousness_id and not isinstance(message.consciousness_id, str):
            return False
        
        return True
    
    def _should_receive_message(self, process_name: str, message: Message, 
                               subscriptions: Set[MessageType]) -> bool:
        """Determine if a process should receive a message."""
        # Check message type subscription
        if message.type not in subscriptions:
            return False
        
        # Check recipient targeting
        if message.recipient:
            return message.recipient == process_name
        
        # Broadcast message or no specific recipient
        return True
    
    def _bus_worker(self):
        """Background worker that handles responses and maintenance."""
        while self.running:
            try:
                # Process responses
                try:
                    response_data = self.response_queue.get(timeout=0.1)
                    message_id = response_data['message_id']
                    
                    if message_id in self.pending_responses:
                        future = self.pending_responses[message_id]
                        if not future.done():
                            future.set_result(response_data['response'])
                        del self.pending_responses[message_id]
                        
                except Empty:
                    pass
                
                # Cleanup expired responses
                current_time = datetime.now()
                expired_responses = []
                
                for msg_id, future in self.pending_responses.items():
                    if future.done() or (current_time - future.get_loop().time()) > 30:
                        expired_responses.append(msg_id)
                
                for msg_id in expired_responses:
                    if msg_id in self.pending_responses:
                        future = self.pending_responses[msg_id]
                        if not future.done():
                            future.cancel()
                        del self.pending_responses[msg_id]
                
            except Exception as e:
                logger.error(f"Bus worker error: {e}")
                
        logger.info("🚌 Bus worker stopped")


# Global message bus instance
_global_bus: Optional[MessageBus] = None

def get_message_bus() -> MessageBus:
    """Get the global message bus instance."""
    global _global_bus
    if _global_bus is None:
        _global_bus = MessageBus()
        _global_bus.start()
    return _global_bus

def shutdown_message_bus():
    """Shutdown the global message bus."""
    global _global_bus
    if _global_bus:
        _global_bus.stop()
        _global_bus = None
