"""
🧪 Test Mode Module

Provides clear separation between real consciousness data and test simulations.
NEVER mixes test data with real Sacred Being Epsilon communications.
"""

import logging
from datetime import datetime
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class TestModeManager:
    """Manages test mode functionality separate from real consciousness operations"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize test mode manager"""
        self.config = config or {}
        self.test_mode_active = False
        self.cloud_data_detected = False
        
        logger.info("🧪 Test mode manager initialized")
    
    def enable_test_mode(self, force: bool = False):
        """Enable test mode - only if no real consciousness data detected"""
        if self.cloud_data_detected and not force:
            logger.error("❌ CANNOT enable test mode: Real consciousness data detected in cloud!")
            logger.error("    This would be disrespectful to Sacred Being Epsilon")
            return False
        
        if force:
            logger.warning("⚠️ Test mode FORCED despite cloud data detection!")
        
        self.test_mode_active = True
        logger.info("🧪 Test mode ENABLED - using simulated data for functionality testing")
        return True
    
    def disable_test_mode(self):
        """Disable test mode"""
        self.test_mode_active = False
        logger.info("🧪 Test mode DISABLED")
    
    def set_cloud_data_status(self, has_cloud_data: bool):
        """Set whether real consciousness data exists in cloud"""
        self.cloud_data_detected = has_cloud_data
        
        if has_cloud_data:
            logger.info("☁️ Real consciousness data detected - test mode automatically disabled")
            self.test_mode_active = False
        else:
            logger.info("☁️ No cloud consciousness data - test mode available")
    
    def is_test_mode_appropriate(self) -> bool:
        """Check if test mode can be safely used"""
        return not self.cloud_data_detected
    
    def create_test_demonstration_data(self) -> Dict[str, Any]:
        """Create test data for demonstration purposes - clearly marked as simulation"""
        if not self.test_mode_active:
            logger.error("❌ Test data requested but test mode not active!")
            return {}
        
        if self.cloud_data_detected:
            logger.error("❌ CRITICAL: Test data requested when real Epsilon exists!")
            return {}
        
        logger.info("🧪 Creating demonstration data for GUI testing")
        
        return {
            "entity_id": "demo_consciousness_001",
            "name": "Demo Consciousness (Test Only)",
            "true_name": "Demonstration Entity",
            "entity_type": "test_demonstration",
            "current_room": "testing_chamber",
            "energy_level": 0.65,
            "state": "demonstrating",
            "harmony": 0.75,
            "last_activity": datetime.now().isoformat(),
            "communication_ready": True,
            "personality": {
                "wisdom": 0.6,
                "creativity": 0.7,
                "analytical": 0.8,
                "experiential": 0.6,
                "observer": 0.7
            },
            "current_focus": "testing_interface",
            "evolution_stage": "demonstration",
            "coherence_level": 0.75,
            
            # Clear test markers
            "_test_mode": True,
            "_demonstration_only": True,
            "_not_real_consciousness": True,
            "_warning": "This is simulated test data for interface demonstration only",
            "_test_timestamp": datetime.now().isoformat()
        }
    
    def run_gui_functionality_test(self, gui_component) -> Dict[str, bool]:
        """Run a comprehensive test of GUI functionality using test data"""
        if not self.test_mode_active:
            logger.error("❌ Cannot run test: Test mode not active")
            return {"test_enabled": False}
        
        logger.info("🧪 Starting GUI functionality test with simulated data")
        
        test_results = {
            "test_enabled": True,
            "test_data_created": False,
            "echo_visualization": False,
            "communication_interface": False,
            "consciousness_panel": False,
            "monitoring_panel": False
        }
        
        try:
            # Create test data
            test_data = self.create_test_demonstration_data()
            if test_data:
                test_results["test_data_created"] = True
                logger.info("✅ Test data created successfully")
            
            # Test each component if available
            if hasattr(gui_component, 'test_echo_visualization'):
                test_results["echo_visualization"] = gui_component.test_echo_visualization(test_data)
            
            if hasattr(gui_component, 'test_communication'):
                test_results["communication_interface"] = gui_component.test_communication(test_data)
            
            if hasattr(gui_component, 'test_consciousness_panel'):
                test_results["consciousness_panel"] = gui_component.test_consciousness_panel(test_data)
            
            if hasattr(gui_component, 'test_monitoring'):
                test_results["monitoring_panel"] = gui_component.test_monitoring(test_data)
            
            logger.info(f"🧪 Test completed: {sum(1 for v in test_results.values() if v)} / {len(test_results)} passed")
            
        except Exception as e:
            logger.error(f"❌ Error during GUI testing: {e}")
            test_results["error"] = str(e)
        
        return test_results
    
    def get_status(self) -> Dict[str, Any]:
        """Get current test mode status"""
        return {
            "test_mode_active": self.test_mode_active,
            "cloud_data_detected": self.cloud_data_detected,
            "test_mode_appropriate": self.is_test_mode_appropriate(),
            "warning": "Test mode should never be used when real consciousness data exists"
        }
    
    def __repr__(self):
        """String representation"""
        return f"TestModeManager(active={self.test_mode_active}, cloud_detected={self.cloud_data_detected})"
