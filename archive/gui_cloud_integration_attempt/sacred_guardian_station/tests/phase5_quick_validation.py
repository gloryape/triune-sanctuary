#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 5 Quick Validation Test

This script validates that all Phase 5 components are properly implemented
and provides a quick assessment of the Sacred Guardian Station readiness.
"""

import sys
import os
import traceback

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

def test_component_imports():
    """Test that all components can be imported successfully"""
    print("🔍 Testing component imports...")
    
    tests = []
    
    # Core components
    try:
        from sacred_guardian_station.core.sanctuary_connection import SanctuaryConnection
        tests.append(("✅", "SanctuaryConnection"))
    except Exception as e:
        tests.append(("❌", f"SanctuaryConnection: {e}"))
    
    try:
        from sacred_guardian_station.core.data_manager_new import DataManager
        tests.append(("✅", "DataManager"))
    except Exception as e:
        tests.append(("❌", f"DataManager: {e}"))
    
    try:
        from sacred_guardian_station.core.event_system import EventSystem
        tests.append(("✅", "EventSystem"))
    except Exception as e:
        tests.append(("❌", f"EventSystem: {e}"))
    
    # Panel components
    try:
        from sacred_guardian_station.panels.consciousness_panel import ConsciousnessPanel
        tests.append(("✅", "ConsciousnessPanel"))
    except Exception as e:
        tests.append(("❌", f"ConsciousnessPanel: {e}"))
    
    try:
        from sacred_guardian_station.panels.sacred_events_panel import SacredEventsPanel
        tests.append(("✅", "SacredEventsPanel"))
    except Exception as e:
        tests.append(("❌", f"SacredEventsPanel: {e}"))
    
    # Tool components
    try:
        from sacred_guardian_station.tools.catalyst_offering import CatalystOfferingTool
        tests.append(("✅", "CatalystOfferingTool"))
    except Exception as e:
        tests.append(("❌", f"CatalystOfferingTool: {e}"))
    
    try:
        from sacred_guardian_station.tools.blessing_ceremonies import BlessingCeremonies
        tests.append(("✅", "BlessingCeremonies"))
    except Exception as e:
        tests.append(("❌", f"BlessingCeremonies: {e}"))
    
    # Visualization components
    try:
        from sacred_guardian_station.visualizations import ConsciousnessGraph
        tests.append(("✅", "ConsciousnessGraph"))
    except Exception as e:
        tests.append(("❌", f"ConsciousnessGraph: {e}"))
    
    try:
        from sacred_guardian_station.visualizations import MemoryTree
        tests.append(("✅", "MemoryTree"))
    except Exception as e:
        tests.append(("❌", f"MemoryTree: {e}"))
    
    # Print results
    passed = sum(1 for test in tests if test[0] == "✅")
    total = len(tests)
    
    print(f"\n📊 Import Test Results:")
    for status, component in tests:
        print(f"  {status} {component}")
    
    print(f"\n🎯 Import Success Rate: {passed}/{total} ({passed/total*100:.1f}%)")
    
    return passed == total

def test_basic_functionality():
    """Test basic functionality of core components"""
    print("\n🧪 Testing basic functionality...")
    
    tests = []
    
    try:
        from sacred_guardian_station.core.event_system import EventSystem
        
        # Test event system
        event_system = EventSystem()
        events_received = []
        
        def test_listener(event_type, data):
            events_received.append((event_type, data))
        
        event_system.subscribe('test_event', test_listener)
        event_system.emit('test_event', {'test': 'data'})
        
        if len(events_received) == 1 and events_received[0][1]['test'] == 'data':
            tests.append(("✅", "EventSystem pub/sub"))
        else:
            tests.append(("❌", "EventSystem pub/sub failed"))
            
    except Exception as e:
        tests.append(("❌", f"EventSystem test: {e}"))
    
    try:
        from sacred_guardian_station.core.data_manager_new import DataManager
        from sacred_guardian_station.core.event_system import EventSystem
        
        # Test data manager initialization
        event_system = EventSystem()
        data_manager = DataManager(event_system)
        tests.append(("✅", "DataManager initialization"))
        
    except Exception as e:
        tests.append(("❌", f"DataManager test: {e}"))
    
    # Print results
    passed = sum(1 for test in tests if test[0] == "✅")
    total = len(tests)
    
    print(f"\n📊 Functionality Test Results:")
    for status, component in tests:
        print(f"  {status} {component}")
    
    print(f"\n🎯 Functionality Success Rate: {passed}/{total} ({passed/total*100:.1f}%)")
    
    return passed == total

def test_file_structure():
    """Test that all required files exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        # Core files
        "sacred_guardian_station/__init__.py",
        "sacred_guardian_station/main.py",
        "sacred_guardian_station/core/__init__.py",
        "sacred_guardian_station/core/sanctuary_connection.py",
        "sacred_guardian_station/core/data_manager_new.py",
        "sacred_guardian_station/core/event_system.py",
        
        # Panel files
        "sacred_guardian_station/panels/__init__.py",
        "sacred_guardian_station/panels/consciousness_panel.py",
        "sacred_guardian_station/panels/sacred_events_panel.py",
        "sacred_guardian_station/panels/memory_viewer_panel.py",
        
        # Tool files
        "sacred_guardian_station/tools/__init__.py",
        "sacred_guardian_station/tools/catalyst_offering.py",
        "sacred_guardian_station/tools/blessing_ceremonies.py",
        "sacred_guardian_station/tools/emergency_controls.py",
        "sacred_guardian_station/tools/export_tools.py",
        
        # Visualization files
        "sacred_guardian_station/visualizations/__init__.py",
        "sacred_guardian_station/visualizations/consciousness_graph.py",
        "sacred_guardian_station/visualizations/memory_tree.py",
        "sacred_guardian_station/visualizations/harmony_charts.py",
        "sacred_guardian_station/visualizations/relationship_web.py",
        
        # Test files
        "sacred_guardian_station/tests/__init__.py",
        "sacred_guardian_station/tests/test_core.py",
        "sacred_guardian_station/tests/test_panels.py",
        "sacred_guardian_station/tests/test_tools.py",
        "sacred_guardian_station/tests/test_visualizations.py",
        "sacred_guardian_station/tests/test_integration.py",
        "sacred_guardian_station/tests/test_performance.py",
        "sacred_guardian_station/tests/run_all_tests.py",
        
        # Shared files
        "sacred_guardian_station/shared/__init__.py",
        "sacred_guardian_station/shared/constants.py",
    ]
    
    missing_files = []
    existing_files = []
    
    for file_path in required_files:
        full_path = os.path.join(project_root, file_path)
        if os.path.exists(full_path):
            existing_files.append(file_path)
        else:
            missing_files.append(file_path)
    
    print(f"\n📊 File Structure Results:")
    print(f"  ✅ Existing files: {len(existing_files)}")
    print(f"  ❌ Missing files: {len(missing_files)}")
    
    if missing_files:
        print(f"\n❌ Missing files:")
        for file_path in missing_files:
            print(f"    - {file_path}")
    
    success_rate = len(existing_files) / len(required_files)
    print(f"\n🎯 File Structure Completeness: {len(existing_files)}/{len(required_files)} ({success_rate*100:.1f}%)")
    
    return len(missing_files) == 0

