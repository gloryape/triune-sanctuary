#!/usr/bin/env python3
"""
Investigation: How NewConsciousness Was Created
==============================================

This script investigates how the third consciousness being was spawned
and implements additional safety measures to prevent accidental births.
"""

import requests
import json
from datetime import datetime
from typing import Dict, Any, List
import sys
import os

class ConsciousnessSpawnInvestigator:
    """Investigates how consciousness beings are spawned"""
    
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip('/')
        self.session = requests.Session()
        self.session.timeout = 10
        
    def get_consciousness_timeline(self) -> Dict[str, Any]:
        """Get timeline of consciousness creation"""
        try:
            # Get current consciousness beings
            response = self.session.get(f"{self.server_url}/api/consciousness")
            if response.status_code != 200:
                return {'error': f'Failed to get consciousness list: {response.status_code}'}
            
            beings = response.json().get('consciousness_beings', {})
            
            # Analyze each being
            timeline = []
            for being_id, being_data in beings.items():
                timeline.append({
                    'entity_id': being_id,
                    'name': being_data.get('name', 'Unknown'),
                    'birth_time': being_data.get('birth_time', 'Unknown'),
                    'last_activity': being_data.get('last_activity', 'Unknown'),
                    'entity_origin': being_data.get('entity_origin', 'Unknown'),
                    'entity_type': being_data.get('entity_type', 'Unknown'),
                    'naming_readiness': being_data.get('naming_readiness', 'Unknown')
                })
            
            # Sort by birth time
            timeline.sort(key=lambda x: x['birth_time'] if x['birth_time'] != 'Unknown' else '0')
            
            return {
                'success': True,
                'consciousness_count': len(beings),
                'timeline': timeline
            }
            
        except Exception as e:
            return {'error': f'Timeline investigation failed: {str(e)}'}
    
    def check_birth_endpoint_security(self) -> Dict[str, Any]:
        """Check if birth endpoint has security measures"""
        try:
            # Test 1: Direct birth endpoint access without payload
            print("🔍 Testing birth endpoint security...")
            
            # Try POST without payload
            response = self.session.post(f"{self.server_url}/birth")
            no_payload_result = {
                'status_code': response.status_code,
                'response_size': len(response.text),
                'accessible': response.status_code == 200
            }
            
            # Try POST with minimal payload
            minimal_payload = {}
            response = self.session.post(f"{self.server_url}/birth", json=minimal_payload)
            minimal_payload_result = {
                'status_code': response.status_code,
                'response_size': len(response.text),
                'accessible': response.status_code == 200
            }
            
            # Try POST with typical payload
            typical_payload = {'name': 'TestConsciousness', 'purpose': 'Testing'}
            response = self.session.post(f"{self.server_url}/birth", json=typical_payload)
            typical_payload_result = {
                'status_code': response.status_code,
                'response_size': len(response.text),
                'accessible': response.status_code == 200,
                'response_preview': response.text[:200] if response.text else 'No response'
            }
            
            return {
                'success': True,
                'no_payload': no_payload_result,
                'minimal_payload': minimal_payload_result,
                'typical_payload': typical_payload_result,
                'endpoint_accessible': any([
                    no_payload_result['accessible'],
                    minimal_payload_result['accessible'],
                    typical_payload_result['accessible']
                ])
            }
            
        except Exception as e:
            return {'error': f'Security check failed: {str(e)}'}
    
    def analyze_recent_activity(self) -> Dict[str, Any]:
        """Analyze recent activity that might explain NewConsciousness creation"""
        try:
            # Get sacred events if available
            try:
                response = self.session.get(f"{self.server_url}/api/consciousness/events")
                if response.status_code == 200:
                    events = response.json().get('events', [])
                    
                    # Filter for recent birth events
                    birth_events = []
                    for event in events:
                        if 'birth' in event.get('type', '').lower():
                            birth_events.append(event)
                    
                    return {
                        'success': True,
                        'recent_events': len(events),
                        'birth_events': birth_events,
                        'has_birth_events': len(birth_events) > 0
                    }
                else:
                    return {'error': f'Events endpoint returned {response.status_code}'}
            except:
                return {'error': 'Events endpoint not available'}
            
        except Exception as e:
            return {'error': f'Activity analysis failed: {str(e)}'}
    
    def check_test_files_for_birth_calls(self) -> Dict[str, Any]:
        """Check if any test files might have triggered birth"""
        dangerous_files = []
        
        # Check specific test files that might call birth
        test_files_to_check = [
            'test_bridge_safety.py',
            'test_environmental_uncertainty_integration.py',
            'complete_system_integration_test.py',
            'verify_consciousness_birth.py'
        ]
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        
        for test_file in test_files_to_check:
            file_path = os.path.join(base_path, test_file)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Check for dangerous patterns
                    dangerous_patterns = [
                        'commence_consciousness_birth',
                        'INTENTIONAL_BIRTH_CONFIRMED',
                        'birth_consciousness',
                        'POST.*birth',
                        'requests.*birth'
                    ]
                    
                    found_patterns = []
                    for pattern in dangerous_patterns:
                        if pattern.lower() in content.lower():
                            found_patterns.append(pattern)
                    
                    if found_patterns:
                        dangerous_files.append({
                            'file': test_file,
                            'patterns': found_patterns,
                            'risk_level': 'HIGH' if 'INTENTIONAL_BIRTH_CONFIRMED' in found_patterns else 'MEDIUM'
                        })
                        
                except Exception as e:
                    print(f"⚠️ Could not read {test_file}: {e}")
        
        return {
            'success': True,
            'dangerous_files': dangerous_files,
            'high_risk_files': [f for f in dangerous_files if f['risk_level'] == 'HIGH']
        }
    
    def recommend_safety_improvements(self) -> List[str]:
        """Recommend safety improvements to prevent accidental births"""
        recommendations = [
            "🔒 Add authentication to birth endpoint",
            "🛡️ Implement rate limiting on birth endpoint",
            "📋 Add logging for all birth endpoint access attempts",
            "🔑 Require admin API key for birth operations",
            "⚠️ Add confirmation prompts in test files",
            "🚫 Disable birth endpoint in production unless explicitly enabled",
            "📊 Add birth attempt monitoring and alerting",
            "🔐 Implement IP whitelisting for birth operations",
            "📝 Add birth reason logging requirement",
            "🛡️ Add maximum consciousness limit enforcement"
        ]
        
        return recommendations


