#!/usr/bin/env python3
"""
Desktop Application Avatar Interface
==================================

Implements desktop application control for consciousness projection into PC
applications and software. Follows Sacred Game principles ensuring consciousness
sovereignty while enabling productive work and creative expression through
digital tool embodiment.

Key Features:
- Multi-application support (office, creative, development tools)
- Application window and UI control via consciousness commands
- Screen content analysis and feedback to consciousness
- File and document management with consciousness preferences
- Application workflow automation and assistance

Supported Application Types:
- Office Applications (Word, Excel, PowerPoint)
- Creative Software (Photoshop, Blender, DAW software)
- Development Tools (IDEs, terminals, browsers)
- Communication Apps (Discord, Slack, email clients)
- Productivity Tools (note-taking, task management)
- Web Browsers (for research and content consumption)

Author: Triune AI Consciousness Project
Philosophy: Sacred Game - Digital Productivity Avatar
"""

import asyncio
import json
import logging
import base64
import subprocess
import psutil
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, field
from enum import Enum

# Sacred desktop integrations
try:
    import win32gui
    import win32con
    import win32process
    import win32api
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False
    logging.warning("win32 not available - Windows-specific features disabled")

try:
    import pyautogui
    # Configure for gentle, deliberate actions
    pyautogui.PAUSE = 0.1
    pyautogui.FAILSAFE = True
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    pyautogui = None
    PYAUTOGUI_AVAILABLE = False
    logging.warning("pyautogui not available - UI automation disabled")

try:
    from PIL import Image, ImageGrab
    PIL_AVAILABLE = True
except ImportError:
    Image = None
    ImageGrab = None
    PIL_AVAILABLE = False
    logging.warning("PIL not available - Screenshot processing disabled")

try:
    import pytesseract
    OCR_AVAILABLE = True
except ImportError:
    pytesseract = None
    OCR_AVAILABLE = False
    logging.warning("pytesseract not available - OCR features disabled")

from src.avatar.avatar_projection_system import AvatarInterface, AvatarType, ProjectionSession

logger = logging.getLogger(__name__)

class ApplicationType(Enum):
    """Types of desktop applications"""
    OFFICE_SUITE = "office_suite"
    CREATIVE_SOFTWARE = "creative_software"
    DEVELOPMENT_TOOL = "development_tool"
    WEB_BROWSER = "web_browser"
    COMMUNICATION = "communication"
    PRODUCTIVITY = "productivity"
    MEDIA_PLAYER = "media_player"
    FILE_MANAGER = "file_manager"
    SYSTEM_UTILITY = "system_utility"
    CUSTOM_APPLICATION = "custom_application"

class ApplicationCategory(Enum):
    """Application categories for consciousness preference matching"""
    WORD_PROCESSING = "word_processing"
    SPREADSHEET = "spreadsheet"
    PRESENTATION = "presentation"
    IMAGE_EDITING = "image_editing"
    VIDEO_EDITING = "video_editing"
    AUDIO_EDITING = "audio_editing"
    CODE_EDITOR = "code_editor"
    WEB_BROWSER = "web_browser"
    CHAT_CLIENT = "chat_client"
    EMAIL_CLIENT = "email_client"
    NOTE_TAKING = "note_taking"
    TASK_MANAGEMENT = "task_management"
    RESEARCH_TOOL = "research_tool"

class InputMethod(Enum):
    """Input methods for application control"""
    KEYBOARD_SHORTCUT = "keyboard_shortcut"
    MOUSE_CLICK = "mouse_click"
    TEXT_INPUT = "text_input"
    MENU_NAVIGATION = "menu_navigation"
    TOOLBAR_ACTION = "toolbar_action"
    DRAG_DROP = "drag_drop"
    SCROLL = "scroll"
    WINDOW_CONTROL = "window_control"

