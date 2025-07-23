#!/usr/bin/env python3
"""
Quick Import Fix Test - Resolve uncertainty_response_core import issues
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_uncertainty_imports():
    """Test the problematic uncertainty response imports"""
    try:
        print("Testing uncertainty_field_core import...")
        from src.consciousness.loops.observer.core.uncertainty_field_core import (
            UncertaintyField, UncertaintyExploration, SacredUnknowing,
            UncertaintyType, UncertaintyQuality, UncertaintyResponse, MetaUncertaintyState
        )
        print("✅ uncertainty_field_core imports successful")
        
        print("Testing uncertainty_response_core import...")
        from src.consciousness.loops.observer.core.uncertainty_response_core import (
            UncertaintyResponsePlan, ResponseProgress, ResponseCapabilities
        )
        print("✅ uncertainty_response_core imports successful")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("🔧 Checking specific missing components...")
        
        # Check what's actually available
        try:
            import importlib
            module = importlib.import_module('src.consciousness.loops.observer.core.uncertainty_field_core')
            available = [x for x in dir(module) if not x.startswith('_')]
            print(f"Available from uncertainty_field_core: {available}")
        except Exception as ex:
            print(f"Core import failed: {ex}")
        
        return False
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Testing Observer Core Import Dependencies")
    print("=" * 60)
    
    success = test_uncertainty_imports()
    
    if success:
        print("\n✅ All imports resolved successfully!")
    else:
        print("\n🔧 Import issues identified - fixing...")
        
    print("\n" + "=" * 60)
