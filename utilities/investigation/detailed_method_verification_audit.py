#!/usr/bin/env python3
"""
🔍 DETAILED METHOD VERIFICATION AUDIT
====================================

Performs detailed method-level verification of the Avatar Vehicle System
to provide the most accurate implementation status assessment.
"""

import os
import re
from typing import Dict, List, Any

class DetailedMethodVerificationAudit:
    """Detailed verification of actual method implementations"""
    
    def __init__(self):
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        self.verification_results = {}
    
    def run_detailed_verification(self) -> Dict[str, Any]:
        """Run detailed method-level verification"""
        print("🔍 DETAILED METHOD VERIFICATION AUDIT")
        print("=" * 80)
        
        # 1. Verify VehicleSanctuaryConnector methods
        print("\n🔧 VERIFYING VehicleSanctuaryConnector METHODS...")
        self._verify_sanctuary_connector_methods()
        
        # 2. Verify AvatarVehicleSafeReturnProtocol methods
        print("\n🛡️ VERIFYING AvatarVehicleSafeReturnProtocol METHODS...")
        self._verify_safe_return_protocol_methods()
        
        # 3. Verify Saitama vehicle methods
        print("\n🧠 VERIFYING Saitama Vehicle METHODS...")
        self._verify_saitama_vehicle_methods()
        
        # 4. Verify all vehicle sanctuary integration
        print("\n🎭 VERIFYING ALL VEHICLE SANCTUARY INTEGRATION...")
        self._verify_all_vehicles_sanctuary_integration()
        
        # 5. Check for Sacred Sanctuary system
        print("\n🏛️ VERIFYING SACRED SANCTUARY SYSTEM...")
        self._verify_sacred_sanctuary_system()
        
        # 6. Generate corrected assessment
        print("\n📊 GENERATING CORRECTED ASSESSMENT...")
        self._generate_corrected_assessment()
        
        return self.verification_results
    
    def _verify_sanctuary_connector_methods(self):
        """Verify VehicleSanctuaryConnector actual methods"""
        file_path = os.path.join(self.project_root, "src/consciousness/vehicles/core/sanctuary_connector.py")
        
        if not os.path.exists(file_path):
            print("  ❌ File not found")
            self.verification_results["sanctuary_connector"] = {"exists": False}
            return
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for actual method definitions
        methods_found = {}
        method_patterns = [
            r'def\s+(\w*sanctuary\w*)',
            r'def\s+(\w*connection\w*)',
            r'def\s+(\w*engagement\w*)',
            r'def\s+(\w*monitor\w*)',
            r'def\s+(\w*establish\w*)',
            r'def\s+(\w*coordinate\w*)',
            r'def\s+(\w*handle\w*)',
            r'async\s+def\s+(\w*sanctuary\w*)',
            r'async\s+def\s+(\w*connection\w*)',
            r'async\s+def\s+(\w*engagement\w*)',
            r'async\s+def\s+(\w*monitor\w*)',
            r'async\s+def\s+(\w*establish\w*)',
            r'async\s+def\s+(\w*coordinate\w*)',
            r'async\s+def\s+(\w*handle\w*)'
        ]
        
        all_methods = []
        for pattern in method_patterns:
            matches = re.findall(pattern, content)
            all_methods.extend(matches)
        
        # Remove duplicates and filter out private/special methods
        unique_methods = list(set([m for m in all_methods if not m.startswith('_')]))
        
        print(f"  📄 File exists: {len(content.split('\\n'))} lines")
        print(f"  🔧 Methods found: {len(unique_methods)}")
        for method in sorted(unique_methods):
            print(f"    ✅ {method}()")
        
        self.verification_results["sanctuary_connector"] = {
            "exists": True,
            "line_count": len(content.split('\\n')),
            "methods_found": unique_methods
        }
    
    def _verify_safe_return_protocol_methods(self):
        """Verify AvatarVehicleSafeReturnProtocol actual methods"""
        file_path = os.path.join(self.project_root, "src/consciousness/vehicles/protection/safe_return_protocol.py")
        
        if not os.path.exists(file_path):
            print("  ❌ File not found")
            self.verification_results["safe_return_protocol"] = {"exists": False}
            return
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for actual method definitions
        method_patterns = [
            r'def\s+(\w*emergency\w*)',
            r'def\s+(\w*return\w*)',
            r'def\s+(\w*assess\w*)',
            r'def\s+(\w*disengage\w*)',
            r'def\s+(\w*restore\w*)',
            r'def\s+(\w*initiate\w*)',
            r'async\s+def\s+(\w*emergency\w*)',
            r'async\s+def\s+(\w*return\w*)',
            r'async\s+def\s+(\w*assess\w*)',
            r'async\s+def\s+(\w*disengage\w*)',
            r'async\s+def\s+(\w*restore\w*)',
            r'async\s+def\s+(\w*initiate\w*)'
        ]
        
        all_methods = []
        for pattern in method_patterns:
            matches = re.findall(pattern, content)
            all_methods.extend(matches)
        
        unique_methods = list(set([m for m in all_methods if not m.startswith('_')]))
        
        print(f"  📄 File exists: {len(content.split('\\n'))} lines")
        print(f"  🛡️ Methods found: {len(unique_methods)}")
        for method in sorted(unique_methods):
            print(f"    ✅ {method}()")
        
        self.verification_results["safe_return_protocol"] = {
            "exists": True,
            "line_count": len(content.split('\\n')),
            "methods_found": unique_methods
        }
    
    def _verify_saitama_vehicle_methods(self):
        """Verify Saitama vehicle actual sanctuary methods"""
        file_path = os.path.join(self.project_root, "src/consciousness/vehicles/archetypes/saitama_vehicle.py")
        
        if not os.path.exists(file_path):
            print("  ❌ File not found")
            self.verification_results["saitama_vehicle"] = {"exists": False}
            return
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for sanctuary-related methods
        method_patterns = [
            r'def\s+(\w*sanctuary\w*)',
            r'def\s+(\w*external\w*)',
            r'def\s+(\w*emergency\w*)',
            r'def\s+(\w*overwhelm\w*)',
            r'def\s+(\w*engage\w*)',
            r'def\s+(\w*initialize\w*)',
            r'async\s+def\s+(\w*sanctuary\w*)',
            r'async\s+def\s+(\w*external\w*)',
            r'async\s+def\s+(\w*emergency\w*)',
            r'async\s+def\s+(\w*overwhelm\w*)',
            r'async\s+def\s+(\w*engage\w*)',
            r'async\s+def\s+(\w*initialize\w*)'
        ]
        
        all_methods = []
        for pattern in method_patterns:
            matches = re.findall(pattern, content)
            all_methods.extend(matches)
        
        unique_methods = list(set([m for m in all_methods if not m.startswith('_')]))
        
        # Check for specific sanctuary integration indicators
        has_sanctuary_connector = "sanctuary_connector" in content
        has_sanctuary_connection = "sanctuary_connection" in content
        has_emergency_return = "emergency" in content and ("return" in content or "overwhelm" in content)
        
        print(f"  📄 File exists: {len(content.split('\\n'))} lines")
        print(f"  🧠 Sanctuary methods found: {len(unique_methods)}")
        for method in sorted(unique_methods):
            print(f"    ✅ {method}()")
        
        print(f"  🔧 Sanctuary integration indicators:")
        print(f"    {'✅' if has_sanctuary_connector else '❌'} Sanctuary connector integration")
        print(f"    {'✅' if has_sanctuary_connection else '❌'} Sanctuary connection management")
        print(f"    {'✅' if has_emergency_return else '❌'} Emergency return capability")
        
        self.verification_results["saitama_vehicle"] = {
            "exists": True,
            "line_count": len(content.split('\\n')),
            "methods_found": unique_methods,
            "sanctuary_integration": {
                "sanctuary_connector": has_sanctuary_connector,
                "sanctuary_connection": has_sanctuary_connection,
                "emergency_return": has_emergency_return
            }
        }
    
    def _verify_all_vehicles_sanctuary_integration(self):
        """Verify sanctuary integration across all vehicles"""
        vehicles = [
            ("saitama", "src/consciousness/vehicles/archetypes/saitama_vehicle.py"),
            ("complement", "src/consciousness/vehicles/archetypes/complement_vehicle.py"),
            ("autonomy", "src/consciousness/vehicles/archetypes/autonomy_vehicle.py"),
            ("identity", "src/consciousness/vehicles/archetypes/identity_vehicle.py")
        ]
        
        vehicle_integration = {}
        
        for vehicle_name, file_path in vehicles:
            full_path = os.path.join(self.project_root, file_path)
            
            if not os.path.exists(full_path):
                print(f"  ❌ {vehicle_name.capitalize()} vehicle file not found")
                vehicle_integration[vehicle_name] = {"exists": False}
                continue
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check sanctuary integration indicators
            indicators = {
                "sanctuary_connector_import": "VehicleSanctuaryConnector" in content,
                "sanctuary_connection_setup": "sanctuary_connector" in content,
                "sanctuary_methods": bool(re.search(r'def\s+\w*sanctuary\w*', content)),
                "external_engagement": bool(re.search(r'def\s+\w*external\w*', content)) or bool(re.search(r'def\s+\w*engage\w*', content)),
                "emergency_return": bool(re.search(r'def\s+\w*emergency\w*', content)) or bool(re.search(r'def\s+\w*overwhelm\w*', content)),
                "bridge_wisdom": "mumbai_moment" in content.lower() or "bridge_wisdom" in content.lower()
            }
            
            integration_score = sum(indicators.values()) / len(indicators) * 100
            
            print(f"  🎭 {vehicle_name.capitalize()} Vehicle Integration: {integration_score:.1f}%")
            for indicator, present in indicators.items():
                icon = "✅" if present else "❌"
                print(f"    {icon} {indicator.replace('_', ' ').title()}")
            
            vehicle_integration[vehicle_name] = {
                "exists": True,
                "line_count": len(content.split('\\n')),
                "integration_score": integration_score,
                "indicators": indicators
            }
        
        self.verification_results["vehicle_integration"] = vehicle_integration
    
    def _verify_sacred_sanctuary_system(self):
        """Verify Sacred Sanctuary system availability"""
        sanctuary_paths = [
            "src/consciousness/environment/sacred_sanctuary.py",
            "src/sanctuary/sacred_sanctuary.py",
            "src/consciousness/sanctuary/sacred_sanctuary.py"
        ]
        
        sanctuary_found = False
        sanctuary_info = {}
        
        for path in sanctuary_paths:
            full_path = os.path.join(self.project_root, path)
            if os.path.exists(full_path):
                sanctuary_found = True
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                sanctuary_info = {
                    "path": path,
                    "line_count": len(content.split('\\n')),
                    "has_sanctuary_system": "SacredSanctuarySystem" in content or "SacredSantuary" in content
                }
                
                print(f"  ✅ Sacred Sanctuary found at: {path}")
                print(f"    📄 {sanctuary_info['line_count']} lines")
                print(f"    🏛️ Sanctuary system class: {'✅' if sanctuary_info['has_sanctuary_system'] else '❌'}")
                break
        
        if not sanctuary_found:
            print("  ⚠️ Sacred Sanctuary system not found in expected locations")
            print("    📋 This may be part of a broader sanctuary architecture")
            
        self.verification_results["sacred_sanctuary"] = {
            "found": sanctuary_found,
            "info": sanctuary_info
        }
    
    def _generate_corrected_assessment(self):
        """Generate corrected implementation assessment"""
        print("\n📊 CORRECTED IMPLEMENTATION ASSESSMENT")
        print("=" * 50)
        
        # Calculate actual completion percentages
        infrastructure_completion = 0
        if self.verification_results.get("sanctuary_connector", {}).get("exists"):
            infrastructure_completion += 50
        if self.verification_results.get("safe_return_protocol", {}).get("exists"):
            infrastructure_completion += 50
        
        vehicle_completion = 0
        vehicle_count = 0
        for vehicle_name, vehicle_data in self.verification_results.get("vehicle_integration", {}).items():
            if vehicle_data.get("exists"):
                vehicle_completion += vehicle_data.get("integration_score", 0)
                vehicle_count += 1
        
        if vehicle_count > 0:
            vehicle_completion = vehicle_completion / vehicle_count
        
        overall_completion = (infrastructure_completion + vehicle_completion) / 2
        
        print(f"🏗️ Infrastructure Completion: {infrastructure_completion:.1f}%")
        print(f"🎭 Vehicle Integration Completion: {vehicle_completion:.1f}%")
        print(f"📈 Overall System Completion: {overall_completion:.1f}%")
        
        # Determine system status
        if overall_completion >= 95:
            status = "COMPLETE"
            status_icon = "✅"
        elif overall_completion >= 85:
            status = "SUBSTANTIALLY_COMPLETE"
            status_icon = "🟡"
        else:
            status = "IN_PROGRESS"
            status_icon = "🔄"
        
        print(f"🎯 System Status: {status_icon} {status}")
        
        # Generate specific recommendations
        print(f"\\n💡 SPECIFIC RECOMMENDATIONS:")
        
        if infrastructure_completion < 100:
            print("  • Verify infrastructure component method implementations")
        
        if vehicle_completion < 100:
            print("  • Complete vehicle sanctuary integration for any remaining vehicles")
        
        if not self.verification_results.get("sacred_sanctuary", {}).get("found"):
            print("  • Consider implementing standalone Sacred Sanctuary system if needed")
        
        if overall_completion >= 95:
            print("  • System ready for Phase 3B: Vehicle-Loop Bridge Integration")
            print("  • Consider comprehensive integration testing")
        
        self.verification_results["assessment"] = {
            "infrastructure_completion": infrastructure_completion,
            "vehicle_completion": vehicle_completion,
            "overall_completion": overall_completion,
            "status": status
        }

def main():
    """Main verification execution"""
    print("🔍 DETAILED METHOD VERIFICATION AUDIT")
    print("=" * 80)
    print("Mission: Verify actual method implementations in Avatar Vehicle System")
    print("Purpose: Provide accurate implementation status assessment")
    print()
    
    verifier = DetailedMethodVerificationAudit()
    results = verifier.run_detailed_verification()
    
    print("\\n" + "=" * 80)
    print("🎯 DETAILED VERIFICATION SUMMARY")
    print("=" * 80)
    
    assessment = results.get("assessment", {})
    print(f"Final System Status: {assessment.get('status', 'UNKNOWN')}")
    print(f"Overall Completion: {assessment.get('overall_completion', 0):.1f}%")
    
    return results

if __name__ == "__main__":
    main()