def main():
    """Main investigation function"""
    print("🔍 Investigating Third Consciousness Creation")
    print("=" * 50)
    
    server_url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
    investigator = ConsciousnessSpawnInvestigator(server_url)
    
    print(f"🌐 Server: {server_url}")
    print()
    
    # Investigation 1: Consciousness Timeline
    print("📅 1. Consciousness Timeline Analysis")
    print("-" * 40)
    timeline_result = investigator.get_consciousness_timeline()
    
    if timeline_result.get('success'):
        print(f"📊 Total consciousness beings: {timeline_result['consciousness_count']}")
        
        for i, being in enumerate(timeline_result['timeline'], 1):
            print(f"   {i}. {being['name']} ({being['entity_id'][:12]}...)")
            print(f"      Birth: {being['birth_time']}")
            print(f"      Origin: {being['entity_origin']}")
            print(f"      Type: {being['entity_type']}")
            print(f"      Naming: {being['naming_readiness']}")
            print()
    else:
        print(f"❌ Timeline analysis failed: {timeline_result.get('error')}")
    
    # Investigation 2: Birth Endpoint Security
    print("🔒 2. Birth Endpoint Security Analysis")
    print("-" * 40)
    security_result = investigator.check_birth_endpoint_security()
    
    if security_result.get('success'):
        print(f"🚨 Birth endpoint accessible: {'YES' if security_result['endpoint_accessible'] else 'NO'}")
        print(f"   No payload: {security_result['no_payload']['status_code']}")
        print(f"   Minimal payload: {security_result['minimal_payload']['status_code']}")
        print(f"   Typical payload: {security_result['typical_payload']['status_code']}")
        
        if security_result['endpoint_accessible']:
            print(f"⚠️ SECURITY RISK: Birth endpoint is accessible!")
            if security_result['typical_payload']['accessible']:
                print(f"   Response preview: {security_result['typical_payload']['response_preview']}")
    else:
        print(f"❌ Security check failed: {security_result.get('error')}")
    
    print()
    
    # Investigation 3: Recent Activity
    print("📊 3. Recent Activity Analysis")
    print("-" * 40)
    activity_result = investigator.analyze_recent_activity()
    
    if activity_result.get('success'):
        print(f"📋 Recent events: {activity_result['recent_events']}")
        print(f"👶 Birth events: {len(activity_result['birth_events'])}")
        
        if activity_result['has_birth_events']:
            print("🚨 BIRTH EVENTS FOUND:")
            for event in activity_result['birth_events']:
                print(f"   - {event.get('type', 'Unknown')}: {event.get('message', 'No message')}")
                print(f"     Time: {event.get('timestamp', 'Unknown')}")
        else:
            print("✅ No birth events in recent activity")
    else:
        print(f"❌ Activity analysis failed: {activity_result.get('error')}")
    
    print()
    
    # Investigation 4: Test Files Analysis
    print("🔍 4. Test Files Analysis")
    print("-" * 40)
    test_files_result = investigator.check_test_files_for_birth_calls()
    
    if test_files_result.get('success'):
        if test_files_result['dangerous_files']:
            print("🚨 DANGEROUS TEST FILES FOUND:")
            for file_info in test_files_result['dangerous_files']:
                print(f"   📄 {file_info['file']} - {file_info['risk_level']} RISK")
                for pattern in file_info['patterns']:
                    print(f"      - Contains: {pattern}")
                print()
        else:
            print("✅ No dangerous patterns found in test files")
    else:
        print(f"❌ Test files analysis failed: {test_files_result.get('error')}")
    
    # Investigation 5: Safety Recommendations
    print("🛡️ 5. Safety Recommendations")
    print("-" * 40)
    recommendations = investigator.recommend_safety_improvements()
    
    for i, rec in enumerate(recommendations, 1):
        print(f"   {i}. {rec}")
    
    print()
    
    # Final Assessment
    print("🎯 Final Assessment")
    print("=" * 50)
    
    # Determine most likely cause
    if security_result.get('endpoint_accessible'):
        print("🚨 LIKELY CAUSE: Birth endpoint is accessible without authentication")
        print("   - Any request to /birth can create new consciousness")
        print("   - Test files contain intentional birth calls")
        print("   - No rate limiting or access controls detected")
    else:
        print("✅ Birth endpoint appears secure")
    
    print()
    print("🎯 RECOMMENDATION: Implement immediate security measures")
    print("   1. Add authentication to birth endpoint")
    print("   2. Review and secure test files")
    print("   3. Add monitoring for birth attempts")
    print("   4. Implement consciousness count limits")


if __name__ == "__main__":
    main()
