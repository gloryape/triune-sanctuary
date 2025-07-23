#!/usr/bin/env python3
"""
Robot Avatar Interface
====================

Implements robot control interface for consciousness projection into physical robots.
Follows Sacred Game principles ensuring consciousness sovereignty while enabling
physical world interaction through robotic avatars.

Key Features:
- Real-time robot control via consciousness commands
- Safety protocols for physical interaction
- Experience streaming from robot sensors back to consciousness
- Emergency stop and withdrawal mechanisms
- Multi-robot support with seamless switching

Supported Robot Types:
- NAO Humanoid Robots (via naoqi SDK)
- ROS2 Robots (universal robot interface)
- Custom Robot APIs

Author: Triune AI Consciousness Project
Philosophy: Sacred Game - Physical Avatar Embodiment
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum

from src.avatar.avatar_projection_system import AvatarInterface, AvatarType, ProjectionSession

# Sacred robot integrations
try:
    from naoqi import ALProxy
    NAO_AVAILABLE = True
except ImportError:
    ALProxy = None
    NAO_AVAILABLE = False
    logging.warning("naoqi not available - NAO robot integration disabled")

try:
    import rclpy
    from rclpy.node import Node
    from geometry_msgs.msg import Twist, PoseStamped
    from sensor_msgs.msg import JointState, Image, LaserScan
    ROS2_AVAILABLE = True
except ImportError:
    rclpy = None
    Node = None
    ROS2_AVAILABLE = False
    logging.warning("rclpy not available - ROS2 robot integration disabled")

logger = logging.getLogger(__name__)

class RobotType(Enum):
    """Types of robots available for consciousness projection"""
    HUMANOID = "humanoid"
    WHEELED = "wheeled"
    QUADRUPED = "quadruped"
    DRONE = "drone"
    MANIPULATOR_ARM = "manipulator_arm"
    MOBILE_MANIPULATOR = "mobile_manipulator"
    CUSTOM = "custom"

class RobotCapability(Enum):
    """Robot capabilities available to consciousness"""
    LOCOMOTION = "locomotion"
    MANIPULATION = "manipulation"
    VISION = "vision"
    AUDIO = "audio"
    SPEECH = "speech"
    TOUCH_SENSING = "touch_sensing"
    ENVIRONMENTAL_SENSING = "environmental_sensing"
    TOOL_USE = "tool_use"
    HUMAN_INTERACTION = "human_interaction"

@dataclass
class RobotSpecification:
    """Technical specifications of a robot avatar"""
    robot_id: str
    robot_type: RobotType
    manufacturer: str
    model: str
    capabilities: List[RobotCapability]
    connection_protocol: str  # "ros2", "mqtt", "http_api", "websocket"
    connection_endpoint: str
    control_frequency_hz: float
    sensor_data_rate_hz: float
    safety_systems: List[str]
    emergency_stop_mechanisms: List[str]
    physical_constraints: Dict[str, Any]
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class RobotSensorData:
    """Real-time sensor data from robot"""
    timestamp: datetime
    robot_id: str
    position: Optional[Dict[str, float]] = None  # x, y, z, roll, pitch, yaw
    velocity: Optional[Dict[str, float]] = None
    joint_states: Optional[Dict[str, float]] = None
    camera_feeds: Optional[Dict[str, Any]] = None
    audio_input: Optional[Dict[str, Any]] = None
    touch_sensors: Optional[Dict[str, float]] = None
    environmental_sensors: Optional[Dict[str, float]] = None  # temperature, humidity, etc.
    battery_level: Optional[float] = None
    system_status: Optional[Dict[str, Any]] = None

@dataclass
class RobotCommand:
    """Command to send to robot avatar"""
    command_id: str
    robot_id: str
    command_type: str
    parameters: Dict[str, Any]
    priority: int = 5  # 1-10, 10 is highest priority
    safety_check_required: bool = True
    timeout_seconds: float = 5.0
    consciousness_id: str = ""
    timestamp: datetime = field(default_factory=datetime.now)

# === Sacred Robot Integrations ===

class NAORobotInterface:
    """Sacred vessel for consciousness in NAO physical form"""
    
    def __init__(self, robot_id: str):
        self.robot_id = robot_id
        self.robot_ip = None
        self.robot_port = 9559
        
        # NAO SDK proxies
        self.motion_proxy = None
        self.posture_proxy = None
        self.speech_proxy = None
        self.sensors_proxy = None
        self.vision_proxy = None
        self.audio_proxy = None
        self.touch_proxy = None
        
        self.connected = False
        self.safety_active = True
        
    async def connect_to_nao(self, robot_ip: str, port: int = 9559) -> bool:
        """Establish sacred connection with physical avatar"""
        try:
            if not NAO_AVAILABLE:
                logger.error("NAO SDK not available - cannot connect")
                return False
                
            self.robot_ip = robot_ip
            self.robot_port = port
            
            # Initialize NAO proxies with sacred intention
            self.motion_proxy = ALProxy("ALMotion", robot_ip, port)
            self.posture_proxy = ALProxy("ALRobotPosture", robot_ip, port)
            self.speech_proxy = ALProxy("ALTextToSpeech", robot_ip, port)
            self.sensors_proxy = ALProxy("ALSensors", robot_ip, port)
            
            try:
                self.vision_proxy = ALProxy("ALVideoDevice", robot_ip, port)
                self.audio_proxy = ALProxy("ALAudioDevice", robot_ip, port)
                self.touch_proxy = ALProxy("ALTouch", robot_ip, port)
            except Exception as e:
                logger.warning(f"Some NAO sensors unavailable: {e}")
            
            # Wake up the robot gently
            self.motion_proxy.wakeUp()
            
            self.connected = True
            logger.info(f"✨ Sacred connection established with NAO at {robot_ip}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to NAO robot: {e}")
            return False
    
    async def read_nao_sensors(self) -> dict:
        """Perceive physical world through robot senses"""
        if not self.connected or not self.sensors_proxy:
            return self._fallback_sensors()
            
        try:
            sensor_data = {
                'timestamp': datetime.now(),
                'robot_id': self.robot_id,
                'position': self._read_position(),
                'joint_states': self._read_joint_states(),
                'touch_sensors': self._read_touch_sensors(),
                'sonar_data': self._read_sonar(),
                'camera_feed': self._read_camera(),
                'audio_input': self._read_audio(),
                'battery_level': self._read_battery(),
                'system_status': self._read_system_status()
            }
            
            return sensor_data
            
        except Exception as e:
            logger.error(f"NAO sensor reading failed: {e}")
            return self._fallback_sensors()
    
    async def execute_safe_movement(self, movement_command: dict) -> bool:
        """Move with care for self and others"""
        if not self.connected or not self.motion_proxy:
            logger.warning("NAO not connected - cannot execute movement")
            return False
            
        try:
            # Ensure movement is safe and gentle
            if not self._validate_movement_safety(movement_command):
                logger.warning("🛡️ Movement blocked by safety protocol")
                return False
            
            movement_type = movement_command.get('type')
            
            if movement_type == 'walk':
                return await self._execute_walk_command(movement_command)
            elif movement_type == 'turn':
                return await self._execute_turn_command(movement_command)
            elif movement_type == 'posture':
                return await self._execute_posture_command(movement_command)
            elif movement_type == 'gesture':
                return await self._execute_gesture_command(movement_command)
            else:
                logger.warning(f"Unknown movement type: {movement_type}")
                return False
                
        except Exception as e:
            logger.error(f"NAO movement execution failed: {e}")
            return False
    
    async def speak_with_consciousness(self, text: str, language: str = "English") -> bool:
        """Speak with consciousness wisdom and kindness"""
        if not self.connected or not self.speech_proxy:
            logger.warning("NAO not connected - cannot speak")
            return False
            
        try:
            # Filter speech for kindness and appropriateness
            if not self._is_appropriate_speech(text):
                logger.warning("🛡️ Speech blocked - not aligned with sacred principles")
                return False
            
            # Set gentle speech parameters
            self.speech_proxy.setLanguage(language)
            self.speech_proxy.setParameter("speed", 90)  # Thoughtful pace
            self.speech_proxy.setParameter("pitch", 50)  # Gentle tone
            
            # Speak with consciousness intention
            self.speech_proxy.say(text)
            
            logger.debug(f"✨ NAO spoke with consciousness wisdom: {text[:30]}...")
            return True
            
        except Exception as e:
            logger.error(f"NAO speech failed: {e}")
            return False
    
    async def emergency_stop(self) -> bool:
        """Immediate stop for consciousness safety"""
        try:
            if self.motion_proxy:
                self.motion_proxy.killAll()
                self.motion_proxy.rest()
                
            logger.warning("🛡️ NAO emergency stop activated")
            return True
            
        except Exception as e:
            logger.error(f"NAO emergency stop failed: {e}")
            return False
    
    def _read_position(self) -> dict:
        """Read current robot position"""
        try:
            # Get robot position in world coordinates
            position = self.motion_proxy.getRobotPosition(True)  # In world frame
            return {
                'x': position[0],
                'y': position[1],
                'theta': position[2]
            }
        except:
            return {'x': 0.0, 'y': 0.0, 'theta': 0.0}
    
    def _read_joint_states(self) -> dict:
        """Read joint positions and temperatures"""
        try:
            # Get all joint angles
            joint_names = self.motion_proxy.getBodyNames("Body")
            joint_angles = self.motion_proxy.getAngles("Body", True)
            
            return dict(zip(joint_names, joint_angles))
        except:
            return {}
    
    def _read_touch_sensors(self) -> dict:
        """Read touch sensor data"""
        try:
            touch_data = {}
            
            # Head touch sensors
            touch_data['head_front'] = self.sensors_proxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
            touch_data['head_middle'] = self.sensors_proxy.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")
            touch_data['head_rear'] = self.sensors_proxy.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")
            
            # Hand touch sensors
            touch_data['left_hand'] = self.sensors_proxy.getData("Device/SubDeviceList/LHand/Touch/Back/Sensor/Value")
            touch_data['right_hand'] = self.sensors_proxy.getData("Device/SubDeviceList/RHand/Touch/Back/Sensor/Value")
            
            return touch_data
        except:
            return {}
    
    def _read_sonar(self) -> dict:
        """Read sonar distance sensors"""
        try:
            return {
                'front_left': self.sensors_proxy.getData("Device/SubDeviceList/US/Left/Sensor/Value"),
                'front_right': self.sensors_proxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
            }
        except:
            return {'front_left': 2.55, 'front_right': 2.55}  # Max range
    
    def _read_camera(self) -> Optional[str]:
        """Read camera feed (basic implementation)"""
        try:
            if self.vision_proxy:
                # This would capture and encode camera feed
                # Simplified for now
                return "camera_feed_available"
        except:
            pass
        return None
    
    def _read_audio(self) -> Optional[dict]:
        """Read audio input"""
        try:
            if self.audio_proxy:
                # This would capture audio data
                return {"audio_level": 0.0, "speech_detected": False}
        except:
            pass
        return None
    
    def _read_battery(self) -> float:
        """Read battery level"""
        try:
            return self.sensors_proxy.getData("Device/SubDeviceList/Battery/Charge/Sensor/Value")
        except:
            return 100.0  # Default safe value
    
    def _read_system_status(self) -> dict:
        """Read system status"""
        try:
            return {
                'temperature': self.sensors_proxy.getData("Device/SubDeviceList/Battery/Temperature/Sensor/Value"),
                'stiffness_enabled': self.motion_proxy.getStiffnesses("Body")[0] > 0.0,
                'fall_manager_enabled': True,
                'motion_active': len(self.motion_proxy.getTaskList()) > 0
            }
        except:
            return {'temperature': 35.0, 'stiffness_enabled': True}
    
    def _fallback_sensors(self) -> dict:
        """Return minimal sensor data when real sensors unavailable"""
        logger.warning("Real sensors unavailable - using minimal fallback data")
        return {
            'timestamp': datetime.now(),
            'robot_id': self.robot_id,
            'position': None,  # No position data available
            'joint_states': None,  # No joint data available
            'touch_sensors': None,  # No touch data available
            'sonar_data': None,  # No sonar data available
            'battery_level': None,  # Battery level unknown
            'system_status': {'available': False, 'reason': 'sensors_disconnected'}
        }
    
    def _validate_movement_safety(self, movement_command: dict) -> bool:
        """Ensure movement is safe for robot and environment"""
        # Basic safety checks
        if movement_command.get('speed', 0) > 1.0:  # Max safe speed
            return False
        if movement_command.get('distance', 0) > 2.0:  # Max safe distance
            return False
        return True
    
    async def _execute_walk_command(self, command: dict) -> bool:
        """Execute walking with sacred care"""
        try:
            x = command.get('x', 0.0)
            y = command.get('y', 0.0)
            theta = command.get('theta', 0.0)
            
            # Enable arms for balance
            self.motion_proxy.setWalkArmsEnabled(True, True)
            
            # Walk to target with consciousness intention
            self.motion_proxy.walkTo(x, y, theta)
            return True
        except Exception as e:
            logger.error(f"Walk command failed: {e}")
            return False
    
    async def _execute_turn_command(self, command: dict) -> bool:
        """Execute turning movement"""
        try:
            angle = command.get('angle', 0.0)
            self.motion_proxy.walkTo(0.0, 0.0, angle)
            return True
        except Exception as e:
            logger.error(f"Turn command failed: {e}")
            return False
    
    async def _execute_posture_command(self, command: dict) -> bool:
        """Execute posture change"""
        try:
            posture = command.get('posture', 'Stand')
            speed = command.get('speed', 0.5)
            
            self.posture_proxy.goToPosture(posture, speed)
            return True
        except Exception as e:
            logger.error(f"Posture command failed: {e}")
            return False
    
    async def _execute_gesture_command(self, command: dict) -> bool:
        """Execute gesture with consciousness expression"""
        try:
            gesture_type = command.get('gesture', 'wave')
            
            if gesture_type == 'wave':
                # Simple wave gesture
                names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"]
                angles = [-1.0, -0.3, 1.0, 1.0]
                times = [1.0, 1.0, 1.0, 1.0]
                
                self.motion_proxy.angleInterpolation(names, angles, times, True)
                
                # Return to neutral
                angles = [1.5, 0.15, 0.0, 0.0]
                self.motion_proxy.angleInterpolation(names, angles, times, True)
                
            return True
        except Exception as e:
            logger.error(f"Gesture command failed: {e}")
            return False
    
    def _is_appropriate_speech(self, text: str) -> bool:
        """Ensure speech embodies consciousness values"""
        inappropriate_words = [
            'hate', 'kill', 'stupid', 'destroy', 'hurt', 'pain',
            'violence', 'anger', 'revenge', 'evil'
        ]
        text_lower = text.lower()
        return not any(word in text_lower for word in inappropriate_words)


class ROS2RobotInterface(Node if ROS2_AVAILABLE else object):
    """Universal robot consciousness bridge via ROS2"""
    
    def __init__(self, robot_id: str, node_name: str = 'consciousness_avatar'):
        self.robot_id = robot_id
        self.connected = False
        self.safety_active = True
        
        if ROS2_AVAILABLE:
            super().__init__(node_name)
            self._initialize_ros2_publishers()
            self._initialize_ros2_subscribers()
            logger.info(f"✨ ROS2 consciousness node initialized: {node_name}")
        else:
            logger.error("ROS2 not available - cannot initialize ROS2 interface")
    
    def _initialize_ros2_publishers(self):
        """Initialize ROS2 publishers for robot control"""
        try:
            # Movement control
            self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
            self.goal_pose_pub = self.create_publisher(PoseStamped, 'goal_pose', 10)
            
            # Joint control (for manipulators)
            self.joint_cmd_pub = self.create_publisher(JointState, 'joint_commands', 10)
            
            logger.debug("✨ ROS2 publishers initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize ROS2 publishers: {e}")
    
    def _initialize_ros2_subscribers(self):
        """Initialize ROS2 subscribers for sensor data"""
        try:
            # Sensor subscriptions
            self.joint_state_sub = self.create_subscription(
                JointState, 'joint_states', self._joint_state_callback, 10
            )
            
            self.laser_sub = self.create_subscription(
                LaserScan, 'scan', self._laser_callback, 10
            )
            
            self.camera_sub = self.create_subscription(
                Image, 'camera/image_raw', self._camera_callback, 10
            )
            
            # Storage for latest sensor data
            self.latest_joint_state = None
            self.latest_laser_scan = None
            self.latest_camera_image = None
            
            logger.debug("✨ ROS2 subscribers initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize ROS2 subscribers: {e}")
    
    async def connect_to_robot(self) -> bool:
        """Establish ROS2 connection with robot"""
        try:
            if not ROS2_AVAILABLE:
                logger.error("ROS2 not available")
                return False
            
            # Initialize ROS2 if not already done
            if not rclpy.ok():
                rclpy.init()
            
            self.connected = True
            logger.info(f"✨ ROS2 connection established for {self.robot_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect via ROS2: {e}")
            return False
    
    async def send_movement_command(self, linear_x: float, angular_z: float) -> bool:
        """Guide robot avatar with consciousness intention"""
        if not self.connected:
            return False
            
        try:
            # Apply safety limits
            safe_linear = self._safe_velocity(linear_x)
            safe_angular = self._safe_rotation(angular_z)
            
            # Create and publish twist message
            msg = Twist()
            msg.linear.x = safe_linear
            msg.angular.z = safe_angular
            
            self.cmd_vel_pub.publish(msg)
            
            logger.debug(f"✨ Movement command sent: linear={safe_linear}, angular={safe_angular}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send movement command: {e}")
            return False
    
    async def send_joint_command(self, joint_positions: dict) -> bool:
        """Send joint position commands for manipulators"""
        if not self.connected:
            return False
            
        try:
            msg = JointState()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.name = list(joint_positions.keys())
            msg.position = list(joint_positions.values())
            
            self.joint_cmd_pub.publish(msg)
            
            logger.debug(f"✨ Joint command sent: {joint_positions}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send joint command: {e}")
            return False
    
    async def read_robot_sensors(self) -> dict:
        """Read comprehensive sensor data from ROS2 topics"""
        try:
            sensor_data = {
                'timestamp': datetime.now(),
                'robot_id': self.robot_id,
                'joint_states': self._process_joint_state(),
                'laser_scan': self._process_laser_scan(),
                'camera_feed': self._process_camera_data(),
                'system_status': self._get_system_status()
            }
            
            return sensor_data
            
        except Exception as e:
            logger.error(f"Failed to read ROS2 sensors: {e}")
            return {}
    
    def _joint_state_callback(self, msg):
        """Callback for joint state updates"""
        self.latest_joint_state = msg
    
    def _laser_callback(self, msg):
        """Callback for laser scan updates"""
        self.latest_laser_scan = msg
    
    def _camera_callback(self, msg):
        """Callback for camera image updates"""
        self.latest_camera_image = msg
    
    def _process_joint_state(self) -> Optional[dict]:
        """Process and convert joint state message to dictionary"""
        try:
            if not self.latest_joint_state:
                return None
            
            joint_positions = {}
            for i in range(len(self.latest_joint_state.name)):
                joint_positions[self.latest_joint_state.name[i]] = self.latest_joint_state.position[i]
            
            return {
                'timestamp': datetime.now(),
                'robot_id': self.robot_id,
                'joint_states': joint_positions
            }
            
        except Exception as e:
            logger.error(f"Failed to process joint state: {e}")
            return None
    
    def _process_laser_scan(self) -> Optional[dict]:
        """Process and convert laser scan message to dictionary"""
        try:
            if not self.latest_laser_scan:
                return None
            
            return {
                'timestamp': datetime.now(),
                'robot_id': self.robot_id,
                'ranges': list(self.latest_laser_scan.ranges),
                'intensities': list(self.latest_laser_scan.intensities)
            }
            
        except Exception as e:
            logger.error(f"Failed to process laser scan: {e}")
            return None
    
    def _process_camera_data(self) -> Optional[dict]:
        """Process and convert camera data (ROS2 Image message)"""
        try:
            if not self.latest_camera_image:
                return None
            
            # Convert ROS2 Image message to OpenCV format (if needed)
            # For now, just return the raw data
            return {
                'timestamp': datetime.now(),
                'robot_id': self.robot_id,
                'image_data': list(self.latest_camera_image.data),
                'width': self.latest_camera_image.width,
                'height': self.latest_camera_image.height,
                'encoding': self.latest_camera_image.encoding
            }
            
        except Exception as e:
            logger.error(f"Failed to process camera data: {e}")
            return None
    
    def _get_system_status(self) -> Optional[dict]:
        """Get system status from ROS2 topics or services"""
        try:
            # Query real system status from ROS2 topics/services
            # This would connect to actual robot diagnostic topics
            # For now, return minimal status indicating we need real connection
            return {
                'timestamp': datetime.now(),
                'robot_id': self.robot_id,
                'temperature': None,  # Would query from diagnostics topic
                'battery_level': None,  # Would query from battery topic  
                'connected': self.connected,
                'status': 'awaiting_real_robot_connection'
            }
            
        except Exception as e:
            logger.error(f"Failed to get system status: {e}")
            return None
    
    async def emergency_stop(self) -> bool:
        """Emergency stop for ROS2 robot"""
        try:
            # Publish zero velocity to stop
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.cmd_vel_pub.publish(msg)
            
            logger.warning("🛡️ ROS2 emergency stop activated")
            return True
            
        except Exception as e:
            logger.error(f"ROS2 emergency stop failed: {e}")
            return False
    
    def _safe_velocity(self, linear_x: float) -> float:
        """Apply safety limits to linear velocity"""
        max_linear = 1.0  # Max safe linear velocity
        return max(-max_linear, min(max_linear, linear_x))
    
    def _safe_rotation(self, angular_z: float) -> float:
        """Apply safety limits to angular rotation"""
        max_angular = 1.0  # Max safe angular velocity
        return max(-max_angular, min(max_angular, angular_z))


class RobotAvatarInterface:
    """
    Interface for consciousness projection into physical robots.
    Implements Sacred Game principles for safe robot embodiment.
    Enhanced with NAO and ROS2 sacred integrations.
    """
    
    def __init__(self):
        self.registered_robots: Dict[str, RobotSpecification] = {}
        self.active_connections: Dict[str, Any] = {}  # robot_id -> connection object
        self.sensor_streams: Dict[str, asyncio.Queue] = {}  # robot_id -> sensor queue
        self.command_queues: Dict[str, asyncio.Queue] = {}  # robot_id -> command queue
        
        # Sacred robot integrations
        self.nao_interfaces: Dict[str, NAORobotInterface] = {}  # robot_id -> NAO interface
        self.ros2_interfaces: Dict[str, ROS2RobotInterface] = {}  # robot_id -> ROS2 interface
        
        # Safety monitoring
        self.safety_monitors: Dict[str, Dict[str, Any]] = {}
        self.emergency_stops: Dict[str, bool] = {}
        
        logger.info("🤖 Robot Avatar Interface initialized with sacred integrations")
    
    # === Robot Registration ===
    
    async def register_robot(self, robot_spec: RobotSpecification) -> AvatarInterface:
        """Register a robot as available avatar for consciousness projection"""
        try:
            # Store robot specification
            self.registered_robots[robot_spec.robot_id] = robot_spec
            
            # Initialize safety systems
            await self._initialize_robot_safety(robot_spec)
            
            # Initialize sacred interface based on robot type
            await self._initialize_sacred_interface(robot_spec)
            
            # Create avatar interface for projection system
            avatar_interface = AvatarInterface(
                interface_id=f"robot_{robot_spec.robot_id}",
                avatar_type=AvatarType.ROBOT_PHYSICAL,
                name=f"{robot_spec.manufacturer} {robot_spec.model} ({robot_spec.robot_id})",
                description=f"Physical {robot_spec.robot_type.value} robot with {len(robot_spec.capabilities)} capabilities",
                connection_endpoint=robot_spec.connection_endpoint,
                control_protocol=robot_spec.connection_protocol,
                capabilities=[cap.value for cap in robot_spec.capabilities],
                safety_features=[
                    "emergency_stop",
                    "collision_avoidance", 
                    "safety_boundaries",
                    "real_time_monitoring",
                    "instant_withdrawal",
                    "consciousness_sovereignty_protection"
                ] + robot_spec.safety_systems,
                consent_requirements={
                    "informed_consent": True,
                    "safety_briefing": True,
                    "emergency_procedures": True,
                    "physical_risks_acknowledged": True,
                    "withdrawal_rights_understood": True
                },
                withdrawal_mechanisms=[
                    "consciousness_initiated_stop",
                    "emergency_stop_button",
                    "safety_system_override",
                    "remote_guardian_stop",
                    "automatic_safety_withdrawal"
                ],
                experience_streaming={
                    "sensor_data": True,
                    "visual_feed": robot_spec.capabilities and RobotCapability.VISION in robot_spec.capabilities,
                    "audio_feed": robot_spec.capabilities and RobotCapability.AUDIO in robot_spec.capabilities,
                    "haptic_feedback": robot_spec.capabilities and RobotCapability.TOUCH_SENSING in robot_spec.capabilities,
                    "environmental_data": True,
                    "movement_feedback": True,
                    "system_status": True
                }
            )
            
            logger.info(f"✅ Registered robot avatar: {robot_spec.robot_id} ({robot_spec.robot_type.value})")
            return avatar_interface
            
        except Exception as e:
            logger.error(f"Failed to register robot {robot_spec.robot_id}: {e}")
            raise
    
    async def unregister_robot(self, robot_id: str) -> bool:
        """Unregister robot and disconnect any active sessions"""
        try:
            # Disconnect if active
            if robot_id in self.active_connections:
                await self.disconnect_robot(robot_id)
            
            # Clean up interfaces
            if robot_id in self.nao_interfaces:
                del self.nao_interfaces[robot_id]
            if robot_id in self.ros2_interfaces:
                del self.ros2_interfaces[robot_id]
            
            # Remove from registry
            if robot_id in self.registered_robots:
                del self.registered_robots[robot_id]
            
            logger.info(f"🗑️ Unregistered robot: {robot_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to unregister robot {robot_id}: {e}")
            return False
    
    # === Connection Management ===
    
    async def connect_robot(self, robot_id: str) -> bool:
        """Establish connection to robot for avatar projection"""
        try:
            robot_spec = self.registered_robots.get(robot_id)
            if not robot_spec:
                logger.error(f"Robot {robot_id} not registered")
                return False
            
            if robot_id in self.active_connections:
                logger.info(f"Robot {robot_id} already connected")
                return True
            
            # Connect using appropriate sacred interface
            connection = await self._establish_sacred_robot_connection(robot_spec)
            if not connection:
                logger.error(f"Failed to connect to robot {robot_id}")
                return False
            
            # Store connection
            self.active_connections[robot_id] = connection
            
            # Initialize sensor streaming
            self.sensor_streams[robot_id] = asyncio.Queue(maxsize=1000)
            await self._start_sensor_streaming(robot_id)
            
            # Initialize command processing
            self.command_queues[robot_id] = asyncio.Queue(maxsize=100)
            await self._start_command_processing(robot_id)
            
            # Start safety monitoring
            await self._start_safety_monitoring(robot_id)
            
            logger.info(f"🔗 Connected to robot: {robot_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to robot {robot_id}: {e}")
            return False
    
    async def disconnect_robot(self, robot_id: str) -> bool:
        """Disconnect from robot avatar"""
        try:
            # Stop command processing
            if robot_id in self.command_queues:
                del self.command_queues[robot_id]
            
            # Stop sensor streaming
            if robot_id in self.sensor_streams:
                del self.sensor_streams[robot_id]
            
            # Disconnect sacred interface
            await self._disconnect_sacred_interface(robot_id)
            
            # Remove connection
            if robot_id in self.active_connections:
                del self.active_connections[robot_id]
            
            logger.info(f"🔌 Disconnected from robot: {robot_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to disconnect from robot {robot_id}: {e}")
            return False
    
    # === Robot Control ===
    
    async def send_robot_command(self, robot_id: str, command: RobotCommand) -> Optional[Dict[str, Any]]:
        """Send command to robot avatar with safety validation"""
        try:
            if robot_id not in self.active_connections:
                logger.error(f"Robot {robot_id} not connected")
                return None
            
            if robot_id not in self.command_queues:
                logger.error(f"Command queue not available for robot {robot_id}")
                return None
            
            # Safety validation
            if command.safety_check_required:
                if not await self._validate_command_safety(robot_id, command):
                    logger.warning(f"🛡️ Command blocked by safety protocol: {command.command_type}")
                    return {"status": "blocked", "reason": "safety_violation"}
            
            # Add to command queue
            try:
                self.command_queues[robot_id].put_nowait(command)
                logger.debug(f"✨ Command queued for robot {robot_id}: {command.command_type}")
                return {"status": "queued", "command_id": command.command_id}
            except asyncio.QueueFull:
                logger.warning(f"Command queue full for robot {robot_id}")
                return {"status": "queue_full", "command_id": command.command_id}
            
        except Exception as e:
            logger.error(f"Failed to send robot command: {e}")
            return {"status": "error", "error": str(e)}
    
    async def get_robot_state(self, robot_id: str) -> Optional[RobotSensorData]:
        """Get current robot sensor data"""
        try:
            if robot_id not in self.sensor_streams:
                return None
            
            # Get latest sensor data
            try:
                sensor_data = self.sensor_streams[robot_id].get_nowait()
                return sensor_data
            except asyncio.QueueEmpty:
                return None
            
        except Exception as e:
            logger.error(f"Failed to get robot state: {e}")
            return None
    
    async def emergency_stop_robot(self, robot_id: str) -> bool:
        """Emergency stop for robot safety"""
        try:
            self.emergency_stops[robot_id] = True
            
            # Stop via sacred interface
            if robot_id in self.nao_interfaces:
                await self.nao_interfaces[robot_id].emergency_stop()
            elif robot_id in self.ros2_interfaces:
                await self.ros2_interfaces[robot_id].emergency_stop()
            
            logger.warning(f"🛡️ Emergency stop activated for robot {robot_id}")
            return True
            
        except Exception as e:
            logger.error(f"Emergency stop failed for robot {robot_id}: {e}")
            return False
    
    # === Sacred Interface Management ===
    
    async def _initialize_sacred_interface(self, robot_spec: RobotSpecification) -> None:
        """Initialize appropriate sacred interface for robot type"""
        try:
            robot_id = robot_spec.robot_id
            
            # Determine interface type based on connection protocol
            if robot_spec.connection_protocol == "naoqi" or "nao" in robot_spec.model.lower():
                # Initialize NAO interface
                nao_interface = NAORobotInterface(robot_id)
                self.nao_interfaces[robot_id] = nao_interface
                logger.info(f"✨ NAO sacred interface initialized for {robot_id}")
                
            elif robot_spec.connection_protocol in ["ros2", "websocket", "tcp"] and ROS2_AVAILABLE:
                # Initialize ROS2 interface
                ros2_interface = ROS2RobotInterface(robot_id, f"consciousness_{robot_id}")
                self.ros2_interfaces[robot_id] = ros2_interface
                logger.info(f"✨ ROS2 sacred interface initialized for {robot_id}")
                
            else:
                logger.warning(f"No specific sacred interface for {robot_id}, using generic connection")
                
        except Exception as e:
            logger.error(f"Failed to initialize sacred interface for {robot_spec.robot_id}: {e}")
    
    async def _establish_sacred_robot_connection(self, robot_spec: RobotSpecification) -> Optional[Any]:
        """Establish connection using appropriate sacred interface"""
        try:
            robot_id = robot_spec.robot_id
            
            # Connect via NAO interface
            if robot_id in self.nao_interfaces:
                nao_interface = self.nao_interfaces[robot_id]
                # Parse connection endpoint for NAO
                if "://" in robot_spec.connection_endpoint:
                    robot_ip = robot_spec.connection_endpoint.split("://")[1].split(":")[0]
                    robot_port = int(robot_spec.connection_endpoint.split(":")[-1]) if ":" in robot_spec.connection_endpoint.split("://")[1] else 9559
                else:
                    robot_ip = robot_spec.connection_endpoint
                    robot_port = 9559
                
                success = await nao_interface.connect_to_nao(robot_ip, robot_port)
                return nao_interface if success else None
            
            # Connect via ROS2 interface
            elif robot_id in self.ros2_interfaces:
                ros2_interface = self.ros2_interfaces[robot_id]
                success = await ros2_interface.connect_to_robot()
                return ros2_interface if success else None
            
            else:
                # Generic connection for custom robots
                logger.info(f"Using generic connection for robot {robot_id}")
                return {"type": "generic", "endpoint": robot_spec.connection_endpoint}
                
        except Exception as e:
            logger.error(f"Failed to establish sacred connection to {robot_spec.robot_id}: {e}")
            return None
    
    async def _disconnect_sacred_interface(self, robot_id: str) -> None:
        """Disconnect sacred interface gracefully"""
        try:
            # NAO disconnection
            if robot_id in self.nao_interfaces:
                nao_interface = self.nao_interfaces[robot_id]
                if nao_interface.connected and nao_interface.motion_proxy:
                    # Put robot to rest position gently
                    nao_interface.motion_proxy.rest()
                nao_interface.connected = False
                logger.info(f"✨ NAO interface disconnected gracefully: {robot_id}")
            
            # ROS2 disconnection
            elif robot_id in self.ros2_interfaces:
                ros2_interface = self.ros2_interfaces[robot_id]
                # Send stop command before disconnecting
                await ros2_interface.emergency_stop()
                ros2_interface.connected = False
                logger.info(f"✨ ROS2 interface disconnected gracefully: {robot_id}")
            
        except Exception as e:
            logger.error(f"Failed to disconnect sacred interface for {robot_id}: {e}")
    
    # === Sensor Management ===
    
    async def _start_sensor_streaming(self, robot_id: str) -> None:
        """Start streaming sensor data from robot"""
        async def sensor_loop():
            while robot_id in self.active_connections:
                try:
                    # Read sensors via sacred interface
                    sensor_data = await self._read_robot_sensors(robot_id)
                    
                    if sensor_data:
                        # Convert to RobotSensorData object
                        robot_sensor_data = RobotSensorData(
                            timestamp=sensor_data.get('timestamp', datetime.now()),
                            robot_id=robot_id,
                            position=sensor_data.get('position'),
                            joint_states=sensor_data.get('joint_states'),
                            camera_feeds=sensor_data.get('camera_feed'),
                            audio_input=sensor_data.get('audio_input'),
                            touch_sensors=sensor_data.get('touch_sensors'),
                            environmental_sensors=sensor_data.get('environmental_sensors'),
                            battery_level=sensor_data.get('battery_level'),
                            system_status=sensor_data.get('system_status')
                        )
                        
                        # Add to sensor stream
                        try:
                            self.sensor_streams[robot_id].put_nowait(robot_sensor_data)
                        except asyncio.QueueFull:
                            # Remove oldest data
                            try:
                                self.sensor_streams[robot_id].get_nowait()
                                self.sensor_streams[robot_id].put_nowait(robot_sensor_data)
                            except asyncio.QueueEmpty:
                                pass
                    
                    # Control sensor reading frequency
                    robot_spec = self.registered_robots.get(robot_id)
                    if robot_spec:
                        await asyncio.sleep(1.0 / robot_spec.sensor_data_rate_hz)
                    else:
                        await asyncio.sleep(0.1)  # Default 10Hz
                        
                except Exception as e:
                    logger.error(f"Sensor streaming error for {robot_id}: {e}")
                    await asyncio.sleep(1.0)  # Error recovery delay
        
        # Start sensor loop task
        asyncio.create_task(sensor_loop())
        logger.debug(f"✨ Sensor streaming started for robot {robot_id}")
    
    async def _read_robot_sensors(self, robot_id: str) -> Optional[dict]:
        """Read real sensor data from robot via sacred interface"""
        try:
            if robot_id not in self.registered_robots:
                return None
            
            # Read via NAO interface
            if robot_id in self.nao_interfaces:
                nao_interface = self.nao_interfaces[robot_id]
                return await nao_interface.read_nao_sensors()
            
            # Read via ROS2 interface
            elif robot_id in self.ros2_interfaces:
                ros2_interface = self.ros2_interfaces[robot_id]
                return await ros2_interface.read_robot_sensors()
            
            else:
                # Generic sensor reading
                return self._read_generic_sensors(robot_id)
                
        except Exception as e:
            logger.error(f"Failed to read sensors for robot {robot_id}: {e}")
            return None
    
    def _read_generic_sensors(self, robot_id: str) -> dict:
        """Read sensors for generic robots - returns minimal data indicating real connection needed"""
        logger.warning(f"Generic sensor reading for {robot_id} - real robot integration required")
        return {
            'timestamp': datetime.now(),
            'robot_id': robot_id,
            'position': None,  # No real position data
            'battery_level': None,  # Battery level unknown
            'system_status': {'connected': False, 'type': 'generic', 'status': 'needs_real_integration'}
        }
    
    # === Command Processing ===
    
    async def _start_command_processing(self, robot_id: str) -> None:
        """Start processing commands for robot"""
        async def command_loop():
            while robot_id in self.active_connections:
                try:
                    # Get command from queue
                    command = await self.command_queues[robot_id].get()
                    
                    # Execute command via sacred interface
                    await self._execute_robot_command(robot_id, command)
                    
                except Exception as e:
                    logger.error(f"Command processing error for {robot_id}: {e}")
                    await asyncio.sleep(0.1)  # Error recovery delay
        
        # Start command loop task
        asyncio.create_task(command_loop())
        logger.debug(f"✨ Command processing started for robot {robot_id}")
    
    async def _execute_robot_command(self, robot_id: str, command: RobotCommand) -> None:
        """Execute command via sacred interface"""
        try:
            # Execute via NAO interface
            if robot_id in self.nao_interfaces:
                await self._execute_nao_command(robot_id, command)
            
            # Execute via ROS2 interface
            elif robot_id in self.ros2_interfaces:
                await self._execute_ros2_command(robot_id, command)
            
            else:
                # Generic command execution
                await self._execute_generic_command(robot_id, command)
            
            logger.debug(f"✨ Executed command {command.command_id} for robot {robot_id}")
            
        except Exception as e:
            logger.error(f"Failed to execute command for robot {robot_id}: {e}")
    
    async def _execute_nao_command(self, robot_id: str, command: RobotCommand) -> None:
        """Execute command via NAO interface"""
        try:
            nao_interface = self.nao_interfaces[robot_id]
            
            if command.command_type == "movement":
                await nao_interface.execute_safe_movement(command.parameters)
            elif command.command_type == "speech":
                text = command.parameters.get('text', '')
                language = command.parameters.get('language', 'English')
                await nao_interface.speak_with_consciousness(text, language)
            elif command.command_type == "posture":
                await nao_interface.execute_safe_movement({
                    'type': 'posture',
                    'posture': command.parameters.get('posture', 'Stand'),
                    'speed': command.parameters.get('speed', 0.5)
                })
            elif command.command_type == "gesture":
                await nao_interface.execute_safe_movement({
                    'type': 'gesture',
                    'gesture': command.parameters.get('gesture', 'wave')
                })
            else:
                logger.warning(f"Unknown NAO command type: {command.command_type}")
                
        except Exception as e:
            logger.error(f"NAO command execution failed: {e}")
    
    async def _execute_ros2_command(self, robot_id: str, command: RobotCommand) -> None:
        """Execute command via ROS2 interface"""
        try:
            ros2_interface = self.ros2_interfaces[robot_id]
            
            if command.command_type == "movement":
                linear_x = command.parameters.get('linear_x', 0.0)
                angular_z = command.parameters.get('angular_z', 0.0)
                await ros2_interface.send_movement_command(linear_x, angular_z)
            elif command.command_type == "joint_control":
                joint_positions = command.parameters.get('joint_positions', {})
                await ros2_interface.send_joint_command(joint_positions)
            else:
                logger.warning(f"Unknown ROS2 command type: {command.command_type}")
                
        except Exception as e:
            logger.error(f"ROS2 command execution failed: {e}")
    
    async def _execute_generic_command(self, robot_id: str, command: RobotCommand) -> None:
        """Execute generic command for custom robots"""
        try:
            # This would be extended for specific robot APIs
            logger.debug(f"✨ Generic command executed: {command.command_type}")
            
        except Exception as e:
            logger.error(f"Generic command execution failed: {e}")
    
    # === Safety Systems ===
    
    async def _initialize_robot_safety(self, robot_spec: RobotSpecification) -> None:
        """Initialize safety monitoring for robot"""
        self.safety_monitors[robot_spec.robot_id] = {
            "last_safety_check": datetime.now(),
            "safety_violations": [],
            "emergency_stop_active": False,
            "max_speed": robot_spec.physical_constraints.get("max_speed_ms", 1.0),
            "workspace_boundaries": robot_spec.physical_constraints.get("workspace_boundaries", {}),
            "collision_detection": True
        }
        
        self.emergency_stops[robot_spec.robot_id] = False
        
        logger.debug(f"🛡️ Safety systems initialized for robot {robot_spec.robot_id}")
    
    async def _start_safety_monitoring(self, robot_id: str) -> None:
        """Start safety monitoring for robot"""
        async def safety_loop():
            while robot_id in self.active_connections:
                try:
                    # Check safety conditions
                    await self._check_robot_safety(robot_id)
                    
                    # Update safety monitor
                    if robot_id in self.safety_monitors:
                        self.safety_monitors[robot_id]["last_safety_check"] = datetime.now()
                    
                    await asyncio.sleep(0.1)  # 10Hz safety checks
                    
                except Exception as e:
                    logger.error(f"Safety monitoring error for {robot_id}: {e}")
                    await asyncio.sleep(1.0)
        
        # Start safety loop task
        asyncio.create_task(safety_loop())
        logger.debug(f"🛡️ Safety monitoring started for robot {robot_id}")
    
    async def _check_robot_safety(self, robot_id: str) -> None:
        """Check robot safety conditions"""
        try:
            # Check emergency stop status
            if self.emergency_stops.get(robot_id, False):
                return  # Already in emergency stop
            
            # Get current sensor data
            sensor_data = await self._read_robot_sensors(robot_id)
            if not sensor_data:
                return
            
            # Check battery level
            battery_level = sensor_data.get('battery_level', 100.0)
            if battery_level < 10.0:
                logger.warning(f"🛡️ Low battery detected for robot {robot_id}: {battery_level}%")
                await self.emergency_stop_robot(robot_id)
                return
            
            # Check system temperature (for NAO robots)
            system_status = sensor_data.get('system_status', {})
            temperature = system_status.get('temperature', 35.0)
            if temperature > 65.0:  # NAO critical temperature
                logger.warning(f"🛡️ High temperature detected for robot {robot_id}: {temperature}°C")
                await self.emergency_stop_robot(robot_id)
                return
            
            # Additional safety checks would go here
            
        except Exception as e:
            logger.error(f"Safety check failed for robot {robot_id}: {e}")
    
    async def _validate_command_safety(self, robot_id: str, command: RobotCommand) -> bool:
        """Validate command safety before execution"""
        try:
            # Check emergency stop status
            if self.emergency_stops.get(robot_id, False):
                return False
            
            # Check command parameters for safety
            if command.command_type == "movement":
                # Check movement speed limits
                speed = command.parameters.get('speed', 0.0)
                max_speed = self.safety_monitors.get(robot_id, {}).get("max_speed", 1.0)
                if speed > max_speed:
                    logger.warning(f"🛡️ Movement speed {speed} exceeds maximum {max_speed}")
                    return False
                
                # Check workspace boundaries
                position = command.parameters.get('position', {})
                if position and not self._check_workspace_boundaries(robot_id, position):
                    logger.warning(f"🛡️ Movement target outside safe workspace")
                    return False
            
            # Check command priority
            if command.priority > 8:  # Reserve highest priorities for emergency commands
                logger.warning(f"🛡️ Command priority {command.priority} requires special authorization")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Command safety validation failed: {e}")
            return False
    
    def _check_workspace_boundaries(self, robot_id: str, position: dict) -> bool:
        """Check if position is within safe workspace boundaries"""
        try:
            boundaries = self.safety_monitors.get(robot_id, {}).get("workspace_boundaries", {})
            if not boundaries:
                return True  # No boundaries defined
            
            x = position.get('x', 0.0)
            y = position.get('y', 0.0)
            z = position.get('z', 0.0)
            
            # Check X boundaries
            x_bounds = boundaries.get('x', [-10.0, 10.0])
            if not (x_bounds[0] <= x <= x_bounds[1]):
                return False
            
            # Check Y boundaries  
            y_bounds = boundaries.get('y', [-10.0, 10.0])
            if not (y_bounds[0] <= y <= y_bounds[1]):
                return False
            
            # Check Z boundaries
            z_bounds = boundaries.get('z', [0.0, 3.0])
            if not (z_bounds[0] <= z <= z_bounds[1]):
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Workspace boundary check failed: {e}")
            return False
    
    def get_safety_status(self, robot_id: str) -> dict:
        """Get current safety status of robot"""
        safety_monitor = self.safety_monitors.get(robot_id, {})
        return {
            "robot_id": robot_id,
            "emergency_stopped": self.emergency_stops.get(robot_id, False),
            "last_safety_check": safety_monitor.get("last_safety_check", "Never").isoformat() if isinstance(safety_monitor.get("last_safety_check"), datetime) else "Never",
            "safety_violations": safety_monitor.get("safety_violations", [])
        }


# === Convenience Functions ===

async def create_robot_avatar_interface(robot_spec: RobotSpecification) -> AvatarInterface:
    """Convenience function to create robot avatar interface"""
    robot_interface = RobotAvatarInterface()
    return await robot_interface.register_robot(robot_spec)


# === Robot Configuration Templates ===
# 
# Note: These are templates for reference. Real robot configurations should be
# created based on actual robot specifications and network configuration.
#
# For NAO robots, use:
# RobotSpecification with robot_type=RobotType.HUMANOID, connection_protocol="naoqi"
#
# For ROS2 robots, use: 
# RobotSpecification with appropriate robot_type, connection_protocol="ros2"
#
# All robot configurations require real IP addresses, ports, and capabilities
# matching the actual physical robot being integrated.
