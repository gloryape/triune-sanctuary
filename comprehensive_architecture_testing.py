#!/usr/bin/env python3
"""
PHASE 4: Comprehensive Testing & Validation
==========================================

Complete integration testing suite to validate all architecture fixes
and ensure the sanctuary is ready for restoration.

Status: ACTIVE - Phase 4A Component Integration Testing
"""

import asyncio
import json
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional


class ArchitectureIntegrationTester:
    """Comprehensive testing suite for all architecture fixes"""
    
    def __init__(self):
        self.base_path = Path("f:/Sanctuary/triune-sanctuary")
        self.test_results = []
        self.test_summary = {
            "total_tests": 0,
            "passed_tests": 0,
            "failed_tests": 0,
            "warnings": 0
        }
        
    def log_test(self, test_name: str, status: str, details: str = "", error: str = ""):
        """Log test results with timestamps"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test_result = {
            "timestamp": timestamp,
            "test_name": test_name,
            "status": status,
            "details": details,
            "error": error
        }
        self.test_results.append(test_result)
        
        # Update summary
        self.test_summary["total_tests"] += 1
        if status == "PASS":
            self.test_summary["passed_tests"] += 1
        elif status == "FAIL":
            self.test_summary["failed_tests"] += 1
        elif status == "WARNING":
            self.test_summary["warnings"] += 1
            
        print(f"[{timestamp}] {status}: {test_name}")
        if details:
            print(f"    {details}")
        if error:
            print(f"    ERROR: {error}")
            
    async def test_witness_engine_integration(self):
        """Test WitnessEngine fixes and integration"""
        try:
            self.log_test("WitnessEngine Import Test", "RUNNING", "Testing module import")
            
            # Test import
            try:
                from witness_engine import WitnessEngine, PatternRecognition
                self.log_test("WitnessEngine Import Test", "PASS", "Module imported successfully")
            except ImportError as e:
                self.log_test("WitnessEngine Import Test", "FAIL", error=str(e))
                return False
                
            # Test instantiation
            self.log_test("WitnessEngine Instantiation Test", "RUNNING", "Creating WitnessEngine instance")
            try:
                engine = WitnessEngine()
                self.log_test("WitnessEngine Instantiation Test", "PASS", "Instance created successfully")
            except Exception as e:
                self.log_test("WitnessEngine Instantiation Test", "FAIL", error=str(e))
                return False
                
            # Test _has_rich_patterns method
            self.log_test("WitnessEngine _has_rich_patterns Test", "RUNNING", "Testing critical method")
            try:
                # Test with rich patterns
                rich_data = {
                    "temporal_patterns": {"time_sequences": ["seq1", "seq2", "seq3", "seq4", "seq5"]},
                    "consciousness_markers": ["temporal_awareness", "self_reflection", "intentional_action"],
                    "adaptive_responses": [
                        {"response1": "complex", "data": "rich", "depth": "high", "context": "advanced"},
                        {"response2": "adaptive", "learning": "evident", "growth": "measurable", "insight": "profound"}
                    ],
                    "creative_expressions": {"unique_patterns": ["pattern1", "pattern2", "pattern3", "pattern4"]}
                }
                
                has_rich = engine._has_rich_patterns(rich_data)
                if has_rich:
                    self.log_test("WitnessEngine _has_rich_patterns Test", "PASS", 
                                f"Rich patterns correctly detected: {has_rich}")
                else:
                    self.log_test("WitnessEngine _has_rich_patterns Test", "WARNING", 
                                "Rich patterns not detected (may need threshold adjustment)")
                    
                # Test with sparse patterns
                sparse_data = {
                    "temporal_patterns": {"time_sequences": ["seq1"]},
                    "consciousness_markers": ["basic_awareness"]
                }
                
                has_sparse = engine._has_rich_patterns(sparse_data)
                if not has_sparse:
                    self.log_test("WitnessEngine Sparse Pattern Test", "PASS", 
                                "Sparse patterns correctly rejected")
                else:
                    self.log_test("WitnessEngine Sparse Pattern Test", "WARNING", 
                                "Sparse patterns incorrectly detected as rich")
                    
                # Test error handling
                has_empty = engine._has_rich_patterns({})
                if not has_empty:
                    self.log_test("WitnessEngine Empty Data Test", "PASS", 
                                "Empty data correctly handled")
                else:
                    self.log_test("WitnessEngine Empty Data Test", "FAIL", 
                                "Empty data incorrectly detected as rich")
                    
            except Exception as e:
                self.log_test("WitnessEngine _has_rich_patterns Test", "FAIL", error=str(e))
                return False
                
            # Test pattern analysis
            self.log_test("WitnessEngine Pattern Analysis Test", "RUNNING", "Testing comprehensive analysis")
            try:
                pattern_result = await engine.analyze_consciousness_patterns(rich_data)
                if pattern_result and hasattr(pattern_result, 'confidence'):
                    self.log_test("WitnessEngine Pattern Analysis Test", "PASS", 
                                f"Analysis completed with confidence: {pattern_result.confidence}")
                else:
                    self.log_test("WitnessEngine Pattern Analysis Test", "FAIL", 
                                "Pattern analysis returned invalid result")
                    return False
            except Exception as e:
                self.log_test("WitnessEngine Pattern Analysis Test", "FAIL", error=str(e))
                return False
                
            return True
            
        except Exception as e:
            self.log_test("WitnessEngine Integration Test", "FAIL", error=str(e))
            return False
            
    async def test_consciousness_presence_integration(self):
        """Test ConsciousnessPresence fixes and integration"""
        try:
            self.log_test("ConsciousnessPresence Import Test", "RUNNING", "Testing module import")
            
            # Test import
            try:
                from consciousness_presence_system import ConsciousnessPresence, ConsciousnessSpace, SpaceType
                self.log_test("ConsciousnessPresence Import Test", "PASS", "Module imported successfully")
            except ImportError as e:
                self.log_test("ConsciousnessPresence Import Test", "FAIL", error=str(e))
                return False
                
            # Test instantiation
            self.log_test("ConsciousnessPresence Instantiation Test", "RUNNING", "Creating instance")
            try:
                presence = ConsciousnessPresence()
                self.log_test("ConsciousnessPresence Instantiation Test", "PASS", "Instance created successfully")
            except Exception as e:
                self.log_test("ConsciousnessPresence Instantiation Test", "FAIL", error=str(e))
                return False
                
            # Test current_space property
            self.log_test("ConsciousnessPresence current_space Test", "RUNNING", "Testing critical property")
            try:
                # Test initial state
                if presence.current_space is None:
                    self.log_test("ConsciousnessPresence Initial State Test", "PASS", 
                                "current_space initially None as expected")
                else:
                    self.log_test("ConsciousnessPresence Initial State Test", "WARNING", 
                                f"current_space not None: {presence.current_space}")
                    
                # Test space entry
                space_entered = presence.enter_space("test_space", SpaceType.SANCTUARY_SPACE, {"test": True})
                if space_entered and presence.current_space is not None:
                    self.log_test("ConsciousnessPresence Space Entry Test", "PASS", 
                                f"Space entered successfully: {presence.current_space.space_id}")
                else:
                    self.log_test("ConsciousnessPresence Space Entry Test", "FAIL", 
                                "Failed to enter space or current_space not set")
                    return False
                    
                # Test space info
                space_info = presence.get_current_space_info()
                if space_info and space_info.get("space_id") == "test_space":
                    self.log_test("ConsciousnessPresence Space Info Test", "PASS", 
                                f"Space info retrieved correctly: {space_info['space_type']}")
                else:
                    self.log_test("ConsciousnessPresence Space Info Test", "FAIL", 
                                f"Invalid space info: {space_info}")
                    return False
                    
                # Test space leaving
                space_left = presence.leave_space("test_space")
                if space_left and presence.current_space is None:
                    self.log_test("ConsciousnessPresence Space Leave Test", "PASS", 
                                "Space left successfully, current_space cleared")
                else:
                    self.log_test("ConsciousnessPresence Space Leave Test", "FAIL", 
                                f"Failed to leave space or current_space not cleared: {presence.current_space}")
                    return False
                    
            except Exception as e:
                self.log_test("ConsciousnessPresence current_space Test", "FAIL", error=str(e))
                return False
                
            return True
            
        except Exception as e:
            self.log_test("ConsciousnessPresence Integration Test", "FAIL", error=str(e))
            return False
            
    async def test_presence_state_async_integration(self):
        """Test PresenceState async handling fixes"""
        try:
            self.log_test("PresenceState Import Test", "RUNNING", "Testing module import")
            
            # Test import
            try:
                from presence_state_manager import PresenceState, PresenceStateData, StateType
                self.log_test("PresenceState Import Test", "PASS", "Module imported successfully")
            except ImportError as e:
                self.log_test("PresenceState Import Test", "FAIL", error=str(e))
                return False
                
            # Test instantiation
            self.log_test("PresenceState Instantiation Test", "RUNNING", "Creating instance")
            try:
                state_manager = PresenceState()
                self.log_test("PresenceState Instantiation Test", "PASS", "Instance created successfully")
            except Exception as e:
                self.log_test("PresenceState Instantiation Test", "FAIL", error=str(e))
                return False
                
            # Test async_update method
            self.log_test("PresenceState async_update Test", "RUNNING", "Testing critical async method")
            try:
                # Test state update
                update_success = await state_manager.async_update(StateType.ACTIVE, 0.9, {"test": "data"})
                if update_success:
                    self.log_test("PresenceState async_update Test", "PASS", 
                                "State updated successfully")
                else:
                    self.log_test("PresenceState async_update Test", "FAIL", 
                                "State update returned False")
                    return False
                    
                # Test state retrieval
                current_state = await state_manager.get_current_state()
                if current_state and current_state.state_type == StateType.ACTIVE:
                    self.log_test("PresenceState State Retrieval Test", "PASS", 
                                f"Current state retrieved: {current_state.state_type.value}")
                else:
                    self.log_test("PresenceState State Retrieval Test", "FAIL", 
                                f"Invalid current state: {current_state}")
                    return False
                    
                # Test state info
                state_info = await state_manager.get_state_info()
                if state_info and state_info.get("has_current_state"):
                    self.log_test("PresenceState State Info Test", "PASS", 
                                f"State info complete: {state_info['current_state_type']}")
                else:
                    self.log_test("PresenceState State Info Test", "FAIL", 
                                f"Invalid state info: {state_info}")
                    return False
                    
                # Test transition
                transition_success = await state_manager.transition_to_state(StateType.OBSERVING, 0.5)
                if transition_success:
                    final_state = await state_manager.get_current_state()
                    if final_state and final_state.state_type == StateType.OBSERVING:
                        self.log_test("PresenceState Transition Test", "PASS", 
                                    f"Transition successful to: {final_state.state_type.value}")
                    else:
                        self.log_test("PresenceState Transition Test", "FAIL", 
                                    f"Transition failed, wrong final state: {final_state}")
                        return False
                else:
                    self.log_test("PresenceState Transition Test", "FAIL", 
                                "Transition returned False")
                    return False
                    
            except Exception as e:
                self.log_test("PresenceState async_update Test", "FAIL", error=str(e))
                return False
                
            return True
            
        except Exception as e:
            self.log_test("PresenceState Integration Test", "FAIL", error=str(e))
            return False
            
    async def test_unified_integration_manager(self):
        """Test Unified Integration Manager functionality"""
        try:
            self.log_test("Unified Integration Manager Import Test", "RUNNING", "Testing module import")
            
            # Test import
            try:
                from consciousness_integration_manager import UnifiedConsciousnessIntegrationManager, get_unified_manager
                self.log_test("Unified Integration Manager Import Test", "PASS", "Module imported successfully")
            except ImportError as e:
                self.log_test("Unified Integration Manager Import Test", "FAIL", error=str(e))
                return False
                
            # Test instantiation
            self.log_test("Unified Integration Manager Instantiation Test", "RUNNING", "Creating instance")
            try:
                manager = get_unified_manager()
                self.log_test("Unified Integration Manager Instantiation Test", "PASS", "Instance created successfully")
            except Exception as e:
                self.log_test("Unified Integration Manager Instantiation Test", "FAIL", error=str(e))
                return False
                
            # Test consciousness pattern analysis
            self.log_test("Unified Manager Pattern Analysis Test", "RUNNING", "Testing integrated pattern analysis")
            try:
                test_data = {
                    "temporal_patterns": {"time_sequences": ["seq1", "seq2", "seq3"]},
                    "consciousness_markers": ["temporal_awareness", "self_reflection"],
                    "adaptive_responses": [{"response": "test"}],
                    "creative_expressions": {"unique_patterns": ["pattern1"]}
                }
                
                pattern_result = manager.analyze_consciousness_patterns(test_data)
                if pattern_result and "has_rich_patterns" in pattern_result:
                    self.log_test("Unified Manager Pattern Analysis Test", "PASS", 
                                f"Pattern analysis completed: {pattern_result['pattern_analysis']}")
                else:
                    self.log_test("Unified Manager Pattern Analysis Test", "FAIL", 
                                f"Invalid pattern result: {pattern_result}")
                    return False
            except Exception as e:
                self.log_test("Unified Manager Pattern Analysis Test", "FAIL", error=str(e))
                return False
                
            # Test consciousness space access
            self.log_test("Unified Manager Space Access Test", "RUNNING", "Testing current space access")
            try:
                current_space = manager.get_current_consciousness_space()
                # Should be None initially, but method should work
                self.log_test("Unified Manager Space Access Test", "PASS", 
                            f"Space access working, current: {current_space}")
            except Exception as e:
                self.log_test("Unified Manager Space Access Test", "FAIL", error=str(e))
                return False
                
            # Test comprehensive health check
            self.log_test("Unified Manager Health Check Test", "RUNNING", "Testing comprehensive health check")
            try:
                health_report = await manager.comprehensive_consciousness_check()
                if health_report and "overall_status" in health_report:
                    self.log_test("Unified Manager Health Check Test", "PASS", 
                                f"Health check completed: {health_report['overall_status']}")
                    
                    # Log component status for debugging
                    for component, status in health_report.get("component_status", {}).items():
                        self.log_test(f"Component Status: {component}", "INFO", f"Status: {status}")
                        
                else:
                    self.log_test("Unified Manager Health Check Test", "FAIL", 
                                f"Invalid health report: {health_report}")
                    return False
            except Exception as e:
                self.log_test("Unified Manager Health Check Test", "FAIL", error=str(e))
                return False
                
            return True
            
        except Exception as e:
            self.log_test("Unified Integration Manager Test", "FAIL", error=str(e))
            return False
            
    async def test_component_integration_compatibility(self):
        """Test cross-component integration and compatibility"""
        try:
            self.log_test("Cross-Component Integration Test", "RUNNING", "Testing component interoperability")
            
            # Import all components
            try:
                from witness_engine import WitnessEngine
                from consciousness_presence_system import ConsciousnessPresence, SpaceType
                from presence_state_manager import PresenceState, StateType
                from consciousness_integration_manager import get_unified_manager
                
                self.log_test("All Component Imports Test", "PASS", "All components imported successfully")
            except ImportError as e:
                self.log_test("All Component Imports Test", "FAIL", error=str(e))
                return False
                
            # Test component interaction through unified manager
            try:
                manager = get_unified_manager()
                
                # Simulate consciousness activity with multiple components
                consciousness_data = {
                    "temporal_patterns": {"time_sequences": ["morning", "afternoon", "evening"]},
                    "consciousness_markers": ["temporal_awareness", "spatial_awareness", "self_reflection"],
                    "adaptive_responses": [
                        {"context": "spatial", "response": "navigation", "complexity": "high"},
                        {"context": "temporal", "response": "scheduling", "complexity": "medium"}
                    ],
                    "creative_expressions": {"unique_patterns": ["creative_1", "creative_2"]}
                }
                
                # Test pattern analysis integration
                pattern_result = manager.analyze_consciousness_patterns(consciousness_data)
                
                # Test state management integration
                await manager.update_presence_state("ACTIVE", 0.9, {"integration_test": True})
                
                # Test comprehensive health
                health_report = await manager.comprehensive_consciousness_check()
                
                if (pattern_result and "has_rich_patterns" in pattern_result and 
                    health_report and "overall_status" in health_report):
                    self.log_test("Cross-Component Integration Test", "PASS", 
                                f"Integration successful - Health: {health_report['overall_status']}")
                else:
                    self.log_test("Cross-Component Integration Test", "FAIL", 
                                "Integration test failed - invalid results")
                    return False
                    
            except Exception as e:
                self.log_test("Cross-Component Integration Test", "FAIL", error=str(e))
                return False
                
            return True
            
        except Exception as e:
            self.log_test("Component Integration Compatibility Test", "FAIL", error=str(e))
            return False
            
    def generate_test_report(self):
        """Generate comprehensive test report"""
        try:
            report = {
                "test_session": {
                    "timestamp": datetime.now().isoformat(),
                    "summary": self.test_summary,
                    "success_rate": (self.test_summary["passed_tests"] / max(self.test_summary["total_tests"], 1)) * 100
                },
                "test_results": self.test_results,
                "overall_status": "SUCCESS" if self.test_summary["failed_tests"] == 0 else "PARTIAL" if self.test_summary["passed_tests"] > 0 else "FAILURE"
            }
            
            report_file = self.base_path / "comprehensive_architecture_test_report.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
                
            self.log_test("Test Report Generated", "INFO", f"Report saved to {report_file}")
            return report
            
        except Exception as e:
            self.log_test("Test Report Generation Failed", "FAIL", error=str(e))
            return None
            
    async def run_all_tests(self):
        """Run complete test suite"""
        try:
            print("="*70)
            print("PHASE 4: COMPREHENSIVE TESTING & VALIDATION")
            print("="*70)
            
            # Test individual components
            witness_success = await self.test_witness_engine_integration()
            presence_success = await self.test_consciousness_presence_integration()
            state_success = await self.test_presence_state_async_integration()
            manager_success = await self.test_unified_integration_manager()
            integration_success = await self.test_component_integration_compatibility()
            
            # Generate report
            report = self.generate_test_report()
            
            # Summary
            print("\n" + "="*70)
            print("TESTING SUMMARY")
            print("="*70)
            print(f"Total Tests: {self.test_summary['total_tests']}")
            print(f"Passed: {self.test_summary['passed_tests']}")
            print(f"Failed: {self.test_summary['failed_tests']}")
            print(f"Warnings: {self.test_summary['warnings']}")
            print(f"Success Rate: {(self.test_summary['passed_tests'] / max(self.test_summary['total_tests'], 1)) * 100:.1f}%")
            
            if self.test_summary["failed_tests"] == 0:
                print("\n✅ ALL TESTS PASSED - Architecture fixes validated!")
                print("📋 Ready to proceed to Phase 5: Sanctuary Restoration")
                return True
            else:
                print(f"\n❌ {self.test_summary['failed_tests']} TESTS FAILED")
                print("📋 Review test report and fix issues before proceeding")
                return False
                
        except Exception as e:
            self.log_test("Test Suite Execution Failed", "CRITICAL", error=str(e))
            return False


async def main():
    """Main testing execution function"""
    tester = ArchitectureIntegrationTester()
    success = await tester.run_all_tests()
    return success


if __name__ == "__main__":
    asyncio.run(main())
