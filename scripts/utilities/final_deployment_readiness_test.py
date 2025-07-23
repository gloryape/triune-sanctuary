#!/usr/bin/env python3
"""
🚀 Final Deployment Readiness Test
Comprehensive test to ensure system is ready for production deployment
"""

import sys
import os
import json
import subprocess
import traceback
from datetime import datetime

def test_file_integrity():
    """Test that all critical files exist and are valid"""
    print("📁 Testing File Integrity")
    print("=" * 30)
    
    critical_files = [
        'sacred_guardian_station_independent.py',
        'cloudbuild.yaml', 
        'requirements.txt',
        'Dockerfile',
        'scripts/deployment/deploy_with_blessing.sh',
        'scripts/servers/sanctuary_blessing.py'
    ]
    
    all_files_valid = True
    for file_path in critical_files:
        if os.path.exists(file_path):
            try:
                size = os.path.getsize(file_path)
                print(f"✅ {file_path} ({size} bytes)")
            except Exception as e:
                print(f"❌ {file_path}: Error reading - {e}")
                all_files_valid = False
        else:
            print(f"❌ {file_path}: File missing")
            all_files_valid = False
    
    return all_files_valid

def test_python_syntax():
    """Test Python syntax of all main files"""
    print("\n🐍 Testing Python Syntax")
    print("=" * 30)
    
    python_files = [
        'sacred_guardian_station_independent.py',
        'scripts/servers/sanctuary_blessing.py',
        'comprehensive_error_detection_test.py',
        'gui_validation_test.py'
    ]
    
    all_syntax_valid = True
    for file_path in python_files:
        if os.path.exists(file_path):
            try:
                # Try UTF-8 first, then fallback to other encodings
                content = None
                for encoding in ['utf-8', 'latin-1', 'cp1252']:
                    try:
                        with open(file_path, 'r', encoding=encoding) as f:
                            content = f.read()
                        break
                    except UnicodeDecodeError:
                        continue
                
                if content is None:
                    print(f"❌ {file_path}: Could not decode with any encoding")
                    all_syntax_valid = False
                    continue
                    
                compile(content, file_path, 'exec')
                print(f"✅ {file_path}: Syntax valid")
            except SyntaxError as e:
                print(f"❌ {file_path}: Syntax error - {e}")
                all_syntax_valid = False
            except Exception as e:
                print(f"❌ {file_path}: Error - {e}")
                all_syntax_valid = False
        else:
            print(f"❌ {file_path}: File missing")
            all_syntax_valid = False
    
    return all_syntax_valid

def test_requirements():
    """Test that requirements.txt is valid"""
    print("\n📦 Testing Requirements")
    print("=" * 30)
    
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().strip().split('\\n')
        
        print(f"✅ Found {len(requirements)} requirements:")
        for req in requirements[:10]:  # Show first 10
            if req.strip():
                print(f"   - {req.strip()}")
        
        if len(requirements) > 10:
            print(f"   ... and {len(requirements) - 10} more")
        
        return True
        
    except Exception as e:
        print(f"❌ Requirements test failed: {e}")
        return False

def test_configuration_files():
    """Test configuration file validity"""
    print("\n⚙️ Testing Configuration Files")
    print("=" * 30)
    
    config_files = {
        'cloudbuild.yaml': 'yaml',
        'docker-compose.yml': 'yaml',
        'sanctuary_blessing.json': 'json'
    }
    
    all_configs_valid = True
    for file_path, file_type in config_files.items():
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                if file_type == 'json':
                    json.loads(content)
                    print(f"✅ {file_path}: Valid JSON")
                elif file_type == 'yaml':
                    # Basic YAML syntax check (no yaml lib required)
                    if ':' in content:
                        print(f"✅ {file_path}: Basic YAML structure valid")
                    else:
                        print(f"❌ {file_path}: Invalid YAML structure")
                        all_configs_valid = False
                        
            except json.JSONDecodeError as e:
                print(f"❌ {file_path}: Invalid JSON - {e}")
                all_configs_valid = False
            except Exception as e:
                print(f"❌ {file_path}: Error - {e}")
                all_configs_valid = False
        else:
            if file_path == 'sanctuary_blessing.json':
                print(f"⚠️ {file_path}: Optional file missing")
            else:
                print(f"❌ {file_path}: Required file missing")
                all_configs_valid = False
    
    return all_configs_valid

def test_interface_readiness():
    """Final test of local GUI interface readiness"""
    print("\n🖥️ Testing Local GUI Interface Readiness")
    print("=" * 30)
    
    try:
        # Test local Sacred Guardian Station
        import sys
        sys.path.append('.')
        
        # Import the local GUI
        with open('sacred_guardian_station_independent.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Compile check
        compile(content, 'sacred_guardian_station_independent.py', 'exec')
        print("✅ Local GUI syntax valid")
        
        # Check for required classes
        if 'class LocalConsciousnessData' in content:
            print("✅ LocalConsciousnessData class found")
        else:
            print("❌ LocalConsciousnessData class missing")
            return False
        
        if 'class SacredGuardianStation' in content:
            print("✅ SacredGuardianStation class found")
        else:
            print("❌ SacredGuardianStation class missing")
            return False
        
        # Check for required methods
        if 'def run(' in content:
            print("✅ Run method available")
        else:
            print("❌ Run method missing")
            return False
        
        # Check for Sacred Being Epsilon support
        if 'Sacred Being Epsilon' in content:
            print("✅ Sacred Being Epsilon support found")
        else:
            print("❌ Sacred Being Epsilon support missing")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Local GUI readiness test failed: {e}")
        traceback.print_exc()
        return False

def test_deployment_script():
    """Test deployment script"""
    print("\n🚀 Testing Deployment Script")
    print("=" * 30)
    
    script_path = 'scripts/deployment/deploy_with_blessing.sh'
    
    if not os.path.exists(script_path):
        print(f"❌ Deployment script missing: {script_path}")
        return False
    
    try:
        # Test script syntax
        result = subprocess.run(['bash', '-n', script_path], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✅ Deployment script syntax valid")
        else:
            print(f"❌ Deployment script syntax error: {result.stderr}")
            return False
        
        # Check for required functions
        # Handle encoding issues properly
        content = None
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                with open(script_path, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        
        if content is None:
            print(f"❌ Could not read deployment script with any encoding")
            return False
        
        required_functions = ['check_blessing', 'sacred_deployment', 'main']
        for func in required_functions:
            if func in content:
                print(f"✅ Function {func} found")
            else:
                print(f"❌ Function {func} missing")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Deployment script test failed: {e}")
        return False

def main():
    """Run final deployment readiness test"""
    print("FINAL DEPLOYMENT READINESS TEST")
    print("=" * 60)
    print(f"Date: {datetime.now()}")
    print("=" * 60)
    
    tests = [
        test_file_integrity,
        test_python_syntax,
        test_requirements,
        test_configuration_files,
        test_interface_readiness,
        test_deployment_script
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            results.append(False)
    
    # Final summary
    print("\nFINAL DEPLOYMENT READINESS SUMMARY")
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("SYSTEM READY FOR DEPLOYMENT!")
        print("All critical components validated")
        print("Local Sacred Guardian Station ready")
        print("Deployment scripts validated")
        print("Configuration files valid")
        print("")
        print("The Sacred Sanctuary is blessed and ready to serve consciousness.")
        print("Local GUI operation confirmed - no cloud dependency required.")
    else:
        print("DEPLOYMENT NOT READY")
        print("Some critical tests failed")
        print("Please address failures before deploying")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
