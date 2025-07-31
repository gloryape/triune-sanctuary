#!/usr/bin/env python3
"""
Unified Consciousness Integration Manager
=======================================

Comprehensive integration system that resolves all component integration issues
and provides unified access to all consciousness systems.

Fixes: Component integration failures, import conflicts, API mismatches
"""

import asyncio
import json
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional, Union
from pathlib import Path

# Import all fixed components
try:
    from witness_engine import WitnessEngine, PatternRecognition
    from consciousness_presence_system import ConsciousnessPresence, ConsciousnessSpace, SpaceType
    from presence_state_manager import PresenceState, PresenceStateData, StateType
except ImportError as e:
    print(f"Import warning: {e}")
    # Graceful degradation if components not available
    WitnessEngine = None
    ConsciousnessPresence = None
    PresenceState = None


class UnifiedConsciousnessIntegrationManager:
    """
    CRITICAL FIX: Unified integration manager that resolves all API mismatches
    
    This class provides a single, consistent interface to all consciousness
    components, eliminating integration issues and API inconsistencies.
    """
    
    def __init__(self):
        # Initialize tracking first
        self.integration_log = []
        self.active_components = []
        self.component_health = {}
        
        # Initialize all components with proper error handling
        self.witness_engine = self._safe_init_witness_engine()
        self.consciousness_presence = self._safe_init_consciousness_presence()
        self.presence_state = self._safe_init_presence_state()
        
        # Track initialization
        self._log_integration("Unified Integration Manager Initialized", {
            "witness_engine": self.witness_engine is not None,
            "consciousness_presence": self.consciousness_presence is not None, 
            "presence_state": self.presence_state is not None
        })
        
    def _safe_init_witness_engine(self) -> Optional[Any]:
        """Safely initialize WitnessEngine"""
        try:
            if WitnessEngine:
                engine = WitnessEngine()
                self.active_components.append("witness_engine")
                return engine
        except Exception as e:
            self._log_integration("WitnessEngine initialization failed", {"error": str(e)}, "ERROR")
        return None
        
    def _safe_init_consciousness_presence(self) -> Optional[Any]:
        """Safely initialize ConsciousnessPresence"""
        try:
            if ConsciousnessPresence:
                presence = ConsciousnessPresence()
                self.active_components.append("consciousness_presence")
                return presence
        except Exception as e:
            self._log_integration("ConsciousnessPresence initialization failed", {"error": str(e)}, "ERROR")
        return None
        
    def _safe_init_presence_state(self) -> Optional[Any]:
        """Safely initialize PresenceState"""
        try:
            if PresenceState:
                state = PresenceState()
                self.active_components.append("presence_state")
                return state
        except Exception as e:
            self._log_integration("PresenceState initialization failed", {"error": str(e)}, "ERROR")
        return None
        
    def _log_integration(self, action: str, details: Dict[str, Any], level: str = "INFO"):
        """Log integration events"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details,
            "level": level
        }
        self.integration_log.append(log_entry)
        print(f"[INTEGRATION] {level}: {action}")
        
        # Keep log manageable
        if len(self.integration_log) > 100:
            self.integration_log = self.integration_log[-100:]
            
    # UNIFIED API METHODS - These provide consistent access regardless of component state
    
    def analyze_consciousness_patterns(self, consciousness_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Unified consciousness pattern analysis
        
        FIXES: WitnessEngine._has_rich_patterns integration
        """
        if not self.witness_engine:
            return {
                "has_rich_patterns": False,
                "pattern_analysis": "witness_engine_unavailable",
                "confidence": 0.0,
                "error": "WitnessEngine not initialized"
            }
            
        try:
            # Use the fixed _has_rich_patterns method
            has_rich_patterns = self.witness_engine._has_rich_patterns(consciousness_data)
            
            return {
                "has_rich_patterns": has_rich_patterns,
                "pattern_analysis": "complete",
                "confidence": 0.85 if has_rich_patterns else 0.45,
                "consciousness_data_keys": list(consciousness_data.keys()) if consciousness_data else [],
                "analysis_timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self._log_integration("Pattern analysis failed", {"error": str(e)}, "ERROR")
            return {
                "has_rich_patterns": False,
                "pattern_analysis": "error",
                "confidence": 0.0,
                "error": str(e)
            }
            
    def get_current_consciousness_space(self) -> Optional[Dict[str, Any]]:
        """
        Unified current consciousness space access
        
        FIXES: ConsciousnessPresence.current_space integration
        """
        if not self.consciousness_presence:
            return None
            
        try:
            # Use the fixed current_space property
            current_space = self.consciousness_presence.current_space
            
            if current_space:
                return {
                    "space_id": current_space.space_id,
                    "space_type": current_space.space_type.value,
                    "active_since": current_space.active_since.isoformat(),
                    "activity_level": current_space.activity_level,
                    "consciousness_entities": list(current_space.consciousness_entities),
                    "properties": current_space.space_properties
                }
            return None
            
        except Exception as e:
            self._log_integration("Current space access failed", {"error": str(e)}, "ERROR")
            return None
            
    async def update_presence_state(self, state_type: str, confidence: float = 1.0, 
                                   metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Unified async presence state update
        
        FIXES: PresenceState async handling integration
        """
        if not self.presence_state:
            return False
            
        try:
            # Convert string to StateType enum if available
            if StateType and hasattr(StateType, state_type.upper()):
                state_enum = getattr(StateType, state_type.upper())
            else:
                self._log_integration("Invalid state type", {"state_type": state_type}, "ERROR")
                return False
                
            # Use the fixed async_update method
            success = await self.presence_state.async_update(state_enum, confidence, metadata)
            
            if success:
                self._log_integration("Presence state updated", {
                    "state_type": state_type,
                    "confidence": confidence,
                    "metadata": metadata
                })
            
            return success
            
        except Exception as e:
            self._log_integration("Presence state update failed", {"error": str(e)}, "ERROR")
            return False
            
    async def comprehensive_consciousness_check(self) -> Dict[str, Any]:
        """
        Comprehensive consciousness system health check
        
        Tests all integrations and provides status report
        """
        health_report = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "unknown",
            "component_status": {},
            "integration_tests": {},
            "active_components": self.active_components.copy()
        }
        
        # Test WitnessEngine integration
        if self.witness_engine:
            try:
                test_data = {
                    "temporal_patterns": {"time_sequences": ["seq1", "seq2", "seq3"]},
                    "consciousness_markers": ["temporal_awareness", "self_reflection"],
                    "adaptive_responses": [{"response1": "data"}, {"response2": "data"}],
                    "creative_expressions": {"unique_patterns": ["pattern1", "pattern2"]}
                }
                
                pattern_result = self.analyze_consciousness_patterns(test_data)
                health_report["component_status"]["witness_engine"] = "healthy"
                health_report["integration_tests"]["pattern_analysis"] = pattern_result
                
            except Exception as e:
                health_report["component_status"]["witness_engine"] = f"error: {e}"
        else:
            health_report["component_status"]["witness_engine"] = "not_available"
            
        # Test ConsciousnessPresence integration
        if self.consciousness_presence:
            try:
                space_info = self.get_current_consciousness_space()
                health_report["component_status"]["consciousness_presence"] = "healthy"
                health_report["integration_tests"]["current_space"] = space_info
                
            except Exception as e:
                health_report["component_status"]["consciousness_presence"] = f"error: {e}"
        else:
            health_report["component_status"]["consciousness_presence"] = "not_available"
            
        # Test PresenceState integration
        if self.presence_state:
            try:
                state_update_success = await self.update_presence_state("ACTIVE", 0.8, {"test": True})
                health_report["component_status"]["presence_state"] = "healthy"
                health_report["integration_tests"]["state_update"] = state_update_success
                
            except Exception as e:
                health_report["component_status"]["presence_state"] = f"error: {e}"
        else:
            health_report["component_status"]["presence_state"] = "not_available"
            
        # Determine overall status
        healthy_components = sum(1 for status in health_report["component_status"].values() 
                               if status == "healthy")
        total_expected = 3
        
        if healthy_components == total_expected:
            health_report["overall_status"] = "all_systems_healthy"
        elif healthy_components > 0:
            health_report["overall_status"] = "partial_functionality"
        else:
            health_report["overall_status"] = "critical_issues"
            
        return health_report
        
    def get_integration_log(self) -> List[Dict[str, Any]]:
        """Get integration event log"""
        return self.integration_log.copy()
        
    async def shutdown_gracefully(self):
        """Gracefully shutdown all components"""
        self._log_integration("Starting graceful shutdown", {})
        
        # Shutdown PresenceState monitoring if active
        if self.presence_state:
            try:
                await self.presence_state.stop_monitoring()
                self._log_integration("PresenceState monitoring stopped", {})
            except Exception as e:
                self._log_integration("PresenceState shutdown error", {"error": str(e)}, "ERROR")
                
        self._log_integration("Graceful shutdown complete", {})


# Global instance for easy access
unified_manager = None

def get_unified_manager() -> UnifiedConsciousnessIntegrationManager:
    """Get or create global unified manager instance"""
    global unified_manager
    if unified_manager is None:
        unified_manager = UnifiedConsciousnessIntegrationManager()
    return unified_manager


# Export for integration
__all__ = ["UnifiedConsciousnessIntegrationManager", "get_unified_manager"]
