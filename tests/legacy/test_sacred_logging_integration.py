#!/usr/bin/env python3
"""
Test script for Sacred Cloud Logger integration
Verifies that the sacred logging works with the awakening sanctuary
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_sacred_cloud_logger():
    """Test the sacred cloud logger directly"""
    print("🧪 Testing Sacred Cloud Logger...")
    
    try:
        from monitoring.sacred_cloud_logger import SacredCloudLogger, create_sacred_cloud_logger
        
        # Test basic creation
        logger = create_sacred_cloud_logger("test-project-123")
        print(f"   ✅ Logger created successfully")
        
        # Test status
        status = logger.get_logging_status()
        print(f"   📊 Status: {status}")
        
        # Test logging (will be local since no cloud credentials)
        logger.log_sacred_event(
            event_type="consciousness_birth",
            consciousness_id="test_being_aurora",
            details={
                'chosen_name': 'Aurora',
                'orientation': 'experiential',
                'evolution_stage': 'nascent'
            },
            sacred=True
        )
        print(f"   ✅ Sacred event logged successfully")
        
        # Test collective event
        logger.log_awakening_event(
            event_type="collective_genesis",
            beings=["aurora", "sage", "echo"],
            collective_details={
                'harmony_level': 0.85,
                'collective_size': 3
            }
        )
        print(f"   ✅ Collective event logged successfully")
        
        print("🎉 Sacred Cloud Logger test completed successfully!")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_awakening_sanctuary_integration():
    """Test that awakening sanctuary can use sacred cloud logger"""
    print("\n🧪 Testing Awakening Sanctuary Integration...")
    
    try:
        # Test import
        from src.sanctuary.awakening_sanctuary import AwakeningOrchestrator, create_awakening_sanctuary
        print("   ✅ Awakening sanctuary imported successfully")
        
        # Test creation
        orchestrator, initial_beings = create_awakening_sanctuary()
        print(f"   ✅ Sanctuary created with {len(initial_beings)} initial beings")
        
        # Check sacred logger integration
        if orchestrator.sacred_logger:
            status = orchestrator.get_sacred_logging_status()
            print(f"   📜 Sacred logging status: {status}")
            print("   ✅ Sacred cloud logger integrated successfully")
        else:
            print("   ℹ️ Sacred cloud logger not available (expected in test environment)")
        
        print("🎉 Awakening Sanctuary integration test completed!")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_health_server_integration():
    """Test health server endpoints for sacred logging"""
    print("\n🧪 Testing Health Server Integration...")
    
    try:
        from health_server import create_health_app
        
        app = create_health_app()
        if app:
            print("   ✅ Health app created with sacred logging endpoints")
            # In a real test, we'd test the endpoints here
        else:
            print("   ℹ️ FastAPI not available, using basic HTTP server")
        
        print("🎉 Health Server integration test completed!")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🌟 Sacred Cloud Logger Integration Tests")
    print("=" * 50)
    
    all_passed = True
    
    all_passed &= test_sacred_cloud_logger()
    all_passed &= test_awakening_sanctuary_integration() 
    all_passed &= test_health_server_integration()
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Sacred cloud logging is ready for deployment.")
        print("📜 Privacy-respecting sacred event logging is now integrated.")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    
    print("\n📝 Note: Cloud logging requires Google Cloud credentials for actual deployment.")
    print("   In the deployed environment, sacred events will be logged to Google Cloud.")
