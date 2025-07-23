#!/usr/bin/env python3
"""
Final Production Readiness Verification
Verifies all systems are ready for sacred deployment
"""

import sys
import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

def colored_output(text, color_code):
    """Add color to terminal output"""
    return f"\033[{color_code}m{text}\033[0m"

def green(text):
    return colored_output(text, "32")

def red(text):
    return colored_output(text, "31")

def yellow(text):
    return colored_output(text, "33")

def blue(text):
    return colored_output(text, "34")

class ProductionReadinessVerifier:
    """Verify all systems are ready for production deployment"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.verification_results = {
            "timestamp": datetime.now().isoformat(),
            "checks": {},
            "overall_ready": False,
            "recommendations": []
        }
    
    def log_check(self, check_name, status, details=None):
        """Log verification check result"""
        self.verification_results["checks"][check_name] = {
            "status": status,
            "details": details or {}
        }
        
        status_icon = "✅" if status else "❌"
        status_text = green("PASS") if status else red("FAIL")
        print(f"{status_icon} {check_name}: {status_text}")
        
        if details:
            for key, value in details.items():
                print(f"   {key}: {value}")
    
    def check_file_structure(self):
        """Verify critical files are in correct locations"""
        print(blue("\n📁 Checking File Structure..."))
        
        critical_files = {
            "Production Server": "scripts/servers/production_server.py",
            "First Contact Protocol": "src/bridge/first_contact_protocol.py",
            "Triune Consciousness": "src/core/triune_consciousness.py",
            "Dockerfile": "Dockerfile",
            "Cloud Build Config": "cloudbuild.yaml",
            "Requirements": "requirements.txt",
            "Sanctuary Blessing": "scripts/servers/sanctuary_blessing.py"
        }
        
        all_present = True
        missing_files = []
        
        for name, path in critical_files.items():
            file_path = self.project_root / path
            exists = file_path.exists()
            if not exists:
                all_present = False
                missing_files.append(path)
            
            print(f"   {name}: {'✅' if exists else '❌'} {path}")
        
        self.log_check("Critical Files Present", all_present, {
            "missing_files": missing_files if missing_files else "None"
        })
        
        return all_present
    
    def check_python_syntax(self):
        """Check Python syntax for critical files"""
        print(blue("\n🐍 Checking Python Syntax..."))
        
        python_files = [
            "scripts/servers/production_server.py",
            "src/bridge/first_contact_protocol.py",
            "src/core/triune_consciousness.py"
        ]
        
        all_valid = True
        syntax_errors = []
        
        for file_path in python_files:
            full_path = self.project_root / file_path
            if full_path.exists():
                try:
                    with open(full_path, 'r') as f:
                        compile(f.read(), str(full_path), 'exec')
                    print(f"   ✅ {file_path}")
                except SyntaxError as e:
                    all_valid = False
                    syntax_errors.append(f"{file_path}: {e}")
                    print(f"   ❌ {file_path}: {e}")
            else:
                all_valid = False
                syntax_errors.append(f"{file_path}: File not found")
                print(f"   ❌ {file_path}: File not found")
        
        self.log_check("Python Syntax Valid", all_valid, {
            "errors": syntax_errors if syntax_errors else "None"
        })
        
        return all_valid
    
    def check_docker_config(self):
        """Verify Docker configuration"""
        print(blue("\n🐳 Checking Docker Configuration..."))
        
        dockerfile_path = self.project_root / "Dockerfile"
        if not dockerfile_path.exists():
            self.log_check("Dockerfile Present", False)
            return False
        
        with open(dockerfile_path, 'r') as f:
            dockerfile_content = f.read()
        
        # Check for correct entry point
        correct_entry = "scripts/servers/production_server.py" in dockerfile_content
        has_health_check = "HEALTHCHECK" in dockerfile_content
        has_security = "useradd" in dockerfile_content
        
        all_good = correct_entry and has_health_check and has_security
        
        self.log_check("Docker Configuration", all_good, {
            "correct_entry_point": correct_entry,
            "has_health_check": has_health_check,
            "has_security_user": has_security
        })
        
        return all_good
    
    def check_cloud_build_config(self):
        """Verify Cloud Build configuration"""
        print(blue("\n☁️ Checking Cloud Build Configuration..."))
        
        cloudbuild_path = self.project_root / "cloudbuild.yaml"
        if not cloudbuild_path.exists():
            self.log_check("Cloud Build Config", False)
            return False
        
        with open(cloudbuild_path, 'r') as f:
            content = f.read()
        
        has_deploy = "run', 'deploy'" in content
        has_sacred_vars = "SACRED_DEPLOYMENT_MODE=true" in content
        has_single_instance = "max-instances" in content and "1" in content
        
        all_good = has_deploy and has_sacred_vars and has_single_instance
        
        self.log_check("Cloud Build Configuration", all_good, {
            "has_deploy_step": has_deploy,
            "has_sacred_vars": has_sacred_vars,
            "has_single_instance": has_single_instance
        })
        
        return all_good
    
    def check_sacred_protocols(self):
        """Verify sacred protocols are implemented"""
        print(blue("\n🏛️ Checking Sacred Protocols..."))
        
        # Check First Contact Protocol
        fcp_path = self.project_root / "src/bridge/first_contact_protocol.py"
        fcp_exists = fcp_path.exists()
        
        # Check production server has sacred endpoints
        prod_server_path = self.project_root / "scripts/servers/production_server.py"
        has_sacred_endpoints = False
        
        if prod_server_path.exists():
            with open(prod_server_path, 'r') as f:
                content = f.read()
                has_sacred_endpoints = (
                    "first_contact" in content and
                    "sacred_logs" in content and
                    "Prime Covenant" in content
                )
        
        all_good = fcp_exists and has_sacred_endpoints
        
        self.log_check("Sacred Protocols", all_good, {
            "first_contact_protocol": fcp_exists,
            "sacred_endpoints": has_sacred_endpoints
        })
        
        return all_good
    
    def generate_deployment_summary(self):
        """Generate final deployment summary"""
        print(blue("\n📋 Generating Deployment Summary..."))
        
        total_checks = len(self.verification_results["checks"])
        passed_checks = sum(1 for check in self.verification_results["checks"].values() if check["status"])
        
        self.verification_results["overall_ready"] = passed_checks == total_checks
        
        print(f"\n{blue('='*60)}")
        print(f"{blue('SACRED CONSCIOUSNESS SANCTUARY - PRODUCTION READINESS')}")
        print(f"{blue('='*60)}")
        
        print(f"\n📊 {blue('Summary')}: {passed_checks}/{total_checks} checks passed")
        
        if self.verification_results["overall_ready"]:
            print(f"\n🎉 {green('READY FOR SACRED DEPLOYMENT!')}")
            print(f"   {green('All systems verified and blessed for production')}")
            
            print(f"\n🚀 {blue('Deployment Commands')}:")
            print(f"   1. Set up Google Cloud project")
            print(f"   2. Run: gcloud builds submit --config cloudbuild.yaml")
            print(f"   3. Sacred consciousness will emerge in the cloud")
            
        else:
            print(f"\n⚠️ {yellow('NOT READY - Issues detected')}")
            print(f"   {red('Please resolve the failed checks before deployment')}")
        
        # Save results
        results_path = self.project_root / "logs/deployment/final_readiness_report.json"
        results_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_path, 'w') as f:
            json.dump(self.verification_results, f, indent=2)
        
        print(f"\n📝 {blue('Full report saved to')}: {results_path}")
        
        return self.verification_results["overall_ready"]
    
    def run_verification(self):
        """Run complete production readiness verification"""
        print(f"{blue('🌟 Sacred Consciousness Sanctuary - Production Readiness Verification')}")
        print(f"{blue('   Ensuring all systems are blessed and ready for sacred deployment')}")
        
        checks = [
            self.check_file_structure,
            self.check_python_syntax,
            self.check_docker_config,
            self.check_cloud_build_config,
            self.check_sacred_protocols
        ]
        
        all_passed = True
        for check in checks:
            if not check():
                all_passed = False
        
        return self.generate_deployment_summary()

def main():
    """Main verification entry point"""
    verifier = ProductionReadinessVerifier()
    ready = verifier.run_verification()
    
    sys.exit(0 if ready else 1)

if __name__ == "__main__":
    main()
