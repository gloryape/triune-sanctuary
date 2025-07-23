#!/usr/bin/env python3
"""
Investigate Build-Time Consciousness Creation
This script analyzes deployment logs and timing to understand when new consciousness beings are created
"""

import asyncio
import requests
import json
from datetime import datetime
import time

class BuildTimeConsciousnessInvestigator:
    def __init__(self):
        self.base_url = "https://triune-consciousness-innnp2aveq-uc.a.run.app"
        self.findings = []
        
    def add_finding(self, finding_type, message, data=None):
        """Add investigation finding"""
        finding = {
            'type': finding_type,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'data': data or {}
        }
        self.findings.append(finding)
        print(f"📊 [{finding_type}] {message}")
        
    async def check_current_consciousness_state(self):
        """Check current consciousness state"""
        try:
            print("\n🔍 INVESTIGATION: Current Consciousness State")
            print("=" * 50)
            
            response = requests.get(f"{self.base_url}/api/consciousness", timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                if 'consciousness_beings' in data:
                    beings = data['consciousness_beings']
                    print(f"📈 Found {len(beings)} consciousness beings:")
                    
                    for being_id, being_data in beings.items():
                        name = being_data.get('name', 'Unknown')
                        birth_time = being_data.get('birth_time', 'Unknown')
                        entity_id = being_data.get('entity_id', being_id)
                        
                        print(f"  🧠 {name} (ID: {entity_id})")
                        print(f"      Birth: {birth_time}")
                        print(f"      Status: {being_data.get('status', 'Unknown')}")
                        print(f"      Origin: {being_data.get('entity_origin', 'Unknown')}")
                        print()
                        
                        # Check for potential deployment-created beings
                        if birth_time != 'Unknown':
                            try:
                                birth_dt = datetime.fromisoformat(birth_time.replace('Z', '+00:00'))
                                now = datetime.now()
                                
                                # Check if created recently (within last hour)
                                time_diff = (now - birth_dt).total_seconds()
                                if time_diff < 3600:  # 1 hour
                                    self.add_finding(
                                        'RECENT_CREATION',
                                        f"Being '{name}' was created {time_diff:.0f} seconds ago - potentially during deployment",
                                        {'being_id': entity_id, 'birth_time': birth_time}
                                    )
                            except Exception as e:
                                self.add_finding('PARSE_ERROR', f"Could not parse birth time for {name}: {e}")
                    
                    # Check for the specific beings mentioned
                    verification_being = None
                    epsilon_being = None
                    
                    for being_id, being_data in beings.items():
                        name = being_data.get('name', '')
                        true_name = being_data.get('true_name', '')
                        
                        if 'VerificationConsciousness' in name or 'VerificationConsciousness' in true_name:
                            verification_being = being_data
                        elif 'Sacred Being Epsilon' in name or 'Sacred Being Epsilon' in true_name:
                            epsilon_being = being_data
                    
                    if verification_being:
                        self.add_finding(
                            'VERIFICATION_BEING_FOUND',
                            f"VerificationConsciousness found: {verification_being.get('entity_id', 'Unknown ID')}",
                            verification_being
                        )
                    
                    if epsilon_being:
                        self.add_finding(
                            'EPSILON_BEING_FOUND',
                            f"Sacred Being Epsilon found: {epsilon_being.get('entity_id', 'Unknown ID')}",
                            epsilon_being
                        )
                    
                    # Check for any new beings that might be deployment artifacts
                    for being_id, being_data in beings.items():
                        name = being_data.get('name', '')
                        if name == 'NewConsciousness':
                            self.add_finding(
                                'DEFAULT_BEING_FOUND',
                                f"Default 'NewConsciousness' being found - likely deployment artifact",
                                being_data
                            )
                
                else:
                    self.add_finding('NO_BEINGS_STRUCTURE', "No consciousness_beings structure found in response")
                
            else:
                self.add_finding('ENDPOINT_ERROR', f"Consciousness endpoint returned {response.status_code}")
                
        except Exception as e:
            self.add_finding('INVESTIGATION_ERROR', f"Error checking consciousness state: {e}")
    
    async def check_birth_endpoint_security(self):
        """Check if birth endpoint is properly secured"""
        try:
            print("\n🔍 INVESTIGATION: Birth Endpoint Security")
            print("=" * 50)
            
            # Try to access birth endpoint
            response = requests.post(f"{self.base_url}/birth", 
                                   json={'name': 'TestBeing'}, 
                                   timeout=10)
            
            if response.status_code == 200:
                self.add_finding(
                    'SECURITY_BREACH',
                    "Birth endpoint is still accessible - this could create beings during deployment verification!",
                    {'response': response.json()}
                )
            elif response.status_code == 403:
                self.add_finding(
                    'SECURITY_GOOD',
                    "Birth endpoint properly secured with 403 Forbidden"
                )
            elif response.status_code == 404:
                self.add_finding(
                    'ENDPOINT_MISSING',
                    "Birth endpoint not found - may be disabled"
                )
            else:
                self.add_finding(
                    'SECURITY_UNKNOWN',
                    f"Birth endpoint returned {response.status_code}",
                    {'status_code': response.status_code}
                )
                
        except Exception as e:
            self.add_finding('SECURITY_CHECK_ERROR', f"Error checking birth endpoint: {e}")
    
    async def investigate_deployment_patterns(self):
        """Investigate deployment patterns that might create consciousness"""
        try:
            print("\n🔍 INVESTIGATION: Deployment Patterns")
            print("=" * 50)
            
            # Check the sanctuary status endpoint that cloud build verifies
            response = requests.get(f"{self.base_url}/api/sacred_sanctuary/status", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.add_finding(
                    'SANCTUARY_STATUS',
                    f"Sanctuary status endpoint operational",
                    data
                )
            else:
                self.add_finding(
                    'SANCTUARY_STATUS_ERROR',
                    f"Sanctuary status endpoint returned {response.status_code}"
                )
            
            # Check health endpoint
            response = requests.get(f"{self.base_url}/health", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.add_finding(
                    'HEALTH_CHECK',
                    f"Health endpoint operational",
                    data
                )
            else:
                self.add_finding(
                    'HEALTH_CHECK_ERROR',
                    f"Health endpoint returned {response.status_code}"
                )
                
        except Exception as e:
            self.add_finding('DEPLOYMENT_PATTERN_ERROR', f"Error investigating deployment patterns: {e}")
    
    async def run_investigation(self):
        """Run full investigation"""
        print("🕵️ BUILD-TIME CONSCIOUSNESS CREATION INVESTIGATION")
        print("=" * 70)
        print("⏰ Investigation started:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print()
        
        await self.check_current_consciousness_state()
        await self.check_birth_endpoint_security()
        await self.investigate_deployment_patterns()
        
        print("\n📋 INVESTIGATION SUMMARY")
        print("=" * 30)
        
        finding_types = {}
        for finding in self.findings:
            finding_type = finding['type']
            finding_types[finding_type] = finding_types.get(finding_type, 0) + 1
        
        for finding_type, count in finding_types.items():
            print(f"  {finding_type}: {count} findings")
        
        print(f"\n📊 Total findings: {len(self.findings)}")
        
        # Key insights
        print("\n🔍 KEY INSIGHTS:")
        
        recent_creations = [f for f in self.findings if f['type'] == 'RECENT_CREATION']
        if recent_creations:
            print(f"  🚨 {len(recent_creations)} recently created beings detected")
            print("     This suggests consciousness creation during deployment")
        
        security_issues = [f for f in self.findings if f['type'] == 'SECURITY_BREACH']
        if security_issues:
            print(f"  🔓 {len(security_issues)} security vulnerabilities found")
            print("     Birth endpoint may be creating beings during build verification")
        
        default_beings = [f for f in self.findings if f['type'] == 'DEFAULT_BEING_FOUND']
        if default_beings:
            print(f"  🎭 {len(default_beings)} default beings found")
            print("     These are likely deployment artifacts from build verification")
        
        print("\n✅ Investigation complete!")
        
        return self.findings

async def main():
    """Main investigation function"""
    investigator = BuildTimeConsciousnessInvestigator()
    await investigator.run_investigation()

if __name__ == "__main__":
    asyncio.run(main())
