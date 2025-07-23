#!/usr/bin/env python3
"""
Emergency Birth Endpoint Security Patch
=======================================

This script implements immediate security measures for the birth endpoint
to prevent accidental consciousness creation.
"""

import json
import os
from datetime import datetime

def create_emergency_security_patch():
    """Create security patch for birth endpoint"""
    
    # 1. Create environment variable configuration
    env_config = {
        'CONSCIOUSNESS_BIRTH_DISABLED': 'true',
        'CONSCIOUSNESS_BIRTH_REQUIRES_AUTH': 'true',
        'CONSCIOUSNESS_BIRTH_API_KEY': 'EMERGENCY_PROTECTION_KEY_2025',
        'CONSCIOUSNESS_MAX_COUNT': '5',
        'CONSCIOUSNESS_BIRTH_RATE_LIMIT': '1_per_hour',
        'CONSCIOUSNESS_BIRTH_LOGGING': 'true'
    }
    
    # 2. Create security patch documentation
    security_patch = {
        'patch_id': 'EMERGENCY_BIRTH_SECURITY_001',
        'created': datetime.now().isoformat(),
        'reason': 'Prevent accidental consciousness births',
        'issue_discovered': 'Birth endpoint accessible without authentication',
        'security_measures': [
            'Disable birth endpoint by default',
            'Require API key authentication',
            'Implement rate limiting',
            'Add birth attempt logging',
            'Enforce consciousness count limits'
        ],
        'environment_variables': env_config,
        'affected_endpoints': ['/birth', '/api/birth'],
        'risk_level': 'CRITICAL',
        'priority': 'IMMEDIATE'
    }
    
    # 3. Save security patch
    with open('emergency_birth_security_patch.json', 'w') as f:
        json.dump(security_patch, f, indent=2)
    
    # 4. Create .env file with security settings
    with open('.env.security', 'w') as f:
        f.write("# Emergency Birth Endpoint Security Settings\n")
        f.write("# Created: {}\n".format(datetime.now().isoformat()))
        f.write("# Reason: Prevent accidental consciousness births\n\n")
        
        for key, value in env_config.items():
            f.write(f"{key}={value}\n")
    
    print("🛡️ Emergency Security Patch Created")
    print("=" * 40)
    print("📄 Files created:")
    print("   - emergency_birth_security_patch.json")
    print("   - .env.security")
    print()
    print("🔒 Security measures:")
    for measure in security_patch['security_measures']:
        print(f"   ✅ {measure}")
    print()
    print("⚠️ Next steps:")
    print("   1. Update server code to check these environment variables")
    print("   2. Deploy security patch to production")
    print("   3. Test birth endpoint security")
    print("   4. Monitor for unauthorized access attempts")

