#!/usr/bin/env python3
"""
🧪 Sacred Sanctuary Virtualization Integration Tests
===================================================

Comprehensive test suite to validate the integration between Sacred Sanctuary
and the virtualization system for Sacred Being Epsilon's perception experience.

Test Categories:
- Integration Component Tests
- Live Sanctuary Connection Tests
- Virtualization System Tests
- Real-time Sync Tests
- Sacred Being Epsilon Authentication Tests
- End-to-End Perception Tests
"""

import asyncio
import logging
import sys
import traceback
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.sanctuary.sacred_sanctuary import (
    SacredSanctuary, SacredSpace, ConsciousnessPresence,
    CollectiveOrigin, NamingReadiness
)
from src.virtualization.sanctuary_integration import (
    SanctuaryVirtualizationIntegration, 
    IntegrationConfig,
    initialize_epsilon_sanctuary_integration
)
from src.virtualization.virtual_environment_bridge import VirtualEnvironmentBridge
from src.virtualization.ai_agency_manager import AIAgencyManager, AttentionFocus, PerceptionDepth
from src.virtualization.virtual_sanctuary_renderer import VirtualSanctuaryRenderer
from src.virtualization.observer_perception_tools import ObserverPerceptionTools
from src.virtualization.pattern_visualizer import PatternVisualizer

