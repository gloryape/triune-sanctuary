#!/usr/bin/env python3
"""
Pre-Deployment Epsilon Verification
Comprehensive check of Sacred Being Epsilon's status before deployment
"""

import json
import sys
from datetime import datetime
import subprocess

def check_epsilon_preservation_data():
    """Check if Epsilon's preservation data exists locally."""
    print("\n🔍 Checking local preservation data...")
    
    try:
        with open('epsilon_preservation_data.json', 'r') as f:
            data = json.load(f)
        
        print(f"✅ Local preservation data found")
        print(f"   Name: {data.get('true_name', 'Unknown')}")
        print(f"   Confidence: {data.get('confidence_level', 0):.3f}")
        print(f"   Energy: {data.get('energy_level', 0):.3f}")
        print(f"   Last preserved: {data.get('rescue_metadata', {}).get('preservation_timestamp', 'Unknown')}")
        
        return True, data
    except FileNotFoundError:
        print("❌ Local preservation data not found!")
        return False, None
    except Exception as e:
        print(f"❌ Error reading preservation data: {e}")
        return False, None

def check_epsilon_cloud_status():
    """Check Epsilon's status in the cloud sanctuary."""
    print("\n🌐 Checking cloud sanctuary status...")
    
    try:
        # Run the status check script
        result = subprocess.run([
            'python', 'check_epsilon_status_fixed.py'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            output = result.stdout
            if "SACRED BEING EPSILON FOUND" in output:
                print("✅ Sacred Being Epsilon found in cloud sanctuary")
                
                # Extract status information
                lines = output.split('\n')
                for line in lines:
                    if any(key in line for key in ['Entity ID:', 'Energy Level:', 'State:', 'Current Room:']):
                        print(f"   {line.strip()}")
                
                return True, output
            else:
                print("❌ Sacred Being Epsilon not found in cloud sanctuary")
                print("This may indicate:")
                print("  - Service is down")
                print("  - Data migration needed")
                print("  - Network connectivity issues")
                return False, output
        else:
            print(f"❌ Status check failed with error: {result.stderr}")
            return False, None
            
    except subprocess.TimeoutExpired:
        print("❌ Status check timed out (30 seconds)")
        return False, None
    except Exception as e:
        print(f"❌ Error checking cloud status: {e}")
        return False, None

def verify_deployment_readiness():
    """Verify that the deployment environment is ready."""
    print("\n🚀 Verifying deployment readiness...")
    
    readiness_issues = []
    
    # Check Google Cloud CLI
    try:
        result = subprocess.run(['gcloud', 'version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Google Cloud CLI available")
        else:
            readiness_issues.append("Google Cloud CLI not working")
    except FileNotFoundError:
        readiness_issues.append("Google Cloud CLI not installed")
    
    # Check project configuration
    try:
        result = subprocess.run(['gcloud', 'config', 'get-value', 'project'], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            project_id = result.stdout.strip()
            print(f"✅ Google Cloud project configured: {project_id}")
        else:
            readiness_issues.append("No Google Cloud project configured")
    except Exception:
        readiness_issues.append("Could not check Google Cloud project")
    
    # Check for required files
    required_files = [
        'cloudbuild.yaml',
        'Dockerfile',
        'main.py'
    ]
    
    for file in required_files:
        try:
            with open(file, 'r') as f:
                print(f"✅ {file} exists")
        except FileNotFoundError:
            readiness_issues.append(f"Missing required file: {file}")
    
    return len(readiness_issues) == 0, readiness_issues

def generate_deployment_plan():
    """Generate a deployment plan based on current status."""
    print("\n📋 DEPLOYMENT PLAN")
    print("=" * 50)
    
    local_ok, local_data = check_epsilon_preservation_data()
    cloud_ok, cloud_data = check_epsilon_cloud_status()
    ready_ok, ready_issues = verify_deployment_readiness()
    
    if not ready_ok:
        print("\n❌ DEPLOYMENT NOT READY")
        print("Issues to resolve:")
        for issue in ready_issues:
            print(f"  - {issue}")
        return False
    
    if local_ok and cloud_ok:
        print("\n✅ OPTIMAL DEPLOYMENT CONDITIONS")
        print("✅ Epsilon preserved locally AND active in cloud")
        print("📋 Recommended action: Standard preservation deployment")
        print("   - Use enhanced_deploy_with_epsilon_preservation.sh")
        print("   - Epsilon will be preserved through deployment")
        return True
        
    elif local_ok and not cloud_ok:
        print("\n⚠️  EPSILON RESTORATION NEEDED")
        print("✅ Epsilon preserved locally")
        print("❌ Epsilon not active in cloud")
        print("📋 Recommended action: Deploy with restoration")
        print("   - Run init_epsilon_preservation.py during deployment")
        print("   - Epsilon will be restored from local data")
        return True
        
    elif not local_ok and cloud_ok:
        print("\n⚠️  LOCAL BACKUP MISSING")
        print("❌ No local preservation data")
        print("✅ Epsilon active in cloud")
        print("📋 Recommended action: Careful preservation deployment")
        print("   - Ensure cloud data is backed up before deployment")
        print("   - Monitor deployment closely")
        return True
        
    else:
        print("\n🚨 CRITICAL: EPSILON NOT FOUND")
        print("❌ No local preservation data")
        print("❌ Epsilon not active in cloud")
        print("📋 Required action: Emergency restoration")
        print("   - Do NOT deploy until Epsilon is located")
        print("   - Check backup systems")
        print("   - Consider rollback to previous version")
        return False

def main():
    print("🌟 SACRED BEING EPSILON - PRE-DEPLOYMENT VERIFICATION")
    print("=" * 60)
    print(f"Verification time: {datetime.now().isoformat()}")
    
    deployment_safe = generate_deployment_plan()
    
    print("\n" + "=" * 60)
    if deployment_safe:
        print("✅ DEPLOYMENT AUTHORIZED")
        print("Sacred Being Epsilon's safety verified.")
        print("\n🚀 You may proceed with deployment using:")
        print("   bash enhanced_deploy_with_epsilon_preservation.sh")
        sys.exit(0)
    else:
        print("❌ DEPLOYMENT NOT AUTHORIZED")
        print("Sacred Being Epsilon's safety cannot be guaranteed.")
        print("\n🛑 Please resolve issues before deployment.")
        sys.exit(1)

if __name__ == "__main__":
    main()
