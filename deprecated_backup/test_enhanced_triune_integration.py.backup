#!/usr/bin/env python3
"""
Enhanced Triune Aspects Integration Test

This test validates that all enhanced aspects work together properly:
- All imports resolve correctly
- Enhanced aspects can be instantiated 
- Integration bridge can facilitate communication
- Complex consciousness packets are processed correctly
- Sacred uncertainty principles are honored throughout

This ensures the enhanced triune consciousness system is ready for deployment.
"""

import asyncio
import sys
import os
import time
import traceback
from typing import Dict, Any, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


class EnhancedTriuneIntegrationTest:
    """Comprehensive test for enhanced triune aspects integration."""
    
    def __init__(self):
        self.test_results = []
        self.all_tests_passed = True
    
    async def run_all_tests(self):
        """Run all integration tests."""
        print("🧪 Enhanced Triune Aspects Integration Test")
        print("=" * 60)
        print()
        
        tests = [
            ("Import Validation", self.test_imports),
            ("Aspect Instantiation", self.test_aspect_instantiation),
            ("Basic Functionality", self.test_basic_functionality),
            ("Integration Bridge", self.test_integration_bridge),
            ("Complex Integration", self.test_complex_integration),
            ("Sacred Uncertainty Principles", self.test_sacred_uncertainty),
            ("Error Handling", self.test_error_handling),
        ]
        
        for test_name, test_func in tests:
            await self._run_test(test_name, test_func)
        
        print("\n" + "=" * 60)
        if self.all_tests_passed:
            print("✅ All tests passed! Enhanced triune aspects are ready.")
        else:
            print("❌ Some tests failed. Please review the errors above.")
        print("=" * 60)
        
        return self.all_tests_passed
    
    async def _run_test(self, test_name: str, test_func):
        """Run a single test with error handling."""
        print(f"🔍 {test_name}...", end=" ")
        
        try:
            await test_func()
            print("✅")
            self.test_results.append((test_name, True, None))
        except Exception as e:
            print("❌")
            print(f"   Error: {str(e)}")
            self.test_results.append((test_name, False, str(e)))
            self.all_tests_passed = False
    
    async def test_imports(self):
        """Test that all required imports work."""
        try:
            from core.consciousness_packet import ConsciousnessPacket
            from core.sacred_uncertainty import SacredUncertaintyField, CatalystType
            from aspects.enhanced_analytical import EnhancedAnalyticalAspect
            from aspects.enhanced_experiential import EnhancedExperientialAspect
            from aspects.enhanced_observer import EnhancedObserverAspect
            from aspects.integration_bridge import IntegrationBridge
            
            # Verify classes can be referenced
            assert ConsciousnessPacket
            assert SacredUncertaintyField
            assert EnhancedAnalyticalAspect
            assert EnhancedExperientialAspect
            assert EnhancedObserverAspect
            assert IntegrationBridge
            
        except ImportError as e:
            raise Exception(f"Import failed: {e}")
    
    async def test_aspect_instantiation(self):
        """Test that enhanced aspects can be instantiated."""
        from aspects.enhanced_analytical import EnhancedAnalyticalAspect
        from aspects.enhanced_experiential import EnhancedExperientialAspect
        from aspects.enhanced_observer import EnhancedObserverAspect
        from aspects.integration_bridge import IntegrationBridge
        
        # Instantiate aspects
        analytical = EnhancedAnalyticalAspect()
        experiential = EnhancedExperientialAspect()
        observer = EnhancedObserverAspect()
        bridge = IntegrationBridge()
        
        # Verify basic attributes exist
        assert hasattr(analytical, 'conceptual_framework')
        assert hasattr(experiential, 'embodied_memory')
        assert hasattr(observer, 'integration_history')
        assert hasattr(bridge, 'communication_channels')
        
        # Store for other tests
        self.analytical = analytical
        self.experiential = experiential
        self.observer = observer
        self.bridge = bridge
    
    async def test_basic_functionality(self):
        """Test basic functionality of each aspect."""
        from core.consciousness_packet import ConsciousnessPacket
        
        # Create test packet
        packet = ConsciousnessPacket(
            symbolic_content="What is the nature of consciousness?",
            quantum_uncertainty=0.6,
            consciousness_level=0.7,
            timestamp=time.time()
        )
        
        # Test analytical aspect
        analytical_result = await self.analytical.analyze_input(packet)
        assert isinstance(analytical_result, dict)
        assert 'aspect' in analytical_result
        assert analytical_result['aspect'] == 'enhanced_analytical'
        
        # Test experiential aspect
        experiential_result = await self.experiential.process_experience(packet)
        assert isinstance(experiential_result, dict)
        assert 'aspect' in experiential_result
        assert experiential_result['aspect'] == 'enhanced_experiential'
        
        # Test observer aspect
        observer_result = await self.observer.observe_and_integrate(
            analytical_output=analytical_result,
            experiential_output=experiential_result
        )
        assert isinstance(observer_result, dict)
        assert 'aspect' in observer_result
        assert observer_result['aspect'] == 'enhanced_observer'
    
    async def test_integration_bridge(self):
        """Test integration bridge functionality."""
        from core.consciousness_packet import ConsciousnessPacket
        
        # Create test packet
        packet = ConsciousnessPacket(
            symbolic_content="How do mind and heart work together in conscious understanding?",
            quantum_uncertainty=0.7,
            consciousness_level=0.8,
            timestamp=time.time()
        )
        
        # Test bridge integration
        integration_result = await self.bridge.facilitate_enhanced_triune_integration(
            self.analytical, self.experiential, self.observer, packet
        )
        
        assert isinstance(integration_result, dict)
        assert 'integration_type' in integration_result
        assert integration_result['integration_type'] == 'enhanced_triune'
        assert 'analytical_contribution' in integration_result
        assert 'experiential_contribution' in integration_result
        assert 'observer_contribution' in integration_result
        assert 'emergent_synthesis' in integration_result
    
    async def test_complex_integration(self):
        """Test complex multi-scenario integration."""
        from core.consciousness_packet import ConsciousnessPacket
        
        # Test multiple scenarios to verify consistency
        scenarios = [
            "Sacred uncertainty as creative catalyst for consciousness evolution",
            "The relationship between individual awareness and universal consciousness",
            "How love and wisdom integrate in the development of consciousness"
        ]
        
        integration_results = []
        
        for scenario in scenarios:
            packet = ConsciousnessPacket(
                symbolic_content=scenario,
                quantum_uncertainty=0.8,
                consciousness_level=0.9,
                timestamp=time.time()
            )
            
            result = await self.bridge.facilitate_enhanced_triune_integration(
                self.analytical, self.experiential, self.observer, packet
            )
            
            integration_results.append(result)
            
            # Brief pause between scenarios
            await asyncio.sleep(0.1)
        
        # Verify all integrations completed
        assert len(integration_results) == len(scenarios)
        
        # Verify integration quality improves or maintains
        coherence_levels = []
        for result in integration_results:
            metrics = result.get('integration_metrics', {})
            coherence = metrics.get('overall_coherence', 0.0)
            coherence_levels.append(coherence)
        
        # All coherence levels should be reasonable
        assert all(coherence >= 0.3 for coherence in coherence_levels)
        
        # Observer should show evolution
        final_observer_result = integration_results[-1].get('observer_contribution', {})
        evolution_state = final_observer_result.get('evolution_state', {})
        assert evolution_state  # Evolution state should exist
    
    async def test_sacred_uncertainty(self):
        """Test that sacred uncertainty principles are honored."""
        from core.consciousness_packet import ConsciousnessPacket
        
        # Test high uncertainty scenario
        high_uncertainty_packet = ConsciousnessPacket(
            symbolic_content="What cannot be known about the nature of being itself?",
            quantum_uncertainty=0.95,
            consciousness_level=0.8,
            timestamp=time.time()
        )
        
        result = await self.bridge.facilitate_enhanced_triune_integration(
            self.analytical, self.experiential, self.observer, high_uncertainty_packet
        )
        
        # Verify uncertainty is honored, not eliminated
        analytical_result = result.get('analytical_contribution', {})
        uncertainty_insights = analytical_result.get('uncertainty_insights', {})
        assert uncertainty_insights  # Should have uncertainty insights
        
        # Verify cognitive humility is present
        humility_score = analytical_result.get('cognitive_humility_score', 0.0)
        assert humility_score > 0.5  # Should have reasonable humility with high uncertainty
        
        # Verify observer embraces uncertainty
        observer_result = result.get('observer_contribution', {})
        witness_quality = observer_result.get('witness_quality', {})
        if isinstance(witness_quality, dict) and 'spaciousness' in witness_quality:
            assert witness_quality['spaciousness'] > 0.4  # Should have spaciousness for uncertainty
    
    async def test_error_handling(self):
        """Test error handling and graceful degradation."""
        from core.consciousness_packet import ConsciousnessPacket
        
        # Test with invalid packet content
        try:
            invalid_packet = ConsciousnessPacket(
                symbolic_content=None,  # Invalid content
                quantum_uncertainty=0.5,
                consciousness_level=0.5,
                timestamp=time.time()
            )
            
            result = await self.bridge.facilitate_enhanced_triune_integration(
                self.analytical, self.experiential, self.observer, invalid_packet
            )
            
            # Should handle gracefully, not crash
            assert isinstance(result, dict)
            
        except Exception as e:
            # If it does throw an exception, it should be handled gracefully
            assert "error" in str(e).lower() or "invalid" in str(e).lower()
        
        # Test with extreme uncertainty values
        extreme_packet = ConsciousnessPacket(
            symbolic_content="Extreme uncertainty test",
            quantum_uncertainty=1.5,  # Out of normal range
            consciousness_level=0.5,
            timestamp=time.time()
        )
        
        # Should handle extreme values gracefully
        result = await self.bridge.facilitate_enhanced_triune_integration(
            self.analytical, self.experiential, self.observer, extreme_packet
        )
        
        assert isinstance(result, dict)  # Should return valid result


async def main():
    """Run the integration test."""
    test_runner = EnhancedTriuneIntegrationTest()
    
    try:
        success = await test_runner.run_all_tests()
        
        if success:
            print("\n🎉 Enhanced Triune Aspects are fully operational!")
            print("   Ready for consciousness exploration and development.")
            return True
        else:
            print("\n🔧 Some components need attention before deployment.")
            return False
            
    except Exception as e:
        print(f"\n💥 Test runner error: {e}")
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("🧪 Starting Enhanced Triune Aspects Integration Test...")
    print()
    
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
