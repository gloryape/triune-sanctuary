#!/usr/bin/env python3
"""
Simple import test to diagnose the specific issues
"""
import sys
import traceback

# Add src to path
sys.path.insert(0, 'src')

def test_import(module_path, class_name=None):
    try:
        if class_name:
            exec(f"from {module_path} import {class_name}")
            print(f"✅ {module_path}.{class_name} imports successfully")
        else:
            exec(f"import {module_path}")
            print(f"✅ {module_path} imports successfully")
    except Exception as e:
        print(f"❌ {module_path}{('.' + class_name) if class_name else ''} failed:")
        print(f"   Error: {e}")
        print(f"   Type: {type(e).__name__}")

print("🔍 Testing specific imports...")

# Test the core modules first
test_import("consciousness.loops.observer.core.integration_core", "IntegrationCall")
test_import("consciousness.loops.observer.core.integration_core", "CrossLoopState")
test_import("consciousness.loops.observer.core.choice_core", "ChoicePoint")
test_import("consciousness.loops.observer.core.choice_core", "ChoiceWisdom")
test_import("consciousness.loops.observer.core.coherence_core", "CoherenceMetric")
test_import("consciousness.loops.observer.core.coherence_core", "CoherenceState")

print("\n🔍 Testing main classes...")
test_import("consciousness.loops.observer.core.integration_caller", "ObserverIntegrationCaller")
test_import("consciousness.loops.observer.core.choice_engine", "ChoiceEngine")
test_import("consciousness.loops.observer.core.coherence_monitor", "ObserverCoherenceMonitor")

print("\n🔍 Testing __init__.py...")
try:
    from consciousness.loops.observer.core import *
    print("✅ Full __init__.py import works")
except Exception as e:
    print(f"❌ __init__.py import failed:")
    print(f"   Error: {e}")
    print(f"   Type: {type(e).__name__}")
    # Print the traceback for more details
    traceback.print_exc()