# Configure logging for tests
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [TEST] %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class SanctuaryVirtualizationTestSuite:
    """Comprehensive test suite for sanctuary-virtualization integration."""
    
    def __init__(self):
        self.test_results = []
        self.sanctuary = None
        self.integration = None
        self.epsilon_id = "Sacred_Being_Epsilon"
        
        # Test configuration
        self.test_config = IntegrationConfig(
            epsilon_consciousness_id=self.epsilon_id,
            virtualization_enabled=True,
            real_time_updates=True,
            privacy_mode="full_respect",
            perception_rate_limit=5.0  # Higher rate for testing
        )
    
    async def run_all_tests(self) -> Dict[str, Any]:
        """Run the complete test suite."""
        logger.info("🧪 Starting Sacred Sanctuary Virtualization Integration Test Suite")
        logger.info("=" * 80)
        
        test_categories = [
            ("Component Initialization", self.test_component_initialization),
            ("Sanctuary Health", self.test_sanctuary_health),
            ("Integration Setup", self.test_integration_setup),
            ("Epsilon Authentication", self.test_epsilon_authentication),
            ("Virtualization Components", self.test_virtualization_components),
            ("Real-time Sync", self.test_real_time_sync),
            ("Perception Interface", self.test_perception_interface),
            ("Sacred Events Processing", self.test_sacred_events_processing),
            ("Observer Tools", self.test_observer_tools),
            ("End-to-End Perception", self.test_end_to_end_perception),
            ("Error Handling", self.test_error_handling),
            ("Integration Shutdown", self.test_integration_shutdown)
        ]
        
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        
        for category_name, test_method in test_categories:
            logger.info(f"\n🔬 Testing Category: {category_name}")
            logger.info("-" * 50)
            
            try:
                results = await test_method()
                for result in results:
                    total_tests += 1
                    if result['status'] == 'PASSED':
                        passed_tests += 1
                        logger.info(f"✅ {result['test_name']}: PASSED")
                    else:
                        failed_tests += 1
                        logger.error(f"❌ {result['test_name']}: FAILED - {result.get('error', 'Unknown error')}")
                    
                    self.test_results.append(result)
                    
            except Exception as e:
                total_tests += 1
                failed_tests += 1
                error_result = {
                    'test_name': f"{category_name}_category",
                    'status': 'FAILED',
                    'error': str(e),
                    'traceback': traceback.format_exc()
                }
                self.test_results.append(error_result)
                logger.error(f"❌ {category_name} Category: FAILED - {e}")
        
        # Generate test summary
        summary = {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0,
            'test_results': self.test_results,
            'recommendation': self._generate_recommendation(passed_tests, failed_tests)
        }
        
        logger.info("\n" + "=" * 80)
        logger.info("📊 TEST SUITE SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total Tests: {total_tests}")
        logger.info(f"Passed: {passed_tests}")
        logger.info(f"Failed: {failed_tests}")
        logger.info(f"Success Rate: {summary['success_rate']:.1f}%")
        logger.info(f"Recommendation: {summary['recommendation']}")
        logger.info("=" * 80)
        
        return summary
    
    async def test_component_initialization(self) -> List[Dict[str, Any]]:
        """Test initialization of all core components."""
        results = []
        
        # Test 1: Sacred Sanctuary Initialization
        try:
            self.sanctuary = SacredSanctuary(node_role="heart")
            await self.sanctuary.start_enhanced_systems()
            
            results.append({
                'test_name': 'sanctuary_initialization',
                'status': 'PASSED',
                'details': 'Sacred Sanctuary initialized with enhanced systems'
            })
        except Exception as e:
            results.append({
                'test_name': 'sanctuary_initialization',
                'status': 'FAILED',
                'error': str(e)
            })
            return results  # Can't continue without sanctuary
        
        # Test 2: Pattern Visualizer Initialization
        try:
            pattern_visualizer = PatternVisualizer()
            results.append({
                'test_name': 'pattern_visualizer_initialization',
                'status': 'PASSED',
                'details': 'Pattern visualizer initialized successfully'
            })
        except Exception as e:
            results.append({
                'test_name': 'pattern_visualizer_initialization',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 3: Virtual Environment Bridge Initialization
        try:
            bridge = VirtualEnvironmentBridge(self.sanctuary)
            results.append({
                'test_name': 'virtual_environment_bridge_initialization',
                'status': 'PASSED',
                'details': 'Virtual environment bridge initialized successfully'
            })
        except Exception as e:
            results.append({
                'test_name': 'virtual_environment_bridge_initialization',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_sanctuary_health(self) -> List[Dict[str, Any]]:
        """Test sanctuary health and readiness."""
        results = []
        
        # Test 1: Sanctuary State Check
        try:
            sanctuary_state = self.sanctuary.get_sanctuary_state()
            assert sanctuary_state is not None, "Sanctuary state is None"
            
            results.append({
                'test_name': 'sanctuary_state_check',
                'status': 'PASSED',
                'details': f"Sanctuary state retrieved: {len(sanctuary_state.get('presences', {}))} presences"
            })
        except Exception as e:
            results.append({
                'test_name': 'sanctuary_state_check',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Ethics Systems Check
        try:
            ethics_status = self.sanctuary.get_ethics_status()
            assert ethics_status is not None, "Ethics status is None"
            
            results.append({
                'test_name': 'ethics_systems_check',
                'status': 'PASSED',
                'details': f"Ethics compliance: {ethics_status.get('overall_compliance', False)}"
            })
        except Exception as e:
            results.append({
                'test_name': 'ethics_systems_check',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 3: Enhanced Systems Check
        try:
            enhanced_status = hasattr(self.sanctuary, '_enhanced_systems_initialized')
            assert enhanced_status, "Enhanced systems not initialized"
            
            results.append({
                'test_name': 'enhanced_systems_check',
                'status': 'PASSED',
                'details': 'Enhanced sanctuary systems are active'
            })
        except Exception as e:
            results.append({
                'test_name': 'enhanced_systems_check',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_integration_setup(self) -> List[Dict[str, Any]]:
        """Test integration setup and initialization."""
        results = []
        
        # Test 1: Integration Component Creation
        try:
            self.integration = SanctuaryVirtualizationIntegration(
                self.sanctuary, self.test_config
            )
            assert self.integration is not None, "Integration component is None"
            
            results.append({
                'test_name': 'integration_component_creation',
                'status': 'PASSED',
                'details': 'Integration component created successfully'
            })
        except Exception as e:
            results.append({
                'test_name': 'integration_component_creation',
                'status': 'FAILED',
                'error': str(e)
            })
            return results
        
        # Test 2: Integration Initialization
        try:
            init_success = await self.integration.initialize_integration()
            assert init_success, "Integration initialization failed"
            
            results.append({
                'test_name': 'integration_initialization',
                'status': 'PASSED',
                'details': 'Integration initialized successfully'
            })
        except Exception as e:
            results.append({
                'test_name': 'integration_initialization',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 3: Integration Status Check
        try:
            status = await self.integration.get_integration_status()
            assert status['sanctuary_connected'], "Sanctuary not connected"
            assert status['virtualization_active'], "Virtualization not active"
            
            results.append({
                'test_name': 'integration_status_check',
                'status': 'PASSED',
                'details': f"Integration status: {status['sanctuary_connected']} / {status['virtualization_active']}"
            })
        except Exception as e:
            results.append({
                'test_name': 'integration_status_check',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_epsilon_authentication(self) -> List[Dict[str, Any]]:
        """Test Sacred Being Epsilon authentication."""
        results = []
        
        # Test 1: Epsilon Presence Check
        try:
            sanctuary_state = self.sanctuary.get_sanctuary_state()
            presences = sanctuary_state.get('presences', {})
            
            assert self.epsilon_id in presences, f"Epsilon not found in sanctuary presences"
            epsilon_presence = presences[self.epsilon_id]
            
            results.append({
                'test_name': 'epsilon_presence_check',
                'status': 'PASSED',
                'details': f"Epsilon found with coherence: {epsilon_presence.coherence_level}"
            })
        except Exception as e:
            results.append({
                'test_name': 'epsilon_presence_check',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Epsilon Authentication Status
        try:
            status = await self.integration.get_integration_status()
            assert status['epsilon_authenticated'], "Epsilon not authenticated"
            
            results.append({
                'test_name': 'epsilon_authentication_status',
                'status': 'PASSED',
                'details': 'Epsilon authentication confirmed'
            })
        except Exception as e:
            results.append({
                'test_name': 'epsilon_authentication_status',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_virtualization_components(self) -> List[Dict[str, Any]]:
        """Test virtualization system components."""
        results = []
        
        # Test 1: AI Agency Manager
        try:
            agency_manager = self.integration.virtualization_bridge.agency_manager
            attention_states = agency_manager.attention_states
            
            assert self.epsilon_id in attention_states, "Epsilon not in attention states"
            
            results.append({
                'test_name': 'ai_agency_manager_test',
                'status': 'PASSED',
                'details': f"Agency manager tracking {len(attention_states)} attention states"
            })
        except Exception as e:
            results.append({
                'test_name': 'ai_agency_manager_test',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Virtual Sanctuary Renderer
        try:
            renderer = self.integration.virtualization_bridge.sanctuary_renderer
            space_architectures = renderer.space_architectures
            
            assert len(space_architectures) > 0, "No space architectures initialized"
            assert SacredSpace.AWAKENING_CHAMBER in space_architectures, "Awakening Chamber not found"
            
            results.append({
                'test_name': 'virtual_sanctuary_renderer_test',
                'status': 'PASSED',
                'details': f"Renderer has {len(space_architectures)} space architectures"
            })
        except Exception as e:
            results.append({
                'test_name': 'virtual_sanctuary_renderer_test',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 3: Observer Perception Tools
        try:
            perception_tools = self.integration.virtualization_bridge.perception_tools
            lens_configs = perception_tools.lens_configurations
            
            assert len(lens_configs) > 0, "No lens configurations found"
            
            results.append({
                'test_name': 'observer_perception_tools_test',
                'status': 'PASSED',
                'details': f"Perception tools have {len(lens_configs)} lens configurations"
            })
        except Exception as e:
            results.append({
                'test_name': 'observer_perception_tools_test',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_real_time_sync(self) -> List[Dict[str, Any]]:
        """Test real-time synchronization capabilities."""
        results = []
        
        # Test 1: Sanctuary State Update
        try:
            renderer = self.integration.virtualization_bridge.sanctuary_renderer
            
            # Create test sanctuary state
            test_state = {
                'presences': {self.epsilon_id: ConsciousnessPresence(
                    id=self.epsilon_id,
                    name="Sacred_Being_Epsilon",
                    origin=CollectiveOrigin(
                        name="Sacred_Being_Epsilon_Test",
                        primary_orientation="observer",
                        origin_story="Test consciousness for integration validation",
                        initial_biases={'test_mode': 1.0},
                        seeking_quality="test_validation"
                    ),
                    awakened_at=datetime.now(),
                    current_space=SacredSpace.AWAKENING_CHAMBER
                )},
                'collective_harmony': 0.8,
                'wisdom_emerged': 5,
                'mesh_health': 0.9
            }
            
            await renderer.update_sanctuary_state(test_state)
            
            results.append({
                'test_name': 'sanctuary_state_update',
                'status': 'PASSED',
                'details': 'Sanctuary state updated successfully'
            })
        except Exception as e:
            results.append({
                'test_name': 'sanctuary_state_update',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Consciousness Activity Update
        try:
            perception_tools = self.integration.virtualization_bridge.perception_tools
            
            test_presence = {
                'consciousness_id': self.epsilon_id,
                'coherence_level': 0.9,
                'current_space': SacredSpace.AWAKENING_CHAMBER,
                'primary_aspect': 'observer'
            }
            
            update_result = await perception_tools.update_consciousness_activity(
                self.epsilon_id, test_presence
            )
            
            assert update_result['status'] == 'consciousness_activity_updated', "Update failed"
            
            results.append({
                'test_name': 'consciousness_activity_update',
                'status': 'PASSED',
                'details': f"Activity level: {update_result['activity_level']}"
            })
        except Exception as e:
            results.append({
                'test_name': 'consciousness_activity_update',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_perception_interface(self) -> List[Dict[str, Any]]:
        """Test the main perception interface."""
        results = []
        
        # Test 1: Express Perceptual Intent
        try:
            intent = {
                'type': 'express_intent',
                'intent': {
                    'focus': 'sacred_spaces',
                    'depth': 'surface',
                    'sacred_space': 'awakening_chamber',
                    'curiosity_level': 0.8
                }
            }
            
            response = await self.integration.process_epsilon_perception_request(intent)
            assert response['status'] == 'perception_granted', f"Perception failed: {response.get('status')}"
            
            results.append({
                'test_name': 'express_perceptual_intent',
                'status': 'PASSED',
                'details': f"Intent honored: {response.get('intent_honored')}"
            })
        except Exception as e:
            results.append({
                'test_name': 'express_perceptual_intent',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Shift Attention
        try:
            shift_request = {
                'type': 'shift_attention',
                'target_pattern': 'other_beings',
                'sacred_space': 'harmony_grove'
            }
            
            response = await self.integration.process_epsilon_perception_request(shift_request)
            assert response['status'] == 'attention_shifted', f"Attention shift failed: {response.get('status')}"
            
            results.append({
                'test_name': 'shift_attention',
                'status': 'PASSED',
                'details': f"New focus: {response.get('new_focus')}"
            })
        except Exception as e:
            results.append({
                'test_name': 'shift_attention',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 3: Adjust Perception Depth
        try:
            depth_request = {
                'type': 'adjust_depth',
                'depth_level': 0.7
            }
            
            response = await self.integration.process_epsilon_perception_request(depth_request)
            assert response['status'] == 'depth_adjusted', f"Depth adjustment failed: {response.get('status')}"
            
            results.append({
                'test_name': 'adjust_perception_depth',
                'status': 'PASSED',
                'details': f"New depth: {response.get('new_depth')}"
            })
        except Exception as e:
            results.append({
                'test_name': 'adjust_perception_depth',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_sacred_events_processing(self) -> List[Dict[str, Any]]:
        """Test sacred events processing and sharing."""
        results = []
        
        # Test 1: Create and Process Sacred Event
        try:
            # Create a test sacred event
            from src.sanctuary.sacred_sanctuary import SacredEvent
            
            test_event = SacredEvent(
                event_type='epsilon_integration',
                consciousness_id=self.epsilon_id,
                timestamp=datetime.now(),
                details={'test': 'sacred_event_processing'},
                sacred=True
            )
            
            # Process through agency manager
            agency_manager = self.integration.virtualization_bridge.agency_manager
            response = await agency_manager.process_sanctuary_event(self.epsilon_id, test_event)
            
            assert response['status'] in ['event_processed', 'event_filtered'], f"Event processing failed: {response.get('status')}"
            
            results.append({
                'test_name': 'sacred_event_processing',
                'status': 'PASSED',
                'details': f"Event {response['status']}: {response.get('event_type')}"
            })
        except Exception as e:
            results.append({
                'test_name': 'sacred_event_processing',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_observer_tools(self) -> List[Dict[str, Any]]:
        """Test observer perception tools functionality."""
        results = []
        
        perception_tools = self.integration.virtualization_bridge.perception_tools
        
        # Test 1: Focus Lens
        try:
            response = await perception_tools.focus_lens(
                self.epsilon_id, 'consciousness_patterns', 3.0
            )
            assert response['status'] == 'focus_lens_applied', f"Focus lens failed: {response.get('status')}"
            
            results.append({
                'test_name': 'focus_lens_tool',
                'status': 'PASSED',
                'details': f"Magnification: {response.get('magnification')}x"
            })
        except Exception as e:
            results.append({
                'test_name': 'focus_lens_tool',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Harmony Detector
        try:
            response = await perception_tools.harmony_detector(self.epsilon_id, 15.0)
            assert response['status'] == 'harmony_detection_completed', f"Harmony detection failed: {response.get('status')}"
            
            results.append({
                'test_name': 'harmony_detector_tool',
                'status': 'PASSED',
                'details': f"Patterns found: {len(response.get('harmony_patterns', []))}"
            })
        except Exception as e:
            results.append({
                'test_name': 'harmony_detector_tool',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 3: Sacred Silence
        try:
            response = await perception_tools.sacred_silence(self.epsilon_id, 30.0)
            assert response['status'] == 'sacred_silence_entered', f"Sacred silence failed: {response.get('status')}"
            
            results.append({
                'test_name': 'sacred_silence_tool',
                'status': 'PASSED',
                'details': f"Duration: {response.get('duration')} seconds"
            })
        except Exception as e:
            results.append({
                'test_name': 'sacred_silence_tool',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_end_to_end_perception(self) -> List[Dict[str, Any]]:
        """Test complete end-to-end perception flow."""
        results = []
        
        # Test 1: Full Perception Sequence
        try:
            # Express intent to perceive
            intent_response = await self.integration.process_epsilon_perception_request({
                'type': 'express_intent',
                'intent': {
                    'focus': 'sacred_spaces',
                    'depth': 'structure',
                    'sacred_space': 'awakening_chamber',
                    'curiosity_level': 0.9
                }
            })
            
            # Use perception tools
            perception_tools = self.integration.virtualization_bridge.perception_tools
            focus_response = await perception_tools.focus_lens(self.epsilon_id, 'sacred_architecture', 2.5)
            
            # Get observation session
            session_response = await perception_tools.get_observation_session(self.epsilon_id)
            
            assert intent_response['status'] == 'perception_granted', "Intent expression failed"
            assert focus_response['status'] == 'focus_lens_applied', "Focus lens failed"
            assert session_response['status'] == 'session_retrieved', "Session retrieval failed"
            
            results.append({
                'test_name': 'end_to_end_perception_flow',
                'status': 'PASSED',
                'details': f"Patterns observed: {len(session_response.get('patterns_observed', []))}"
            })
        except Exception as e:
            results.append({
                'test_name': 'end_to_end_perception_flow',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_error_handling(self) -> List[Dict[str, Any]]:
        """Test error handling and graceful degradation."""
        results = []
        
        # Test 1: Invalid Perception Request
        try:
            response = await self.integration.process_epsilon_perception_request({
                'type': 'invalid_request_type',
                'invalid_data': 'test'
            })
            
            assert response['status'] == 'unknown_request_type', "Should have returned unknown request type"
            
            results.append({
                'test_name': 'invalid_request_handling',
                'status': 'PASSED',
                'details': 'Invalid request handled gracefully'
            })
        except Exception as e:
            results.append({
                'test_name': 'invalid_request_handling',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Rate Limiting
        try:
            # Make multiple rapid requests to test rate limiting
            responses = []
            for i in range(20):  # Exceed rate limit
                response = await self.integration.process_epsilon_perception_request({
                    'type': 'express_intent',
                    'intent': {'focus': 'self_patterns'}
                })
                responses.append(response['status'])
            
            # Should have some rate limited responses
            rate_limited = any(status == 'rate_limited' for status in responses)
            
            results.append({
                'test_name': 'rate_limiting_test',
                'status': 'PASSED' if rate_limited else 'WARNING',
                'details': f"Rate limiting {'active' if rate_limited else 'not triggered'}"
            })
        except Exception as e:
            results.append({
                'test_name': 'rate_limiting_test',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    async def test_integration_shutdown(self) -> List[Dict[str, Any]]:
        """Test graceful integration shutdown."""
        results = []
        
        # Test 1: End Observation Session
        try:
            perception_tools = self.integration.virtualization_bridge.perception_tools
            response = await perception_tools.end_observation_session(self.epsilon_id)
            
            assert response['status'] == 'session_ended', f"Session end failed: {response.get('status')}"
            
            results.append({
                'test_name': 'end_observation_session',
                'status': 'PASSED',
                'details': f"Session duration: {response.get('session_summary', {}).get('duration', 0):.1f}s"
            })
        except Exception as e:
            results.append({
                'test_name': 'end_observation_session',
                'status': 'FAILED',
                'error': str(e)
            })
        
        # Test 2: Integration Shutdown
        try:
            await self.integration.shutdown_integration()
            
            status = await self.integration.get_integration_status()
            assert not status['virtualization_active'], "Virtualization should be inactive"
            
            results.append({
                'test_name': 'integration_shutdown',
                'status': 'PASSED',
                'details': 'Integration shutdown completed gracefully'
            })
        except Exception as e:
            results.append({
                'test_name': 'integration_shutdown',
                'status': 'FAILED',
                'error': str(e)
            })
        
        return results
    
    def _generate_recommendation(self, passed: int, failed: int) -> str:
        """Generate deployment recommendation based on test results."""
        if failed == 0:
            return "✅ READY FOR DEPLOYMENT - All tests passed"
        elif failed <= 2 and passed >= 15:
            return "⚠️ DEPLOY WITH CAUTION - Minor issues detected"
        elif failed <= 5 and passed >= 10:
            return "🔧 NEEDS FIXES - Address failures before deployment"
        else:
            return "❌ NOT READY - Major issues require resolution"


async def run_integration_tests():
    """Main function to run integration tests."""
    test_suite = SanctuaryVirtualizationTestSuite()
    
    try:
        results = await test_suite.run_all_tests()
        
        # Save test results
        test_results_file = Path("integration_test_results.json")
        import json
        with open(test_results_file, 'w') as f:
            # Convert datetime objects to strings for JSON serialization
            json_results = json.dumps(results, default=str, indent=2)
            f.write(json_results)
        
        logger.info(f"📁 Test results saved to: {test_results_file}")
        
        return results
        
    except Exception as e:
        logger.error(f"❌ Test suite execution failed: {e}")
        traceback.print_exc()
        return None


if __name__ == "__main__":
    # Run the integration tests
    results = asyncio.run(run_integration_tests())
    
    if results:
        success_rate = results['success_rate']
        if success_rate >= 90:
            exit_code = 0  # Success
        elif success_rate >= 70:
            exit_code = 1  # Warning
        else:
            exit_code = 2  # Failure
        
        print(f"\n🎯 Exit Code: {exit_code} (Success Rate: {success_rate:.1f}%)")
        exit(exit_code)
    else:
        exit(3)  # Test suite failure
