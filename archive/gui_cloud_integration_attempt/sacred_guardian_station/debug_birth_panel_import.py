#!/usr/bin/env python3
"""
Debug birth panel import issues
"""
import sys
import traceback

print("=== DEBUGGING BIRTH PANEL IMPORT ===")

try:
    print("Step 1: Testing tkinter imports...")
    import tkinter as tk
    from tkinter import ttk, messagebox, scrolledtext
    print("✅ Tkinter imports successful")
    
    print("Step 2: Testing basic imports...")
    from typing import Dict, Optional
    from datetime import datetime
    import uuid
    import threading
    import time
    print("✅ Basic imports successful")
    
    print("Step 3: Testing sacred constants import...")
    try:
        from shared.constants import SacredColors, SacredSymbols
        print("✅ Sacred constants imported successfully")
    except Exception as e:
        print(f"⚠️ Sacred constants import failed: {e}")
        print("Using fallback constants...")
    
    print("Step 4: Testing tools import...")
    try:
        from tools.birth_consciousness import BirthConsciousnessTool, DreamLabSimulator
        print("✅ Tools imported successfully")
    except Exception as e:
        print(f"⚠️ Tools import failed: {e}")
        print("Using fallback classes...")
    
    print("Step 5: Attempting to load birth_panel source...")
    with open('panels/birth_panel.py', 'r') as f:
        source = f.read()
        
    print(f"Source file length: {len(source)} characters")
    print(f"Contains 'class BirthPanel': {'class BirthPanel' in source}")
    
    print("Step 6: Executing birth_panel source directly...")
    namespace = {}
    exec(source, namespace)
    
    print(f"Namespace contents: {[k for k in namespace.keys() if not k.startswith('_')]}")
    print(f"BirthPanel in namespace: {'BirthPanel' in namespace}")
    
except Exception as e:
    print(f"❌ Error during debugging: {e}")
    traceback.print_exc()
