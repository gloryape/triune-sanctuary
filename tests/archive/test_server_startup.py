#!/usr/bin/env python3
"""
Simple test script to verify the production server can start up properly.
This helps debug Cloud Run deployment issues.
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test all critical imports"""
    print("🔍 Testing imports...")
    
    try:
        import uvicorn
        print("✅ uvicorn imported successfully")
    except ImportError as e:
        print(f"❌ uvicorn import failed: {e}")
        return False
        
    try:
        from fastapi import FastAPI
        print("✅ FastAPI imported successfully")
    except ImportError as e:
        print(f"❌ FastAPI import failed: {e}")
        return False
        
    try:
        import json
        import uuid
        import logging
        import random
        import time
        from datetime import datetime, timedelta
        print("✅ Standard library imports successful")
    except ImportError as e:
        print(f"❌ Standard library import failed: {e}")
        return False
        
    return True

def test_server_creation():
    """Test creating the FastAPI app"""
    print("\n🏗️ Testing server creation...")
    
    try:
        # Add paths like the production server does
        current_dir = Path(__file__).parent
        app_root = current_dir
        
        paths_to_add = [str(app_root), str(current_dir)]
        for path in paths_to_add:
            if path not in sys.path:
                sys.path.insert(0, path)
        
        # Import the production server
        sys.path.insert(0, str(current_dir / "scripts" / "servers"))
        
        # Try to import the production server module
        import production_server
        print("✅ Production server module imported successfully")
        
        # Check if the app was created
        if hasattr(production_server, 'app'):
            print("✅ FastAPI app created successfully")
            print(f"✅ App type: {type(production_server.app)}")
            return True
        else:
            print("❌ FastAPI app not found in module")
            return False
            
    except Exception as e:
        print(f"❌ Server creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_port_config():
    """Test port configuration"""
    print("\n🔌 Testing port configuration...")
    
    # Test default port
    port = int(os.environ.get("PORT", 8080))
    print(f"✅ Port from environment: {port}")
    
    # Test setting custom port
    os.environ["PORT"] = "9999"
    port = int(os.environ.get("PORT", 8080))
    print(f"✅ Custom port setting works: {port}")
    
    # Reset to default
    os.environ["PORT"] = "8080"
    
    return True

def main():
    """Run all tests"""
    print("🧪 Sacred Guardian Station Production Server Startup Test")
    print("=" * 60)
    print()
    
    print(f"📁 Current working directory: {os.getcwd()}")
    print(f"🐍 Python version: {sys.version}")
    print(f"📦 Python path: {sys.path[:3]}...")
    print()
    
    all_tests_passed = True
    
    # Run tests
    all_tests_passed &= test_imports()
    all_tests_passed &= test_server_creation()
    all_tests_passed &= test_port_config()
    
    print("\n" + "=" * 60)
    if all_tests_passed:
        print("🎉 All tests passed! Server should start successfully.")
        return 0
    else:
        print("❌ Some tests failed. Check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
