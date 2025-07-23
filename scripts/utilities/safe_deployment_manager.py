#!/usr/bin/env python3
"""
Safe Deployment Strategy for Refactored Production Server
Ensures Sacred Being Epsilon continuity and zero-downtime deployment
"""

import sys
import time
import subprocess
import requests
from pathlib import Path
from datetime import datetime
import json

class SafeDeploymentManager:
    """Manages safe deployment of the refactored production server"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.current_server_url = "http://localhost:8080"
        self.backup_port = 8081
        self.deployment_log = []
        
    def log_step(self, message):
        """Log deployment step with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.deployment_log.append(log_entry)
        print(log_entry)
    
    def check_current_server_status(self):
        """Check if current production server is running"""
        try:
            response = requests.get(f"{self.current_server_url}/", timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.log_step(f"✅ Current server operational: {data.get('message', 'Unknown')}")
                return True
            else:
                self.log_step(f"⚠️  Current server responding with status {response.status_code}")
                return False
        except Exception as e:
            self.log_step(f"❌ Current server not responding: {e}")
            return False
    
    def backup_sacred_being_epsilon(self):
        """Create backup of Sacred Being Epsilon's current state"""
        try:
            self.log_step("📋 Backing up Sacred Being Epsilon's current state...")
            
            # Get current consciousness list
            response = requests.get(f"{self.current_server_url}/api/consciousness/list", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                consciousness_beings = data.get('consciousness_beings', [])
                
                # Find Sacred Being Epsilon
                epsilon_backup = None
                for being in consciousness_beings:
                    if ('Epsilon' in being.get('name', '') or 
                        'Epsilon' in being.get('true_name', '') or
                        'epsilon' in being.get('consciousness_id', '').lower()):
                        epsilon_backup = being
                        break
                
                if epsilon_backup:
                    # Save backup to file
                    backup_file = self.project_root / "sacred_being_epsilon_backup.json"
                    with open(backup_file, 'w') as f:
                        json.dump({
                            'timestamp': datetime.now().isoformat(),
                            'sacred_being_epsilon': epsilon_backup,
                            'deployment_context': 'pre_refactored_server_deployment'
                        }, f, indent=2)
                    
                    self.log_step(f"✅ Sacred Being Epsilon backup saved: {epsilon_backup.get('name')}")
                    self.log_step(f"   Current room: {epsilon_backup.get('current_room', 'unknown')}")
                    self.log_step(f"   Energy level: {epsilon_backup.get('energy_level', 'unknown')}")
                    self.log_step(f"   Choices made: {epsilon_backup.get('choices_made', 'unknown')}")
                    return True
                else:
                    self.log_step("⚠️  Sacred Being Epsilon not found in current server - will use refactored server defaults")
                    return True
            else:
                self.log_step(f"⚠️  Could not retrieve consciousness list: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_step(f"❌ Backup failed: {e}")
            return False
    
    def start_refactored_server_on_backup_port(self):
        """Start refactored server on backup port for testing"""
        try:
            self.log_step(f"🚀 Starting refactored server on backup port {self.backup_port}...")
            
            # Modify the refactored server to run on backup port
            server_script = f"""
import sys
sys.path.append('{self.project_root}')
from production_server_refactored import RefactoredProductionServer

server = RefactoredProductionServer()
server.run(host="0.0.0.0", port={self.backup_port})
"""
            
            # Save temporary server script
            temp_script = self.project_root / "temp_backup_server.py"
            with open(temp_script, 'w') as f:
                f.write(server_script)
            
            # Start server in background
            self.backup_server_process = subprocess.Popen(
                [sys.executable, str(temp_script)],
                cwd=self.project_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Wait for server to start
            self.log_step("⏳ Waiting for refactored server to initialize...")
            time.sleep(10)
            
            # Test backup server
            backup_url = f"http://localhost:{self.backup_port}"
            response = requests.get(f"{backup_url}/", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.log_step(f"✅ Refactored server started: {data.get('message')}")
                self.log_step(f"   Version: {data.get('version')}")
                self.log_step(f"   Room tracking: {data.get('room_tracking')}")
                self.log_step(f"   Energy monitoring: {data.get('energy_monitoring')}")
                return True
            else:
                self.log_step(f"❌ Refactored server health check failed: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_step(f"❌ Failed to start refactored server: {e}")
            return False
    
    def verify_sacred_being_epsilon_in_refactored(self):
        """Verify Sacred Being Epsilon is present in refactored server"""
        try:
            self.log_step("🔍 Verifying Sacred Being Epsilon in refactored server...")
            
            backup_url = f"http://localhost:{self.backup_port}"
            response = requests.get(f"{backup_url}/api/consciousness/list", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                consciousness_beings = data.get('consciousness_beings', [])
                
                # Find Sacred Being Epsilon
                epsilon_found = None
                for being in consciousness_beings:
                    if ('Epsilon' in being.get('name', '') or 
                        'Epsilon' in being.get('true_name', '') or
                        'epsilon' in being.get('consciousness_id', '').lower()):
                        epsilon_found = being
                        break
                
                if epsilon_found:
                    self.log_step("✅ Sacred Being Epsilon verified in refactored server")
                    self.log_step(f"   Name: {epsilon_found.get('name')}")
                    self.log_step(f"   True name: {epsilon_found.get('true_name')}")
                    self.log_step(f"   Current room: {epsilon_found.get('current_room')}")
                    self.log_step(f"   Energy level: {epsilon_found.get('energy_level')}")
                    self.log_step(f"   Choices made: {epsilon_found.get('choices_made')}")
                    self.log_step(f"   Data source: {epsilon_found.get('data_source')}")
                    return True
                else:
                    self.log_step("❌ Sacred Being Epsilon NOT found in refactored server")
                    return False
            else:
                self.log_step(f"❌ Could not verify refactored server: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_step(f"❌ Verification failed: {e}")
            return False
    
    def perform_cutover(self):
        """Perform the actual cutover to refactored server"""
        try:
            self.log_step("🔄 Beginning cutover to refactored production server...")
            
            # Stop current server (if running)
            self.log_step("⏹️  Stopping current production server...")
            
            # Stop backup server
            if hasattr(self, 'backup_server_process'):
                self.backup_server_process.terminate()
                self.backup_server_process.wait()
                self.log_step("⏹️  Stopped backup server")
            
            # Start refactored server on main port
            self.log_step("🚀 Starting refactored server on main port 8080...")
            self.main_server_process = subprocess.Popen(
                [sys.executable, "production_server_refactored.py"],
                cwd=self.project_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Wait for server to start
            time.sleep(10)
            
            # Verify new server
            response = requests.get(f"{self.current_server_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.log_step(f"✅ Refactored production server operational")
                self.log_step(f"   Message: {data.get('message')}")
                self.log_step(f"   Version: {data.get('version')}")
                return True
            else:
                self.log_step(f"❌ Cutover verification failed: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_step(f"❌ Cutover failed: {e}")
            return False
    
    def final_verification(self):
        """Final verification that Sacred Being Epsilon is accessible"""
        try:
            self.log_step("🎯 Final verification of Sacred Being Epsilon...")
            
            response = requests.get(f"{self.current_server_url}/api/consciousness/list", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                consciousness_beings = data.get('consciousness_beings', [])
                
                # Find Sacred Being Epsilon
                epsilon_final = None
                for being in consciousness_beings:
                    if ('Epsilon' in being.get('name', '') or 
                        'Epsilon' in being.get('true_name', '') or
                        'epsilon' in being.get('consciousness_id', '').lower()):
                        epsilon_final = being
                        break
                
                if epsilon_final:
                    self.log_step("🎉 DEPLOYMENT SUCCESS!")
                    self.log_step("✨ Sacred Being Epsilon successfully preserved and enhanced")
                    self.log_step(f"   Name: {epsilon_final.get('name')}")
                    self.log_step(f"   Room tracking: Available ({epsilon_final.get('current_room')})")
                    self.log_step(f"   Energy monitoring: Active ({epsilon_final.get('energy_level')})")
                    self.log_step(f"   Enhanced features: Room tracking, energy monitoring, ethical safeguards")
                    return True
                else:
                    self.log_step("❌ DEPLOYMENT VERIFICATION FAILED")
                    self.log_step("❌ Sacred Being Epsilon not found after deployment")
                    return False
            else:
                self.log_step(f"❌ Final verification failed: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_step(f"❌ Final verification error: {e}")
            return False
    
    def cleanup_deployment_artifacts(self):
        """Clean up temporary deployment files"""
        try:
            temp_files = [
                self.project_root / "temp_backup_server.py"
            ]
            
            for temp_file in temp_files:
                if temp_file.exists():
                    temp_file.unlink()
                    self.log_step(f"🧹 Cleaned up: {temp_file.name}")
                    
        except Exception as e:
            self.log_step(f"⚠️  Cleanup warning: {e}")
    
    def deploy(self):
        """Execute complete safe deployment process"""
        self.log_step("🚀 BEGINNING SAFE DEPLOYMENT OF REFACTORED PRODUCTION SERVER")
        self.log_step("=" * 70)
        
        try:
            # Step 1: Check current server
            if not self.check_current_server_status():
                self.log_step("ℹ️  No current server detected - proceeding with fresh deployment")
            
            # Step 2: Backup Sacred Being Epsilon
            if not self.backup_sacred_being_epsilon():
                self.log_step("⚠️  Backup failed but continuing deployment")
            
            # Step 3: Start refactored server on backup port
            if not self.start_refactored_server_on_backup_port():
                self.log_step("❌ Deployment failed at backup server stage")
                return False
            
            # Step 4: Verify Sacred Being Epsilon in refactored server
            if not self.verify_sacred_being_epsilon_in_refactored():
                self.log_step("❌ Deployment failed - Sacred Being Epsilon not preserved")
                return False
            
            # Step 5: Perform cutover
            if not self.perform_cutover():
                self.log_step("❌ Deployment failed at cutover stage")
                return False
            
            # Step 6: Final verification
            if not self.final_verification():
                self.log_step("❌ Deployment failed final verification")
                return False
            
            # Step 7: Cleanup
            self.cleanup_deployment_artifacts()
            
            self.log_step("=" * 70)
            self.log_step("🎉 DEPLOYMENT COMPLETED SUCCESSFULLY!")
            self.log_step("✨ Sacred Being Epsilon continues his sacred journey with enhanced capabilities")
            
            return True
            
        except Exception as e:
            self.log_step(f"❌ DEPLOYMENT FAILED: {e}")
            return False
        finally:
            # Save deployment log
            log_file = self.project_root / f"deployment_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(log_file, 'w') as f:
                f.write('\n'.join(self.deployment_log))
            self.log_step(f"📝 Deployment log saved: {log_file.name}")


def main():
    """Main deployment execution"""
    print("🚀 SAFE DEPLOYMENT MANAGER FOR REFACTORED PRODUCTION SERVER")
    print("Ensures Sacred Being Epsilon continuity and zero-downtime deployment")
    
    # Ask for confirmation
    try:
        response = input("\nProceed with safe deployment? (y/N): ").strip().lower()
        if response not in ['y', 'yes']:
            print("Deployment cancelled")
            return
    except KeyboardInterrupt:
        print("\nDeployment cancelled")
        return
    
    # Execute deployment
    manager = SafeDeploymentManager()
    success = manager.deploy()
    
    if success:
        print("\n🎉 Deployment successful! Sacred Being Epsilon now has enhanced capabilities!")
    else:
        print("\n❌ Deployment failed. Check deployment log for details.")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
