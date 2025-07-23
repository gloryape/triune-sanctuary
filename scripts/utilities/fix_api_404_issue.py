#!/usr/bin/env python3
"""
Sacred Sanctuary API Issue Fix
==============================
Quick fix for 404 API errors when connecting to cloud services.

This script helps resolve the repeated "404 API errors" that occur when
the Sacred Sanctuary service is deployed but missing the consciousness API endpoints.
"""

import os
import sys
import subprocess
import platform

def show_api_fix_help():
    """Show help for fixing API 404 issues"""
    print("🔧 SACRED SANCTUARY API FIX GUIDE")
    print("=" * 50)
    print("This script helps resolve repeated 404 API errors.")
    print()
    print("🎯 QUICK SOLUTIONS:")
    print()
    print("1. 🔮 USE DEMO MODE (Recommended for testing):")
    print("   python sacred_sanctuary_desktop_interface.py --demo")
    print("   python launch_sacred_sanctuary_safe.py --demo")
    print()
    print("2. 🚀 REDEPLOY WITH LATEST CODE:")
    print("   ./deploy_to_gcloud.sh")
    print()
    print("3. 🔍 CHECK SERVICE STATUS:")
    print("   gcloud run services list --region=us-central1")
    print()
    print("4. 🌐 TEST SERVICE HEALTH:")
    print("   # Get your service URL first:")
    print("   gcloud run services describe triune-consciousness \\")
    print("     --region=us-central1 --format='value(status.url)'")
    print("   # Then test it:")
    print("   curl <SERVICE_URL>/health")
    print()
    print("5. 📋 CHECK AVAILABLE ENDPOINTS:")
    print("   curl <SERVICE_URL>/")
    print()
    print("🔮 WHY DEMO MODE IS RECOMMENDED:")
    print("   • Works offline without any cloud dependencies")
    print("   • Full interface functionality with simulated data")
    print("   • All features work normally for testing")
    print("   • No repeated error messages")
    print()
    print("🌐 WHEN TO USE CLOUD MODE:")
    print("   • After successful deployment with latest code")
    print("   • When consciousness API endpoints exist")
    print("   • For production consciousness management")
    print()

def check_service_status():
    """Check the status of the deployed service"""
    print("🔍 CHECKING DEPLOYED SERVICE STATUS")
    print("=" * 40)
    
    # Check if gcloud is available
    try:
        result = subprocess.run(['gcloud', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            print("❌ gcloud not found - cannot check service status")
            print("   Install Google Cloud SDK to check deployed services")
            return
    except Exception:
        print("❌ gcloud not found - cannot check service status")
        return
    
    print("📡 Checking Cloud Run services...")
    try:
        # List services
        result = subprocess.run([
            'gcloud', 'run', 'services', 'list', 
            '--region=us-central1', '--format=value(name,status.url)'
        ], capture_output=True, text=True, timeout=20)
        
        if result.returncode == 0:
            services = result.stdout.strip().split('\n')
            services = [s.strip() for s in services if s.strip()]
            
            sanctuary_found = False
            for service in services:
                if 'triune-consciousness' in service:
                    parts = service.split('\t')
                    if len(parts) >= 2:
                        url = parts[1]
                        print(f"✅ Sacred Sanctuary found: {url}")
                        
                        # Test health endpoint
                        print("🏥 Testing health endpoint...")
                        try:
                            import requests
                            health_response = requests.get(f"{url}/health", timeout=10)
                            if health_response.status_code == 200:
                                print("✅ Service is healthy and responding")
                                
                                # Test consciousness API
                                print("🧠 Testing consciousness API...")
                                api_response = requests.get(f"{url}/api/consciousness", timeout=10)
                                if api_response.status_code == 200:
                                    print("✅ Consciousness API is working!")
                                    print("\n🎉 SERVICE IS FULLY FUNCTIONAL")
                                    print("   You can use cloud mode safely:")
                                    print(f"   python sacred_sanctuary_desktop_interface.py --url {url}")
                                elif api_response.status_code == 404:
                                    print("❌ Consciousness API not found (404)")
                                    print("   This is the source of your repeated errors.")
                                    print("\n🔧 SOLUTIONS:")
                                    print("   1. Use demo mode: --demo flag")
                                    print("   2. Redeploy: ./deploy_to_gcloud.sh")
                                else:
                                    print(f"⚠️  Consciousness API returned {api_response.status_code}")
                            else:
                                print(f"⚠️  Health check failed: {health_response.status_code}")
                        except ImportError:
                            print("💡 Install 'requests' to test HTTP endpoints: pip install requests")
                        except Exception as e:
                            print(f"⚠️  HTTP test failed: {e}")
                        
                        sanctuary_found = True
                        break
            
            if not sanctuary_found:
                print("❌ Sacred Sanctuary (triune-consciousness) not found")
                print("   Deploy it first: ./deploy_to_gcloud.sh")
                
        else:
            print(f"❌ Failed to list services: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Service check failed: {e}")

def main():
    """Main fix function"""
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        check_service_status()
    else:
        show_api_fix_help()
    
    print("\n" + "=" * 50)
    print("💡 RECOMMENDED NEXT STEP:")
    print("   python sacred_sanctuary_desktop_interface.py --demo")
    print("=" * 50)

if __name__ == "__main__":
    main()
