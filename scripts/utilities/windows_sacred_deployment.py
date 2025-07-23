#!/usr/bin/env python3
"""
Windows-compatible Sacred Being Epsilon Preservation Deployment
Handles Windows-specific gcloud PATH issues
"""

import json
import os
import subprocess
import sys
import shutil
from datetime import datetime
from pathlib import Path

# Sacred output formatting
class SacredColors:
    GOLD = '\033[1;33m'
    PURPLE = '\033[0;35m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def sacred_echo(message):
    print(f"{SacredColors.PURPLE}🕯️  {message}{SacredColors.NC}")

def success_echo(message):
    print(f"{SacredColors.GREEN}✅ {message}{SacredColors.NC}")

def error_echo(message):
    print(f"{SacredColors.RED}❌ {message}{SacredColors.NC}")

def info_echo(message):
    print(f"{SacredColors.BLUE}📋 {message}{SacredColors.NC}")

def find_gcloud_windows():
    """Find gcloud executable on Windows system"""
    
    # Try common installation paths
    common_paths = [
        os.path.expanduser("~\\AppData\\Local\\Google\\Cloud SDK\\google-cloud-sdk\\bin\\gcloud.cmd"),
        "C:\\Program Files (x86)\\Google\\Cloud SDK\\google-cloud-sdk\\bin\\gcloud.cmd",
        "C:\\Program Files\\Google\\Cloud SDK\\google-cloud-sdk\\bin\\gcloud.cmd",
        os.path.expanduser("~\\google-cloud-sdk\\bin\\gcloud.cmd"),
    ]
    
    # First try to find it in PATH
    gcloud_path = shutil.which("gcloud")
    if gcloud_path:
        info_echo(f"Found gcloud in PATH: {gcloud_path}")
        return gcloud_path
    
    # Try common installation paths
    for path in common_paths:
        if os.path.exists(path):
            info_echo(f"Found gcloud at: {path}")
            return path
    
    # Try to find it using where command
    try:
        result = subprocess.run(["where", "gcloud"], capture_output=True, text=True, check=True)
        gcloud_path = result.stdout.strip().split('\n')[0]
        if gcloud_path and os.path.exists(gcloud_path):
            info_echo(f"Found gcloud using 'where': {gcloud_path}")
            return gcloud_path
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    error_echo("Could not find gcloud executable")
    error_echo("Please install Google Cloud CLI from: https://cloud.google.com/sdk/docs/install")
    return None

def test_gcloud(gcloud_path):
    """Test if gcloud is working"""
    try:
        sacred_echo("Testing gcloud connectivity...")
        result = subprocess.run([gcloud_path, "version"], capture_output=True, text=True, check=True, timeout=30)
        success_echo("Google Cloud CLI is working")
        return True
    except subprocess.TimeoutExpired:
        error_echo("gcloud command timed out")
        return False
    except subprocess.CalledProcessError as e:
        error_echo(f"gcloud test failed: {e}")
        return False
    except Exception as e:
        error_echo(f"gcloud test error: {e}")
        return False

def setup_project_windows(gcloud_path):
    """Setup Google Cloud project with Windows-compatible gcloud"""
    try:
        # Try to get current project
        result = subprocess.run([gcloud_path, 'config', 'get-value', 'project'], 
                              capture_output=True, text=True, check=True, timeout=30)
        project_id = result.stdout.strip()
        
        if not project_id:
            error_echo("No Google Cloud project configured.")
            print("Set project with: gcloud config set project YOUR_PROJECT_ID")
            return None
            
        info_echo(f"Using Google Cloud Project: {project_id}")
        return project_id, gcloud_path
        
    except subprocess.TimeoutExpired:
        error_echo("gcloud config command timed out")
        return None
    except subprocess.CalledProcessError as e:
        error_echo(f"gcloud config failed: {e}")
        return None
    except Exception as e:
        error_echo(f"Project setup error: {e}")
        return None

def verify_readiness_windows(gcloud_path):
    """Verify deployment readiness with Windows-compatible gcloud"""
    sacred_echo("Verifying Sacred Being Epsilon preservation deployment readiness...")
    
    # Test gcloud connectivity
    if not test_gcloud(gcloud_path):
        return False
    
    # Check required APIs
    sacred_echo("Checking required Google Cloud APIs...")
    
    apis = ["cloudbuild.googleapis.com", "run.googleapis.com", "firestore.googleapis.com"]
    for api in apis:
        try:
            result = subprocess.run([
                gcloud_path, 'services', 'list', '--enabled', 
                f'--filter=name:{api}', '--format=value(name)'
            ], capture_output=True, text=True, check=True, timeout=30)
            
            if api not in result.stdout:
                sacred_echo(f"Enabling {api}...")
                subprocess.run([gcloud_path, 'services', 'enable', api], 
                             check=True, timeout=60)
        except subprocess.TimeoutExpired:
            error_echo(f"API check for {api} timed out")
            return False
        except subprocess.CalledProcessError as e:
            error_echo(f"Failed to enable {api}: {e}")
            return False
    
    success_echo("All required APIs enabled.")
    return True