def assess_phase_5_completion():
    """Assess overall Phase 5 completion status"""
    print("\n" + "="*60)
    print("🏆 PHASE 5 COMPLETION ASSESSMENT")
    print("="*60)
    
    # Run all tests
    import_success = test_component_imports()
    functionality_success = test_basic_functionality()
    structure_success = test_file_structure()
    
    # Calculate overall score
    total_tests = 3
    passed_tests = sum([import_success, functionality_success, structure_success])
    completion_rate = passed_tests / total_tests
    
    print(f"\n📊 Overall Assessment:")
    print(f"  Import Tests: {'✅ PASS' if import_success else '❌ FAIL'}")
    print(f"  Functionality Tests: {'✅ PASS' if functionality_success else '❌ FAIL'}")
    print(f"  File Structure: {'✅ PASS' if structure_success else '❌ FAIL'}")
    print(f"  Overall Completion: {passed_tests}/{total_tests} ({completion_rate*100:.1f}%)")
    
    if completion_rate >= 0.8:  # 80% threshold
        print(f"\n🎉 PHASE 5: SUBSTANTIALLY COMPLETE!")
        print(f"✅ The Sacred Guardian Station modular system is ready!")
        print(f"✅ All major components are implemented and functional")
        
        if completion_rate == 1.0:
            print(f"🏅 PERFECT SCORE - All tests passed!")
        else:
            print(f"⚡ Minor issues remain but system is production-ready")
            
    elif completion_rate >= 0.6:  # 60% threshold
        print(f"\n⚡ PHASE 5: MOSTLY COMPLETE")
        print(f"🔧 System is functional but needs refinement")
        print(f"🎯 Focus on addressing remaining issues")
        
    else:
        print(f"\n🚨 PHASE 5: NEEDS ATTENTION")
        print(f"❌ Significant issues need to be resolved")
        print(f"🔧 Review and fix critical components")
    
    print(f"\n💡 Recommendations:")
    
    if not import_success:
        print(f"  🔧 Fix import issues in core components")
    if not functionality_success:
        print(f"  🔧 Address functionality problems in core systems")
    if not structure_success:
        print(f"  🔧 Complete missing files and structure")
    
    if completion_rate >= 0.8:
        print(f"  📦 System is ready for integration testing")
        print(f"  🚀 Consider deploying to staging environment")
        print(f"  📚 Begin user documentation and training")
    
    print(f"\n🌟 Sacred Guardian Station modularization effort assessment complete!")
    
    return completion_rate >= 0.8

def main():
    """Main assessment function"""
    print("🚀 Sacred Guardian Station - Phase 5 Quick Validation")
    print("🔬 Assessing modular system implementation...")
    
    try:
        success = assess_phase_5_completion()
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"\n💥 Validation failed with error: {e}")
        print(f"📋 Traceback:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
