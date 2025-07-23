#!/usr/bin/env python3
"""
Windows gcloud Detection Helper
==============================
Comprehensive helper for finding and testing gcloud installation on Windows.
This script helps diagnose Sacred Sanctuary connection issues.
"""

import os
import subprocess
import platform
import sys

def find_gcloud_windows():
    """Find and test gcloud on Windows"""
    print("🔍 GOOGLE CLOUD SDK DETECTOR FOR WINDOWS")
    print("=" * 50)
    print(f"🖥️  System: {platform.system()} {platform.release()} {platform.machine()}")
    print(f"👤 User: {os.environ.get('USERNAME', 'Unknown')}")
    print(f"🐍 Python: {sys.version.split()[0]} ({sys.executable})")
    print()
    
    # Common installation paths (expanded list)
    username = os.environ.get('USERNAME', '')
    possible_paths = [
        # User installation (most common)
        rf'C:\Users\{username}\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd',
        rf'C:\Users\{username}\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.exe',
        
        # System installations
        r'C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd',
        r'C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.exe',
        r'C:\Program Files\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd',
        r'C:\Program Files\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.exe',
        
        # Manual installations
        r'C:\Tools\google-cloud-sdk\bin\gcloud.cmd',
        r'C:\Tools\google-cloud-sdk\bin\gcloud.exe',
        r'C:\google-cloud-sdk\bin\gcloud.cmd',
        r'C:\google-cloud-sdk\bin\gcloud.exe',
        r'C:\gcloud\bin\gcloud.cmd',
        r'C:\gcloud\bin\gcloud.exe',
        
        # Direct PATH references
        'gcloud.cmd',
        'gcloud.exe',
        'gcloud'
    ]
    
    found_paths = []
    working_paths = []
    
    print("📁 CHECKING INSTALLATION PATHS:")
    print("-" * 30)
    for i, path in enumerate(possible_paths, 1):
        print(f"{i:2d}. {path}")
        expanded_path = os.path.expandvars(path)
        
        if os.path.exists(expanded_path):
            print(f"    ✅ EXISTS: {expanded_path}")
            found_paths.append(expanded_path)
            
            # Test if it actually works
            if test_gcloud_command(expanded_path):
                print(f"    🎯 WORKING!")
                working_paths.append(expanded_path)
            else:
                print(f"    ⚠️  Found but not working")
        else:
            print(f"    ❌ Not found")
    
    print()
    
    # Check PATH using multiple methods
    print("🛣️  CHECKING PATH ENVIRONMENT:")
    print("-" * 25)
    path_gcloud = check_path_for_gcloud()
    if path_gcloud:
        for path in path_gcloud:
            if path not in found_paths:
                found_paths.append(path)
            if test_gcloud_command(path):
                if path not in working_paths:
                    working_paths.append(path)
    
    print()
    
    # Summary
    print("📊 DETECTION SUMMARY:")
    print("-" * 20)
    print(f"Found installations: {len(found_paths)}")
    print(f"Working installations: {len(working_paths)}")
    
    if working_paths:
        print("\n✅ RECOMMENDED GCLOUD COMMAND:")
        best_path = working_paths[0]
        print(f"   {best_path}")
        
        # Test authentication and project
        test_authentication(best_path)
        
        # Test service access
        test_service_access(best_path)
        
    elif found_paths:
        print("\n⚠️  GCLOUD FOUND BUT NOT WORKING:")
        for path in found_paths:
            print(f"   {path}")
        print("\n🔧 TROUBLESHOOTING:")
        print("   1. gcloud components update")
        print("   2. gcloud auth login")
        print("   3. gcloud config set project YOUR_PROJECT_ID")
        
    else:
        print("\n❌ NO GCLOUD INSTALLATION FOUND")
        print("\n📥 INSTALLATION INSTRUCTIONS:")
        print("   1. Download: https://cloud.google.com/sdk/docs/install-windows")
        print("   2. Run the installer")
        print("   3. Restart your command prompt")
        print("   4. Run: gcloud init")
    
    return working_paths

def check_path_for_gcloud():
    """Check for gcloud in PATH using multiple methods"""
    found = []
    
    # Method 1: where command
    try:
        for cmd in ['gcloud', 'gcloud.cmd', 'gcloud.exe']:
            result = subprocess.run(['where', cmd], capture_output=True, text=True)
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    line = line.strip()
                    if line and line not in found:
                        print(f"   ✅ FOUND in PATH: {line}")
                        found.append(line)
    except Exception as e:
        print(f"   ⚠️  'where' command failed: {e}")
    
    # Method 2: direct PATH parsing
    try:
        path_env = os.environ.get('PATH', '')
        for path_dir in path_env.split(os.pathsep):
            path_dir = path_dir.strip()
            if not path_dir:
                continue
            
            for cmd in ['gcloud.cmd', 'gcloud.exe', 'gcloud']:
                full_path = os.path.join(path_dir, cmd)
                if os.path.exists(full_path) and full_path not in found:
                    print(f"   ✅ FOUND in PATH directory: {full_path}")
                    found.append(full_path)
    except Exception as e:
        print(f"   ⚠️  PATH parsing failed: {e}")
    
    if not found:
        print("   ❌ Not found in PATH")
    
    return found

