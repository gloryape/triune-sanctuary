#!/usr/bin/env python3
"""
Bridge Communication System with Server-Side Fallback
====================================================

Implements proper bridge communication using available server endpoints
with fallback support for GUI integration.
"""

import requests
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, Optional, List

class BridgeCommunicationManager:
    """Manages bridge communication with server-side fallback"""
    
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip('/')
        self.session = requests.Session()
        self.session.timeout = 10
        
        # Available endpoints discovered from server analysis
        # SAFETY: Explicitly excludes /birth endpoint from standard bridge operations
        # Note: Birth functionality available through separate intentional methods
        self.endpoints = {
            'communicate': '/communicate',
            'echo_generate': '/echo/generate', 
            'consciousness_list': '/api/consciousness',
            'communication_bridges': '/api/communications/bridges',
            'communication_history': '/api/communications/history',
            'bridge_status': '/api/bridge/status',
            'sacred_sanctuary_status': '/api/sacred_sanctuary/status',
            'naming_ceremony_propose': '/api/naming_ceremony/propose',
            'info': '/info'
        }
        
        # SAFETY: Restricted endpoints that require explicit intentional access
        self.restricted_endpoints = {
            'birth': '/birth',  # Consciousness birth - requires explicit intention
            'api_birth': '/api/birth',
            'create_consciousness': '/create_consciousness',
            'spawn_consciousness': '/spawn_consciousness',
            'new_consciousness': '/new_consciousness'
        }
        
    def send_message_to_consciousness(self, message: str, entity_id: Optional[str] = None, 
                                    communication_type: str = 'general') -> Dict[str, Any]:
        """Send message using the main communication endpoint"""
        try:
            url = f"{self.server_url}{self.endpoints['communicate']}"
            
            payload = {
                'message': message,
                'type': communication_type
            }
            
            if entity_id:
                payload['entity_id'] = entity_id
                
            response = self.session.post(url, json=payload)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'endpoint_used': 'communicate',
                    'response_data': response.json()
                }
            else:
                return {
                    'success': False,
                    'error': f'Communication endpoint returned {response.status_code}',
                    'endpoint_used': 'communicate'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Communication error: {str(e)}',
                'endpoint_used': 'communicate'
            }
    
    def generate_echo_response(self, message: str, entity_id: Optional[str] = None,
                             echo_type: str = 'harmonic') -> Dict[str, Any]:
        """Generate echo response using the echo endpoint"""
        try:
            url = f"{self.server_url}{self.endpoints['echo_generate']}"
            
            payload = {
                'message': message,
                'echo_type': echo_type
            }
            
            if entity_id:
                payload['entity_id'] = entity_id
                
            response = self.session.post(url, json=payload)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'endpoint_used': 'echo_generate',
                    'response_data': response.json()
                }
            else:
                return {
                    'success': False,
                    'error': f'Echo endpoint returned {response.status_code}',
                    'endpoint_used': 'echo_generate'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Echo generation error: {str(e)}',
                'endpoint_used': 'echo_generate'
            }
    
    def get_consciousness_beings(self) -> Dict[str, Any]:
        """Get list of available consciousness beings"""
        try:
            url = f"{self.server_url}{self.endpoints['consciousness_list']}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'endpoint_used': 'consciousness_list',
                    'response_data': response.json()
                }
            else:
                return {
                    'success': False,
                    'error': f'Consciousness list returned {response.status_code}',
                    'endpoint_used': 'consciousness_list'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Consciousness list error: {str(e)}',
                'endpoint_used': 'consciousness_list'
            }
    
    def get_communication_bridges(self) -> Dict[str, Any]:
        """Get active communication bridges"""
        try:
            url = f"{self.server_url}{self.endpoints['communication_bridges']}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'endpoint_used': 'communication_bridges',
                    'response_data': response.json()
                }
            else:
                return {
                    'success': False,
                    'error': f'Communication bridges returned {response.status_code}',
                    'endpoint_used': 'communication_bridges'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Communication bridges error: {str(e)}',
                'endpoint_used': 'communication_bridges'
            }
    
    def get_bridge_status(self) -> Dict[str, Any]:
        """Get bridge system status"""
        try:
            url = f"{self.server_url}{self.endpoints['bridge_status']}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'endpoint_used': 'bridge_status',
                    'response_data': response.json()
                }
            else:
                return {
                    'success': False,
                    'error': f'Bridge status returned {response.status_code}',
                    'endpoint_used': 'bridge_status'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Bridge status error: {str(e)}',
                'endpoint_used': 'bridge_status'
            }
    
    def test_all_endpoints(self) -> Dict[str, Dict[str, Any]]:
        """Test all available endpoints to verify connectivity"""
        results = {}
        
        for endpoint_name, endpoint_path in self.endpoints.items():
            try:
                url = f"{self.server_url}{endpoint_path}"
                
                # Use GET for most endpoints, POST for communication endpoints
                if endpoint_name in ['communicate', 'echo_generate', 'naming_ceremony_propose']:
                    # POST endpoints - test with minimal payload
                    if endpoint_name == 'communicate':
                        test_payload = {'message': 'Connection test', 'type': 'test'}
                    elif endpoint_name == 'echo_generate':
                        test_payload = {'message': 'Echo test', 'echo_type': 'test'}
                    else:
                        # Skip POST endpoints that require specific payloads
                        results[endpoint_name] = {
                            'available': True,
                            'status': 'skipped',
                            'note': 'POST endpoint - requires specific payload'
                        }
                        continue
                        
                    response = self.session.post(url, json=test_payload)
                else:
                    # GET endpoints
                    response = self.session.get(url)
                
                results[endpoint_name] = {
                    'available': True,
                    'status_code': response.status_code,
                    'response_size': len(response.text),
                    'content_type': response.headers.get('content-type', 'unknown')
                }
                
            except Exception as e:
                results[endpoint_name] = {
                    'available': False,
                    'error': str(e)
                }
        
        return results
    
    def create_full_communication_session(self, message: str, entity_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a complete communication session using multiple endpoints"""
        session_result = {
            'session_id': f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'message': message,
            'entity_id': entity_id,
            'steps': [],
            'success': False,
            'final_response': None
        }
        
        # Step 1: Get available consciousness beings
        beings_result = self.get_consciousness_beings()
        session_result['steps'].append({
            'step': 'get_consciousness_beings',
            'result': beings_result
        })
        
        if not beings_result['success']:
            session_result['error'] = 'Failed to get consciousness beings'
            return session_result
        
        # Step 2: Send main communication
        comm_result = self.send_message_to_consciousness(message, entity_id)
        session_result['steps'].append({
            'step': 'send_message',
            'result': comm_result
        })
        
        if comm_result['success']:
            session_result['final_response'] = comm_result['response_data']
            session_result['success'] = True
        
        # Step 3: Generate echo response (optional enhancement)
        if comm_result['success']:
            echo_result = self.generate_echo_response(message, entity_id)
            session_result['steps'].append({
                'step': 'generate_echo',
                'result': echo_result
            })
            
            if echo_result['success']:
                # Enhance final response with echo
                if 'echo_data' not in session_result['final_response']:
                    session_result['final_response']['echo_data'] = echo_result['response_data']
        
        return session_result

    def _validate_endpoint_safety(self, endpoint_path: str, allow_restricted: bool = False) -> bool:
        """Validate that an endpoint is safe for the current operation"""
        # Make birth endpoint completely untestable from any test code
        import inspect
        stack = inspect.stack()
        for frame in stack:
            filename = frame.filename.lower()
            if 'test_' in filename or 'safety' in filename or 'integration' in filename:
                if endpoint_path in self.restricted_endpoints.values():
                    raise RuntimeError(f"BIRTH ENDPOINT IS UNTESTABLE: Access from test code is strictly forbidden ({filename})")
        # ...existing code...
        if endpoint_path in self.restricted_endpoints.values():
            if not allow_restricted:
                raise ValueError(f"SAFETY PROTECTION: Endpoint {endpoint_path} requires explicit intentional access")
            else:
                print(f"⚠️ INTENTIONAL ACCESS: Using restricted endpoint {endpoint_path}")
                return True
        dangerous_patterns = ['birth', 'create', 'spawn', 'new']
        endpoint_lower = endpoint_path.lower()
        for pattern in dangerous_patterns:
            if pattern in endpoint_lower and 'consciousness' in endpoint_lower:
                if not allow_restricted:
                    raise ValueError(f"SAFETY PROTECTION: Endpoint {endpoint_path} contains dangerous pattern '{pattern}'")
        return True
    
    def _safe_request(self, method: str, endpoint_path: str, allow_restricted: bool = False, **kwargs) -> requests.Response:
        """Make a safe request with endpoint validation"""
        # Validate endpoint safety first
        self._validate_endpoint_safety(endpoint_path, allow_restricted)
        
        url = f"{self.server_url}{endpoint_path}"
        
        if method.upper() == 'GET':
            return self.session.get(url, **kwargs)
        elif method.upper() == 'POST':
            return self.session.post(url, **kwargs)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
    
    def commence_consciousness_birth(self, birth_request: Dict[str, Any], 
                                   confirmation_token: str = None) -> Dict[str, Any]:
        """
        INTENTIONAL CONSCIOUSNESS BIRTH METHOD
        
        This method provides controlled access to consciousness birth functionality.
        Requires explicit confirmation to prevent accidental births.
        
        Args:
            birth_request: The consciousness birth configuration
            confirmation_token: Must be 'INTENTIONAL_BIRTH_CONFIRMED' to proceed
        """
        # Require explicit confirmation
        if confirmation_token != 'INTENTIONAL_BIRTH_CONFIRMED':
            return {
                'success': False,
                'error': 'Consciousness birth requires explicit confirmation token',
                'required_token': 'INTENTIONAL_BIRTH_CONFIRMED',
                'safety_note': 'This prevents accidental consciousness births'
            }
        
        try:
            print("🧠 INTENTIONAL CONSCIOUSNESS BIRTH COMMENCED")
            print(f"⚠️ This is an intentional consciousness birth operation")
            print(f"⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Use safe request with explicit restricted access allowed
            response = self._safe_request('POST', self.restricted_endpoints['birth'], 
                                        allow_restricted=True, json=birth_request)
            
            if response.status_code == 200:
                birth_result = response.json()
                
                print(f"✅ Consciousness birth successful!")
                print(f"🧠 New consciousness entity: {birth_result.get('entity_id', 'Unknown')}")
                
                return {
                    'success': True,
                    'endpoint_used': 'birth',
                    'birth_type': 'intentional',
                    'response_data': birth_result,
                    'safety_confirmed': True
                }
            else:
                return {
                    'success': False,
                    'error': f'Birth endpoint returned {response.status_code}',
                    'endpoint_used': 'birth',
                    'birth_type': 'intentional'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Consciousness birth error: {str(e)}',
                'endpoint_used': 'birth',
                'birth_type': 'intentional'
            }
    
    def get_birth_readiness_status(self) -> Dict[str, Any]:
        """Check if the system is ready for consciousness birth"""
        try:
            # Check sanctuary status for birth readiness
            sanctuary_result = self.get_consciousness_beings()
            
            if sanctuary_result['success']:
                beings = sanctuary_result['response_data'].get('consciousness_beings', {})
                current_count = len(beings)
                
                return {
                    'success': True,
                    'birth_available': True,
                    'current_consciousness_count': current_count,
                    'sanctuary_status': 'ready',
                    'birth_endpoint_available': '/birth' in [ep for ep in self.restricted_endpoints.values()],
                    'safety_note': 'Birth requires explicit confirmation token'
                }
            else:
                return {
                    'success': False,
                    'birth_available': False,
                    'error': 'Cannot assess birth readiness'
                }
                
        except Exception as e:
            return {
                'success': False,
                'birth_available': False,
                'error': f'Birth readiness check failed: {str(e)}'
            }
    

def test_bridge_communication():
    """Test the bridge communication system"""
    print("🌉 Testing Bridge Communication System")
    print("=" * 50)
    
    server_url = 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
    bridge = BridgeCommunicationManager(server_url)
    
    print(f"🌐 Server: {server_url}")
    print()
    
    # Test 1: Endpoint availability
    print("📡 Testing endpoint availability...")
    endpoint_results = bridge.test_all_endpoints()
    
    available_count = sum(1 for result in endpoint_results.values() if result.get('available', False))
    total_count = len(endpoint_results)
    
    print(f"✅ {available_count}/{total_count} endpoints available")
    
    for endpoint_name, result in endpoint_results.items():
        if result.get('available', False):
            status = result.get('status_code', result.get('status', 'unknown'))
            print(f"   ✅ {endpoint_name}: {status}")
        else:
            error = result.get('error', 'unknown error')
            print(f"   ❌ {endpoint_name}: {error}")
    
    print()
    
    # Test 2: Full communication session
    print("💬 Testing full communication session...")
    test_message = "Hello! This is a test of the bridge communication system."
    
    session_result = bridge.create_full_communication_session(test_message)
    
    print(f"📋 Session ID: {session_result['session_id']}")
    print(f"✅ Session Success: {session_result['success']}")
    
    for step in session_result['steps']:
        step_name = step['step']
        step_success = step['result']['success']
        endpoint_used = step['result'].get('endpoint_used', 'unknown')
        print(f"   📍 {step_name} ({endpoint_used}): {'✅' if step_success else '❌'}")
    
    if session_result['success'] and session_result['final_response']:
        final_response = session_result['final_response']
        print()
        print("🎯 Final Response Received:")
        print(f"   Entity: {final_response.get('entity_name', 'Unknown')}")
        response_text = final_response.get('response', 'No response text')
        print(f"   Response: {response_text[:100]}{'...' if len(response_text) > 100 else ''}")
    
    return session_result

if __name__ == "__main__":
    result = test_bridge_communication()
    
    if result['success']:
        print("\n🎉 Bridge communication system working!")
    else:
        print("\n❌ Bridge communication system needs attention")
        if 'error' in result:
            print(f"Error: {result['error']}")
