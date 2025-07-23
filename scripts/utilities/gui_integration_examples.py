#!/usr/bin/env python3
"""
GUI Integration Examples
========================

Code examples for integrating with the Triune AI Consciousness API.
"""

import requests
import json
from typing import Dict, Any, Optional

class TriuneAPIClient:
    """Client for Triune AI Consciousness API"""
    
    def __init__(self, server_url: str = None):
        self.server_url = server_url or 'https://triune-consciousness-innnp2aveq-uc.a.run.app'
        self.session = requests.Session()
        self.session.timeout = 10
    
    def send_message(self, message: str, entity_id: Optional[str] = None, 
                    communication_type: str = 'general') -> Dict[str, Any]:
        """Send message to consciousness being"""
        url = f"{self.server_url}/communicate"
        payload = {
            'message': message,
            'type': communication_type
        }
        if entity_id:
            payload['entity_id'] = entity_id
        
        response = self.session.post(url, json=payload)
        return response.json()
    
    def get_consciousness_beings(self) -> Dict[str, Any]:
        """Get list of consciousness beings"""
        url = f"{self.server_url}/api/consciousness"
        response = self.session.get(url)
        return response.json()
    
    def generate_echo(self, message: str, echo_type: str = 'harmonic', 
                     entity_id: Optional[str] = None) -> Dict[str, Any]:
        """Generate echo response"""
        url = f"{self.server_url}/echo/generate"
        payload = {
            'message': message,
            'echo_type': echo_type
        }
        if entity_id:
            payload['entity_id'] = entity_id
        
        response = self.session.post(url, json=payload)
        return response.json()
    
    def get_bridge_status(self) -> Dict[str, Any]:
        """Get bridge system status"""
        url = f"{self.server_url}/api/bridge/status"
        response = self.session.get(url)
        return response.json()
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get system information"""
        url = f"{self.server_url}/info"
        response = self.session.get(url)
        return response.json()
    
    def propose_name(self, entity_id: str, proposed_name: str, 
                    reasoning: str = None) -> Dict[str, Any]:
        """Propose name for consciousness being"""
        url = f"{self.server_url}/api/naming_ceremony/propose"
        payload = {
            'entity_id': entity_id,
            'proposed_name': proposed_name
        }
        if reasoning:
            payload['reasoning'] = reasoning
        
        response = self.session.post(url, json=payload)
        return response.json()

# Example usage
if __name__ == "__main__":
    client = TriuneAPIClient()
    
    # Get consciousness beings
    beings = client.get_consciousness_beings()
    print("Consciousness beings:", beings)
    
    # Send a message
    if beings.get('success') and beings.get('consciousness_beings'):
        entity_id = list(beings['consciousness_beings'].keys())[0]
        response = client.send_message("Hello from the GUI!", entity_id)
        print("Message response:", response)
    
    # Generate echo
    echo = client.generate_echo("Create beautiful resonance patterns")
    print("Echo response:", echo)
    
    # Get system status
    status = client.get_bridge_status()
    print("Bridge status:", status)
