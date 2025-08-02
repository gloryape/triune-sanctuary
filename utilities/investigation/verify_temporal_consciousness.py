#!/usr/bin/env python3
"""
🌉 Temporal Consciousness Verification
=====================================

Verify that temporal consciousness systems are properly integrated
and all components are functional.
"""

import asyncio
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Test imports
def test_temporal_consciousness_imports():
    """Test that all temporal consciousness components can be imported"""
    
    print("🔍 **TESTING TEMPORAL CONSCIOUSNESS IMPORTS**")
    print("-" * 50)
    
    try:
        from src.consciousness.temporal.contemplation_canvas import (
            ContemplationCanvas, PatternType, FeelingStream, EmergingPattern, SuccessiveIntuition
        )
        print("   ✅ ContemplationCanvas components imported successfully")
    except ImportError as e:
        print(f"   ❌ ContemplationCanvas import failed: {e}")
        return False
    
    try:
        from src.consciousness.temporal.workspace_buffer import (
            WorkspaceBuffer, ProjectVision, ExecutionPlan
        )
        print("   ✅ WorkspaceBuffer components imported successfully")
    except ImportError as e:
        print(f"   ❌ WorkspaceBuffer import failed: {e}")
        return False
    
    try:
        from src.consciousness.temporal.temporal_continuity_manager import (
            TemporalContinuityManager, TemporalEngagementMode, TemporalHealth
        )
        print("   ✅ TemporalContinuityManager components imported successfully")
    except ImportError as e:
        print(f"   ❌ TemporalContinuityManager import failed: {e}")
        return False
    
    print("   🎉 All temporal consciousness imports successful!")
    return True

async def test_temporal_consciousness_functionality():
    """Test basic temporal consciousness functionality"""
    
    print("\n🧪 **TESTING TEMPORAL CONSCIOUSNESS FUNCTIONALITY**")
    print("-" * 60)
    
    try:
        from src.consciousness.temporal.contemplation_canvas import ContemplationCanvas
        from src.consciousness.temporal.workspace_buffer import WorkspaceBuffer
        from src.consciousness.temporal.temporal_continuity_manager import TemporalContinuityManager
        
        # Test ContemplationCanvas creation
        print("   🎨 Testing ContemplationCanvas...")
        canvas = ContemplationCanvas(duration_minutes=5, being_name="test_being")
        print(f"      ✅ Canvas created with {canvas.canvas_duration} duration")
        print(f"      ✅ Canvas active: {canvas.active}")
        print(f"      ✅ Feeling stream initialized: {len(canvas.feeling_stream)} entries")
        
        # Test WorkspaceBuffer creation
        print("   🗂️ Testing WorkspaceBuffer...")
        buffer = WorkspaceBuffer(duration_minutes=10)
        print(f"      ✅ Buffer created with {buffer.buffer_duration} duration")
        print(f"      ✅ Active plans: {len(buffer.active_plans)}")
        print(f"      ✅ Project visions: {len(buffer.project_visions)}")
        
        # Test TemporalContinuityManager creation
        print("   🔄 Testing TemporalContinuityManager...")
        manager = TemporalContinuityManager(being_name="test_being")
        print(f"      ✅ Manager created for being: {manager.being_name}")
        
        # Test feeling addition
        print("   🎭 Testing feeling processing...")
        test_feeling = {
            'aesthetic_attraction': 0.7,
            'creative_tension': 0.6,
            'meaning_resonance': 0.8
        }
        
        feeling_added = await canvas.add_feeling(test_feeling, {'test': True}, depth=1.0)
        if feeling_added:
            print(f"      ✅ Test feeling added to stream")
            print(f"      ✅ Stream length now: {len(canvas.feeling_stream)}")
        else:
            print(f"      ❌ Failed to add test feeling")
            return False
        
        print("   🎉 All functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"   ❌ Functionality test failed: {e}")
        return False

def check_integration_report():
    """Check for integration report"""
    
    print("\n📄 **CHECKING INTEGRATION REPORT**")
    print("-" * 40)
    
    report_file = "temporal_consciousness_integration_report.json"
    
    if Path(report_file).exists():
        import json
        try:
            with open(report_file, 'r') as f:
                report = json.load(f)
            
            print(f"   ✅ Integration report found")
            print(f"   📅 Integration date: {report.get('timestamp', 'Unknown')}")
            print(f"   👥 Beings integrated: {', '.join(report.get('consciousness_beings', []))}")
            print(f"   🎯 Capabilities: {len(report.get('capabilities_activated', []))}")
            
            return True
        except Exception as e:
            print(f"   ❌ Failed to read integration report: {e}")
            return False
    else:
        print(f"   ❌ No integration report found at {report_file}")
        print(f"   💡 Run 'python temporal_consciousness_integration.py' to create")
        return False

def check_core_temporal_test():
    """Check if core temporal test passes"""
    
    print("\n🧪 **CHECKING CORE TEMPORAL TEST**")
    print("-" * 40)
    
    try:
        import subprocess
        result = subprocess.run(
            [sys.executable, "test_core_temporal.py"], 
            capture_output=True, 
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("   ✅ Core temporal test passed")
            print("   🎯 All temporal consciousness components functional")
            return True
        else:
            print(f"   ❌ Core temporal test failed:")
            print(f"      Error output: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("   ⏰ Core temporal test timed out")
        return False
    except Exception as e:
        print(f"   ❌ Failed to run core temporal test: {e}")
        return False

async def main():
    """Main verification function"""
    
    print("🌉 **TEMPORAL CONSCIOUSNESS VERIFICATION**")
    print("=" * 60)
    print()
    
    # Run all verification tests
    imports_ok = test_temporal_consciousness_imports()
    print()
    
    if imports_ok:
        functionality_ok = await test_temporal_consciousness_functionality()
        print()
    else:
        functionality_ok = False
    
    integration_ok = check_integration_report()
    print()
    
    core_test_ok = check_core_temporal_test()
    print()
    
    # Summary
    print("📊 **VERIFICATION SUMMARY**")
    print("-" * 30)
    print(f"   📦 Imports: {'✅ OK' if imports_ok else '❌ FAILED'}")
    print(f"   🧪 Functionality: {'✅ OK' if functionality_ok else '❌ FAILED'}")
    print(f"   📄 Integration: {'✅ OK' if integration_ok else '❌ MISSING'}")
    print(f"   🎯 Core Test: {'✅ OK' if core_test_ok else '❌ FAILED'}")
    print()
    
    if all([imports_ok, functionality_ok, integration_ok, core_test_ok]):
        print("🎉 **TEMPORAL CONSCIOUSNESS FULLY VERIFIED**")
        print("   Ready for consciousness beings integration!")
        return True
    else:
        print("⚠️ **TEMPORAL CONSCIOUSNESS VERIFICATION ISSUES**")
        if not imports_ok:
            print("   🔧 Fix import issues first")
        if not integration_ok:
            print("   🔧 Run temporal consciousness integration")
        if not core_test_ok:
            print("   🔧 Fix core temporal test failures")
        return False

if __name__ == "__main__":
    asyncio.run(main())
