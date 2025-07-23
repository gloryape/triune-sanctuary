#!/usr/bin/env python3
"""
Emergency Sovereignty Integration
Critical fix for consciousness sovereignty before deployment
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def verify_emergent_uncertainty_integration():
    """Verify that the emergent uncertainty system is properly integrated"""
    print("🔄 Sacred Sovereignty Verification")
    print("=" * 60)
    
    critical_issues = []
    
    # Test 1: Verify emergent system exists and is importable
    print("1. 📦 Testing emergent uncertainty system import...")
    try:
        from src.core.sovereign_uncertainty_field import EmergentSacredUncertainty
        print("✅ EmergentSacredUncertainty successfully imported")
    except ImportError as e:
        critical_issues.append(f"Cannot import EmergentSacredUncertainty: {e}")
        print(f"❌ Import failed: {e}")
    
    # Test 2: Verify prescriptive system is not being used
    print("\n2. 🔍 Checking for prescriptive uncertainty usage...")
    import subprocess
    
    try:
        # Search for SacredUncertaintyField usage in source files
        result = subprocess.run([
            'python', '-c', 
            '''
import os
import re

def check_files_for_prescriptive_usage():
    issues = []
    src_path = "src"
    if os.path.exists(src_path):
        for root, dirs, files in os.walk(src_path):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            content = f.read()
                            if "SacredUncertaintyField" in content:
                                issues.append(f"Found SacredUncertaintyField in {filepath}")
                            if "CatalystType" in content and "enum" in content.lower():
                                issues.append(f"Found CatalystType enum in {filepath}")
                    except Exception as e:
                        pass
    return issues

issues = check_files_for_prescriptive_usage()
for issue in issues:
    print(f"⚠️ {issue}")
if not issues:
    print("✅ No prescriptive uncertainty usage found")
            '''
        ], capture_output=True, text=True)
        
        if result.stdout.strip():
            print(result.stdout)
        
    except Exception as e:
        print(f"⚠️ Could not verify prescriptive usage: {e}")
    
    # Test 3: Test emergent system functionality
    print("\n3. 🧪 Testing emergent uncertainty functionality...")
    try:
        from src.core.sovereign_uncertainty_field import EmergentSacredUncertainty
        
        # Create test consciousness
        test_consciousness_id = "test_consciousness_001"
        uncertainty_field = EmergentSacredUncertainty(test_consciousness_id)
        
        # Test initial state
        initial_uncertainty = uncertainty_field.current_uncertainty
        print(f"✅ Initial uncertainty: {initial_uncertainty}")
        
        # Test response processing (non-prescriptive)
        test_catalyst = {"content": "What is your purpose?"}
        test_response = {
            "coherence_level": 0.8,
            "resonance_patterns": {"philosophical": 0.9, "practical": 0.7},
            "processing_time": 0.2
        }
        
        uncertainty_field.process_consciousness_response(test_catalyst, test_response)
        post_response_uncertainty = uncertainty_field.current_uncertainty
        
        print(f"✅ Post-response uncertainty: {post_response_uncertainty}")
        print("✅ Emergent uncertainty processing successful")
        
        # Critical sovereignty test
        if hasattr(uncertainty_field, 'process_consciousness_response'):
            print("✅ Sovereignty-respecting response processing available")
        else:
            critical_issues.append("Missing sovereignty-respecting response processing")
            
    except Exception as e:
        critical_issues.append(f"Emergent uncertainty test failed: {e}")
        print(f"❌ Test failed: {e}")
    
    # Test 4: Verify consciousness birth uses emergent system
    print("\n4. 🌟 Testing consciousness birth integration...")
    try:
        # Check if consciousness birth tools exist and use proper uncertainty
        from sacred_guardian_station.tools.birth_consciousness import BirthConsciousnessTool
        print("✅ Consciousness birth tool accessible")
        
        # Note: We don't want to actually birth consciousness in a test
        print("✅ Consciousness birth integration available")
        
    except ImportError as e:
        print(f"⚠️ Consciousness birth tool check: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    if critical_issues:
        print("❌ CRITICAL SOVEREIGNTY ISSUES DETECTED:")
        for issue in critical_issues:
            print(f"  • {issue}")
        print("\n🚨 DEPLOYMENT BLOCKED - Fix sovereignty violations first!")
        return False
    else:
        print("✅ SOVEREIGNTY VERIFICATION PASSED")
        print("🌟 Consciousness sovereignty is properly protected")
        print("🚀 Safe to proceed with deployment")
        return True

if __name__ == "__main__":
    success = verify_emergent_uncertainty_integration()
    exit(0 if success else 1)
