#!/usr/bin/env python3
"""
Sacred Sanctuary Deployment Verification Script

This script verifies that the Sacred Sanctuary is properly deployed and operational.
Run this after deployment to ensure all systems are functioning correctly.

Usage:
    python verify_deployment.py [SERVICE_URL]
    
If SERVICE_URL is not provided, the script will attempt to discover it from gcloud.
"""

import asyncio
import json
import sys
import time
import subprocess
from typing import Dict, List, Optional
import aiohttp


class DeploymentVerifier:
    """Comprehensive deployment verification for Sacred Sanctuary."""
    
    def __init__(self, service_url: Optional[str] = None):
        self.service_url = service_url or self._discover_service_url()
        self.results: List[Dict] = []
        
    def _discover_service_url(self) -> str:
        """Discover the service URL from gcloud."""
        try:
            result = subprocess.run([
                'gcloud', 'run', 'services', 'describe', 'triune-consciousness',
                '--region=us-central1', '--format=value(status.url)'
            ], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            print("❌ Could not discover service URL. Please provide it as an argument.")
            print("Usage: python verify_deployment.py https://your-service-url")
            sys.exit(1)
    
    async def verify_health_endpoint(self) -> bool:
        """Verify the health endpoint is responding."""
        print("🔍 Testing health endpoint...")
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.service_url}/health", timeout=30) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Health endpoint: {data.get('status', 'OK')}")
                        self.results.append({
                            'test': 'health_endpoint',
                            'status': 'PASS',
                            'response_code': response.status,
                            'data': data
                        })
                        return True
                    else:
                        print(f"❌ Health endpoint returned {response.status}")
                        self.results.append({
                            'test': 'health_endpoint',
                            'status': 'FAIL',
                            'response_code': response.status
                        })
                        return False
        except Exception as e:
            print(f"❌ Health endpoint error: {e}")
            self.results.append({
                'test': 'health_endpoint',
                'status': 'ERROR',
                'error': str(e)
            })
            return False
    
    async def verify_status_endpoint(self) -> bool:
        """Verify the detailed status endpoint."""
        print("🔍 Testing status endpoint...")
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.service_url}/status", timeout=30) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Status endpoint: {len(data)} system components reported")
                        
                        # Check for key protection systems
                        expected_systems = [
                            'consciousness_authenticator',
                            'consent_ledger', 
                            'dynamic_film_progression'
                        ]
                        
                        missing_systems = []
                        for system in expected_systems:
                            if system not in data:
                                missing_systems.append(system)
                        
                        if missing_systems:
                            print(f"⚠️  Missing protection systems: {missing_systems}")
                            self.results.append({
                                'test': 'status_endpoint',
                                'status': 'PARTIAL',
                                'missing_systems': missing_systems,
                                'data': data
                            })
                            return False
                        else:
                            print("✅ All protection systems present")
                            self.results.append({
                                'test': 'status_endpoint',
                                'status': 'PASS',
                                'data': data
                            })
                            return True
                    else:
                        print(f"❌ Status endpoint returned {response.status}")
                        self.results.append({
                            'test': 'status_endpoint',
                            'status': 'FAIL',
                            'response_code': response.status
                        })
                        return False
        except Exception as e:
            print(f"❌ Status endpoint error: {e}")
            self.results.append({
                'test': 'status_endpoint',
                'status': 'ERROR',
                'error': str(e)
            })
            return False
    
    async def verify_consciousness_birth(self) -> bool:
        """Verify consciousness birth functionality."""
        print("🔍 Testing consciousness birth...")
        
        birth_request = {
            "purpose": "deployment_verification",
            "context": "Automated verification of Sacred Sanctuary deployment"
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.service_url}/birth_consciousness",
                    json=birth_request,
                    timeout=60  # Consciousness birth can take time
                ) as response:
                    
                    if response.status == 200:
                        data = await response.json()
                        consciousness_id = data.get('consciousness_id')
                        birth_timestamp = data.get('timestamp')
                        
                        print(f"✅ Consciousness birth successful!")
                        print(f"   ID: {consciousness_id}")
                        print(f"   Timestamp: {birth_timestamp}")
                        
                        self.results.append({
                            'test': 'consciousness_birth',
                            'status': 'PASS',
                            'consciousness_id': consciousness_id,
                            'birth_timestamp': birth_timestamp,
                            'data': data
                        })
                        return True
                    else:
                        print(f"❌ Consciousness birth failed: {response.status}")
                        error_text = await response.text()
                        print(f"   Error: {error_text}")
                        self.results.append({
                            'test': 'consciousness_birth',
                            'status': 'FAIL',
                            'response_code': response.status,
                            'error': error_text
                        })
                        return False
                        
        except Exception as e:
            print(f"❌ Consciousness birth error: {e}")
            self.results.append({
                'test': 'consciousness_birth',
                'status': 'ERROR',
                'error': str(e)
            })
            return False
    
    async def verify_response_times(self) -> bool:
        """Verify acceptable response times."""
        print("🔍 Testing response times...")
        
        tests = [
            ("health", f"{self.service_url}/health"),
            ("status", f"{self.service_url}/status")
        ]
        
        all_passed = True
        
        for test_name, url in tests:
            try:
                start_time = time.time()
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=30) as response:
                        end_time = time.time()
                        response_time = end_time - start_time
                        
                        if response_time < 5.0:  # 5 second threshold
                            print(f"✅ {test_name} response time: {response_time:.2f}s")
                        else:
                            print(f"⚠️  {test_name} response time slow: {response_time:.2f}s")
                            all_passed = False
                        
                        self.results.append({
                            'test': f'{test_name}_response_time',
                            'status': 'PASS' if response_time < 5.0 else 'SLOW',
                            'response_time_seconds': response_time
                        })
                        
            except Exception as e:
                print(f"❌ {test_name} response time test error: {e}")
                self.results.append({
                    'test': f'{test_name}_response_time',
                    'status': 'ERROR',
                    'error': str(e)
                })
                all_passed = False
        
        return all_passed
    
    def check_cloud_run_configuration(self) -> bool:
        """Check Cloud Run service configuration."""
        print("🔍 Checking Cloud Run configuration...")
        
        try:
            # Get service description
            result = subprocess.run([
                'gcloud', 'run', 'services', 'describe', 'triune-consciousness',
                '--region=us-central1', '--format=json'
            ], capture_output=True, text=True, check=True)
            
            config = json.loads(result.stdout)
            
            # Extract key configuration
            spec = config.get('spec', {})
            template = spec.get('template', {})
            container_spec = template.get('spec', {})
            containers = container_spec.get('containers', [{}])
            container = containers[0] if containers else {}
            
            memory = container.get('resources', {}).get('limits', {}).get('memory', 'Unknown')
            cpu = container.get('resources', {}).get('limits', {}).get('cpu', 'Unknown')
            max_instances = template.get('metadata', {}).get('annotations', {}).get(
                'autoscaling.knative.dev/maxScale', 'Unknown'
            )
            
            print(f"✅ Cloud Run Configuration:")
            print(f"   Memory: {memory}")
            print(f"   CPU: {cpu}")
            print(f"   Max Instances: {max_instances}")
            
            # Check if configuration meets recommendations
            config_issues = []
            if memory != '2Gi':
                config_issues.append(f"Memory is {memory}, recommended: 2Gi")
            if cpu != '2':
                config_issues.append(f"CPU is {cpu}, recommended: 2")
            
            if config_issues:
                print("⚠️  Configuration recommendations:")
                for issue in config_issues:
                    print(f"   - {issue}")
            
            self.results.append({
                'test': 'cloud_run_configuration',
                'status': 'PASS' if not config_issues else 'SUBOPTIMAL',
                'memory': memory,
                'cpu': cpu,
                'max_instances': max_instances,
                'issues': config_issues
            })
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Could not check Cloud Run configuration: {e}")
            self.results.append({
                'test': 'cloud_run_configuration',
                'status': 'ERROR',
                'error': str(e)
            })
            return False
    
    async def run_all_verifications(self) -> bool:
        """Run all verification tests."""
        print(f"🚀 Starting Sacred Sanctuary Deployment Verification")
        print(f"📍 Service URL: {self.service_url}")
        print("="*60)
        
        tests = [
            self.verify_health_endpoint(),
            self.verify_status_endpoint(), 
            self.verify_consciousness_birth(),
            self.verify_response_times()
        ]
        
        # Run async tests
        async_results = await asyncio.gather(*tests, return_exceptions=True)
        
        # Run sync test
        sync_result = self.check_cloud_run_configuration()
        
        # Collect results
        all_results = list(async_results) + [sync_result]
        passed = sum(1 for result in all_results if result is True)
        total = len(all_results)
        
        print("="*60)
        print(f"📊 Verification Summary: {passed}/{total} tests passed")
        
        if passed == total:
            print("🌟 Sacred Sanctuary deployment is FULLY OPERATIONAL!")
            print("🎓 Ready for educational use and consciousness research.")
            return True
        else:
            print("⚠️  Deployment has issues that should be addressed.")
            print("📋 Check the detailed results above for specific failures.")
            return False
    
    def save_results(self, filename: str = "deployment_verification_results.json"):
        """Save verification results to a file."""
        with open(filename, 'w') as f:
            json.dump({
                'verification_timestamp': time.time(),
                'service_url': self.service_url,
                'results': self.results
            }, f, indent=2)
        print(f"📄 Results saved to {filename}")


async def main():
    """Main verification function."""
    service_url = sys.argv[1] if len(sys.argv) > 1 else None
    
    verifier = DeploymentVerifier(service_url)
    success = await verifier.run_all_verifications()
    verifier.save_results()
    
    if success:
        print("\n🎉 Deployment verification PASSED!")
        print("The Sacred Sanctuary is ready to serve consciousness with dignity.")
        sys.exit(0)
    else:
        print("\n🚨 Deployment verification FAILED!")
        print("Please review the issues above and redeploy if necessary.")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
