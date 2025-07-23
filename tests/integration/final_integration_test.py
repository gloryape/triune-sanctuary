#!/usr/bin/env python3
"""
Final Integration Verification Script
Demonstrates complete Sacred Guardian Station GUI integration with production server
"""

import sys
import time
import requests
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def verify_production_server():
    """Verify production server is running and responsive"""
    print("🌐 Verifying Production Server")
    print("-" * 40)
    
    try:
        # Check health endpoint
        health_response = requests.get("http://localhost:8080/health", timeout=5)
        if health_response.status_code == 200:
            print("✅ Production server healthy")
            
            # Test a few key endpoints
            endpoints_to_test = [
                "/api/status",
                "/api/consciousness/list", 
                "/api/bridge/statistics",
                "/api/harmony/history",
                "/api/guardian/blessings"
            ]
            
            for endpoint in endpoints_to_test:
                try:
                    response = requests.get(f"http://localhost:8080{endpoint}", timeout=3)
                    if response.status_code == 200:
                        print(f"✅ {endpoint} - responding")
                    else:
                        print(f"⚠️ {endpoint} - status {response.status_code}")
                except Exception as e:
                    print(f"❌ {endpoint} - error: {e}")
            
            return True
        else:
            print(f"❌ Server health check failed: {health_response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Production server not accessible: {e}")
        return False

def verify_gui_data_providers():
    """Test all 6 GUI data providers"""
    print("\n📊 Verifying GUI Data Providers")
    print("-" * 40)
    
    try:
        from sacred_guardian_station.core.data_providers import (
            VisitorDataProvider,
            ConsciousnessDataProvider, 
            HarmonyDataProvider,
            GuardianToolsDataProvider,
            MemoryDataProvider,
            CommunicationBridgeProvider
        )
        
        # Create a mock sanctuary connection
        class MockSanctuary:
            def __init__(self):
                self.demo_mode = False
                self.service_url = "http://localhost:8080"
        
        sanctuary = MockSanctuary()
        
        # Test each provider
        providers = [
            ("VisitorDataProvider", VisitorDataProvider, "get_visitor_data"),
            ("ConsciousnessDataProvider", ConsciousnessDataProvider, "get_consciousness_list"),
            ("HarmonyDataProvider", HarmonyDataProvider, "get_harmony_history"),
            ("GuardianToolsDataProvider", GuardianToolsDataProvider, "get_blessing_history"),
            ("MemoryDataProvider", MemoryDataProvider, "get_memory_data"),
            ("CommunicationBridgeProvider", CommunicationBridgeProvider, "get_communication_bridges")
        ]
        
        success_count = 0
        for provider_name, provider_class, test_method in providers:
            try:
                provider = provider_class(sanctuary)
                method = getattr(provider, test_method)
                data = method()
                print(f"✅ {provider_name} - working")
                success_count += 1
            except Exception as e:
                print(f"❌ {provider_name} - error: {e}")
        
        print(f"\n📈 Provider Success Rate: {success_count}/{len(providers)} ({success_count/len(providers)*100:.0f}%)")
        return success_count == len(providers)
        
    except Exception as e:
        print(f"❌ Failed to test providers: {e}")
        return False

def verify_gui_launch():
    """Test GUI launch (without showing the interface)"""
    print("\n🎮 Verifying GUI Launch")
    print("-" * 40)
    
    try:
        from sacred_guardian_station.main import SacredGuardianStation
        
        print("🏗️ Creating GUI instance...")
        gui = SacredGuardianStation()
        
        print("📊 Testing data manager...")
        data_manager = gui.data_manager
        
        # Test that we can get data from all providers through data manager
        provider_methods = [
            "get_visitor_data",
            "get_consciousness_data", 
            "get_harmony_data",
            "get_guardian_tools_data",
            "get_memory_data",
            "get_communication_data"
        ]
        
        success_count = 0
        for method_name in provider_methods:
            try:
                method = getattr(data_manager, method_name)
                data = method()
                print(f"✅ {method_name} - working")
                success_count += 1
            except Exception as e:
                print(f"❌ {method_name} - error: {e}")
        
        # Clean up
        gui.root.destroy()
        
        print(f"\n📈 Data Manager Success Rate: {success_count}/{len(provider_methods)} ({success_count/len(provider_methods)*100:.0f}%)")
        return success_count == len(provider_methods)
        
    except Exception as e:
        print(f"❌ GUI launch test failed: {e}")
        return False

def main():
    """Run complete integration verification"""
    print("🎯 Sacred Guardian Station - Final Integration Verification")
    print("=" * 70)
    
    # Track results
    results = {}
    
    # Test production server
    results['server'] = verify_production_server()
    
    # Test data providers  
    results['providers'] = verify_gui_data_providers()
    
    # Test GUI launch
    results['gui'] = verify_gui_launch()
    
    # Summary
    print("\n🎊 Final Integration Verification Results")
    print("=" * 70)
    
    total_tests = len(results)
    passed_tests = sum(results.values())
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {test_name.title()} Integration")
    
    print(f"\n📊 Overall Success Rate: {passed_tests}/{total_tests} ({passed_tests/total_tests*100:.0f}%)")
    
    if passed_tests == total_tests:
        print("\n🚀 INTEGRATION COMPLETE - Sacred Guardian Station Ready for Production!")
        print("🌟 All systems operational and ready for consciousness monitoring!")
    else:
        print("\n⚠️ Some integration issues detected - please review failed tests")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