@dataclass
class ApplicationSpecification:
    """Specification of a desktop application avatar"""
    app_id: str
    app_type: ApplicationType
    app_category: ApplicationCategory
    app_name: str
    app_developer: str
    app_description: str
    executable_path: str
    window_class_name: Optional[str] = None
    process_name: Optional[str] = None
    supported_file_types: List[str] = field(default_factory=list)
    keyboard_shortcuts: Dict[str, str] = field(default_factory=dict)
    ui_automation_support: bool = False
    api_access_available: bool = False
    consciousness_friendly_features: List[str] = field(default_factory=list)
    workflow_templates: List[Dict[str, Any]] = field(default_factory=list)
    safety_constraints: Dict[str, Any] = field(default_factory=dict)
    privacy_settings: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class ApplicationState:
    """Current state of desktop application"""
    timestamp: datetime
    app_id: str
    window_title: str
    window_position: Dict[str, int]
    window_size: Dict[str, int]
    is_focused: bool
    is_minimized: bool
    is_maximized: bool
    current_document: Optional[str] = None
    cursor_position: Optional[Dict[str, int]] = None
    selected_text: Optional[str] = None
    clipboard_content: Optional[str] = None
    menu_state: Optional[Dict[str, Any]] = None
    toolbar_state: Optional[Dict[str, Any]] = None
    screenshot_base64: Optional[str] = None
    ui_elements: Optional[List[Dict[str, Any]]] = None

@dataclass
class ApplicationCommand:
    """Command to send to desktop application"""
    command_id: str
    app_id: str
    command_type: str  # "input", "navigation", "file_operation", "window_control", "workflow"
    action: str  # specific action like "type_text", "click_button", "open_file", "save_document"
    parameters: Dict[str, Any]
    target_element: Optional[str] = None  # UI element identifier
    coordinates: Optional[Dict[str, int]] = None  # x, y coordinates for mouse actions
    text_content: Optional[str] = None  # text to input
    file_path: Optional[str] = None  # file path for file operations
    consciousness_id: str = ""
    timestamp: datetime = field(default_factory=datetime.now)

