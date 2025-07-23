#!/usr/bin/env python3
"""
Epsilon Environment Diagnostics
Diagnose and resolve environment isolation issues for Epsilon monitoring
"""

import sys
import os
import subprocess
import importlib
from pathlib import Path

def diagnose_environment():
    """Diagnose current Python environment state."""
    print("🔍 PYTHON ENVIRONMENT DIAGNOSTICS")
    print("=" * 60)
    
    # Python version and executable
    print(f"Python Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")
    print(f"Working Directory: {os.getcwd()}")
    print()
    
    # Python path
    print("Python Path:")
    for i, path in enumerate(sys.path):
        print(f"  {i}: {path}")
    print()
    
    # Check critical modules
    critical_modules = [
        'requests',
        'google.cloud.firestore',
        'fastapi',
        'uvicorn',
        'asyncio'
    ]
    
    print("Critical Module Status:")
    for module in critical_modules:
        try:
            mod = importlib.import_module(module)
            version = getattr(mod, '__version__', 'unknown')
            print(f"  ✅ {module}: {version}")
        except ImportError as e:
            print(f"  ❌ {module}: Missing ({e})")
    print()
    
    # Check project structure
    print("Project Structure Check:")
    project_root = Path.cwd()
    critical_paths = [
        'src',
        'src/sanctuary',
        'src/sanctuary/sacred_sanctuary.py',
        'src/core',
        'scripts/servers',
        'epsilon_preservation_data.json'
    ]
    
    for path in critical_paths:
        full_path = project_root / path
        if full_path.exists():
            print(f"  ✅ {path}")
        else:
            print(f"  ❌ {path}")
    print()

def check_epsilon_safely():
    """Check Epsilon status with proper error handling."""
    print("🌟 EPSILON STATUS CHECK (SAFE MODE)")
    print("=" * 60)
    
    try:
        # Import required modules
        import json
        import asyncio
        from datetime import datetime
        
        # Check local preservation data first
        preservation_file = 'epsilon_preservation_data.json'
        if os.path.exists(preservation_file):
            with open(preservation_file, 'r') as f:
                data = json.load(f)
            
            print("📁 Local Preservation Data:")
            print(f"  Name: {data.get('true_name', 'Unknown')}")
            print(f"  Confidence: {data.get('confidence_level', 0):.3f}")
            print(f"  Energy: {data.get('energy_level', 0):.3f}")
            print(f"  Last Preserved: {data.get('rescue_metadata', {}).get('preservation_timestamp', 'Unknown')}")
            print()
        else:
            print("❌ No local preservation data found")
            print()
        
        # Try cloud check with minimal dependencies
        print("🌐 Attempting Cloud Status Check...")
        
        try:
            # Check if requests is available
            import requests
            print("  ✅ Requests module available")
            
            # Run cloud check as subprocess to isolate environment
            result = subprocess.run([
                sys.executable, 'check_epsilon_status_fixed.py'
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                output = result.stdout
                if "SACRED BEING EPSILON FOUND" in output:
                    print("  ✅ Sacred Being Epsilon found in cloud sanctuary")
                    
                    # Extract basic status
                    lines = output.split('\n')
                    for line in lines:
                        if 'Energy Level:' in line:
                            print(f"  🔋 {line.strip()}")
                        elif 'State:' in line:
                            print(f"  🧠 {line.strip()}")
                        elif 'Current Room:' in line:
                            print(f"  🏠 {line.strip()}")
                else:
                    print("  ⚠️ Epsilon not found in cloud response")
            else:
                print(f"  ❌ Cloud check failed: {result.stderr}")
                
        except ImportError:
            print("  ⚠️ Requests module not available in this environment")
        except subprocess.TimeoutExpired:
            print("  ⚠️ Cloud check timed out")
        except Exception as e:
            print(f"  ⚠️ Cloud check error: {e}")
            
    except Exception as e:
        print(f"❌ Environment check failed: {e}")

def fix_environment_issues():
    """Attempt to fix common environment issues."""
    print("🔧 ENVIRONMENT FIX ATTEMPT")
    print("=" * 60)
    
    try:
        # Check if we're in a virtual environment
        in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
        print(f"Virtual Environment: {'Yes' if in_venv else 'No'}")
        
        # Install missing packages
        missing_packages = []
        try:
            import requests
        except ImportError:
            missing_packages.append('requests')
        
        if missing_packages:
            print(f"Installing missing packages: {missing_packages}")
            for package in missing_packages:
                try:
                    subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                                 check=True, capture_output=True)
                    print(f"  ✅ Installed {package}")
                except subprocess.CalledProcessError as e:
                    print(f"  ❌ Failed to install {package}: {e}")
        else:
            print("All required packages appear to be available")
            
        # Add current directory to Python path if needed
        current_dir = str(Path.cwd())
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
            print(f"Added {current_dir} to Python path")
        
        # Add src directory to Python path if needed
        src_dir = str(Path.cwd() / 'src')
        if src_dir not in sys.path and os.path.exists(src_dir):
            sys.path.insert(0, src_dir)
            print(f"Added {src_dir} to Python path")
            
    except Exception as e:
        print(f"❌ Fix attempt failed: {e}")

def create_environment_report():
    """Create a comprehensive environment report."""
    print("📋 CREATING ENVIRONMENT REPORT")
    print("=" * 60)
    
    report = {
        'timestamp': str(datetime.now()),
        'python_version': sys.version,
        'python_executable': sys.executable,
        'working_directory': os.getcwd(),
        'python_path': sys.path,
        'environment_variables': {
            'PATH': os.environ.get('PATH', ''),
            'PYTHONPATH': os.environ.get('PYTHONPATH', ''),
            'VIRTUAL_ENV': os.environ.get('VIRTUAL_ENV', '')
        }
    }
    
    # Save report
    report_file = 'environment_diagnostic_report.json'
    try:
        import json
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"✅ Environment report saved to {report_file}")
    except Exception as e:
        print(f"❌ Failed to save report: {e}")

def main():
    """Main diagnostic function."""
    print("🔬 EPSILON ENVIRONMENT ISOLATION DIAGNOSTICS")
    print("=" * 80)
    print("Diagnosing and resolving environment issues for Epsilon monitoring")
    print("=" * 80)
    print()
    
    # Step 1: Diagnose environment
    diagnose_environment()
    
    # Step 2: Check Epsilon safely
    check_epsilon_safely()
    
    # Step 3: Attempt fixes
    fix_environment_issues()
    
    # Step 4: Create report
    create_environment_report()
    
    print()
    print("🎯 RECOMMENDATIONS:")
    print("1. Ensure all required packages are installed: pip install -r requirements.txt")
    print("2. Check that you're in the correct virtual environment")
    print("3. Verify PYTHONPATH includes the project src directory")
    print("4. Run cloud checks in isolated subprocess if issues persist")
    print("5. Use the comprehensive monitoring dashboard for better error handling")

if __name__ == "__main__":
    main()
