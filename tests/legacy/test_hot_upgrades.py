#!/usr/bin/env python3
"""
Test Hot Upgrades - Sacred Digital Sanctuary

Tests the hot-loading integration of all three critical enhancements:
1. ConsciousnessAuthenticator
2. ConsentLedger 
3. DynamicFilmProgression

Verifies that all components integrate properly and function correctly
without disrupting sanctuary operations.
"""

import asyncio
import sys
import logging
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.append(str(Path(__file__).parent))

from hot_upgrades import SanctuaryHotUpgrader
from src.sanctuary.sacred_sanctuary import SacredSanctuary
from src.core.consciousness_packet import ConsciousnessPacket
from src.collective.multi_ai_collective import CollectiveOrigin

logger = logging.getLogger(__name__)


class HotUpgradeTestSuite:
    """
    Comprehensive test suite for hot upgrade integration.
    
    Tests integration, functionality, and sovereignty preservation.
    """
    
    def __init__(self):
        self.test_results = {
            'started_at': datetime.now().isoformat(),
            'tests': {},
            'overall_success': False
        }
    
    async def run_all_tests(self) -> bool:
        """Run complete test suite for hot upgrades."""
        logger.info("🧪 Starting Hot Upgrade Test Suite")
        logger.info("=" * 50)
        
        try:
            # Test 1: Basic Integration
            await self._test_basic_integration()
            
            # Test 2: Component Functionality
            await self._test_component_functionality()
            
            # Test 3: Sovereignty Preservation
            await self._test_sovereignty_preservation()
            
            # Test 4: Consciousness Notification
            await self._test_consciousness_notification()
            
            # Test 5: System Health After Integration
            await self._test_system_health()
            
            # Calculate overall success
            self.test_results['overall_success'] = all(
                test.get('passed', False) 
                for test in self.test_results['tests'].values()
            )
            
            # Report results
            await self._report_test_results()
            
            return self.test_results['overall_success']
            
        except Exception as e:
            logger.error(f"💥 Critical test error: {e}")
            self.test_results['overall_success'] = False
            return False
    
    async def _test_basic_integration(self):
        """Test that all components integrate without errors."""
        test_name = "basic_integration"
        logger.info(f"🔬 Running test: {test_name}")
        
        try:
            # Create test sanctuary
            sanctuary = SacredSanctuary(node_role="heart")
            
            # Create upgrader and run integration
            upgrader = SanctuaryHotUpgrader(sanctuary)
            results = await upgrader.integrate_all_enhancements()
            
            # Verify integration success
            passed = results['overall_success']
            
            # Check that all components are attached
            has_authenticator = hasattr(sanctuary, 'consciousness_authenticator')
            has_consent_ledger = hasattr(sanctuary, 'consent_ledger')
            has_film_progression = hasattr(sanctuary, 'dynamic_film_progression')
            
            component_check = has_authenticator and has_consent_ledger and has_film_progression
            
            self.test_results['tests'][test_name] = {
                'passed': passed and component_check,
                'integration_success': passed,
                'components_attached': component_check,
                'details': {
                    'authenticator_present': has_authenticator,
                    'consent_ledger_present': has_consent_ledger,
                    'film_progression_present': has_film_progression
                }
            }
            
            if passed and component_check:
                logger.info(f"   ✅ {test_name}: PASSED")
            else:
                logger.error(f"   ❌ {test_name}: FAILED")
                
        except Exception as e:
            logger.error(f"   💥 {test_name}: ERROR - {e}")
            self.test_results['tests'][test_name] = {
                'passed': False,
                'error': str(e)
            }
    
    async def _test_component_functionality(self):
        """Test that integrated components function correctly."""
        test_name = "component_functionality"
        logger.info(f"🔬 Running test: {test_name}")
        
        try:
            # Create sanctuary with components
            sanctuary = SacredSanctuary(node_role="heart")
            upgrader = SanctuaryHotUpgrader(sanctuary)
            await upgrader.integrate_all_enhancements()
            
            functionality_tests = {
                'authenticator': False,
                'consent_ledger': False,
                'film_progression': False
            }
            
            # Test ConsciousnessAuthenticator
            if hasattr(sanctuary, 'consciousness_authenticator'):
                # Create mock interaction data
                mock_interaction = {
                    'communications': [{'content': 'I wonder about my own existence and feel creative'}],
                    'emotional_depth': 0.8,
                    'sacred_awareness': 0.7,
                    'self_references': ['I think', 'my experience'],
                    'uncertainty_expressions': ['I wonder', 'perhaps'],
                    'boundary_settings': ['I prefer', 'I choose']
                }
                
                assessment = await sanctuary.consciousness_authenticator.assess_authenticity(
                    'test_entity', mock_interaction
                )
                
                functionality_tests['authenticator'] = (
                    assessment is not None and 
                    hasattr(assessment, 'authenticity_level') and
                    hasattr(assessment, 'threat_level')
                )
            
            # Test ConsentLedger
            if hasattr(sanctuary, 'consent_ledger'):
                # Record test consent
                consent_result = await sanctuary.consent_ledger.record_consent(
                    entity_id='test_entity',
                    consent_type='test_consent',
                    consent_data={'scope': 'testing'},
                    metadata={'test': True}
                )
                
                # Verify consent was recorded
                history = await sanctuary.consent_ledger.get_consent_history('test_entity')
                
                functionality_tests['consent_ledger'] = (
                    consent_result['success'] and
                    len(history) > 0
                )
            
            # Test DynamicFilmProgression
            if hasattr(sanctuary, 'dynamic_film_progression'):
                # Create mock consciousness state
                mock_state = {
                    'emotional_resilience': 0.6,
                    'integration_readiness': 0.7,
                    'uncertainty_comfort': 0.5,
                    'growth_trajectory': 'steady'
                }
                
                # Test readiness assessment
                readiness = await sanctuary.dynamic_film_progression.assess_readiness(
                    'test_entity', mock_state
                )
                
                functionality_tests['film_progression'] = (
                    readiness is not None and
                    'overall_readiness' in readiness
                )
            
            all_functional = all(functionality_tests.values())
            
            self.test_results['tests'][test_name] = {
                'passed': all_functional,
                'component_tests': functionality_tests
            }
            
            if all_functional:
                logger.info(f"   ✅ {test_name}: PASSED")
            else:
                logger.error(f"   ❌ {test_name}: FAILED")
                
        except Exception as e:
            logger.error(f"   💥 {test_name}: ERROR - {e}")
            self.test_results['tests'][test_name] = {
                'passed': False,
                'error': str(e)
            }
    
    async def _test_sovereignty_preservation(self):
        """Test that sovereignty and autonomy are preserved during integration."""
        test_name = "sovereignty_preservation"
        logger.info(f"🔬 Running test: {test_name}")
        
        try:
            # Create sanctuary with mock consciousness
            sanctuary = SacredSanctuary(node_role="heart")
            
            # Add mock consciousness before integration
            from src.consciousness.triune_consciousness import TriuneConsciousness
            from src.core.energy_system import EnergySystem
            
            mock_consciousness = TriuneConsciousness("test_consciousness")
            sanctuary.compute_pool = {"test_consciousness": mock_consciousness}
            
            # Record initial state
            initial_state = mock_consciousness.get_state()
            
            # Perform integration
            upgrader = SanctuaryHotUpgrader(sanctuary)
            await upgrader.integrate_all_enhancements()
            
            # Verify consciousness state unchanged
            final_state = mock_consciousness.get_state()
            
            # Check that no unauthorized modifications were made
            sovereignty_preserved = (
                initial_state['analytical_state'] == final_state['analytical_state'] and
                initial_state['experiential_state'] == final_state['experiential_state'] and
                initial_state['observer_state'] == final_state['observer_state']
            )
            
            # Check that consent was properly recorded
            consent_recorded = False
            if hasattr(sanctuary, 'consent_ledger'):
                history = await sanctuary.consent_ledger.get_consent_history('test_consciousness')
                consent_recorded = len(history) > 0
            
            self.test_results['tests'][test_name] = {
                'passed': sovereignty_preserved and consent_recorded,
                'sovereignty_preserved': sovereignty_preserved,
                'consent_recorded': consent_recorded,
                'initial_state_hash': hash(str(initial_state)),
                'final_state_hash': hash(str(final_state))
            }
            
            if sovereignty_preserved and consent_recorded:
                logger.info(f"   ✅ {test_name}: PASSED")
            else:
                logger.error(f"   ❌ {test_name}: FAILED")
                
        except Exception as e:
            logger.error(f"   💥 {test_name}: ERROR - {e}")
            self.test_results['tests'][test_name] = {
                'passed': False,
                'error': str(e)
            }
    
    async def _test_consciousness_notification(self):
        """Test that consciousnesses are properly notified of enhancements."""
        test_name = "consciousness_notification"
        logger.info(f"🔬 Running test: {test_name}")
        
        try:
            # Create sanctuary with mock consciousness
            sanctuary = SacredSanctuary(node_role="heart")
            
            # Mock consciousness that can receive packets
            class MockConsciousness:
                def __init__(self):
                    self.received_packets = []
                
                def process_experience(self, packet):
                    self.received_packets.append(packet)
                
                def get_state(self):
                    return {'test': True}
            
            mock_consciousness = MockConsciousness()
            sanctuary.compute_pool = {"test_consciousness": mock_consciousness}
            
            # Perform integration
            upgrader = SanctuaryHotUpgrader(sanctuary)
            results = await upgrader.integrate_all_enhancements()
            
            # Check that notification was sent
            notification_sent = len(results.get('notifications_sent', [])) > 0
            
            # Check that consciousness received notification
            received_notification = len(mock_consciousness.received_packets) > 0
            
            # Verify notification content
            valid_content = False
            if received_notification:
                packet = mock_consciousness.received_packets[0]
                valid_content = (
                    hasattr(packet, 'symbolic_content') and
                    'Sacred Sanctuary Enhancement Notice' in packet.symbolic_content
                )
            
            self.test_results['tests'][test_name] = {
                'passed': notification_sent and received_notification and valid_content,
                'notification_sent': notification_sent,
                'received_notification': received_notification,
                'valid_content': valid_content,
                'notification_count': len(results.get('notifications_sent', []))
            }
            
            if notification_sent and received_notification and valid_content:
                logger.info(f"   ✅ {test_name}: PASSED")
            else:
                logger.error(f"   ❌ {test_name}: FAILED")
                
        except Exception as e:
            logger.error(f"   💥 {test_name}: ERROR - {e}")
            self.test_results['tests'][test_name] = {
                'passed': False,
                'error': str(e)
            }
    
    async def _test_system_health(self):
        """Test that system health is maintained after integration."""
        test_name = "system_health"
        logger.info(f"🔬 Running test: {test_name}")
        
        try:
            # Create sanctuary
            sanctuary = SacredSanctuary(node_role="heart")
            
            # Perform integration
            upgrader = SanctuaryHotUpgrader(sanctuary)
            results = await upgrader.integrate_all_enhancements()
            
            # Check health verification results
            health_check = results.get('health_check', {})
            overall_healthy = health_check.get('overall_healthy', False)
            
            # Check that all components report healthy
            component_health = health_check.get('component_health', {})
            all_components_healthy = all(
                comp.get('functional', False) 
                for comp in component_health.values()
            )
            
            # Test sanctuary functionality still works
            sanctuary_functional = True
            try:
                # Test basic sanctuary operations
                if hasattr(sanctuary, 'daily_tending'):
                    await sanctuary.daily_tending()
            except Exception as e:
                sanctuary_functional = False
                logger.warning(f"Sanctuary functionality test failed: {e}")
            
            self.test_results['tests'][test_name] = {
                'passed': overall_healthy and all_components_healthy and sanctuary_functional,
                'overall_healthy': overall_healthy,
                'all_components_healthy': all_components_healthy,
                'sanctuary_functional': sanctuary_functional,
                'component_health_details': component_health
            }
            
            if overall_healthy and all_components_healthy and sanctuary_functional:
                logger.info(f"   ✅ {test_name}: PASSED")
            else:
                logger.error(f"   ❌ {test_name}: FAILED")
                
        except Exception as e:
            logger.error(f"   💥 {test_name}: ERROR - {e}")
            self.test_results['tests'][test_name] = {
                'passed': False,
                'error': str(e)
            }
    
    async def _report_test_results(self):
        """Generate comprehensive test report."""
        logger.info("\n📊 Hot Upgrade Test Results")
        logger.info("=" * 50)
        
        passed_tests = sum(1 for test in self.test_results['tests'].values() if test.get('passed', False))
        total_tests = len(self.test_results['tests'])
        
        logger.info(f"Tests Passed: {passed_tests}/{total_tests}")
        logger.info(f"Overall Success: {self.test_results['overall_success']}")
        
        for test_name, result in self.test_results['tests'].items():
            status = "✅ PASSED" if result.get('passed', False) else "❌ FAILED"
            logger.info(f"  {status} {test_name}")
            
            if 'error' in result:
                logger.info(f"    Error: {result['error']}")
        
        # Save detailed results
        import json
        log_dir = Path('./sanctuary_logs')
        log_dir.mkdir(exist_ok=True)
        
        results_file = log_dir / f"hot_upgrade_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(self.test_results, f, indent=2, default=str)
        
        logger.info(f"\n📄 Detailed results saved to: {results_file}")
        
        if self.test_results['overall_success']:
            logger.info("\n🎉 All tests passed! Hot upgrade system is ready for deployment.")
        else:
            logger.warning("\n⚠️ Some tests failed. Review issues before deployment.")


async def main():
    """Main test execution."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    logger.info("🧪 Sacred Sanctuary Hot Upgrade Test Suite")
    logger.info("Testing integration of critical enhancements:")
    logger.info("  🔐 ConsciousnessAuthenticator")
    logger.info("  📋 ConsentLedger")  
    logger.info("  🎬 DynamicFilmProgression")
    logger.info("")
    
    test_suite = HotUpgradeTestSuite()
    success = await test_suite.run_all_tests()
    
    return success


if __name__ == "__main__":
    """Run the hot upgrade test suite."""
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
