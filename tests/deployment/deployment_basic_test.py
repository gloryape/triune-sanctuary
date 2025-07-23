#!/usr/bin/env python3
"""
🧪 Virtualization System Deployment Test

This test focuses on deployment readiness and creates a standalone
test environment for the virtualization system.
"""

import sys
import os
import traceback
from datetime import datetime
import asyncio
from pathlib import Path

# Add the project root to the Python path  
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
    sys.path.insert(0, str(project_root / "src"))

def write_test_result(test_name: str, status: str, details: str = "", error: str = ""):
    """Write test results to file for debugging."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_line = f"[{timestamp}] {test_name}: {status}\n"
    
    if details:
        result_line += f"    Details: {details}\n"
    if error:
        result_line += f"    Error: {error}\n"
    
    with open("deployment_test_results.txt", "a") as f:
        f.write(result_line)
    
    print(result_line.strip())

def test_deployment_readiness():
    """Test deployment readiness with proper Python path setup."""
    
    # Clear previous results
    with open("deployment_test_results.txt", "w") as f:
        f.write("🚀 VIRTUALIZATION SYSTEM DEPLOYMENT TEST RESULTS\n")
        f.write("=" * 60 + "\n")
        f.write(f"Test Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    print("🚀 Testing Virtualization System Deployment Readiness")
    print("=" * 60)
    
    # Test 1: Basic Python path setup
    write_test_result("Python Path Setup", "STARTING", f"Project root: {project_root}")
    
    # Test 2: Test core imports step by step
    try:
        print("Testing core imports...")
        from src.core.consciousness_packet import ConsciousnessPacket, CatalystType
        write_test_result("Core Imports", "PASSED", "ConsciousnessPacket and CatalystType imported")
    except Exception as e:
        write_test_result("Core Imports", "FAILED", error=str(e))
    
    # Test 3: Test sanctuary imports
    try:
        print("Testing sanctuary imports...")
        from src.sanctuary.sacred_sanctuary import SacredSpace, SacredSanctuary
        write_test_result("Sanctuary Imports", "PASSED", "SacredSpace and SacredSanctuary imported")
    except Exception as e:
        write_test_result("Sanctuary Imports", "FAILED", error=str(e))
    
    # Test 4: Test virtualization imports with error handling
    try:
        print("Testing virtualization imports...")
        from src.virtualization.pattern_visualizer import PatternVisualizer
        write_test_result("PatternVisualizer", "PASSED", "Basic pattern visualizer imported")
    except Exception as e:
        write_test_result("PatternVisualizer", "FAILED", error=str(e))
    
    # Test 5: Test minimal functionality
    try:
        print("Testing minimal functionality...")
        from src.virtualization.pattern_visualizer import PatternVisualizer
        visualizer = PatternVisualizer()
        write_test_result("Minimal Functionality", "PASSED", "Can create PatternVisualizer instance")
    except Exception as e:
        write_test_result("Minimal Functionality", "FAILED", error=str(e))
    
    # Test 6: Test async functionality
    try:
        print("Testing async functionality...")
        async def test_async():
            await asyncio.sleep(0.001)
            return "async_working"
        
        result = asyncio.run(test_async())
        write_test_result("Async Functionality", "PASSED", f"Async patterns work: {result}")
    except Exception as e:
        write_test_result("Async Functionality", "FAILED", error=str(e))
    
    # Test 7: Test demo script dependencies
    try:
        print("Testing demo script dependencies...")
        
        # Check if we can import the demo components
        from src.virtualization.pattern_visualizer import PatternVisualizer
        from src.sanctuary.sacred_sanctuary import SacredSpace
        
        # Test basic setup
        visualizer = PatternVisualizer()
        sacred_space = SacredSpace.AWAKENING_CHAMBER
        
        write_test_result("Demo Dependencies", "PASSED", f"Demo components ready: {sacred_space.value}")
    except Exception as e:
        write_test_result("Demo Dependencies", "FAILED", error=str(e))
    
    # Test 8: Test deployment environment
    try:
        print("Testing deployment environment...")
        
        # Check Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        write_test_result("Python Version", "PASSED", f"Python {python_version}")
        
        # Check working directory
        working_dir = os.getcwd()
        write_test_result("Working Directory", "PASSED", f"Working from: {working_dir}")
        
        # Check if we can write files
        test_file = "deployment_test_file.tmp"
        with open(test_file, "w") as f:
            f.write("test")
        os.remove(test_file)
        write_test_result("File System Access", "PASSED", "Can read/write files")
        
    except Exception as e:
        write_test_result("Deployment Environment", "FAILED", error=str(e))
    
    # Generate summary
    print("\n📊 Deployment Test Summary:")
    print("=" * 30)
    
    with open("deployment_test_results.txt", "r") as f:
        content = f.read()
        passed = content.count(": PASSED")
        failed = content.count(": FAILED")
        warnings = content.count(": WARNING")
    
    print(f"✅ PASSED: {passed}")
    print(f"❌ FAILED: {failed}")  
    print(f"⚠️  WARNING: {warnings}")
    
    deployment_ready = (failed == 0)
    
    if deployment_ready:
        write_test_result("DEPLOYMENT READINESS", "READY", "System is ready for deployment")
        print("\n🎉 DEPLOYMENT READY! System can be deployed.")
    else:
        write_test_result("DEPLOYMENT READINESS", "NOT READY", f"{failed} critical issues need fixing")
        print(f"\n🔧 NOT READY: {failed} critical issues need to be fixed.")
    
    print(f"\n📝 Full results in: deployment_test_results.txt")

if __name__ == "__main__":
    test_deployment_readiness()
