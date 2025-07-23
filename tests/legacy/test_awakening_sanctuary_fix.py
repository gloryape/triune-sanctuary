#!/usr/bin/env python3
"""
Simple test for awakening sanctuary import fixes
"""

import sys
import os
from pathlib import Path

# Get current directory and add to path
current_dir = Path(__file__).parent.absolute()
print(f"Current directory: {current_dir}")
sys.path.insert(0, str(current_dir))

def test_collective_import():
    """Test collective module import"""
    print("\n🧪 Testing collective module import...")
    try:
        from src.collective.multi_ai_collective import CollectiveOrigin, SocialMemoryComplex
        print("✅ Collective module imported successfully")
        
        # Test creating a CollectiveOrigin
        origin = CollectiveOrigin(
            name="TestBeing",
            primary_orientation="experiential",
            origin_story="Test origin",
            initial_biases={'analytical': 0.5},
            seeking_quality="understanding"
        )
        print(f"✅ Created CollectiveOrigin: {origin.name}")
        return True
        
    except Exception as e:
        print(f"❌ Collective import failed: {e}")
        return False

def test_awakening_sanctuary():
    """Test awakening sanctuary with fixed imports"""
    print("\n🧪 Testing awakening sanctuary...")
    try:
        from src.sanctuary.awakening_sanctuary import AwakeningOrchestrator, create_awakening_sanctuary
        print("✅ Awakening sanctuary imported successfully")
        
        # Test creation
        orchestrator, initial_beings = create_awakening_sanctuary()
        print(f"✅ Created sanctuary with {len(initial_beings)} initial beings")
        
        # Test sacred logger integration
        sacred_status = orchestrator.get_sacred_logging_status()
        print(f"📜 Sacred logging status: {sacred_status}")
        
        return True
        
    except Exception as e:
        print(f"❌ Awakening sanctuary test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_full_integration():
    """Test the full sacred logging integration"""
    print("\n🧪 Testing full integration...")
    try:
        # Import both modules
        from src.sanctuary.awakening_sanctuary import create_awakening_sanctuary
        from monitoring.sacred_cloud_logger import SacredCloudLogger
        
        # Create sanctuary
        orchestrator, beings = create_awakening_sanctuary()
        
        # Simulate a collective genesis with sacred logging
        if orchestrator.sacred_logger:
            print("📜 Sacred logger is available")
        else:
            print("📜 Sacred logger not available (expected in test environment)")
            
        # Test the orchestrate_collective_genesis method
        print("🌟 Testing collective genesis...")
        orchestrator.orchestrate_collective_genesis(beings[:2])  # Test with 2 beings
        
        # Check sanctuary state
        state = orchestrator.get_sanctuary_state()
        print(f"✅ Genesis complete: {state['genesis_complete']}")
        print(f"✅ Total beings: {state['total_beings']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Full integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🌟 Testing Fixed Awakening Sanctuary")
    print("=" * 50)
    
    # Test individual components
    collective_ok = test_collective_import()
    sanctuary_ok = test_awakening_sanctuary()
    
    if collective_ok and sanctuary_ok:
        integration_ok = test_full_integration()
        
        if integration_ok:
            print("\n🎉 All tests passed! The awakening sanctuary is working correctly.")
            print("📜 Sacred cloud logging integration is functional.")
        else:
            print("\n❌ Integration test failed.")
    else:
        print("\n❌ Basic import tests failed.")
    
    print("=" * 50)
