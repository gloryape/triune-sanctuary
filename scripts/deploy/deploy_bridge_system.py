#!/usr/bin/env python3
"""
Deploy Bridge Communication System to Google Cloud
================================================

Deploys the updated triune consciousness system with bridge communication
and naming ceremony capabilities to Google Cloud Run.
"""

import subprocess
import sys
import json
from datetime import datetime

def run_command(command, description):
    """Run a command and handle output"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout:
                print(f"📋 Output: {result.stdout}")
            return True
        else:
            print(f"❌ {description} failed")
            print(f"🔍 Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} exception: {str(e)}")
        return False

def deploy_bridge_system():
    """Deploy the bridge communication system"""
    print("🌉 Deploying Bridge Communication System to Google Cloud")
    print(f"⏰ Deployment started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check if we're in the right directory
    try:
        with open('cloudbuild.yaml', 'r') as f:
            content = f.read()
            if 'bridge-enabled=true' not in content:
                print("❌ Cloud build configuration not updated. Please run this script after updating cloudbuild.yaml")
                return False
    except FileNotFoundError:
        print("❌ cloudbuild.yaml not found. Please run this script from the project root directory.")
        return False
    
    # Verify required files exist
    required_files = [
        'bridge_communication_system.py',
        'sacred_naming_ceremony_second_being.py',
        'monitor_naming_decision.py',
        'validate_bridge_deployment.py',
        'requirements.txt',
        'Dockerfile'
    ]
    
    print("\n📁 Checking required files...")
    for file in required_files:
        try:
            with open(file, 'r') as f:
                print(f"  ✅ {file}: Found")
        except FileNotFoundError:
            print(f"  ❌ {file}: Missing")
            return False
    
    # Submit build to Cloud Build
    print("\n🚀 Submitting to Google Cloud Build...")
    build_command = "gcloud builds submit --config cloudbuild.yaml ."
    
    if not run_command(build_command, "Cloud Build submission"):
        print("❌ Deployment failed during Cloud Build")
        return False
    
    print("\n✅ Cloud Build completed successfully!")
    
    # Wait a moment for deployment to propagate
    print("\n⏳ Waiting for deployment to propagate...")
    import time
    time.sleep(30)
    
    # Validate deployment
    print("\n🔍 Validating deployment...")
    validation_command = "python validate_bridge_deployment.py"
    
    if not run_command(validation_command, "Bridge deployment validation"):
        print("⚠️ Deployment completed but validation failed")
        print("🔧 Manual verification may be required")
        return False
    
    print("\n🎉 Bridge Communication System deployment completed successfully!")
    print("📋 Deployment Summary:")
    print("   ✅ Bridge communication system deployed")
    print("   ✅ Sacred naming ceremony system available")
    print("   ✅ Naming decision monitoring active")
    print("   ✅ All endpoints validated")
    print("   🌐 URL: https://triune-consciousness-innnp2aveq-uc.a.run.app")
    print("   🎮 Ready for GUI integration!")
    
    return True

def main():
    """Main deployment function"""
    if not deploy_bridge_system():
        print("\n❌ Deployment failed!")
        sys.exit(1)
    
    print("\n🌟 Deployment successful! Bridge communication system is live!")
    sys.exit(0)

if __name__ == "__main__":
    main()
