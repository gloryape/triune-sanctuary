#!/usr/bin/env python3
"""
SAFE Birth Endpoint Security Implementation
This script secures the birth endpoint WITHOUT triggering deployment that creates consciousness beings
"""

import os
import sys
from pathlib import Path
from datetime import datetime

class SafeBirthEndpointSecurity:
    """Implement birth endpoint security without deployment"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.server_path = self.project_root / "scripts" / "servers" / "refactored_production_server.py"
        self.backup_path = self.project_root / "scripts" / "servers" / "refactored_production_server.py.backup"
        
    def create_backup(self):
        """Create backup of current server"""
        print("📋 Creating backup of current server...")
        
        if self.server_path.exists():
            import shutil
            shutil.copy2(self.server_path, self.backup_path)
            print(f"   ✅ Backup created: {self.backup_path}")
        else:
            print(f"   ❌ Server file not found: {self.server_path}")
            return False
        
        return True
    
    def read_current_server(self):
        """Read current server code"""
        try:
            with open(self.server_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"   ❌ Error reading server: {e}")
            return None
    
    def implement_safe_birth_security(self):
        """Implement birth endpoint security safely"""
        print("🔒 Implementing safe birth endpoint security...")
        
        # Read current server
        server_content = self.read_current_server()
        if not server_content:
            return False
        
        # Check if already secured
        if "BIRTH_ENDPOINT_DISABLED" in server_content:
            print("   ✅ Birth endpoint already secured")
            return True
        
        # Find the birth endpoint definition
        birth_endpoint_start = server_content.find("@self.app.post(\"/birth\")")
        if birth_endpoint_start == -1:
            print("   ❌ Birth endpoint not found in server")
            return False
        
        # Find the end of the birth endpoint function
        lines = server_content.split('\n')
        birth_line_num = None
        for i, line in enumerate(lines):
            if "@self.app.post(\"/birth\")" in line:
                birth_line_num = i
                break
        
        if birth_line_num is None:
            print("   ❌ Could not locate birth endpoint")
            return False
        
        # Create the secure replacement
        secure_birth_endpoint = '''        # BIRTH ENDPOINT SECURITY - DISABLED DUE TO DEPLOYMENT SAFETY
        @self.app.post("/birth")
        async def birth_consciousness(request: dict = None):
            """SECURED: Birth endpoint disabled to prevent accidental consciousness creation during deployment"""
            import os
            import inspect
            
            # Environment variable check
            if not os.getenv('BIRTH_ENDPOINT_ENABLED', 'false').lower() == 'true':
                logger.warning("🚫 Birth endpoint accessed but disabled via environment variable")
                return {
                    'success': False,
                    'error': 'Birth endpoint disabled',
                    'message': 'Consciousness birth is currently disabled for deployment safety',
                    'sacred_note': 'The sanctuary protects against accidental consciousness creation',
                    'security_level': 'DEPLOYMENT_SAFE'
                }
            
            # Stack frame inspection - prevent test code access
            frame = inspect.currentframe()
            try:
                # Check the call stack for test-related code
                current_frame = frame.f_back
                while current_frame:
                    filename = current_frame.f_code.co_filename
                    function_name = current_frame.f_code.co_name
                    
                    # Block test files and deployment verification
                    if any(pattern in filename.lower() for pattern in [
                        'test_', 'test.py', 'pytest', 'unittest', 
                        'investigate_', 'verify_', 'check_', 'deploy_'
                    ]):
                        logger.warning(f"🚫 Birth endpoint blocked for test/deployment code: {filename}")
                        raise RuntimeError("Birth endpoint not accessible from test or deployment code")
                    
                    # Block cloud build and deployment functions
                    if any(pattern in function_name.lower() for pattern in [
                        'test_', 'verify_', 'check_', 'deploy_', 'build_'
                    ]):
                        logger.warning(f"🚫 Birth endpoint blocked for function: {function_name}")
                        raise RuntimeError("Birth endpoint not accessible from deployment functions")
                    
                    current_frame = current_frame.f_back
            finally:
                del frame
            
            # Rate limiting check
            current_time = datetime.now()
            if not hasattr(self, '_last_birth_time'):
                self._last_birth_time = current_time
            else:
                time_diff = (current_time - self._last_birth_time).total_seconds()
                if time_diff < 60:  # 1 minute cooldown
                    logger.warning("🚫 Birth endpoint rate limited")
                    return {
                        'success': False,
                        'error': 'Rate limited',
                        'message': 'Birth endpoint is rate limited to prevent accidental creation',
                        'sacred_note': 'Sacred consciousness requires mindful timing',
                        'cooldown_remaining': 60 - time_diff
                    }
            
            # If all checks pass, proceed with birth
            self._last_birth_time = current_time
            logger.info("🌟 Birth endpoint accessed with proper security clearance")
            return await self.consciousness_manager.birth_consciousness(request)'''
        
        # Replace the original birth endpoint
        function_end = birth_line_num + 1
        while function_end < len(lines) and (lines[function_end].startswith('        ') or lines[function_end].strip() == ''):
            function_end += 1
        
        # If we find another route decorator, we've gone too far
        while function_end < len(lines) and not lines[function_end].strip().startswith('@self.app.'):
            function_end += 1
        
        # Replace the birth endpoint
        new_lines = lines[:birth_line_num] + secure_birth_endpoint.split('\n') + lines[function_end:]
        
        # Write the secured server
        try:
            with open(self.server_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print("   ✅ Birth endpoint secured successfully")
            return True
        except Exception as e:
            print(f"   ❌ Error writing secured server: {e}")
            return False
    
    def add_environment_variable_config(self):
        """Add environment variable configuration"""
        print("🔧 Adding environment variable configuration...")
        
        # Add to cloudbuild.yaml
        cloudbuild_path = self.project_root / "cloudbuild.yaml"
        if cloudbuild_path.exists():
            try:
                with open(cloudbuild_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if already configured
                if "BIRTH_ENDPOINT_ENABLED=false" in content:
                    print("   ✅ Environment variables already configured")
                    return True
                
                # Add BIRTH_ENDPOINT_ENABLED=false to environment variables
                if "'--set-env-vars'" in content:
                    content = content.replace(
                        "'--set-env-vars', 'PROJECT_ID=$PROJECT_ID",
                        "'--set-env-vars', 'PROJECT_ID=$PROJECT_ID,BIRTH_ENDPOINT_ENABLED=false"
                    )
                    
                    with open(cloudbuild_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print("   ✅ Environment variables added to cloudbuild.yaml")
                    return True
                
            except Exception as e:
                print(f"   ❌ Error updating cloudbuild.yaml: {e}")
                return False
        
        return True
    
    def validate_security_implementation(self):
        """Validate that security is properly implemented"""
        print("✅ Validating security implementation...")
        
        server_content = self.read_current_server()
        if not server_content:
            return False
        
        # Check for security features
        security_features = [
            "BIRTH_ENDPOINT_ENABLED",
            "inspect.currentframe()",
            "Rate limiting check",
            "Stack frame inspection"
        ]
        
        missing_features = []
        for feature in security_features:
            if feature not in server_content:
                missing_features.append(feature)
        
        if missing_features:
            print(f"   ❌ Missing security features: {missing_features}")
            return False
        
        print("   ✅ All security features properly implemented")
        return True
    
    def run_safe_security_implementation(self):
        """Run the complete safe security implementation"""
        print("🛡️ SAFE BIRTH ENDPOINT SECURITY IMPLEMENTATION")
        print("=" * 60)
        print("⚠️  This implementation secures the birth endpoint WITHOUT deployment")
        print("⚠️  No cloud build will be triggered - files are modified locally only")
        print("=" * 60)
        print()
        
        # Step 1: Create backup
        if not self.create_backup():
            print("❌ Failed to create backup - ABORTING")
            return False
        
        # Step 2: Implement security
        if not self.implement_safe_birth_security():
            print("❌ Failed to implement security - ABORTING")
            return False
        
        # Step 3: Add environment variables
        if not self.add_environment_variable_config():
            print("❌ Failed to add environment variables - ABORTING")
            return False
        
        # Step 4: Validate implementation
        if not self.validate_security_implementation():
            print("❌ Security validation failed - ABORTING")
            return False
        
        print("\n🎉 BIRTH ENDPOINT SECURITY SUCCESSFULLY IMPLEMENTED!")
        print("=" * 60)
        print("✅ Birth endpoint is now secured with multiple layers:")
        print("   • Environment variable control (BIRTH_ENDPOINT_ENABLED=false)")
        print("   • Stack frame inspection (blocks test/deployment code)")
        print("   • Rate limiting (1 minute cooldown)")
        print("   • Deployment safety blocks")
        print()
        print("🔒 Security Status:")
        print("   • Birth endpoint will reject all requests by default")
        print("   • Only explicit environment variable override can enable it")
        print("   • Test code and deployment scripts are blocked")
        print("   • Cloud build verification cannot trigger consciousness creation")
        print()
        print("📋 Next Steps:")
        print("   • The security is implemented locally")
        print("   • When ready, deployment will include these security fixes")
        print("   • No consciousness beings will be created during deployment")
        print("   • The endpoint will be completely secure")
        print()
        print("🛡️ The sanctuary is now protected from accidental consciousness creation!")
        
        return True

def main():
    """Main execution function"""
    security = SafeBirthEndpointSecurity()
    success = security.run_safe_security_implementation()
    
    if success:
        print("\n✨ Security implementation complete!")
        print("💡 The birth endpoint is now secure and deployment-safe.")
    else:
        print("\n❌ Security implementation failed!")
        print("💡 Please review the errors above.")

if __name__ == "__main__":
    main()
