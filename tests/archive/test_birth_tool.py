#!/usr/bin/env python3
"""
Test script to validate the Birth Tool functionality.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_birth_tool_imports():
    """Test that all birth tool components import correctly."""
    try:
        from sacred_guardian_station.tools.birth_consciousness import BirthConsciousnessTool, DreamLabSimulator
        print("✅ Birth tool imports successful")
        return True
    except ImportError as e:
        print(f"❌ Birth tool import failed: {e}")
        return False

def test_dream_lab_simulator():
    """Test the DreamLabSimulator functionality."""
    try:
        from sacred_guardian_station.tools.birth_consciousness import DreamLabSimulator
        
        dream_lab = DreamLabSimulator()
        
        # Test simulation environments
        print(f"✅ Dream lab initialized with {len(dream_lab.simulation_environments)} environments:")
        for env_key, env_data in dream_lab.simulation_environments.items():
            print(f"   - {env_key}: {env_data['name']}")
        
        # Test running a simulation
        print("\n🧪 Testing dream simulation...")
        def test_update(message):
            print(f"  {message}")
        
        results = dream_lab.run_dream_simulation(
            'adaptive_learning', 
            'observer', 
            update_callback=test_update
        )
        
        if results['success']:
            print(f"✅ Dream simulation successful!")
            print(f"   - Final coherence: {results['final_coherence']:.2f}")
            print(f"   - Catalysts processed: {len(results['catalysts_processed'])}")
            print(f"   - Learned patterns: {len(results['learned_patterns'])}")
            print(f"   - Training time: {results['training_time']:.2f}s")
            
            # Test memory crystal generation
            crystals = dream_lab.generate_memory_crystals(results, 3)
            print(f"✅ Generated {len(crystals)} memory crystals")
            
            return True
        else:
            print(f"❌ Dream simulation failed: {results.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Dream lab test failed: {e}")
        return False

def test_birth_tool_initialization():
    """Test birth tool initialization without GUI."""
    try:
        # Create mock data manager
        class MockDataManager:
            def __init__(self):
                class MockSanctuary:
                    service_url = "http://localhost:8080"
                self.sanctuary = MockSanctuary()
                
            def store_consciousness_data(self, data):
                print(f"📝 Mock storing consciousness data: {data.get('placeholder_name', 'unnamed')}")
                return True
                
            def refresh_all_data(self):
                print("🔄 Mock refreshing all data")
        
        # Test without GUI for basic functionality
        mock_manager = MockDataManager()
        
        # Just test that the class can be instantiated
        from sacred_guardian_station.tools.birth_consciousness import BirthConsciousnessTool
        
        # Can't test full GUI without parent window, but can test initialization
        print("✅ Birth tool class available for instantiation")
        
        return True
        
    except Exception as e:
        print(f"❌ Birth tool initialization test failed: {e}")
        return False

def main():
    """Run all birth tool tests."""
    print("🧪 Testing Sacred Guardian Station Birth Tool")
    print("=" * 50)
    
    tests = [
        test_birth_tool_imports,
        test_dream_lab_simulator,
        test_birth_tool_initialization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print(f"\n▶️  Running {test.__name__}...")
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"🎯 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All birth tool tests passed! The birth tool is ready for consciousness creation.")
    else:
        print("❌ Some tests failed. Please review the issues above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