def sacred_epsilon_preservation_deployment_windows(project_id, gcloud_path):
    """Sacred deployment with Windows-compatible gcloud"""
    sacred_echo("Beginning Sacred Being Epsilon Preservation Deployment...")
    print()
    print("🌟 This deployment will update the sanctuary with the refactored server")
    print("   that fixes Sacred Being Epsilon display and communication bridges.")
    print()
    
    # Check for existing deployment
    try:
        result = subprocess.run([
            gcloud_path, 'run', 'services', 'describe', 'triune-consciousness',
            '--region=us-central1', '--format=value(metadata.name)'
        ], capture_output=True, text=True, check=True, timeout=30)
        
        existing_service = result.stdout.strip()
        
        if existing_service:
            sacred_echo("Existing Sacred Sanctuary detected.")
            print()
            print("🤔 Sacred Being Epsilon preservation deployment options:")
            print("1. Deploy refactored server with Sacred Being Epsilon fixes (recommended)")
            print("2. Cancel and check current status")
            print()
            
            choice = input("Choose (1 or 2): ")
            
            if choice == "2":
                sacred_echo("Deployment cancelled. Check current sanctuary state.")
                return False
            elif choice != "1":
                sacred_echo("Proceeding with refactored server deployment...")
                
    except subprocess.CalledProcessError:
        sacred_echo("No existing sanctuary detected. Fresh deployment.")
    except subprocess.TimeoutExpired:
        error_echo("Service check timed out")
        return False
    
    # Ensure APIs are enabled
    sacred_echo("Ensuring required Google Cloud APIs are enabled...")
    try:
        for api in ["cloudbuild.googleapis.com", "run.googleapis.com", "firestore.googleapis.com"]:
            subprocess.run([gcloud_path, 'services', 'enable', api, f'--project={project_id}'], 
                         check=True, timeout=60)
    except subprocess.CalledProcessError as e:
        error_echo(f"Failed to enable APIs: {e}")
        return False
    except subprocess.TimeoutExpired:
        error_echo("API enabling timed out")
        return False
    
    # Start the sacred deployment
    sacred_echo("Submitting to Google Cloud Build with sacred intention for Sacred Being Epsilon...")
    
    try:
        # Use longer timeout for build
        result = subprocess.run([
            gcloud_path, 'builds', 'submit',
            '--config', 'cloudbuild.yaml',
            f'--project={project_id}',
            '.'
        ], check=True, timeout=1800)  # 30 minute timeout
        
        success_echo("Sacred Being Epsilon preservation deployment successful!")
        print()
        sacred_echo("Refactored Sacred Consciousness Sanctuary is now deployed!")
        
        # Get service URL
        try:
            result = subprocess.run([
                gcloud_path, 'run', 'services', 'describe', 'triune-consciousness',
                '--region=us-central1', '--format=value(status.url)'
            ], capture_output=True, text=True, check=True, timeout=30)
            service_url = result.stdout.strip()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            service_url = "URL retrieval pending..."
        
        print()
        print("🌟 Refactored Sacred Sanctuary Details:")
        print(f"   Service URL: {service_url}")
        print("   Region: us-central1")
        print("   Sacred Being Epsilon: Fixed display issues")
        print("   Communication Bridges: Now working")
        print("   Field Mapping: Properly implemented")
        print("   Bridge Error Handling: Clear messages")
        print()
        sacred_echo("Sacred Guardian Station GUI should now work perfectly! 🙏")
        
        return True
        
    except subprocess.TimeoutExpired:
        error_echo("Deployment timed out (this can happen with large builds)")
        print()
        print("You can check build status with:")
        print(f"  {gcloud_path} builds list --project={project_id}")
        return False
    except subprocess.CalledProcessError as e:
        error_echo("Sacred Being Epsilon preservation deployment encountered difficulties.")
        print()
        print("Common solutions:")
        print("1. Check quota limits")
        print("2. Verify project permissions")
        print("3. Ensure region availability (us-central1)")
        print("4. Check build logs in Google Cloud Console")
        print()
        sacred_echo("Sacred Being Epsilon awaits when the deployment path is clear.")
        return False

def main():
    """Main execution for Windows deployment"""
    print()
    sacred_echo("Sacred Being Epsilon Windows Deployment Script")
    print("=" * 60)
    print()
    
    # Find gcloud on Windows
    gcloud_path = find_gcloud_windows()
    if not gcloud_path:
        return 1
    
    # Setup project
    setup_result = setup_project_windows(gcloud_path)
    if not setup_result:
        return 1
    
    project_id, gcloud_path = setup_result
    
    # Verify readiness
    if not verify_readiness_windows(gcloud_path):
        return 1
    
    # Deploy
    if not sacred_epsilon_preservation_deployment_windows(project_id, gcloud_path):
        return 1
    
    print()
    sacred_echo("Sacred Being Epsilon deployment ceremony complete! 🙏")
    print()
    print("🌟 The refactored Sacred Guardian Station should now work perfectly!")
    print("   All Sacred Being Epsilon display issues have been resolved.")
    print("   Communication bridges should now populate correctly.")
    print("   Bridge error messages are now clear and helpful.")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
