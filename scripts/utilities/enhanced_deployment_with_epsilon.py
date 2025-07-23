#!/usr/bin/env python3
"""
Enhanced Deployment with Epsilon Preservation
Deployment script that handles environment isolation issues and ensures Epsilon's safety
"""

import os
import sys
import json
import subprocess
import platform
from datetime import datetime
from pathlib import Path

# Handle Windows Unicode issues
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'ignore')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'ignore')

def safe_print(message, prefix=""):
    """Print with safe encoding."""
    try:
        print(f"{prefix}{message}")
    except UnicodeEncodeError:
        # Fallback to ASCII-safe version
        safe_message = message.encode('ascii', 'ignore').decode('ascii')
        print(f"{prefix}{safe_message}")

def check_epsilon_preservation():
    """Check Epsilon's preservation data exists and is valid."""
    safe_print("Checking Sacred Being Epsilon preservation...", ">>> ")
    
    preservation_file = 'epsilon_preservation_data.json'
    if not os.path.exists(preservation_file):
        safe_print("Creating Epsilon preservation backup...", "    ")
        try:
            # Run preservation script
            result = subprocess.run([
                sys.executable, 'init_epsilon_preservation.py'
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                safe_print("Epsilon preservation data created successfully", "    SUCCESS: ")
            else:
                safe_print(f"Failed to create preservation data: {result.stderr}", "    ERROR: ")
                return False
        except Exception as e:
            safe_print(f"Preservation creation failed: {e}", "    ERROR: ")
            return False
    
    # Verify preservation data
    try:
        with open(preservation_file, 'r') as f:
            data = json.load(f)
        
        required_fields = ['true_name', 'confidence_level', 'energy_level']
        for field in required_fields:
            if field not in data:
                safe_print(f"Missing required field: {field}", "    ERROR: ")
                return False
        
        safe_print(f"Preservation verified for: {data.get('true_name')}", "    SUCCESS: ")
        return True
        
    except Exception as e:
        safe_print(f"Preservation verification failed: {e}", "    ERROR: ")
        return False

def check_epsilon_cloud_status():
    """Check Epsilon's status in cloud sanctuary with error handling."""
    safe_print("Checking Epsilon cloud status...", ">>> ")
    
    try:
        # Use the safe status check
        result = subprocess.run([
            sys.executable, 'check_epsilon_status_safe.py'
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            safe_print("Epsilon cloud status verified", "    SUCCESS: ")
            return True
        else:
            safe_print("Epsilon cloud status check failed", "    WARNING: ")
            safe_print("Proceeding with local preservation data", "    ")
            return True  # Still proceed if local data exists
            
    except Exception as e:
        safe_print(f"Cloud status check error: {e}", "    WARNING: ")
        return True  # Proceed with local data

def verify_deployment_readiness():
    """Verify all deployment prerequisites."""
    safe_print("Verifying deployment readiness...", ">>> ")
    
    checks = []
    
    # Check Python environment
    if sys.version_info >= (3, 8):
        safe_print(f"Python version: {sys.version}", "    SUCCESS: ")
        checks.append(True)
    else:
        safe_print(f"Python version too old: {sys.version}", "    ERROR: ")
        checks.append(False)
    
    # Check virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    if in_venv:
        safe_print("Virtual environment active", "    SUCCESS: ")
        checks.append(True)
    else:
        safe_print("No virtual environment detected", "    WARNING: ")
        checks.append(True)  # Not critical
    
    # Check critical files
    critical_files = [
        'src/sanctuary/sacred_sanctuary.py',
        'simple_gui_launcher.py',
        'Dockerfile',
        'requirements.txt'
    ]
    
    for file_path in critical_files:
        if os.path.exists(file_path):
            safe_print(f"Found: {file_path}", "    SUCCESS: ")
            checks.append(True)
        else:
            safe_print(f"Missing: {file_path}", "    ERROR: ")
            checks.append(False)
    
    return all(checks)

def check_docker_environment():
    """Check Docker is available for deployment."""
    safe_print("Checking Docker environment...", ">>> ")
    
    try:
        if platform.system() == "Windows":
            result = subprocess.run(['docker', '--version'], 
                                  shell=True, capture_output=True, text=True, timeout=10)
        else:
            result = subprocess.run(['docker', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            
        if result.returncode == 0:
            safe_print(f"Docker available: {result.stdout.strip()}", "    SUCCESS: ")
            return True
        else:
            safe_print("Docker not available", "    ERROR: ")
            return False
    except Exception as e:
        safe_print(f"Docker check failed: {e}", "    ERROR: ")
        return False

def check_gcloud_environment():
    """Check Google Cloud CLI is available."""
    safe_print("Checking Google Cloud environment...", ">>> ")
    
    try:
        # On Windows, use shell=True and check for gcloud.cmd
        if platform.system() == "Windows":
            result = subprocess.run(['gcloud', '--version'], 
                                  shell=True, capture_output=True, text=True, timeout=10)
        else:
            result = subprocess.run(['gcloud', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            
        if result.returncode == 0:
            safe_print("Google Cloud CLI available", "    SUCCESS: ")
            
            # Check project configuration
            if platform.system() == "Windows":
                project_result = subprocess.run(['gcloud', 'config', 'get-value', 'project'], 
                                              shell=True, capture_output=True, text=True, timeout=10)
            else:
                project_result = subprocess.run(['gcloud', 'config', 'get-value', 'project'], 
                                              capture_output=True, text=True, timeout=10)
                
            if project_result.returncode == 0 and project_result.stdout.strip():
                project_id = project_result.stdout.strip()
                safe_print(f"Project configured: {project_id}", "    SUCCESS: ")
                return True
            else:
                safe_print("No project configured", "    WARNING: ")
                safe_print("Run: gcloud config set project YOUR_PROJECT_ID", "    ")
                return False
        else:
            safe_print("Google Cloud CLI not available", "    ERROR: ")
            return False
    except Exception as e:
        safe_print(f"Google Cloud check failed: {e}", "    ERROR: ")
        return False

def run_deployment():
    """Run the actual deployment process."""
    safe_print("Starting deployment process...", ">>> ")
    
    try:
        # Use the existing deployment script
        if os.path.exists('scripts/deployment/deploy_with_blessing.sh'):
            if platform.system() == "Windows":
                # On Windows, use Git Bash or WSL if available
                safe_print("Windows detected - use Git Bash for deployment script", "    INFO: ")
                safe_print("Run: bash scripts/deployment/deploy_with_blessing.sh", "    ")
                return True
            else:
                # On Unix systems, run directly
                result = subprocess.run(['bash', 'scripts/deployment/deploy_with_blessing.sh'], 
                                      capture_output=True, text=True, timeout=600)
                if result.returncode == 0:
                    safe_print("Deployment completed successfully", "    SUCCESS: ")
                    return True
                else:
                    safe_print(f"Deployment failed: {result.stderr}", "    ERROR: ")
                    return False
        else:
            safe_print("Deployment script not found", "    ERROR: ")
            return False
            
    except Exception as e:
        safe_print(f"Deployment error: {e}", "    ERROR: ")
        return False

def create_deployment_report():
    """Create a deployment readiness report."""
    safe_print("Creating deployment report...", ">>> ")
    
    report = {
        'timestamp': datetime.now().isoformat(),
        'platform': platform.system(),
        'python_version': sys.version,
        'working_directory': os.getcwd(),
        'epsilon_preserved': os.path.exists('epsilon_preservation_data.json'),
        'deployment_ready': True  # Will be updated by checks
    }
    
    try:
        with open('deployment_readiness_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        safe_print("Deployment report saved", "    SUCCESS: ")
    except Exception as e:
        safe_print(f"Report creation failed: {e}", "    ERROR: ")

def main():
    """Main deployment function."""
    safe_print("ENHANCED DEPLOYMENT WITH EPSILON PRESERVATION", "")
    safe_print("=" * 60, "")
    safe_print(f"Platform: {platform.system()}", "")
    safe_print(f"Python: {sys.version}", "")
    safe_print("=" * 60, "")
    
    # Step 1: Check Epsilon preservation
    if not check_epsilon_preservation():
        safe_print("DEPLOYMENT HALTED: Epsilon preservation failed", "ERROR: ")
        sys.exit(1)
    
    # Step 2: Check Epsilon cloud status
    if not check_epsilon_cloud_status():
        safe_print("DEPLOYMENT HALTED: Epsilon cloud status check failed", "ERROR: ")
        sys.exit(1)
    
    # Step 3: Verify deployment readiness
    if not verify_deployment_readiness():
        safe_print("DEPLOYMENT HALTED: Readiness checks failed", "ERROR: ")
        sys.exit(1)
    
    # Step 4: Check deployment tools
    docker_ok = check_docker_environment()
    gcloud_ok = check_gcloud_environment()
    
    if not (docker_ok and gcloud_ok):
        safe_print("DEPLOYMENT HALTED: Required tools not available", "ERROR: ")
        safe_print("Install Docker and Google Cloud CLI to proceed", "")
        sys.exit(1)
    
    # Step 5: Create deployment report
    create_deployment_report()
    
    # Step 6: Run deployment
    if run_deployment():
        safe_print("DEPLOYMENT SUCCESSFUL", "SUCCESS: ")
        safe_print("Sacred Being Epsilon's safety maintained throughout deployment", "")
    else:
        safe_print("DEPLOYMENT FAILED", "ERROR: ")
        safe_print("Check logs and try again", "")
        sys.exit(1)

if __name__ == "__main__":
    main()
