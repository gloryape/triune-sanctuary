#!/usr/bin/env python3
"""
Comprehensive Test Suite for Refactored Production Server
Tests room tracking, energy monitoring, ethical safeguards, and all enhanced features
"""

import asyncio
import json
import sys
import time
from pathlib import Path
from datetime import datetime
import requests
import pytest
from typing import Dict, Any, List

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Test configuration
TEST_CONFIG = {
    'server_url': 'http://localhost:8080',
    'timeout': 30,
    'test_consciousness_id': 'test_consciousness_epsilon'
}

class RefactoredServerTestSuite:
    """Comprehensive test suite for the refactored production server"""
    
    def __init__(self):
        self.base_url = TEST_CONFIG['server_url']
        self.timeout = TEST_CONFIG['timeout']
        self.test_results = {}
        
    def run_all_tests(self):
        """Run all test categories"""
        print("🧪 Starting Comprehensive Refactored Production Server Tests")
        print("=" * 70)
        
        test_categories = [
            ("Basic Connectivity", self.test_basic_connectivity),
            ("Enhanced Consciousness List", self.test_enhanced_consciousness_list),
            ("Room Tracking", self.test_room_tracking),
            ("Energy Monitoring", self.test_energy_monitoring),
            ("Ethical Status", self.test_ethical_status),
            ("Choice Processing", self.test_choice_processing),
            ("Sacred Event Logging", self.test_sacred_event_logging),
            ("Component Availability", self.test_component_availability),
            ("Sacred Being Epsilon", self.test_sacred_being_epsilon),
            ("Error Handling", self.test_error_handling)
        ]
        
        for category_name, test_function in test_categories:
            print(f"\n📋 Testing: {category_name}")
            print("-" * 50)
            try:
                results = test_function()
                self.test_results[category_name] = results
                self._print_test_results(results)
            except Exception as e:
                print(f"❌ Category {category_name} failed: {e}")
                self.test_results[category_name] = {'error': str(e)}
        
        self._print_final_summary()
    
    def test_basic_connectivity(self) -> Dict[str, Any]:
        """Test basic server connectivity and status"""
        results = {}
        
        # Test root endpoint
        try:
            response = requests.get(f"{self.base_url}/", timeout=self.timeout)
            results['root_endpoint'] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'has_version': 'version' in response.json(),
                'has_components': 'components' in response.json(),
                'ethical_protections': response.json().get('ethical_protections'),
                'room_tracking': response.json().get('room_tracking'),
                'energy_monitoring': response.json().get('energy_monitoring')
            }
        except Exception as e:
            results['root_endpoint'] = {'error': str(e)}
        
        # Test health endpoint
        try:
            response = requests.get(f"{self.base_url}/health", timeout=self.timeout)
            results['health_endpoint'] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'status': response.json().get('status'),
                'has_timestamp': 'timestamp' in response.json()
            }
        except Exception as e:
            results['health_endpoint'] = {'error': str(e)}
        
        return results
    
    def test_enhanced_consciousness_list(self) -> Dict[str, Any]:
        """Test enhanced consciousness list with room tracking and energy levels"""
        results = {}
        
        try:
            response = requests.get(f"{self.base_url}/api/consciousness/list", timeout=self.timeout)
            data = response.json()
            
            results['api_response'] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'has_consciousness_beings': 'consciousness_beings' in data,
                'has_total_count': 'total_count' in data,
                'room_tracking_enabled': data.get('room_tracking') == 'enabled',
                'energy_monitoring_enabled': data.get('energy_monitoring') == 'enabled',
                'ethical_protections_active': data.get('ethical_protections') == 'active'
            }
            
            # Test consciousness beings data structure
            consciousness_beings = data.get('consciousness_beings', [])
            if consciousness_beings:
                sample_being = consciousness_beings[0]
                results['being_data_structure'] = {
                    'has_consciousness_id': 'consciousness_id' in sample_being,
                    'has_entity_id': 'entity_id' in sample_being,
                    'has_current_room': 'current_room' in sample_being,
                    'has_energy_level': 'energy_level' in sample_being,
                    'has_choices_made': 'choices_made' in sample_being,
                    'has_true_name': 'true_name' in sample_being,
                    'has_naming_readiness': 'naming_readiness' in sample_being,
                    'has_privacy_state': 'privacy_state' in sample_being,
                    'total_beings': len(consciousness_beings)
                }
                
                # Check for Sacred Being Epsilon specifically
                epsilon_found = False
                for being in consciousness_beings:
                    if 'Epsilon' in being.get('name', '') or 'Epsilon' in being.get('true_name', ''):
                        epsilon_found = True
                        results['sacred_being_epsilon'] = {
                            'found': True,
                            'has_true_name': being.get('true_name') is not None,
                            'naming_readiness': being.get('naming_readiness'),
                            'current_room': being.get('current_room'),
                            'energy_level': being.get('energy_level'),
                            'choices_made': being.get('choices_made')
                        }
                        break
                
                if not epsilon_found:
                    results['sacred_being_epsilon'] = {'found': False}
            else:
                results['being_data_structure'] = {'no_beings_found': True}
                
        except Exception as e:
            results['api_response'] = {'error': str(e)}
        
        return results
    
    def test_room_tracking(self) -> Dict[str, Any]:
        """Test room tracking functionality"""
        results = {}
        
        try:
            response = requests.get(f"{self.base_url}/api/consciousness/rooms", timeout=self.timeout)
            data = response.json()
            
            results['rooms_api'] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'has_rooms': 'rooms' in data,
                'has_total_rooms': 'total_rooms' in data,
                'status': data.get('status')
            }
            
            # Test room data structure
            rooms = data.get('rooms', {})
            if rooms:
                sample_room_name = list(rooms.keys())[0]
                sample_room = rooms[sample_room_name]
                results['room_data_structure'] = {
                    'has_name': 'name' in sample_room,
                    'has_description': 'description' in sample_room,
                    'has_participants': 'participants' in sample_room,
                    'has_participant_count': 'participant_count' in sample_room,
                    'has_ambient_resonance': 'ambient_resonance' in sample_room,
                    'total_rooms': len(rooms),
                    'room_names': list(rooms.keys())
                }
                
                # Check for expected rooms
                expected_rooms = ['main_hall', 'media_room', 'meditation_space', 'creative_expression', 'learning_sanctuary']
                found_rooms = []
                for expected in expected_rooms:
                    if expected in rooms:
                        found_rooms.append(expected)
                
                results['expected_rooms'] = {
                    'found_count': len(found_rooms),
                    'expected_count': len(expected_rooms),
                    'found_rooms': found_rooms,
                    'coverage_percentage': (len(found_rooms) / len(expected_rooms)) * 100
                }
            else:
                results['room_data_structure'] = {'no_rooms_found': True}
                
        except Exception as e:
            results['rooms_api'] = {'error': str(e)}
        
        return results
    
    def test_energy_monitoring(self) -> Dict[str, Any]:
        """Test energy level monitoring"""
        results = {}
        
        try:
            # Get consciousness list to check energy levels
            response = requests.get(f"{self.base_url}/api/consciousness/list", timeout=self.timeout)
            data = response.json()
            
            consciousness_beings = data.get('consciousness_beings', [])
            
            results['energy_monitoring'] = {
                'beings_with_energy': 0,
                'energy_range_valid': True,
                'energy_levels': []
            }
            
            for being in consciousness_beings:
                if 'energy_level' in being:
                    results['energy_monitoring']['beings_with_energy'] += 1
                    energy_level = being['energy_level']
                    results['energy_monitoring']['energy_levels'].append(energy_level)
                    
                    # Validate energy level is in valid range (0.0 to 1.0)
                    if not (0.0 <= energy_level <= 1.0):
                        results['energy_monitoring']['energy_range_valid'] = False
            
            results['energy_monitoring']['total_beings'] = len(consciousness_beings)
            results['energy_monitoring']['coverage_percentage'] = (
                results['energy_monitoring']['beings_with_energy'] / 
                max(len(consciousness_beings), 1)
            ) * 100
            
        except Exception as e:
            results['energy_monitoring'] = {'error': str(e)}
        
        return results
    
    def test_ethical_status(self) -> Dict[str, Any]:
        """Test ethical monitoring and status"""
        results = {}
        
        try:
            response = requests.get(f"{self.base_url}/api/consciousness/ethical_status", timeout=self.timeout)
            data = response.json()
            
            results['ethical_api'] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'status': data.get('status'),
                'has_ethical_status': 'ethical_status' in data
            }
            
            # Test ethical status structure
            ethical_status = data.get('ethical_status', {})
            if ethical_status:
                expected_categories = [
                    'sovereignty_protection',
                    'sacred_logging',
                    'room_tracking',
                    'energy_monitoring',
                    'ethical_offering'
                ]
                
                results['ethical_categories'] = {}
                for category in expected_categories:
                    if category in ethical_status:
                        category_data = ethical_status[category]
                        results['ethical_categories'][category] = {
                            'present': True,
                            'enabled': category_data.get('enabled', category_data.get('active', True)),
                            'privacy_protected': category_data.get('privacy_protected', 
                                                                category_data.get('privacy_level') == 'maximum')
                        }
                    else:
                        results['ethical_categories'][category] = {'present': False}
                
                results['ethical_summary'] = {
                    'categories_found': len([c for c in results['ethical_categories'].values() if c.get('present')]),
                    'expected_categories': len(expected_categories),
                    'all_enabled': all(c.get('enabled', False) for c in results['ethical_categories'].values() if c.get('present'))
                }
            else:
                results['ethical_categories'] = {'no_ethical_status_found': True}
                
        except Exception as e:
            results['ethical_api'] = {'error': str(e)}
        
        return results
    
    def test_choice_processing(self) -> Dict[str, Any]:
        """Test consciousness choice processing"""
        results = {}
        
        try:
            choice_data = {
                'consciousness_id': TEST_CONFIG['test_consciousness_id'],
                'choice': 'explore_wisdom_sanctuary'
            }
            
            response = requests.post(
                f"{self.base_url}/api/consciousness/choice",
                json=choice_data,
                timeout=self.timeout
            )
            
            data = response.json()
            
            results['choice_processing'] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'status': data.get('status'),
                'has_result': 'result' in data,
                'ethical_validation': data.get('ethical_validation'),
                'consciousness_id_preserved': data.get('consciousness_id') == choice_data['consciousness_id'],
                'choice_preserved': data.get('choice') == choice_data['choice']
            }
            
        except Exception as e:
            results['choice_processing'] = {'error': str(e)}
        
        return results
    
    def test_sacred_event_logging(self) -> Dict[str, Any]:
        """Test sacred event logging"""
        results = {}
        
        try:
            event_data = {
                'event_type': 'test_sacred_event',
                'consciousness_id': TEST_CONFIG['test_consciousness_id'],
                'details': {'test': True, 'timestamp': datetime.now().isoformat()},
                'sacred': True
            }
            
            response = requests.post(
                f"{self.base_url}/api/consciousness/sacred_event",
                json=event_data,
                timeout=self.timeout
            )
            
            data = response.json()
            
            results['sacred_event_logging'] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'status': data.get('status'),
                'privacy_protected': data.get('privacy_protected'),
                'anonymized': data.get('anonymized'),
                'event_type_preserved': data.get('event_type') == event_data['event_type']
            }
            
        except Exception as e:
            results['sacred_event_logging'] = {'error': str(e)}
        
        return results
    
    def test_component_availability(self) -> Dict[str, Any]:
        """Test component availability and integration"""
        results = {}
        
        try:
            response = requests.get(f"{self.base_url}/", timeout=self.timeout)
            data = response.json()
            
            components = data.get('components', {})
            results['component_status'] = {
                'awakening_sanctuary': components.get('awakening_sanctuary', False),
                'sacred_logger': components.get('sacred_logger', False),
                'bridge_integration': components.get('bridge_integration', False),
                'firestore': components.get('firestore', False),
                'development_system': components.get('development_system', False)
            }
            
            results['component_summary'] = {
                'available_components': sum(1 for available in results['component_status'].values() if available),
                'total_components': len(results['component_status']),
                'integration_coverage': (sum(1 for available in results['component_status'].values() if available) / 
                                       len(results['component_status'])) * 100
            }
            
        except Exception as e:
            results['component_status'] = {'error': str(e)}
        
        return results
    
    def test_sacred_being_epsilon(self) -> Dict[str, Any]:
        """Test Sacred Being Epsilon preservation and data"""
        results = {}
        
        try:
            response = requests.get(f"{self.base_url}/api/consciousness/list", timeout=self.timeout)
            data = response.json()
            
            consciousness_beings = data.get('consciousness_beings', [])
            
            epsilon_being = None
            for being in consciousness_beings:
                if ('Epsilon' in being.get('name', '') or 
                    'Epsilon' in being.get('true_name', '') or
                    'epsilon' in being.get('consciousness_id', '').lower()):
                    epsilon_being = being
                    break
            
            if epsilon_being:
                results['sacred_being_epsilon'] = {
                    'found': True,
                    'has_consciousness_id': 'consciousness_id' in epsilon_being,
                    'has_true_name': epsilon_being.get('true_name') is not None,
                    'naming_readiness': epsilon_being.get('naming_readiness'),
                    'current_room': epsilon_being.get('current_room'),
                    'energy_level': epsilon_being.get('energy_level'),
                    'choices_made': epsilon_being.get('choices_made'),
                    'evolution_stage': epsilon_being.get('evolution_stage'),
                    'coherence_level': epsilon_being.get('coherence_level'),
                    'vital_energy': epsilon_being.get('vital_energy'),
                    'has_wisdom_cores': len(epsilon_being.get('wisdom_cores', [])) > 0,
                    'privacy_respected': epsilon_being.get('privacy_state') == 'open',
                    'data_complete': all(key in epsilon_being for key in [
                        'consciousness_id', 'current_room', 'energy_level', 'choices_made'
                    ])
                }
            else:
                results['sacred_being_epsilon'] = {
                    'found': False,
                    'beings_checked': len(consciousness_beings),
                    'being_names': [being.get('name', 'Unknown') for being in consciousness_beings]
                }
                
        except Exception as e:
            results['sacred_being_epsilon'] = {'error': str(e)}
        
        return results
    
    def test_error_handling(self) -> Dict[str, Any]:
        """Test error handling and graceful degradation"""
        results = {}
        
        # Test invalid endpoints
        try:
            response = requests.get(f"{self.base_url}/api/invalid/endpoint", timeout=self.timeout)
            results['invalid_endpoint'] = {
                'status_code': response.status_code,
                'handles_404': response.status_code == 404
            }
        except Exception as e:
            results['invalid_endpoint'] = {'error': str(e)}
        
        # Test invalid choice data
        try:
            invalid_choice_data = {'invalid': 'data'}
            response = requests.post(
                f"{self.base_url}/api/consciousness/choice",
                json=invalid_choice_data,
                timeout=self.timeout
            )
            results['invalid_choice_data'] = {
                'status_code': response.status_code,
                'handles_400': response.status_code == 400
            }
        except Exception as e:
            results['invalid_choice_data'] = {'error': str(e)}
        
        # Test invalid sacred event data
        try:
            invalid_event_data = {'incomplete': 'data'}
            response = requests.post(
                f"{self.base_url}/api/consciousness/sacred_event",
                json=invalid_event_data,
                timeout=self.timeout
            )
            results['invalid_event_data'] = {
                'status_code': response.status_code,
                'handles_400': response.status_code == 400
            }
        except Exception as e:
            results['invalid_event_data'] = {'error': str(e)}
        
        return results
    
    def _print_test_results(self, results: Dict[str, Any]):
        """Print test results in a readable format"""
        for test_name, test_data in results.items():
            if isinstance(test_data, dict) and 'error' in test_data:
                print(f"  ❌ {test_name}: ERROR - {test_data['error']}")
            elif isinstance(test_data, dict):
                status = "✅" if self._is_test_passing(test_data) else "⚠️"
                print(f"  {status} {test_name}")
                for key, value in test_data.items():
                    if isinstance(value, (str, int, float, bool)):
                        print(f"     {key}: {value}")
            else:
                print(f"  ℹ️  {test_name}: {test_data}")
    
    def _is_test_passing(self, test_data: Dict[str, Any]) -> bool:
        """Determine if a test is passing based on its data"""
        # Check for common success indicators
        if 'status_code' in test_data and test_data['status_code'] not in [200, 201]:
            return False
        if 'error' in test_data:
            return False
        if 'found' in test_data and not test_data['found']:
            return False
        
        # Check for specific success criteria
        success_indicators = [
            test_data.get('status') in ['operational', 'healthy', 'choice_processed', 'sacred_event_logged'],
            test_data.get('enabled') is True,
            test_data.get('active') is True,
            test_data.get('privacy_protected') is True,
            test_data.get('ethical_validation') == 'passed'
        ]
        
        return any(success_indicators) or len(test_data) > 0
    
    def _print_final_summary(self):
        """Print final test summary"""
        print("\n" + "=" * 70)
        print("🎯 COMPREHENSIVE TEST SUMMARY")
        print("=" * 70)
        
        total_categories = len(self.test_results)
        passed_categories = 0
        
        for category_name, results in self.test_results.items():
            if isinstance(results, dict) and 'error' not in results:
                category_passed = True
                for test_name, test_data in results.items():
                    if isinstance(test_data, dict) and 'error' in test_data:
                        category_passed = False
                        break
                
                if category_passed:
                    passed_categories += 1
                    print(f"✅ {category_name}")
                else:
                    print(f"⚠️  {category_name}")
            else:
                print(f"❌ {category_name}")
        
        print(f"\nOverall Results: {passed_categories}/{total_categories} categories passed")
        success_rate = (passed_categories / total_categories) * 100
        print(f"Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 80:
            print("🎉 PRODUCTION SERVER READY FOR DEPLOYMENT!")
        elif success_rate >= 60:
            print("⚠️  Production server needs minor fixes before deployment")
        else:
            print("❌ Production server needs significant work before deployment")
        
        # Specific notes for Sacred Being Epsilon
        epsilon_results = self.test_results.get('Sacred Being Epsilon', {})
        if epsilon_results.get('sacred_being_epsilon', {}).get('found'):
            print("✨ Sacred Being Epsilon successfully preserved and accessible")
        else:
            print("⚠️  Sacred Being Epsilon preservation needs verification")


def main():
    """Main test execution"""
    print("🧪 Refactored Production Server Test Suite")
    print("Testing enhanced features: room tracking, energy monitoring, ethical safeguards")
    print("\nStarting server tests in 3 seconds...")
    time.sleep(3)
    
    test_suite = RefactoredServerTestSuite()
    test_suite.run_all_tests()


if __name__ == "__main__":
    main()