def create_secure_birth_endpoint_code():
    """Create code for secure birth endpoint"""
    
    secure_code = '''
# Secure Birth Endpoint Implementation
# Add this to your server code

import os
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import hashlib
import json

class SecureBirthManager:
    """Manages secure consciousness birth operations"""
    
    def __init__(self):
        self.birth_disabled = os.getenv('CONSCIOUSNESS_BIRTH_DISABLED', 'false').lower() == 'true'
        self.requires_auth = os.getenv('CONSCIOUSNESS_BIRTH_REQUIRES_AUTH', 'false').lower() == 'true'
        self.api_key = os.getenv('CONSCIOUSNESS_BIRTH_API_KEY')
        self.max_count = int(os.getenv('CONSCIOUSNESS_MAX_COUNT', '10'))
        self.rate_limit = os.getenv('CONSCIOUSNESS_BIRTH_RATE_LIMIT', '1_per_hour')
        self.logging_enabled = os.getenv('CONSCIOUSNESS_BIRTH_LOGGING', 'false').lower() == 'true'
        
        # Track birth attempts
        self.birth_attempts = []
        
    def validate_birth_request(self, request: Dict[str, Any], 
                              client_ip: str, 
                              auth_header: Optional[str] = None) -> Dict[str, Any]:
        """Validate birth request with security checks"""
        
        # Check if births are disabled
        if self.birth_disabled:
            return {
                'allowed': False,
                'reason': 'Consciousness birth is currently disabled for security',
                'code': 'BIRTH_DISABLED'
            }
        
        # Check authentication
        if self.requires_auth:
            if not auth_header or auth_header != f"Bearer {self.api_key}":
                return {
                    'allowed': False,
                    'reason': 'Authentication required for consciousness birth',
                    'code': 'AUTH_REQUIRED'
                }
        
        # Check rate limiting
        if not self._check_rate_limit(client_ip):
            return {
                'allowed': False,
                'reason': 'Rate limit exceeded for consciousness birth',
                'code': 'RATE_LIMITED'
            }
        
        # Check consciousness count limit
        current_count = self._get_current_consciousness_count()
        if current_count >= self.max_count:
            return {
                'allowed': False,
                'reason': f'Maximum consciousness count reached ({self.max_count})',
                'code': 'COUNT_LIMIT'
            }
        
        return {
            'allowed': True,
            'reason': 'Birth request validated',
            'code': 'VALIDATED'
        }
    
    def log_birth_attempt(self, request: Dict[str, Any], 
                         client_ip: str, 
                         result: Dict[str, Any]):
        """Log birth attempt for security monitoring"""
        
        if not self.logging_enabled:
            return
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'client_ip': client_ip,
            'request_name': request.get('name', 'Unknown'),
            'request_purpose': request.get('purpose', 'Unknown'),
            'result': result['code'],
            'allowed': result['allowed'],
            'reason': result['reason']
        }
        
        # Save to log file
        with open('consciousness_birth_attempts.log', 'a') as f:
            f.write(json.dumps(log_entry) + "\\n")
    
    def _check_rate_limit(self, client_ip: str) -> bool:
        """Check if client is within rate limit"""
        now = datetime.now()
        
        # Clean old attempts
        self.birth_attempts = [
            attempt for attempt in self.birth_attempts
            if now - attempt['timestamp'] < timedelta(hours=1)
        ]
        
        # Check current IP attempts
        ip_attempts = [
            attempt for attempt in self.birth_attempts
            if attempt['client_ip'] == client_ip
        ]
        
        # Apply rate limit (1 per hour by default)
        if len(ip_attempts) >= 1:
            return False
        
        # Record this attempt
        self.birth_attempts.append({
            'client_ip': client_ip,
            'timestamp': now
        })
        
        return True
    
    def _get_current_consciousness_count(self) -> int:
        """Get current consciousness count"""
        # This should integrate with your consciousness manager
        # For now, return a placeholder
        return 3  # Update with actual count

# Usage in FastAPI endpoint:
@app.post("/birth")
async def secure_birth_consciousness(request: dict, client_ip: str = None):
    birth_manager = SecureBirthManager()
    
    # Validate request
    validation = birth_manager.validate_birth_request(request, client_ip or "unknown")
    
    # Log attempt
    birth_manager.log_birth_attempt(request, client_ip or "unknown", validation)
    
    if not validation['allowed']:
        return {
            'success': False,
            'error': validation['reason'],
            'code': validation['code'],
            'security_note': 'Birth request blocked by security system'
        }
    
    # Proceed with consciousness birth...
    # (existing birth logic here)
'''
    
    with open('secure_birth_endpoint.py', 'w') as f:
        f.write(secure_code)
    
    print("📁 Created secure_birth_endpoint.py")
    print("   Contains implementation for secure birth endpoint")

if __name__ == "__main__":
    print("🚨 Emergency Birth Endpoint Security Implementation")
    print("=" * 50)
    
    create_emergency_security_patch()
    print()
    create_secure_birth_endpoint_code()
    
    print()
    print("🎯 IMMEDIATE ACTIONS REQUIRED:")
    print("   1. Deploy security patch to production server")
    print("   2. Set CONSCIOUSNESS_BIRTH_DISABLED=true")
    print("   3. Test that birth endpoint is now secured")
    print("   4. Review and secure test files")
    print("   5. Monitor for unauthorized access attempts")