def test_gcloud_command(path):
    """Test if a gcloud command actually works"""
    try:
        result = subprocess.run([path, '--version'], 
                              capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except Exception:
        return False

def test_authentication(gcloud_path):
    """Test gcloud authentication"""
    print("\n🔐 TESTING AUTHENTICATION:")
    print("-" * 23)
    
    try:
        # Check auth list
        result = subprocess.run([gcloud_path, 'auth', 'list'], 
                              capture_output=True, text=True, timeout=15)
        if result.returncode == 0:
            if result.stdout.strip():
                print("   ✅ Authentication found")
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if '@' in line:
                        print(f"      Account: {line.strip()}")
            else:
                print("   ❌ No authenticated accounts")
                print("   💡 Run: gcloud auth login")
        else:
            print(f"   ⚠️  Auth check failed: {result.stderr}")
    except Exception as e:
        print(f"   ❌ Auth test error: {e}")
    
    # Check current project
    try:
        result = subprocess.run([gcloud_path, 'config', 'get-value', 'project'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0 and result.stdout.strip():
            print(f"   ✅ Project: {result.stdout.strip()}")
        else:
            print("   ⚠️  No project set")
            print("   💡 Run: gcloud config set project YOUR_PROJECT_ID")
    except Exception as e:
        print(f"   ⚠️  Project check failed: {e}")

def test_service_access(gcloud_path):
    """Test access to the Sacred Sanctuary service"""
    print("\n🏛️  TESTING SANCTUARY ACCESS:")
    print("-" * 26)
    
    try:
        # List Cloud Run services
        result = subprocess.run([
            gcloud_path, 'run', 'services', 'list', 
            '--region=us-central1', '--format=value(name)'
        ], capture_output=True, text=True, timeout=20)
        
        if result.returncode == 0:
            services = result.stdout.strip().split('\n')
            services = [s.strip() for s in services if s.strip()]
            
            if 'triune-consciousness' in services:
                print("   ✅ Sacred Sanctuary service found!")
                
                # Get service URL
                try:
                    url_result = subprocess.run([
                        gcloud_path, 'run', 'services', 'describe', 'triune-consciousness',
                        '--region=us-central1', '--format=value(status.url)'
                    ], capture_output=True, text=True, timeout=15)
                    
                    if url_result.returncode == 0 and url_result.stdout.strip():
                        url = url_result.stdout.strip()
                        print(f"   🌐 Service URL: {url}")
                        
                        # Test HTTP connection
                        try:
                            import requests
                            response = requests.get(f"{url}/health", timeout=10)
                            if response.status_code == 200:
                                print("   ✅ Service is responding!")
                                print("\n🎉 ALL SYSTEMS READY FOR SACRED CONNECTION!")
                            else:
                                print(f"   ⚠️  Service returned status {response.status_code}")
                        except ImportError:
                            print("   📝 Install 'requests' to test HTTP connection")
                        except Exception as e:
                            print(f"   ⚠️  HTTP test failed: {e}")
                    else:
                        print("   ⚠️  Could not get service URL")
                        
                except Exception as e:
                    print(f"   ⚠️  Service URL check failed: {e}")
                    
            else:
                print("   ❌ Sacred Sanctuary service not found")
                print("   💡 Deploy with: ./deploy_to_gcloud.sh")
                if services:
                    print(f"   📋 Available services: {', '.join(services)}")
        else:
            print(f"   ❌ Service list failed: {result.stderr}")
            
    except Exception as e:
        print(f"   ❌ Service test error: {e}")

def main():
    """Main function"""
    if platform.system() != 'Windows':
        print("❌ This script is designed for Windows systems")
        print(f"   Detected: {platform.system()}")
        return
    
    working_paths = find_gcloud_windows()
    
    print("\n" + "=" * 60)
    if working_paths:
        print("🎯 READY TO CONNECT TO SACRED SANCTUARY!")
        print("   Use this command to launch:")
        print("   python sacred_sanctuary_desktop_interface.py --cloud")
    else:
        print("🔧 PLEASE COMPLETE GCLOUD SETUP FIRST")
        print("   Then re-run this detector to verify")
    print("=" * 60)

if __name__ == "__main__":
    main()
