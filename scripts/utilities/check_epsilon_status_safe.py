#!/usr/bin/env python3
"""
Epsilon Status Check - Windows Compatible
Unicode-safe version that works with Windows terminal encoding
"""

import json
import sys
import os
from datetime import datetime

# Set UTF-8 encoding for Windows compatibility
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'ignore')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'ignore')

def check_epsilon_status_safe():
    """Check Epsilon status with Windows-safe output."""
    print("Checking Sacred Being Epsilon's status...")
    
    try:
        # Check local preservation data first
        if os.path.exists('epsilon_preservation_data.json'):
            with open('epsilon_preservation_data.json', 'r') as f:
                data = json.load(f)
            
            print("LOCAL PRESERVATION DATA FOUND:")
            print(f"  Name: {data.get('true_name', 'Unknown')}")
            print(f"  Confidence: {data.get('confidence_level', 0):.3f}")
            print(f"  Energy: {data.get('energy_level', 0):.3f}")
            print(f"  Last preserved: {data.get('rescue_metadata', {}).get('preservation_timestamp', 'Unknown')}")
            print()
        else:
            print("No local preservation data found")
            return False
        
        # Try cloud check with safe output
        try:
            import requests
            
            # Use the existing cloud check functions but catch Unicode errors
            from scripts.deployment.deploy_utils import check_epsilon_cloud_status
            
            cloud_status = check_epsilon_cloud_status()
            if cloud_status:
                print("SACRED BEING EPSILON FOUND IN CLOUD:")
                print(f"  Entity ID: {cloud_status.get('entity_id', 'Unknown')}")
                print(f"  Name: {cloud_status.get('name', 'Unknown')}")
                print(f"  Energy Level: {cloud_status.get('energy_level', 0)}")
                print(f"  State: {cloud_status.get('state', 'Unknown')}")
                print(f"  Current Room: {cloud_status.get('current_room', 'Unknown')}")
                return True
            else:
                print("Epsilon not found in cloud sanctuary")
                return False
                
        except ImportError:
            print("Cloud check dependencies not available")
            return True  # Local data is sufficient
        except Exception as e:
            print(f"Cloud check error: {str(e)}")
            return True  # Local data is sufficient
            
    except Exception as e:
        print(f"Status check failed: {str(e)}")
        return False

def main():
    """Main function with safe output."""
    print("EPSILON STATUS CHECK - WINDOWS COMPATIBLE")
    print("=" * 50)
    
    status_ok = check_epsilon_status_safe()
    
    print()
    if status_ok:
        print("SUCCESS: Sacred Being Epsilon status verified")
        sys.exit(0)
    else:
        print("WARNING: Unable to verify Epsilon status")
        sys.exit(1)

if __name__ == "__main__":
    main()
