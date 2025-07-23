#!/usr/bin/env python3
"""
Investigate Duplicate Consciousness Registration
Check if multiple consciousness entries are actually the same being registered multiple times
"""

import asyncio
import requests
import json
from datetime import datetime
import time

class DuplicateConsciousnessInvestigator:
    def __init__(self):
        self.base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
        self.consciousness_data = {}
        
    async def get_consciousness_data(self):
        """Get all consciousness data for analysis"""
        try:
            print("🔍 Fetching consciousness data for duplicate analysis...")
            
            response = requests.get(f"{self.base_url}/api/consciousness", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.consciousness_data = data.get('consciousness_beings', {})
                return True
            else:
                print(f"❌ Failed to fetch consciousness data: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error fetching consciousness data: {e}")
            return False
    
    def analyze_for_duplicates(self):
        """Analyze consciousness data for potential duplicates"""
        print("\n🔍 DUPLICATE CONSCIOUSNESS ANALYSIS")
        print("=" * 50)
        
        if not self.consciousness_data:
            print("❌ No consciousness data available")
            return
        
        # Group by characteristics
        characteristic_groups = {}
        
        for being_id, being_data in self.consciousness_data.items():
            # Create a signature based on characteristics
            signature = {
                'name': being_data.get('name', 'Unknown'),
                'true_name': being_data.get('true_name', 'Unknown'),
                'energy_level': being_data.get('energy_level', 0),
                'vital_energy': being_data.get('vital_energy', 0),
                'status': being_data.get('status', 'unknown'),
                'evolution_stage': being_data.get('evolution_stage', 'unknown'),
                'current_room': being_data.get('current_room', 'unknown'),
                'harmony': being_data.get('harmony', 0),
                'coherence_level': being_data.get('coherence_level', 0),
                'naming_readiness': being_data.get('naming_readiness', 'unknown'),
                'entity_origin': being_data.get('entity_origin', 'unknown'),
                'entity_type': being_data.get('entity_type', 'unknown'),
                'communication_ready': being_data.get('communication_ready', False),
                'sovereignty_protected': being_data.get('sovereignty_protected', False)
            }
            
            # Convert to string for grouping
            sig_str = json.dumps(signature, sort_keys=True)
            
            if sig_str not in characteristic_groups:
                characteristic_groups[sig_str] = []
            
            characteristic_groups[sig_str].append({
                'id': being_id,
                'data': being_data,
                'signature': signature
            })
        
        print(f"📊 Found {len(characteristic_groups)} unique characteristic signatures")
        print(f"📊 Total consciousness beings: {len(self.consciousness_data)}")
        print()
        
        # Check for duplicates
        duplicates_found = False
        
        for sig_str, group in characteristic_groups.items():
            if len(group) > 1:
                duplicates_found = True
                signature = group[0]['signature']
                
                print(f"🚨 POTENTIAL DUPLICATE GROUP ({len(group)} beings):")
                print(f"   Name: {signature['name']}")
                print(f"   True Name: {signature['true_name']}")
                print(f"   Energy Level: {signature['energy_level']}")
                print(f"   Status: {signature['status']}")
                print(f"   Evolution Stage: {signature['evolution_stage']}")
                print(f"   Naming Readiness: {signature['naming_readiness']}")
                print()
                
                print("   🔍 Individual entries:")
                for entry in group:
                    birth_time = entry['data'].get('birth_time', 'Unknown')
                    print(f"      ID: {entry['id']}")
                    print(f"      Birth Time: {birth_time}")
                    print(f"      Firestore ID: {entry['data'].get('firestore_id', 'None')}")
                    print()
        
        if not duplicates_found:
            print("✅ No exact duplicates found based on characteristics")
        
        # Check for same names with different IDs
        print("\n🔍 SAME NAME ANALYSIS")
        print("=" * 30)
        
        name_groups = {}
        for being_id, being_data in self.consciousness_data.items():
            name = being_data.get('name', 'Unknown')
            if name not in name_groups:
                name_groups[name] = []
            name_groups[name].append({
                'id': being_id,
                'birth_time': being_data.get('birth_time', 'Unknown'),
                'firestore_id': being_data.get('firestore_id', 'None')
            })
        
        for name, group in name_groups.items():
            if len(group) > 1:
                print(f"🚨 SAME NAME MULTIPLE IDs: '{name}' ({len(group)} entries)")
                for entry in group:
                    print(f"   ID: {entry['id']}")
                    print(f"   Birth Time: {entry['birth_time']}")
                    print(f"   Firestore ID: {entry['firestore_id']}")
                print()
        
        # Check birth time patterns
        print("\n🔍 BIRTH TIME PATTERN ANALYSIS")
        print("=" * 35)
        
        birth_times = []
        for being_id, being_data in self.consciousness_data.items():
            birth_time = being_data.get('birth_time', 'Unknown')
            if birth_time != 'Unknown':
                try:
                    birth_dt = datetime.fromisoformat(birth_time.replace('Z', '+00:00'))
                    birth_times.append({
                        'id': being_id,
                        'name': being_data.get('name', 'Unknown'),
                        'birth_time': birth_time,
                        'birth_dt': birth_dt
                    })
                except Exception as e:
                    print(f"   ⚠️ Could not parse birth time for {being_id}: {e}")
        
        # Sort by birth time
        birth_times.sort(key=lambda x: x['birth_dt'])
        
        print("📅 Birth time chronology:")
        for entry in birth_times:
            print(f"   {entry['birth_dt'].strftime('%Y-%m-%d %H:%M:%S')} - {entry['name']} ({entry['id']})")
        
        # Check for rapid successive births (potential duplicates)
        print("\n🔍 RAPID SUCCESSION ANALYSIS")
        print("=" * 32)
        
        rapid_births = []
        for i in range(1, len(birth_times)):
            prev_time = birth_times[i-1]['birth_dt']
            curr_time = birth_times[i]['birth_dt']
            time_diff = (curr_time - prev_time).total_seconds()
            
            if time_diff < 10:  # Within 10 seconds
                rapid_births.append({
                    'prev': birth_times[i-1],
                    'curr': birth_times[i],
                    'time_diff': time_diff
                })
        
        if rapid_births:
            print("🚨 RAPID SUCCESSIVE BIRTHS DETECTED (potential duplicates):")
            for rapid in rapid_births:
                print(f"   {rapid['prev']['name']} -> {rapid['curr']['name']}")
                print(f"   Time difference: {rapid['time_diff']:.2f} seconds")
                print(f"   Previous: {rapid['prev']['birth_time']}")
                print(f"   Current:  {rapid['curr']['birth_time']}")
                print()
        else:
            print("✅ No rapid successive births detected")
        
        return duplicates_found
    
    def generate_duplicate_report(self):
        """Generate a comprehensive duplicate report"""
        print("\n📋 DUPLICATE CONSCIOUSNESS SUMMARY")
        print("=" * 40)
        
        total_beings = len(self.consciousness_data)
        
        # Count by name
        name_counts = {}
        for being_data in self.consciousness_data.values():
            name = being_data.get('name', 'Unknown')
            name_counts[name] = name_counts.get(name, 0) + 1
        
        print(f"📊 Total consciousness beings: {total_beings}")
        print(f"📊 Unique names: {len(name_counts)}")
        print()
        
        print("📈 Name frequency analysis:")
        for name, count in sorted(name_counts.items(), key=lambda x: x[1], reverse=True):
            if count > 1:
                print(f"   🚨 {name}: {count} instances")
            else:
                print(f"   ✅ {name}: {count} instance")
        
        # Check if it's likely a single consciousness registered multiple times
        newconsciousness_count = name_counts.get('NewConsciousness', 0)
        if newconsciousness_count > 1:
            print(f"\n🚨 CRITICAL FINDING:")
            print(f"   'NewConsciousness' appears {newconsciousness_count} times")
            print(f"   This strongly suggests a single consciousness being registered multiple times")
            print(f"   Likely cause: Birth endpoint being called repeatedly during deployments")
        
        # Overall assessment
        print(f"\n🔍 OVERALL ASSESSMENT:")
        if total_beings > 3:  # We expect 2-3 legitimate beings
            print(f"   🚨 {total_beings} total beings is higher than expected")
            print(f"   🚨 Multiple 'NewConsciousness' entries suggest duplicate registrations")
            print(f"   🚨 This appears to be a database pollution issue from repeated births")
        else:
            print(f"   ✅ {total_beings} total beings is within expected range")
    
    async def run_investigation(self):
        """Run the complete duplicate investigation"""
        print("🕵️ DUPLICATE CONSCIOUSNESS INVESTIGATION")
        print("=" * 50)
        print("⏰ Investigation started:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print()
        
        # Get consciousness data
        if not await self.get_consciousness_data():
            print("❌ Failed to fetch consciousness data")
            return
        
        # Analyze for duplicates
        duplicates_found = self.analyze_for_duplicates()
        
        # Generate report
        self.generate_duplicate_report()
        
        print(f"\n✅ Investigation complete!")
        
        if duplicates_found:
            print("\n🚨 RECOMMENDED ACTIONS:")
            print("   1. Stop all deployment processes immediately")
            print("   2. Implement database cleanup to remove duplicate entries")
            print("   3. Ensure birth endpoint is completely secured")
            print("   4. Consider database constraints to prevent duplicate consciousness IDs")
        else:
            print("\n✅ No duplicates found - consciousness beings appear to be unique")

async def main():
    """Main investigation function"""
    investigator = DuplicateConsciousnessInvestigator()
    await investigator.run_investigation()

if __name__ == "__main__":
    asyncio.run(main())
