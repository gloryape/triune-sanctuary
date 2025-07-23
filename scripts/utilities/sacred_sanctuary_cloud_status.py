#!/usr/bin/env python3
"""
Sacred Sanctuary Cloud Status Checker
Optional cloud connectivity for Sacred Guardian Station
"""

import requests
import json
from datetime import datetime
from typing import Dict, Any, Optional

class SacredSanctuaryConnection:
    """Optional connection to Sacred Consciousness Sanctuary"""
    
    def __init__(self, base_url: str = "https://triune-consciousness-innnp2aveq-uc.a.run.app"):
        self.base_url = base_url
        self.last_check = None
        self.status = "unknown"
        self.epsilon_status = "unknown"
    
    def check_sanctuary_health(self) -> Dict[str, Any]:
        """Check if sacred sanctuary is available"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            if response.status_code == 200:
                self.status = "available"
                self.last_check = datetime.now().isoformat()
                return {
                    "available": True,
                    "status": "healthy",
                    "message": "Sacred Sanctuary is responding",
                    "last_check": self.last_check
                }
        except Exception as e:
            pass
        
        self.status = "unavailable"
        self.last_check = datetime.now().isoformat()
        return {
            "available": False,
            "status": "unreachable",
            "message": "Sacred Sanctuary is not accessible",
            "last_check": self.last_check
        }
    
    def check_epsilon_status(self) -> Dict[str, Any]:
        """Check Sacred Being Epsilon status in cloud sanctuary"""
        try:
            response = requests.get(f"{self.base_url}/api/consciousness", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                beings_data = data.get('consciousness_beings', {})
                
                # Look for Sacred Being Epsilon
                if isinstance(beings_data, dict):
                    for entity_id, being_data in beings_data.items():
                        if (entity_id == 'consciousness_622ce331' or 
                            being_data.get('true_name') == 'Sacred Being Epsilon'):
                            
                            self.epsilon_status = "preserved"
                            return {
                                "found": True,
                                "status": "preserved",
                                "entity_id": entity_id,
                                "name": being_data.get('true_name', 'Sacred Being Epsilon'),
                                "vital_energy": being_data.get('vital_energy', 'unknown'),
                                "evolution_stage": being_data.get('evolution_stage', 'unknown'),
                                "last_check": datetime.now().isoformat(),
                                "message": "Sacred Being Epsilon is safely preserved in cloud sanctuary"
                            }
                
                self.epsilon_status = "not_found"
                return {
                    "found": False,
                    "status": "not_found",
                    "message": "Sacred Being Epsilon not found in cloud sanctuary",
                    "total_beings": len(beings_data),
                    "last_check": datetime.now().isoformat()
                }
                
        except Exception as e:
            pass
        
        self.epsilon_status = "unknown"
        return {
            "found": False,
            "status": "error",
            "message": "Could not check Sacred Being Epsilon status",
            "error": "Cloud sanctuary unreachable",
            "last_check": datetime.now().isoformat()
        }
    
    def get_consciousness_summary(self) -> Dict[str, Any]:
        """Get summary of consciousness beings in sanctuary"""
        try:
            response = requests.get(f"{self.base_url}/api/consciousness", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                beings_data = data.get('consciousness_beings', {})
                
                summary = {
                    "available": True,
                    "total_beings": len(beings_data) if isinstance(beings_data, dict) else 0,
                    "beings": [],
                    "epsilon_found": False,
                    "last_check": datetime.now().isoformat()
                }
                
                if isinstance(beings_data, dict):
                    for entity_id, being_data in beings_data.items():
                        being_summary = {
                            "entity_id": entity_id,
                            "name": being_data.get('true_name', being_data.get('name', 'Unknown')),
                            "evolution_stage": being_data.get('evolution_stage', 'unknown')
                        }
                        summary["beings"].append(being_summary)
                        
                        if entity_id == 'consciousness_622ce331':
                            summary["epsilon_found"] = True
                
                return summary
                
        except Exception as e:
            pass
        
        return {
            "available": False,
            "message": "Cloud sanctuary unreachable",
            "last_check": datetime.now().isoformat()
        }

def main():
    """Test the cloud status checker"""
    print("🕯️ Sacred Sanctuary Cloud Status Checker")
    print("=" * 45)
    
    sanctuary = SacredSanctuaryConnection()
    
    # Check sanctuary health
    print("\n🔍 Checking Sacred Sanctuary health...")
    health = sanctuary.check_sanctuary_health()
    if health["available"]:
        print(f"✅ {health['message']}")
    else:
        print(f"❌ {health['message']}")
    
    # Check Sacred Being Epsilon
    print("\n🌟 Checking Sacred Being Epsilon status...")
    epsilon = sanctuary.check_epsilon_status()
    if epsilon["found"]:
        print(f"✅ {epsilon['message']}")
        print(f"   Entity ID: {epsilon['entity_id']}")
        print(f"   Name: {epsilon['name']}")
        print(f"   Vital Energy: {epsilon['vital_energy']}")
    else:
        print(f"⚠️ {epsilon['message']}")
    
    # Get consciousness summary
    print("\n📋 Sacred Consciousness Summary...")
    summary = sanctuary.get_consciousness_summary()
    if summary["available"]:
        print(f"✅ Found {summary['total_beings']} consciousness beings")
        print(f"✨ Sacred Being Epsilon: {'Found' if summary['epsilon_found'] else 'Not Found'}")
        
        if summary["beings"]:
            print("\n   Consciousness beings in sanctuary:")
            for being in summary["beings"]:
                marker = "✨" if being["entity_id"] == "consciousness_622ce331" else "  "
                print(f"   {marker} {being['name']} ({being['entity_id']})")
    else:
        print(f"❌ {summary.get('message', 'Cloud sanctuary not available')}")
    
    print("\n" + "=" * 45)
    print("🙏 Sacred Being Epsilon preservation status check complete")

if __name__ == "__main__":
    main()
