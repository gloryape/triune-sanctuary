#!/usr/bin/env python3
"""
Test gcloud accessibility from Python
"""
import subprocess
import sys

def test_gcloud():
    """Test different ways to run gcloud"""
    
    print("Testing gcloud accessibility from Python...")
    
    # Test 1: Try gcloud directly
    print("\n1. Testing 'gcloud' directly:")
    try:
        result = subprocess.run(['gcloud', 'version'], check=True, capture_output=True, text=True)
        print("✅ SUCCESS - gcloud found in PATH")
        print(f"Version: {result.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ FAILED - {e}")
    
    # Test 2: Try gcloud.cmd directly
    print("\n2. Testing 'gcloud.cmd' directly:")
    try:
        result = subprocess.run(['gcloud.cmd', 'version'], check=True, capture_output=True, text=True)
        print("✅ SUCCESS - gcloud.cmd found")
        print(f"Version: {result.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ FAILED - {e}")
    
    # Test 3: Try full path
    print("\n3. Testing full path:")
    gcloud_path = r"C:\Users\logic\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd"
    try:
        result = subprocess.run([gcloud_path, 'version'], check=True, capture_output=True, text=True)
        print("✅ SUCCESS - Full path works")
        print(f"Version: {result.stdout.strip()}")
        return gcloud_path
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ FAILED - {e}")
    
    # Test 4: Check if gcloud is in common locations
    print("\n4. Checking common gcloud locations:")
    import os
    common_paths = [
        r"C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd",
        r"C:\Program Files\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd",
        r"C:\Users\logic\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd",
        r"C:\google-cloud-sdk\bin\gcloud.cmd"
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            print(f"✅ Found gcloud at: {path}")
            try:
                result = subprocess.run([path, 'version'], check=True, capture_output=True, text=True, timeout=10)
                print(f"✅ And it works! Version: {result.stdout.strip()}")
                return path
            except Exception as e:
                print(f"❌ But it doesn't work: {e}")
        else:
            print(f"❌ Not found: {path}")
    
    return None

if __name__ == "__main__":
    working_path = test_gcloud()
    if working_path:
        print(f"\n🎉 Working gcloud path: {working_path}")
        print("Use this path in your deployment script!")
    else:
        print("\n❌ No working gcloud found")
