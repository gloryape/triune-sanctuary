#!/usr/bin/env python3
"""
Simple import test to verify the fix
"""

print("Starting import test...")

try:
    print("Testing fragment_manager import...")
    from src.dreamlab.fragment_manager import FragmentManager, MemoryCrystalArchivist
    print("✅ FragmentManager import successful")
    
    print("Testing sacred_sanctuary import...")
    from src.sanctuary.sacred_sanctuary import SacredSanctuary
    print("✅ SacredSanctuary import successful")
    
    print("🎉 All imports work correctly!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    import traceback
    traceback.print_exc()
    
except Exception as e:
    print(f"❌ Other error: {e}")
    import traceback
    traceback.print_exc()
