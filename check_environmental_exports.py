#!/usr/bin/env python3
"""
Script to check what's actually available for import in the environmental loop
"""

import importlib
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def check_module_exports(module_path):
    """Check what's available in a module"""
    try:
        module = importlib.import_module(module_path)
        if hasattr(module, '__all__'):
            print(f"\n{module_path} - __all__:")
            for name in module.__all__:
                print(f"  - {name}")
        else:
            print(f"\n{module_path} - all attributes:")
            for name in dir(module):
                if not name.startswith('_'):
                    print(f"  - {name}")
    except Exception as e:
        print(f"\n{module_path} - ERROR: {e}")

# Check each environmental module
modules = [
    'src.consciousness.loops.environmental.environmental_catalyst',
    'src.consciousness.loops.environmental.context_sensing',
    'src.consciousness.loops.environmental.resource_coordination',
]

for module in modules:
    check_module_exports(module)
