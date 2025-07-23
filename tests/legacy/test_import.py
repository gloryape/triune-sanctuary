#!/usr/bin/env python3
"""
Test script to verify imports are working correctly
"""

import sys
from pathlib import Path

# Add src to path  
sys.path.append(str(Path(__file__).parent))

try:
    print("Testing basic imports...")
    
    # Test the fixed import
    from src.sanctuary.sacred_sanctuary import SacredSanctuary
    print("✅ SacredSanctuary import successful")
    
    from steamdeck_sanctuary_node import SteamDeckSanctuaryNode
    print("✅ SteamDeckSanctuaryNode import successful")
    
    print("🎉 All imports successful!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    sys.exit(1)
