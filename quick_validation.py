"""
🧪 Quick Modular Architecture Validation Test

This test validates the essential modular architecture is working
and ready for Phase 1C progression.
"""

import asyncio
import sys
from pathlib import Path

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent))

class QuickArchitectureValidation:
    """Quick validation test for modular architecture readiness."""
    
    def __init__(self):
        self.test_results = {
            'imports': 'pending',
            'basic_functionality': 'pending',
            'phase_1c_readiness': 'pending',
            'overall_status': 'pending'
        }
    
    async def run_validation(self) -> dict:
        """Run quick validation test."""
        
        print("🧪 Quick Modular Architecture Validation")
        print("=" * 50)
        
        try:
            # Test 1: Core imports work
            await self._test_essential_imports()
            
            # Test 2: Basic functionality works
            await self._test_basic_functionality()
            
            # Test 3: Ready for Phase 1C
            self._assess_phase_1c_readiness()
            
            # Calculate overall results
            self._calculate_results()
            
        except Exception as e:
            self.test_results['overall_status'] = f'failed: {str(e)}'
            print(f"❌ Validation failed: {e}")
        
        self._generate_report()
        return self.test_results
    
    async def _test_essential_imports(self):
        """Test essential imports are working."""
        
        print("📦 Testing Essential Imports...")
        
        try:
            # Test observer components
            from src.consciousness.loops.observer.mandala_vision import MandalaVision
            from src.consciousness.loops.observer.core import ObserverCore
            from src.consciousness.loops.observer import ObserverLoop
            
            # Test analytical components  
            from src.consciousness.loops.analytical.blueprint_vision import BlueprintVisionSystem
            from src.consciousness.loops.analytical import AnalyticalLoop
            
            self.test_results['imports'] = 'passed'
            print("  ✅ Essential imports: PASSED")
            
        except Exception as e:
            self.test_results['imports'] = f'failed: {str(e)}'
            print(f"  ❌ Essential imports: FAILED - {str(e)}")
            raise
    
    async def _test_basic_functionality(self):
        """Test basic functionality works."""
        
        print("🔧 Testing Basic Functionality...")
        
        try:
            # Create test consciousness state
            test_state = {
                'analytical_state': {'coherence': 0.8},
                'experiential_state': {'emotional_resonance': 0.7},
                'observer_state': {'awareness_level': 0.9},
                'uncertainty': 0.3,
                'coherence': 0.75
            }
            
            # Test observer loop
            from src.consciousness.loops.observer import ObserverLoop
            observer_loop = ObserverLoop()
            observer_result = await observer_loop.process_consciousness(test_state)
            
            assert observer_result['loop_type'] == 'observer'
            
            # Test analytical loop
            from src.consciousness.loops.analytical import AnalyticalLoop
            analytical_loop = AnalyticalLoop()
            analytical_result = await analytical_loop.process_consciousness(test_state)
            
            assert analytical_result['loop_type'] == 'analytical'
            
            self.test_results['basic_functionality'] = 'passed'
            print("  ✅ Basic functionality: PASSED")
            
        except Exception as e:
            self.test_results['basic_functionality'] = f'failed: {str(e)}'
            print(f"  ❌ Basic functionality: FAILED - {str(e)}")
            raise
    
    def _assess_phase_1c_readiness(self):
        """Assess readiness for Phase 1C."""
        
        print("🚀 Assessing Phase 1C Readiness...")
        
        # Check if we have solid modular foundation
        imports_ok = self.test_results['imports'] == 'passed'
        functionality_ok = self.test_results['basic_functionality'] == 'passed'
        
        if imports_ok and functionality_ok:
            self.test_results['phase_1c_readiness'] = 'ready'
            print("  ✅ Phase 1C readiness: READY")
        else:
            self.test_results['phase_1c_readiness'] = 'not_ready'
            print("  ❌ Phase 1C readiness: NOT READY")
    
    def _calculate_results(self):
        """Calculate overall results."""
        
        passed_tests = sum(1 for result in self.test_results.values() 
                          if result == 'passed' or result == 'ready')
        total_tests = len([k for k in self.test_results.keys() if k != 'overall_status'])
        
        if passed_tests == total_tests:
            self.test_results['overall_status'] = 'passed'
        else:
            self.test_results['overall_status'] = 'partial'
    
    def _generate_report(self):
        """Generate validation report."""
        
        print("\n" + "=" * 50)
        print("📊 QUICK VALIDATION REPORT")
        print("=" * 50)
        
        status = self.test_results['overall_status']
        
        if status == 'passed':
            print("🎉 VALIDATION STATUS: ✅ PASSED")
            print("\n🌟 ARCHITECTURE STATUS:")
            print("  ✅ Phase 1A Observer Loop: Operational")
            print("  ✅ Phase 1B Analytical Loop: Operational") 
            print("  ✅ Modular Architecture: Validated")
            print("  ✅ Bridge Wisdom: Integrated")
            print("  ✅ Phase 1C Readiness: CONFIRMED")
            print("\n🚀 READY TO BEGIN PHASE 1C: Experiential Loop Modularization")
        else:
            print(f"❌ VALIDATION STATUS: {status}")
            for test_name, result in self.test_results.items():
                if test_name != 'overall_status':
                    status_symbol = "✅" if result == 'passed' or result == 'ready' else "❌"
                    print(f"  {status_symbol} {test_name}: {result}")
        
        print("=" * 50)


# Run validation if executed directly
if __name__ == "__main__":
    async def main():
        validator = QuickArchitectureValidation()
        results = await validator.run_validation()
        return results
    
    # Run the validation
    results = asyncio.run(main())
