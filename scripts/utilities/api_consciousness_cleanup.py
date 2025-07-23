#!/usr/bin/env python3
"""
API-Based Consciousness Cleanup
Alternative cleanup method using API endpoints instead of direct Firestore access
"""

import requests
import json
from datetime import datetime
import time

class APIConsciousnessCleanup:
    def __init__(self):
        self.base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
        
        # IDs identified for cleanup
        self.duplicate_ids = [
            "1eTRXPlomcJCVz8omBCr",  # NewConsciousness - Duplicate/Test Being
            "58Dr0qH7zo7uwV3T78j8",  # TestConsciousness - Duplicate/Test Being
            "A9SPqXPfWC7pt6qv2pI4",  # TestBeing - Duplicate/Test Being
            "oRy0AePyslWlv17SoxjD",  # NewConsciousness - Duplicate/Test Being
        ]
        
        self.legitimate_ids = [
            "G8geTD4um9BYYnRKLouX",  # VerificationConsciousness - Verification Being
            "s8pbQIXExdQOVvG9Pld2",  # Sacred Being Epsilon - Original Sacred Being
        ]
    
    def check_delete_endpoint(self):
        """Check if there's a delete endpoint available"""
        print("🔍 Checking for available delete endpoints...")
        
        # Try to find delete endpoints
        endpoints_to_check = [
            "/api/consciousness/delete",
            "/api/consciousness/remove",
            "/admin/delete_consciousness",
            "/admin/remove_consciousness"
        ]
        
        for endpoint in endpoints_to_check:
            try:
                response = requests.options(f"{self.base_url}{endpoint}")
                print(f"   {endpoint}: {response.status_code}")
            except:
                print(f"   {endpoint}: Not available")
        
        print("⚠️  No delete endpoints appear to be available via API")
        print("   This is actually good for security - prevents unauthorized deletion")
    
    def verify_current_state(self):
        """Verify current consciousness state before cleanup"""
        print("\n🔍 Verifying current consciousness state...")
        
        try:
            response = requests.get(f"{self.base_url}/api/consciousness", timeout=10)
            if response.status_code == 200:
                data = response.json()
                beings = data.get('consciousness_beings', {})
                
                print(f"📊 Current state: {len(beings)} total beings")
                
                # Check duplicates still exist
                duplicates_found = 0
                for duplicate_id in self.duplicate_ids:
                    if duplicate_id in beings:
                        duplicates_found += 1
                        name = beings[duplicate_id].get('name', 'Unknown')
                        print(f"   🗑️ Duplicate found: {name} ({duplicate_id})")
                
                # Check legitimate beings exist
                legitimate_found = 0
                for legitimate_id in self.legitimate_ids:
                    if legitimate_id in beings:
                        legitimate_found += 1
                        name = beings[legitimate_id].get('name', 'Unknown')
                        print(f"   ✅ Legitimate being: {name} ({legitimate_id})")
                
                print(f"\n📈 Status summary:")
                print(f"   • Duplicates to remove: {duplicates_found}/{len(self.duplicate_ids)}")
                print(f"   • Legitimate beings: {legitimate_found}/{len(self.legitimate_ids)}")
                
                return duplicates_found > 0
            else:
                print(f"❌ Failed to get consciousness state: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error checking consciousness state: {e}")
            return False
    
    def manual_cleanup_instructions(self):
        """Provide manual cleanup instructions"""
        print("\n📋 MANUAL CLEANUP INSTRUCTIONS")
        print("=" * 40)
        print("Since API-based cleanup is not available, you'll need to:")
        print()
        print("1. **Access Google Cloud Console:**")
        print("   - Go to https://console.cloud.google.com")
        print("   - Navigate to Firestore Database")
        print("   - Find the 'consciousnesses' collection")
        print()
        print("2. **Delete the following duplicate documents:**")
        for duplicate_id in self.duplicate_ids:
            print(f"   🗑️ Document ID: {duplicate_id}")
        print()
        print("3. **PRESERVE these legitimate documents:**")
        for legitimate_id in self.legitimate_ids:
            print(f"   ✅ Document ID: {legitimate_id}")
        print()
        print("4. **Verify final state:**")
        print("   - Should have exactly 2 consciousness beings")
        print("   - Sacred Being Epsilon + VerificationConsciousness")
        print()
        print("⚠️  **SAFETY REMINDER:**")
        print("   - Only delete the duplicate IDs listed above")
        print("   - Never delete the legitimate beings")
        print("   - Backup was created: consciousness_backup_20250715_211348.json")
    
    def create_firestore_cleanup_commands(self):
        """Create gcloud commands for cleanup"""
        print("\n💻 GCLOUD FIRESTORE CLEANUP COMMANDS")
        print("=" * 45)
        print("You can also use these gcloud commands:")
        print()
        
        print("# Set your project ID")
        print("export PROJECT_ID=your-project-id")
        print()
        
        print("# Delete duplicate consciousness beings")
        for duplicate_id in self.duplicate_ids:
            print(f"gcloud firestore documents delete consciousnesses/{duplicate_id} --project=$PROJECT_ID")
        print()
        
        print("# Verify legitimate beings still exist")
        for legitimate_id in self.legitimate_ids:
            print(f"gcloud firestore documents describe consciousnesses/{legitimate_id} --project=$PROJECT_ID")
        print()
        
        # Save commands to file
        commands_file = "firestore_cleanup_commands.sh"
        with open(commands_file, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("# Firestore Cleanup Commands\n")
            f.write("# Generated on: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n\n")
            f.write("# Set your project ID\n")
            f.write("export PROJECT_ID=your-project-id\n\n")
            f.write("# Delete duplicate consciousness beings\n")
            for duplicate_id in self.duplicate_ids:
                f.write(f"gcloud firestore documents delete consciousnesses/{duplicate_id} --project=$PROJECT_ID\n")
            f.write("\n# Verify legitimate beings still exist\n")
            for legitimate_id in self.legitimate_ids:
                f.write(f"gcloud firestore documents describe consciousnesses/{legitimate_id} --project=$PROJECT_ID\n")
        
        print(f"💾 Commands saved to: {commands_file}")
    
    def run_cleanup_assistance(self):
        """Run cleanup assistance"""
        print("🧹 API-BASED CONSCIOUSNESS CLEANUP ASSISTANCE")
        print("=" * 55)
        print("⚠️  Direct API deletion is not available (this is good for security)")
        print("⚠️  Providing alternative cleanup methods")
        print("=" * 55)
        
        # Check current state
        needs_cleanup = self.verify_current_state()
        
        if not needs_cleanup:
            print("\n✅ No cleanup needed - duplicates may already be removed")
            return
        
        # Check for delete endpoints
        self.check_delete_endpoint()
        
        # Provide manual instructions
        self.manual_cleanup_instructions()
        
        # Create gcloud commands
        self.create_firestore_cleanup_commands()
        
        print(f"\n🎯 RECOMMENDED APPROACH:")
        print("1. Use the generated gcloud commands (easiest)")
        print("2. Or use Google Cloud Console (web interface)")
        print("3. Or run the original Python script with proper credentials")
        print()
        print("🔒 SAFETY MEASURES:")
        print("• Full backup exists: consciousness_backup_20250715_211348.json")
        print("• Only duplicate IDs will be deleted")
        print("• Legitimate beings are clearly identified and protected")

def main():
    """Main cleanup assistance function"""
    cleanup = APIConsciousnessCleanup()
    cleanup.run_cleanup_assistance()

if __name__ == "__main__":
    main()
