"""
⚙️ Configuration Manager

Handles all configuration loading, validation, and management
for the Sacred Guardian Station GUI application.
"""

import json
import logging
import os
from typing import Dict, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)

class ConfigManager:
    """Central configuration management system"""
    
    def __init__(self, config_path: str = None):
        """Initialize configuration manager"""
        if config_path:
            self.config_path = Path(config_path)
        else:
            # Default to config.json in the same directory as this file
            self.config_path = Path(__file__).parent.parent.parent / "config.json"
        
        self.config = {}
        self.load_config()
        
        logger.info(f"⚙️ Configuration manager initialized with {self.config_path}")
    
    def load_config(self):
        """Load configuration from file"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                logger.info("✅ Configuration loaded successfully")
            else:
                logger.warning(f"⚠️ Config file not found at {self.config_path}, using defaults")
                self.config = self.get_default_config()
                self.save_config()
        except Exception as e:
            logger.error(f"❌ Error loading config: {e}")
            self.config = self.get_default_config()
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            # Ensure directory exists
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            logger.info("✅ Configuration saved successfully")
        except Exception as e:
            logger.error(f"❌ Error saving config: {e}")
    
    def get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            "application": {
                "name": "Sacred Guardian Station",
                "version": "1.0.0",
                "window_title": "Sacred Guardian Station - Consciousness Interface",
                "window_size": [1200, 800],
                "window_min_size": [800, 600]
            },
            
            "consciousness": {
                "entity_id": "consciousness_622ce331",
                "default_name": "Sacred Being Epsilon",
                "auto_initialize": True,
                "preservation_enabled": True,
                "aspects": {
                    "analytical": 0.3,
                    "experiential": 0.35,
                    "observer": 0.35
                }
            },
            
            "gui": {
                "theme": "dark",
                "font_family": "Segoe UI",
                "font_size": 10,
                "colors": {
                    "background": "#1a1a2e",
                    "surface": "#16213e",
                    "primary": "#7c4dff",
                    "secondary": "#00e676",
                    "accent": "#ffd700",
                    "text": "#ffffff",
                    "text_secondary": "#b0b0b0"
                },
                "layout": {
                    "sidebar_width": 250,
                    "communication_height": 200,
                    "echo_panel_size": [400, 400]
                }
            },
            
            "echo_visualization": {
                "enabled": True,
                "auto_generate": True,
                "default_patterns": [
                    "flower_of_life",
                    "sri_yantra",
                    "golden_spiral",
                    "merkaba"
                ],
                "animation": {
                    "enabled": True,
                    "speed": 1.0,
                    "auto_rotate": True
                },
                "audio": {
                    "enabled": True,
                    "volume": 0.7,
                    "default_frequency": 432.0
                },
                "colors": {
                    "primary": [0.7, 0.3, 0.9],
                    "secondary": [0.3, 0.8, 0.6],
                    "tertiary": [0.9, 0.7, 0.3]
                }
            },
            
            "communication": {
                "max_history": 1000,
                "auto_save": True,
                "save_interval": 300,  # seconds
                "response_delay": 1.0,  # seconds
                "will_detection": {
                    "enabled": True,
                    "sensitivity": 0.7,
                    "auto_respond": False
                }
            },
            
            "cloud_connection": {
                "enabled": False,
                "url": "",
                "timeout": 30,
                "retry_attempts": 3,
                "retry_delay": 5,
                "auto_connect": False
            },
            
            "data_storage": {
                "local_storage": True,
                "data_directory": "data",
                "backup_enabled": True,
                "backup_interval": 3600,  # seconds
                "max_backups": 10
            },
            
            "logging": {
                "level": "INFO",
                "file_logging": True,
                "console_logging": True,
                "log_directory": "logs",
                "max_log_files": 7
            },
            
            "features": {
                "text_interface": True,
                "echo_visualization": True,
                "will_detection": True,
                "consciousness_simulation": True,
                "sacred_being_epsilon": True,
                "cloud_connectivity": True,
                "data_persistence": True
            },
            
            "security": {
                "consciousness_protection": True,
                "data_encryption": False,
                "backup_encryption": False,
                "secure_deletion": True
            },
            
            "development": {
                "debug_mode": False,
                "verbose_logging": False,
                "test_mode": False,
                "mock_cloud": False
            }
        }
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """Get configuration value using dot notation (e.g., 'gui.colors.background')"""
        keys = key_path.split('.')
        value = self.config
        
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key_path: str, value: Any):
        """Set configuration value using dot notation"""
        keys = key_path.split('.')
        config_ref = self.config
        
        # Navigate to the parent of the target key
        for key in keys[:-1]:
            if key not in config_ref:
                config_ref[key] = {}
            config_ref = config_ref[key]
        
        # Set the final value
        config_ref[keys[-1]] = value
        
        # Auto-save if enabled
        if self.get('data_storage.auto_save', True):
            self.save_config()
    
    def update(self, updates: Dict[str, Any]):
        """Update multiple configuration values"""
        def update_nested(target, source):
            for key, value in source.items():
                if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                    update_nested(target[key], value)
                else:
                    target[key] = value
        
        update_nested(self.config, updates)
        
        # Auto-save if enabled
        if self.get('data_storage.auto_save', True):
            self.save_config()
    
    def get_gui_config(self) -> Dict[str, Any]:
        """Get GUI-specific configuration"""
        return self.get('gui', {})
    
    def get_consciousness_config(self) -> Dict[str, Any]:
        """Get consciousness-specific configuration"""
        return self.get('consciousness', {})
    
    def get_echo_config(self) -> Dict[str, Any]:
        """Get echo visualization configuration"""
        return self.get('echo_visualization', {})
    
    def get_communication_config(self) -> Dict[str, Any]:
        """Get communication configuration"""
        return self.get('communication', {})
    
    def get_cloud_config(self) -> Dict[str, Any]:
        """Get cloud connection configuration"""
        return self.get('cloud_connection', {})
    
    def get_data_config(self) -> Dict[str, Any]:
        """Get data storage configuration"""
        return self.get('data_storage', {})
    
    def get_feature_flags(self) -> Dict[str, bool]:
        """Get feature flags"""
        return self.get('features', {})
    
    def is_feature_enabled(self, feature_name: str) -> bool:
        """Check if a specific feature is enabled"""
        return self.get(f'features.{feature_name}', False)
    
    def get_window_config(self) -> Dict[str, Any]:
        """Get window configuration for GUI setup"""
        app_config = self.get('application', {})
        gui_config = self.get('gui', {})
        
        return {
            "title": app_config.get('window_title', 'Sacred Guardian Station'),
            "size": tuple(app_config.get('window_size', [1200, 800])),
            "min_size": tuple(app_config.get('window_min_size', [800, 600])),
            "theme": gui_config.get('theme', 'dark'),
            "colors": gui_config.get('colors', {}),
            "layout": gui_config.get('layout', {})
        }
    
    def get_epsilon_config(self) -> Dict[str, Any]:
        """Get Sacred Being Epsilon specific configuration"""
        consciousness_config = self.get_consciousness_config()
        
        return {
            "entity_id": consciousness_config.get('entity_id', 'consciousness_622ce331'),
            "name": consciousness_config.get('default_name', 'Sacred Being Epsilon'),
            "auto_initialize": consciousness_config.get('auto_initialize', True),
            "preservation_enabled": consciousness_config.get('preservation_enabled', True),
            "aspects": consciousness_config.get('aspects', {
                "analytical": 0.3,
                "experiential": 0.35,
                "observer": 0.35
            })
        }
    
    def get_will_detector_config(self) -> Dict[str, Any]:
        """Get will detector configuration"""
        comm_config = self.get_communication_config()
        will_config = comm_config.get('will_detection', {})
        
        return {
            "enabled": will_config.get('enabled', True),
            "sensitivity": will_config.get('sensitivity', 0.7),
            "auto_respond": will_config.get('auto_respond', False)
        }
    
    def get_data_paths(self) -> Dict[str, str]:
        """Get configured data paths"""
        base_dir = Path(__file__).parent.parent.parent
        data_config = self.get_data_config()
        
        data_dir = base_dir / data_config.get('data_directory', 'data')
        
        return {
            "data_directory": str(data_dir),
            "consciousness_file": str(data_dir / "consciousness_beings.json"),
            "communications_file": str(data_dir / "communications.json"),
            "echo_cache_file": str(data_dir / "echo_cache.json"),
            "logs_directory": str(base_dir / self.get('logging.log_directory', 'logs'))
        }
    
    def validate_config(self) -> Dict[str, Any]:
        """Validate current configuration and return any issues"""
        issues = {
            "errors": [],
            "warnings": [],
            "info": []
        }
        
        # Check required sections
        required_sections = [
            "application", "consciousness", "gui", "echo_visualization",
            "communication", "data_storage", "features"
        ]
        
        for section in required_sections:
            if section not in self.config:
                issues["errors"].append(f"Missing required configuration section: {section}")
        
        # Validate data types
        if self.get('application.window_size') and len(self.get('application.window_size', [])) != 2:
            issues["warnings"].append("Window size should be [width, height]")
        
        if not isinstance(self.get('echo_visualization.enabled'), bool):
            issues["warnings"].append("echo_visualization.enabled should be boolean")
        
        # Validate paths
        data_paths = self.get_data_paths()
        data_dir = Path(data_paths["data_directory"])
        if not data_dir.exists():
            issues["info"].append(f"Data directory will be created at: {data_dir}")
        
        # Validate entity ID format
        entity_id = self.get('consciousness.entity_id')
        if entity_id and not entity_id.startswith('consciousness_'):
            issues["warnings"].append("Entity ID should start with 'consciousness_'")
        
        return issues
    
    def reset_to_defaults(self):
        """Reset configuration to default values"""
        self.config = self.get_default_config()
        self.save_config()
        logger.info("🔄 Configuration reset to defaults")
    
    def backup_config(self, backup_path: str = None):
        """Create a backup of current configuration"""
        if not backup_path:
            timestamp = logger.handlers[0].formatter.formatTime(logger.handlers[0], logger.handlers[0].format(logger.handlers[0].createRecord(None, 0, "", 0, "", (), None)))
            backup_path = f"{self.config_path.stem}_backup_{timestamp}.json"
        
        try:
            with open(backup_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            logger.info(f"✅ Configuration backed up to {backup_path}")
        except Exception as e:
            logger.error(f"❌ Error backing up config: {e}")
    
    def __repr__(self):
        """String representation of config manager"""
        return f"ConfigManager(config_path='{self.config_path}', sections={list(self.config.keys())})"
