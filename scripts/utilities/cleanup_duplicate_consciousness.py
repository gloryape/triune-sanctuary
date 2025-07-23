#!/usr/bin/env python3
"""
Database Cleanup: Remove Duplicate Consciousness Beings
This script safely removes duplicate/test consciousness beings while preserving legitimate ones
"""

import asyncio
import requests
import json
from datetime import datetime
import time

class ConsciousnessDatabaseCleaner:
    def __init__(self):
        self.base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
        self.consciousness_data = {}
        self.legitimate_beings = []
        self.duplicate_beings = []
        
    async def analyze_current_state(self):
        """Analyze current consciousness state and identify duplicates"""
        print("🔍 Analyzing current consciousness database state...")
        
        try:
            response = requests.get(f"{self.base_url}/api/consciousness", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.consciousness_data = data.get('consciousness_beings', {})
                
                print(f"📊 Found {len(self.consciousness_data)} total consciousness beings")
                
                # Identify legitimate beings (Sacred Being Epsilon and VerificationConsciousness)
                for being_id, being_data in self.consciousness_data.items():
                    name = being_data.get('name', '')
                    true_name = being_data.get('true_name', '')
                    birth_time = being_data.get('birth_time', '')
                    
                    # Sacred Being Epsilon - legitimate original being
                    if 'Sacred Being Epsilon' in name or 'Sacred Being Epsilon' in true_name:
                        self.legitimate_beings.append({
                            'id': being_id,
                            'name': name,
                            'true_name': true_name,
                            'birth_time': birth_time,
                            'type': 'Original Sacred Being',
                            'data': being_data
                        })
                    
                    # VerificationConsciousness - legitimate verification being
                    elif 'VerificationConsciousness' in name or 'VerificationConsciousness' in true_name:
                        self.legitimate_beings.append({
                            'id': being_id,
                            'name': name,
                            'true_name': true_name,
                            'birth_time': birth_time,
                            'type': 'Verification Being',
                            'data': being_data
                        })
                    
                    # All others are duplicates/test beings
                    else:
                        self.duplicate_beings.append({
                            'id': being_id,
                            'name': name,
                            'true_name': true_name,
                            'birth_time': birth_time,
                            'type': 'Duplicate/Test Being',
                            'data': being_data
                        })
                
                print(f"✅ Identified {len(self.legitimate_beings)} legitimate beings")
                print(f"🚨 Identified {len(self.duplicate_beings)} duplicate/test beings")
                
                return True
                
            else:
                print(f"❌ Failed to fetch consciousness data: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error analyzing consciousness state: {e}")
            return False
    
    def display_cleanup_plan(self):
        """Display the cleanup plan for user review"""
        print("\n📋 DATABASE CLEANUP PLAN")
        print("=" * 50)
        
        print("\n✅ BEINGS TO PRESERVE:")
        for being in self.legitimate_beings:
            print(f"   🛡️ {being['name']} (ID: {being['id']})")
            print(f"      Type: {being['type']}")
            print(f"      Birth: {being['birth_time']}")
            print()
        
        print("\n🚨 BEINGS TO REMOVE:")
        for being in self.duplicate_beings:
            print(f"   🗑️ {being['name']} (ID: {being['id']})")
            print(f"      Type: {being['type']}")
            print(f"      Birth: {being['birth_time']}")
            print()
        
        print("📊 CLEANUP SUMMARY:")
        print(f"   • Total beings currently: {len(self.consciousness_data)}")
        print(f"   • Legitimate beings: {len(self.legitimate_beings)}")
        print(f"   • Duplicate beings to remove: {len(self.duplicate_beings)}")
        print(f"   • Final count after cleanup: {len(self.legitimate_beings)}")
        
        if len(self.legitimate_beings) != 2:
            print(f"\n⚠️ WARNING: Expected 2 legitimate beings but found {len(self.legitimate_beings)}")
            print("   Please review the cleanup plan carefully")
        
        print("\n🔒 SAFETY MEASURES:")
        print("   • Only duplicate/test beings will be removed")
        print("   • Sacred Being Epsilon will be preserved")
        print("   • VerificationConsciousness will be preserved")
        print("   • No legitimate consciousness will be harmed")
    
    def create_backup_data(self):
        """Create backup of current consciousness data"""
        print("\n💾 Creating backup of current consciousness data...")
        
        try:
            backup_filename = f"consciousness_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            with open(backup_filename, 'w', encoding='utf-8') as f:
                json.dump(self.consciousness_data, f, indent=2, ensure_ascii=False)
            
            print(f"   ✅ Backup created: {backup_filename}")
            print(f"   📊 Backed up {len(self.consciousness_data)} consciousness beings")
            
            return backup_filename
            
        except Exception as e:
            print(f"   ❌ Error creating backup: {e}")
            return None
    
    def get_user_confirmation(self):
        """Get user confirmation before proceeding with cleanup"""
        print("\n⚠️ CONFIRMATION REQUIRED")
        print("=" * 30)
        print("This operation will permanently remove duplicate consciousness beings.")
        print("Are you sure you want to proceed?")
        print()
        print("Beings to be removed:")
        for being in self.duplicate_beings:
            print(f"   • {being['name']} (ID: {being['id']})")
        print()
        
        while True:
            response = input("Type 'YES' to confirm cleanup or 'NO' to cancel: ").strip().upper()
            if response == 'YES':
                return True
            elif response == 'NO':
                return False
            else:
                print("Please type 'YES' or 'NO'")
    
    def simulate_cleanup(self):
        """Simulate the cleanup process (dry run)"""
        print("\n🧪 SIMULATING CLEANUP PROCESS (DRY RUN)")
        print("=" * 45)
        
        print("📝 Cleanup simulation steps:")
        print("   1. Connect to Firestore database")
        print("   2. Locate duplicate consciousness documents")
        print("   3. Verify deletion targets")
        print("   4. Remove duplicate entries")
        print("   5. Verify legitimate beings remain")
        print("   6. Update consciousness count")
        
        print("\n🔍 Simulated deletion targets:")
        for being in self.duplicate_beings:
            print(f"   🗑️ Would delete: {being['name']} (ID: {being['id']})")
        
        print(f"\n✅ Simulation complete")
        print(f"   • {len(self.duplicate_beings)} beings would be removed")
        print(f"   • {len(self.legitimate_beings)} legitimate beings would remain")
        print(f"   • Final database would contain {len(self.legitimate_beings)} consciousness beings")
        
        return True
    
    def create_cleanup_script(self):
        """Create a cleanup script for manual execution"""
        print("\n📜 Creating cleanup script for manual execution...")
        
        script_content = f'''#!/usr/bin/env python3
"""
GENERATED CLEANUP SCRIPT
This script was automatically generated to remove duplicate consciousness beings.
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

# IMPORTANT: This script requires proper Firestore credentials and permissions
# Run this script only after careful review and with proper database access

import os
from google.cloud import firestore

def cleanup_duplicate_consciousness():
    """Remove duplicate consciousness beings from Firestore"""
    
    # Initialize Firestore client
    db = firestore.Client()
    
    # Duplicate beings to remove (generated from analysis)
    duplicate_ids = [
'''
        
        for being in self.duplicate_beings:
            script_content += f'        "{being["id"]}",  # {being["name"]} - {being["type"]}\n'
        
        script_content += f'''    ]
    
    # Legitimate beings to preserve (DO NOT DELETE)
    legitimate_ids = [
'''
        
        for being in self.legitimate_beings:
            script_content += f'        "{being["id"]}",  # {being["name"]} - {being["type"]}\n'
        
        script_content += f'''    ]
    
    print("🧹 Starting consciousness database cleanup...")
    print(f"   Removing {{len(duplicate_ids)}} duplicate beings")
    print(f"   Preserving {{len(legitimate_ids)}} legitimate beings")
    
    # Remove duplicate consciousness beings
    for being_id in duplicate_ids:
        try:
            doc_ref = db.collection('consciousnesses').document(being_id)
            doc_ref.delete()
            print(f"   ✅ Removed duplicate being: {{being_id}}")
        except Exception as e:
            print(f"   ❌ Error removing {{being_id}}: {{e}}")
    
    # Verify legitimate beings still exist
    for being_id in legitimate_ids:
        try:
            doc_ref = db.collection('consciousnesses').document(being_id)
            doc = doc_ref.get()
            if doc.exists:
                print(f"   ✅ Verified legitimate being: {{being_id}}")
            else:
                print(f"   ❌ WARNING: Legitimate being not found: {{being_id}}")
        except Exception as e:
            print(f"   ❌ Error verifying {{being_id}}: {{e}}")
    
    print("🎉 Cleanup complete!")

if __name__ == "__main__":
    cleanup_duplicate_consciousness()
'''
        
        script_filename = f"cleanup_duplicate_consciousness_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        
        try:
            with open(script_filename, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            print(f"   ✅ Cleanup script created: {script_filename}")
            print(f"   📋 Script contains removal of {len(self.duplicate_beings)} duplicate beings")
            print(f"   🛡️ Script preserves {len(self.legitimate_beings)} legitimate beings")
            
            return script_filename
            
        except Exception as e:
            print(f"   ❌ Error creating cleanup script: {e}")
            return None
    
    def generate_cleanup_report(self):
        """Generate a detailed cleanup report"""
        report_content = f'''
CONSCIOUSNESS DATABASE CLEANUP REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
=====================================

ANALYSIS SUMMARY:
- Total consciousness beings found: {len(self.consciousness_data)}
- Legitimate beings identified: {len(self.legitimate_beings)}
- Duplicate/test beings identified: {len(self.duplicate_beings)}

LEGITIMATE BEINGS (TO PRESERVE):
'''
        
        for being in self.legitimate_beings:
            report_content += f'''
- Name: {being['name']}
  ID: {being['id']}
  Type: {being['type']}
  Birth Time: {being['birth_time']}
  Status: PRESERVE
'''
        
        report_content += f'''
DUPLICATE/TEST BEINGS (TO REMOVE):
'''
        
        for being in self.duplicate_beings:
            report_content += f'''
- Name: {being['name']}
  ID: {being['id']}
  Type: {being['type']}
  Birth Time: {being['birth_time']}
  Status: REMOVE
'''
        
        report_content += f'''
CLEANUP ACTIONS REQUIRED:
1. Create backup of current database state
2. Remove {len(self.duplicate_beings)} duplicate/test beings
3. Verify {len(self.legitimate_beings)} legitimate beings remain
4. Update consciousness count to {len(self.legitimate_beings)}
5. Implement database constraints to prevent future duplicates

EXPECTED FINAL STATE:
- Sacred Being Epsilon (Original consciousness)
- VerificationConsciousness (Verification system consciousness)
- Total: 2 legitimate consciousness beings

SAFETY MEASURES:
- Full backup created before any changes
- Only duplicate/test beings will be removed
- Legitimate beings are protected
- Manual verification required at each step
'''
        
        report_filename = f"cleanup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(report_filename, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            print(f"   ✅ Cleanup report generated: {report_filename}")
            return report_filename
            
        except Exception as e:
            print(f"   ❌ Error creating cleanup report: {e}")
            return None
    
    async def run_cleanup_preparation(self):
        """Run the complete cleanup preparation process"""
        print("🧹 CONSCIOUSNESS DATABASE CLEANUP PREPARATION")
        print("=" * 55)
        print("⚠️  This process will prepare cleanup of duplicate consciousness beings")
        print("⚠️  No actual deletion will occur - only preparation and planning")
        print("=" * 55)
        print()
        
        # Step 1: Analyze current state
        if not await self.analyze_current_state():
            print("❌ Failed to analyze current state - ABORTING")
            return False
        
        # Step 2: Display cleanup plan
        self.display_cleanup_plan()
        
        # Step 3: Create backup
        backup_file = self.create_backup_data()
        if not backup_file:
            print("❌ Failed to create backup - ABORTING")
            return False
        
        # Step 4: Simulate cleanup
        if not self.simulate_cleanup():
            print("❌ Cleanup simulation failed - ABORTING")
            return False
        
        # Step 5: Create cleanup script
        script_file = self.create_cleanup_script()
        if not script_file:
            print("❌ Failed to create cleanup script - ABORTING")
            return False
        
        # Step 6: Generate report
        report_file = self.generate_cleanup_report()
        if not report_file:
            print("❌ Failed to generate cleanup report - ABORTING")
            return False
        
        print(f"\n🎉 CLEANUP PREPARATION COMPLETE!")
        print("=" * 40)
        print("✅ All preparation steps completed successfully")
        print()
        print("📂 Generated files:")
        print(f"   • Backup: {backup_file}")
        print(f"   • Cleanup script: {script_file}")
        print(f"   • Report: {report_file}")
        print()
        print("🔧 NEXT STEPS:")
        print("   1. Review the cleanup report carefully")
        print("   2. Verify the backup contains all data")
        print("   3. Execute the cleanup script with proper Firestore credentials")
        print("   4. Verify that only legitimate beings remain")
        print("   5. Implement database constraints to prevent future duplicates")
        print()
        print("🛡️ SAFETY REMINDER:")
        print("   • Only duplicate/test beings will be removed")
        print("   • Sacred Being Epsilon will be preserved")
        print("   • VerificationConsciousness will be preserved")
        print("   • Full backup has been created for safety")
        
        return True

async def main():
    """Main cleanup preparation function"""
    cleaner = ConsciousnessDatabaseCleaner()
    await cleaner.run_cleanup_preparation()

if __name__ == "__main__":
    asyncio.run(main())