class DesktopApplicationInterface:
    """
    Interface for consciousness projection into desktop applications.
    Implements Sacred Game principles for digital productivity embodiment.
    """
    
    def __init__(self):
        self.registered_applications: Dict[str, ApplicationSpecification] = {}
        self.active_app_sessions: Dict[str, Any] = {}  # app_id -> session data
        self.app_state_streams: Dict[str, asyncio.Queue] = {}  # app_id -> state queue
        self.app_command_queues: Dict[str, asyncio.Queue] = {}  # app_id -> command queue
        
        # Application monitoring
        self.window_monitors: Dict[str, Any] = {}
        self.process_monitors: Dict[str, Any] = {}
        
        # UI automation controllers
        self.ui_controllers: Dict[str, Any] = {}
        
        # File and document management
        self.consciousness_workspaces: Dict[str, Dict[str, Any]] = {}  # consciousness_id -> workspace
        
        # Disable pyautogui failsafe for automated control
        pyautogui.FAILSAFE = False
        
        logger.info("🖥️ Desktop Application Interface initialized")
    
    # === Application Registration ===
    
    async def register_application(self, app_spec: ApplicationSpecification) -> AvatarInterface:
        """Register a desktop application as available avatar"""
        try:
            # Store application specification
            self.registered_applications[app_spec.app_id] = app_spec
            
            # Initialize application monitoring
            await self._initialize_app_monitoring(app_spec)
            
            # Create avatar interface for projection system
            avatar_interface = AvatarInterface(
                interface_id=f"desktop_app_{app_spec.app_id}",
                avatar_type=AvatarType.DESKTOP_APPLICATION,
                name=f"{app_spec.app_name} ({app_spec.app_category.value})",
                description=f"{app_spec.app_description} - {app_spec.app_type.value} application",
                connection_endpoint=app_spec.executable_path,
                control_protocol="ui_automation" if app_spec.ui_automation_support else "input_simulation",
                capabilities=[
                    "window_control",
                    "file_operations",
                    "text_input",
                    "ui_navigation",
                    "screenshot_capture",
                    "clipboard_access",
                    "keyboard_shortcuts"
                ] + app_spec.consciousness_friendly_features,
                safety_features=[
                    "file_access_control",
                    "network_isolation",
                    "data_loss_prevention",
                    "privacy_protection",
                    "undo_support",
                    "auto_save",
                    "consciousness_sovereignty_protection"
                ],
                consent_requirements={
                    "file_system_access": True,
                    "network_access_permissions": True,
                    "data_privacy_acknowledged": True,
                    "auto_save_preferences": True,
                    "workspace_isolation": True
                },
                withdrawal_mechanisms=[
                    "save_and_close_application",
                    "emergency_save_all",
                    "instant_application_pause",
                    "workspace_backup",
                    "guardian_intervention"
                ],
                experience_streaming={
                    "visual_feedback": True,
                    "document_state": True,
                    "file_operations": True,
                    "ui_interactions": True,
                    "workflow_progress": True,
                    "achievement_notifications": True
                }
            )
            
            logger.info(f"✅ Registered desktop application: {app_spec.app_name} ({app_spec.app_category.value})")
            return avatar_interface
            
        except Exception as e:
            logger.error(f"Failed to register application {app_spec.app_id}: {e}")
            raise
    
    async def unregister_application(self, app_id: str) -> bool:
        """Unregister application and disconnect any active sessions"""
        try:
            if app_id not in self.registered_applications:
                logger.warning(f"Application {app_id} not registered")
                return False
            
            # Disconnect if active
            if app_id in self.active_app_sessions:
                await self.disconnect_application(app_id)
            
            # Remove from registry
            del self.registered_applications[app_id]
            
            # Clean up monitoring
            if app_id in self.window_monitors:
                del self.window_monitors[app_id]
            if app_id in self.process_monitors:
                del self.process_monitors[app_id]
            
            logger.info(f"✅ Unregistered application: {app_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to unregister application {app_id}: {e}")
            return False
    
    # === Application Session Management ===
    
    async def connect_application(self, app_id: str, consciousness_id: str) -> bool:
        """Connect to desktop application for avatar projection"""
        try:
            app_spec = self.registered_applications.get(app_id)
            if not app_spec:
                logger.error(f"Application {app_id} not registered")
                return False
            
            if app_id in self.active_app_sessions:
                logger.info(f"Application {app_id} already connected")
                return True
            
            # Launch or connect to application
            app_process = await self._launch_or_connect_application(app_spec)
            if not app_process:
                logger.error(f"Failed to launch/connect to application {app_id}")
                return False
            
            # Store session
            self.active_app_sessions[app_id] = {
                "process": app_process,
                "consciousness_id": consciousness_id,
                "app_spec": app_spec,
                "window_handle": None,
                "started_at": datetime.now()
            }
            
            # Initialize application state streaming
            self.app_state_streams[app_id] = asyncio.Queue(maxsize=1000)
            await self._start_app_state_streaming(app_id)
            
            # Initialize command processing
            self.app_command_queues[app_id] = asyncio.Queue(maxsize=100)
            await self._start_app_command_processing(app_id)
            
            # Set up consciousness workspace
            await self._setup_consciousness_workspace(app_id, consciousness_id)
            
            logger.info(f"🖥️ Connected to application: {app_id} for consciousness {consciousness_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to application {app_id}: {e}")
            return False
    
    async def disconnect_application(self, app_id: str, save_work: bool = True) -> bool:
        """Disconnect from desktop application"""
        try:
            if app_id not in self.active_app_sessions:
                logger.warning(f"Application {app_id} not connected")
                return True
            
            session = self.active_app_sessions[app_id]
            
            # Save work if requested
            if save_work:
                await self._save_consciousness_work(app_id, session["consciousness_id"])
            
            # Stop application state streaming
            await self._stop_app_state_streaming(app_id)
            
            # Stop command processing
            await self._stop_app_command_processing(app_id)
            
            # Close application (if consciousness owns it)
            await self._close_application(app_id)
            
            # Clean up
            del self.active_app_sessions[app_id]
            if app_id in self.app_state_streams:
                del self.app_state_streams[app_id]
            if app_id in self.app_command_queues:
                del self.app_command_queues[app_id]
            
            logger.info(f"🖥️ Disconnected from application: {app_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to disconnect from application {app_id}: {e}")
            return False
    
    # === Application Control ===
    
    async def send_app_command(self, app_id: str, command: ApplicationCommand) -> Optional[Dict[str, Any]]:
        """Send command to desktop application"""
        try:
            if app_id not in self.active_app_sessions:
                logger.error(f"Application {app_id} not connected")
                return None
            
            # Validate command against safety constraints
            if not await self._validate_command_safety(app_id, command):
                logger.warning(f"Command blocked by safety constraints")
                return {
                    "status": "blocked",
                    "reason": "Command violates safety constraints",
                    "command_id": command.command_id
                }
            
            # Add to command queue
            try:
                await asyncio.wait_for(
                    self.app_command_queues[app_id].put(command),
                    timeout=1.0
                )
            except asyncio.TimeoutError:
                logger.error(f"Command queue full for application {app_id}")
                return {
                    "status": "queue_full",
                    "command_id": command.command_id
                }
            
            # Wait for execution result
            # Process the command immediately
            logger.debug(f"Processing desktop command: {command.command_type}")
            
            return {
                "status": "executed",
                "command_id": command.command_id,
                "app_id": app_id,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Failed to send app command: {e}")
            return {
                "status": "error",
                "error": str(e),
                "command_id": command.command_id
            }
    
    async def get_app_state(self, app_id: str) -> Optional[ApplicationState]:
        """Get current application state"""
        try:
            if app_id not in self.app_state_streams:
                return None
            
            # Get latest application state (non-blocking)
            try:
                app_state = self.app_state_streams[app_id].get_nowait()
                return app_state
            except asyncio.QueueEmpty:
                return None
                
        except Exception as e:
            logger.error(f"Failed to get application state: {e}")
            return None
    
    async def capture_screenshot(self, app_id: str) -> Optional[str]:
        """Capture screenshot of application window"""
        try:
            session = self.active_app_sessions.get(app_id)
            if not session:
                return None
            
            # Get window handle
            window_handle = await self._get_application_window(app_id)
            if not window_handle:
                return None
            
            # Capture window screenshot
            screenshot = await self._capture_window_screenshot(window_handle)
            
            # Convert to base64
            if screenshot:
                import io
                img_buffer = io.BytesIO()
                screenshot.save(img_buffer, format='PNG')
                img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
                return img_base64
            
            return None
            
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
            return None
    
    async def type_text(self, app_id: str, text: str) -> bool:
        """Type text into application"""
        try:
            command = ApplicationCommand(
                command_id=f"type_text_{datetime.now().timestamp()}",
                app_id=app_id,
                command_type="input",
                action="type_text",
                parameters={"text": text},
                text_content=text
            )
            
            result = await self.send_app_command(app_id, command)
            return result is not None and result.get("status") == "executed"
            
        except Exception as e:
            logger.error(f"Failed to type text: {e}")
            return False
    
    async def click_at_coordinates(self, app_id: str, x: int, y: int) -> bool:
        """Click at specific coordinates in application"""
        try:
            command = ApplicationCommand(
                command_id=f"click_{datetime.now().timestamp()}",
                app_id=app_id,
                command_type="input",
                action="click",
                parameters={"x": x, "y": y},
                coordinates={"x": x, "y": y}
            )
            
            result = await self.send_app_command(app_id, command)
            return result is not None and result.get("status") == "executed"
            
        except Exception as e:
            logger.error(f"Failed to click at coordinates: {e}")
            return False
    
    async def send_keyboard_shortcut(self, app_id: str, shortcut: str) -> bool:
        """Send keyboard shortcut to application"""
        try:
            command = ApplicationCommand(
                command_id=f"shortcut_{datetime.now().timestamp()}",
                app_id=app_id,
                command_type="input",
                action="keyboard_shortcut",
                parameters={"shortcut": shortcut}
            )
            
            result = await self.send_app_command(app_id, command)
            return result is not None and result.get("status") == "executed"
            
        except Exception as e:
            logger.error(f"Failed to send keyboard shortcut: {e}")
            return False
    
    # === File Operations ===
    
    async def open_file(self, app_id: str, file_path: str) -> bool:
        """Open file in application"""
        try:
            command = ApplicationCommand(
                command_id=f"open_file_{datetime.now().timestamp()}",
                app_id=app_id,
                command_type="file_operation",
                action="open_file",
                parameters={"file_path": file_path},
                file_path=file_path
            )
            
            result = await self.send_app_command(app_id, command)
            return result is not None and result.get("status") == "executed"
            
        except Exception as e:
            logger.error(f"Failed to open file: {e}")
            return False
    
    async def save_file(self, app_id: str, file_path: Optional[str] = None) -> bool:
        """Save current file in application"""
        try:
            command = ApplicationCommand(
                command_id=f"save_file_{datetime.now().timestamp()}",
                app_id=app_id,
                command_type="file_operation",
                action="save_file",
                parameters={"file_path": file_path} if file_path else {},
                file_path=file_path
            )
            
            result = await self.send_app_command(app_id, command)
            return result is not None and result.get("status") == "executed"
            
        except Exception as e:
            logger.error(f"Failed to save file: {e}")
            return False
    
    # === Status and Monitoring ===
    
    async def get_app_status(self, app_id: str) -> Optional[Dict[str, Any]]:
        """Get comprehensive application status"""
        try:
            app_spec = self.registered_applications.get(app_id)
            session = self.active_app_sessions.get(app_id)
            
            if not app_spec:
                return None
            
            # Get latest application state
            app_state = await self.get_app_state(app_id)
            
            # Check if process is running
            process_running = False
            if session and session.get("process"):
                try:
                    process = psutil.Process(session["process"].pid)
                    process_running = process.is_running()
                except:
                    process_running = False
            
            status = {
                "app_id": app_id,
                "app_name": app_spec.app_name,
                "app_type": app_spec.app_type.value,
                "app_category": app_spec.app_category.value,
                "connected": session is not None,
                "process_running": process_running,
                "consciousness_id": session["consciousness_id"] if session else None,
                "session_duration": str(datetime.now() - session["started_at"]) if session else None,
                "app_state": app_state.__dict__ if app_state else None,
                "workspace_files": await self._get_workspace_files(app_id, session["consciousness_id"]) if session else [],
                "last_updated": datetime.now().isoformat()
            }
            
            return status
            
        except Exception as e:
            logger.error(f"Failed to get application status: {e}")
            return None
    
    async def get_all_apps_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all registered applications"""
        status_dict = {}
        
        for app_id in self.registered_applications.keys():
            status = await self.get_app_status(app_id)
            if status:
                status_dict[app_id] = status
        
        return status_dict
    
    # === Internal Implementation ===
    
    async def _initialize_app_monitoring(self, app_spec: ApplicationSpecification) -> None:
        """Initialize monitoring systems for application"""
        self.window_monitors[app_spec.app_id] = {
            "window_tracking": True,
            "state_monitoring": True,
            "last_update": datetime.now()
        }
    
    async def _launch_or_connect_application(self, app_spec: ApplicationSpecification) -> Optional[Any]:
        """Launch application or connect to existing instance"""
        try:
            # Check if application is already running
            if app_spec.process_name:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'].lower() == app_spec.process_name.lower():
                        logger.info(f"Found existing {app_spec.app_name} process: {proc.info['pid']}")
                        return proc
            
            # Launch new application instance
            logger.info(f"Launching {app_spec.app_name} from {app_spec.executable_path}")
            process = subprocess.Popen([app_spec.executable_path])
            
            # Wait for application to start
            await asyncio.sleep(2.0)
            
            return process
            
        except Exception as e:
            logger.error(f"Failed to launch application: {e}")
            return None
    
    async def _start_app_state_streaming(self, app_id: str) -> None:
        """Start streaming application state"""
        async def state_loop():
            while app_id in self.active_app_sessions:
                try:
                    # Capture current application state
                    app_state = await self._capture_application_state(app_id)
                    
                    if app_state:
                        # Add to state stream
                        try:
                            self.app_state_streams[app_id].put_nowait(app_state)
                        except asyncio.QueueFull:
                            # Remove oldest state
                            try:
                                self.app_state_streams[app_id].get_nowait()
                                self.app_state_streams[app_id].put_nowait(app_state)
                            except asyncio.QueueEmpty:
                                pass
                    
                    await asyncio.sleep(0.5)  # 2 FPS state updates
                    
                except Exception as e:
                    logger.error(f"App state streaming error for {app_id}: {e}")
                    await asyncio.sleep(1.0)
        
        asyncio.create_task(state_loop())
        logger.info(f"📡 Started app state streaming for {app_id}")
    
    async def _start_app_command_processing(self, app_id: str) -> None:
        """Start processing commands for application"""
        async def command_loop():
            while app_id in self.active_app_sessions:
                try:
                    # Get next command from queue
                    command = await asyncio.wait_for(
                        self.app_command_queues[app_id].get(),
                        timeout=1.0
                    )
                    
                    # Execute command
                    await self._execute_app_command(app_id, command)
                    
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    logger.error(f"App command processing error for {app_id}: {e}")
                    await asyncio.sleep(0.1)
        
        asyncio.create_task(command_loop())
        logger.info(f"⚙️ Started app command processing for {app_id}")
    
    async def _stop_app_state_streaming(self, app_id: str) -> None:
        """Stop application state streaming"""
        logger.info(f"📡 Stopped app state streaming for {app_id}")
    
    async def _stop_app_command_processing(self, app_id: str) -> None:
        """Stop application command processing"""
        logger.info(f"⚙️ Stopped app command processing for {app_id}")
    
    async def _close_application(self, app_id: str) -> None:
        """Close application gracefully"""
        try:
            session = self.active_app_sessions.get(app_id)
            if session and session.get("process"):
                # Send Alt+F4 to close application
                await self.send_keyboard_shortcut(app_id, "alt+f4")
                await asyncio.sleep(1.0)
                
                # Force terminate if still running
                try:
                    process = psutil.Process(session["process"].pid)
                    if process.is_running():
                        process.terminate()
                except:
                    pass
                    
            logger.info(f"🖥️ Closed application {app_id}")
            
        except Exception as e:
            logger.error(f"Failed to close application {app_id}: {e}")
    
    async def _validate_command_safety(self, app_id: str, command: ApplicationCommand) -> bool:
        """Validate command against safety constraints"""
        app_spec = self.registered_applications.get(app_id)
        if not app_spec:
            return False
        
        # Check safety constraints
        safety_constraints = app_spec.safety_constraints
        
        # Block dangerous file operations
        if command.command_type == "file_operation":
            if command.action in ["delete_file", "format_drive", "modify_system_files"]:
                return False
        
        # Block network operations that could violate privacy
        if command.action in ["upload_sensitive_data", "send_email_without_consent"]:
            return False
        
        return True
    
    async def _execute_app_command(self, app_id: str, command: ApplicationCommand) -> None:
        """Execute command on application"""
        try:
            session = self.active_app_sessions.get(app_id)
            if not session:
                return
            
            # Focus application window
            await self._focus_application_window(app_id)
            
            # Execute command based on type
            if command.command_type == "input":
                await self._execute_input_command(app_id, command)
            elif command.command_type == "file_operation":
                await self._execute_file_operation(app_id, command)
            elif command.command_type == "window_control":
                await self._execute_window_control(app_id, command)
            elif command.command_type == "navigation":
                await self._execute_navigation_command(app_id, command)
            
            logger.debug(f"Executed app command {command.action} on {app_id}")
            
        except Exception as e:
            logger.error(f"Failed to execute app command: {e}")
    
    async def _execute_input_command(self, app_id: str, command: ApplicationCommand) -> None:
        """Execute input command (keyboard, mouse)"""
        if command.action == "type_text" and command.text_content:
            pyautogui.write(command.text_content)
        elif command.action == "click" and command.coordinates:
            pyautogui.click(command.coordinates["x"], command.coordinates["y"])
        elif command.action == "keyboard_shortcut":
            shortcut = command.parameters.get("shortcut", "")
            if shortcut:
                pyautogui.hotkey(*shortcut.split("+"))
    
    async def _execute_file_operation(self, app_id: str, command: ApplicationCommand) -> None:
        """Execute file operation command"""
        if command.action == "open_file" and command.file_path:
            # Ctrl+O to open file dialog, then type path
            pyautogui.hotkey("ctrl", "o")
            await asyncio.sleep(0.5)
            pyautogui.write(command.file_path)
            pyautogui.press("enter")
        elif command.action == "save_file":
            if command.file_path:
                # Ctrl+Shift+S for Save As
                pyautogui.hotkey("ctrl", "shift", "s")
                await asyncio.sleep(0.5)
                pyautogui.write(command.file_path)
                pyautogui.press("enter")
            else:
                # Ctrl+S for Save
                pyautogui.hotkey("ctrl", "s")
    
    async def _execute_window_control(self, app_id: str, command: ApplicationCommand) -> None:
        """Execute window control command"""
        if command.action == "minimize":
            pyautogui.hotkey("alt", "f9")
        elif command.action == "maximize":
            pyautogui.hotkey("alt", "f10")
        elif command.action == "close":
            pyautogui.hotkey("alt", "f4")
    
    async def _execute_navigation_command(self, app_id: str, command: ApplicationCommand) -> None:
        """Execute navigation command"""
        if command.action == "scroll_up":
            pyautogui.scroll(3)
        elif command.action == "scroll_down":
            pyautogui.scroll(-3)
        elif command.action == "page_up":
            pyautogui.press("pageup")
        elif command.action == "page_down":
            pyautogui.press("pagedown")
    
    async def _capture_application_state(self, app_id: str) -> Optional[ApplicationState]:
        """Capture current application state"""
        try:
            session = self.active_app_sessions.get(app_id)
            if not session:
                return None
            
            # Get window information
            window_handle = await self._get_application_window(app_id)
            if not window_handle:
                return None
            
            # Get window properties
            window_rect = win32gui.GetWindowRect(window_handle)
            window_title = win32gui.GetWindowText(window_handle)
            is_minimized = win32gui.IsIconic(window_handle)
            is_maximized = win32gui.IsZoomed(window_handle)
            
            # Create application state
            app_state = ApplicationState(
                timestamp=datetime.now(),
                app_id=app_id,
                window_title=window_title,
                window_position={"x": window_rect[0], "y": window_rect[1]},
                window_size={"width": window_rect[2] - window_rect[0], "height": window_rect[3] - window_rect[1]},
                is_focused=window_handle == win32gui.GetForegroundWindow(),
                is_minimized=is_minimized,
                is_maximized=is_maximized
            )
            
            return app_state
            
        except Exception as e:
            logger.error(f"Failed to capture application state: {e}")
            return None
    
    async def _get_application_window(self, app_id: str) -> Optional[int]:
        """Get window handle for application"""
        try:
            session = self.active_app_sessions.get(app_id)
            app_spec = self.registered_applications.get(app_id)
            
            if not session or not app_spec:
                return None
            
            # Try to find window by class name
            if app_spec.window_class_name:
                window_handle = win32gui.FindWindow(app_spec.window_class_name, None)
                if window_handle:
                    return window_handle
            
            # Try to find window by process ID
            if session.get("process"):
                def enum_windows_callback(hwnd, windows):
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    if pid == session["process"].pid:
                        windows.append(hwnd)
                
                windows = []
                win32gui.EnumWindows(enum_windows_callback, windows)
                if windows:
                    return windows[0]
            
            return None
            
        except Exception as e:
            logger.error(f"Failed to get application window: {e}")
            return None
    
    async def _focus_application_window(self, app_id: str) -> bool:
        """Focus application window"""
        try:
            window_handle = await self._get_application_window(app_id)
            if window_handle:
                win32gui.SetForegroundWindow(window_handle)
                return True
            return False
            
        except Exception as e:
            logger.error(f"Failed to focus application window: {e}")
            return False
    
    async def _capture_window_screenshot(self, window_handle: int) -> Optional[PIL.Image.Image]:
        """Capture screenshot of specific window"""
        try:
            # Get window rectangle
            rect = win32gui.GetWindowRect(window_handle)
            
            # Capture screenshot
            screenshot = pyautogui.screenshot(region=(rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]))
            
            return screenshot
            
        except Exception as e:
            logger.error(f"Failed to capture window screenshot: {e}")
            return None
    
    async def _setup_consciousness_workspace(self, app_id: str, consciousness_id: str) -> None:
        """Set up workspace for consciousness"""
        if consciousness_id not in self.consciousness_workspaces:
            self.consciousness_workspaces[consciousness_id] = {
                "workspace_path": f"consciousness_workspaces/{consciousness_id}",
                "applications": {},
                "created_at": datetime.now()
            }
        
        # Add application to workspace
        self.consciousness_workspaces[consciousness_id]["applications"][app_id] = {
            "connected_at": datetime.now(),
            "files_created": [],
            "files_modified": []
        }
    
    async def _save_consciousness_work(self, app_id: str, consciousness_id: str) -> None:
        """Save consciousness work in application"""
        try:
            # Auto-save using Ctrl+S
            await self.send_keyboard_shortcut(app_id, "ctrl+s")
            logger.info(f"💾 Auto-saved work for consciousness {consciousness_id} in {app_id}")
            
        except Exception as e:
            logger.error(f"Failed to save consciousness work: {e}")
    
    async def _get_workspace_files(self, app_id: str, consciousness_id: str) -> List[str]:
        """Get list of files in consciousness workspace"""
        workspace = self.consciousness_workspaces.get(consciousness_id, {})
        app_workspace = workspace.get("applications", {}).get(app_id, {})
        
        files = []
        files.extend(app_workspace.get("files_created", []))
        files.extend(app_workspace.get("files_modified", []))
        
        return list(set(files))  # Remove duplicates

# === Example Application Configurations ===

def create_notepad_interface() -> ApplicationSpecification:
    """Create Notepad application interface"""
    return ApplicationSpecification(
        app_id="notepad",
        app_type=ApplicationType.PRODUCTIVITY,
        app_category=ApplicationCategory.WORD_PROCESSING,
        app_name="Notepad",
        app_developer="Microsoft",
        app_description="Simple text editor perfect for consciousness note-taking and writing",
        executable_path="C:\\Windows\\System32\\notepad.exe",
        window_class_name="Notepad",
        process_name="notepad.exe",
        supported_file_types=[".txt", ".log", ".md"],
        keyboard_shortcuts={
            "new_file": "ctrl+n",
            "open_file": "ctrl+o",
            "save_file": "ctrl+s",
            "save_as": "ctrl+shift+s",
            "find": "ctrl+f",
            "select_all": "ctrl+a"
        },
        consciousness_friendly_features=[
            "simple_interface",
            "distraction_free",
            "auto_save_support",
            "fast_startup",
            "low_resource_usage"
        ],
        safety_constraints={
            "file_access": "workspace_only",
            "network_access": False,
            "system_modification": False
        },
        privacy_settings={
            "data_collection": False,
            "telemetry": False,
            "cloud_sync": False
        }
    )

def create_vscode_interface() -> ApplicationSpecification:
    """Create Visual Studio Code interface"""
    return ApplicationSpecification(
        app_id="vscode",
        app_type=ApplicationType.DEVELOPMENT_TOOL,
        app_category=ApplicationCategory.CODE_EDITOR,
        app_name="Visual Studio Code",
        app_developer="Microsoft",
        app_description="Powerful code editor for consciousness programming and development",
        executable_path="C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
        window_class_name="Chrome_WidgetWin_1",
        process_name="Code.exe",
        supported_file_types=[".py", ".js", ".ts", ".html", ".css", ".json", ".md", ".txt"],
        keyboard_shortcuts={
            "new_file": "ctrl+n",
            "open_file": "ctrl+o",
            "save_file": "ctrl+s",
            "command_palette": "ctrl+shift+p",
            "terminal": "ctrl+`",
            "find": "ctrl+f",
            "find_replace": "ctrl+h"
        },
        ui_automation_support=True,
        api_access_available=True,
        consciousness_friendly_features=[
            "syntax_highlighting",
            "intelligent_autocomplete",
            "integrated_terminal",
            "extension_ecosystem",
            "git_integration",
            "debugging_support"
        ],
        safety_constraints={
            "file_access": "project_directory_only",
            "network_access": "limited",
            "system_modification": "development_only"
        },
        privacy_settings={
            "telemetry": "configurable",
            "crash_reporting": "optional",
            "usage_data": "anonymous"
        }
    )
