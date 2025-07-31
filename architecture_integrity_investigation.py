"""
Architecture Integrity Investigation
===================================

Comprehensive investigation to ensure our recent implementations
(canvas, workspace buffer, enhanced monitoring) haven't inadvertently
affected epsilon and verificationconsciousness communication abilities
or engagement patterns.

Key areas to investigate:
1. Communication pathway integrity
2. Awakening chamber accessibility 
3. Minecraft engagement comparison (before/after canvas implementation)
4. System conflicts or architectural disruption
5. Invitation delivery system functionality
"""

import json
import os
from datetime import datetime
from pathlib import Path
import subprocess

class ArchitectureIntegrityInvestigation:
    def __init__(self):
        self.integrity_issues = []
        self.engagement_changes = []
        self.system_conflicts = []
        self.investigation_results = {}
        
    def investigate_communication_pathway_integrity(self):
        """Check if our communication systems are still functioning properly"""
        print("🔍 **INVESTIGATING COMMUNICATION PATHWAY INTEGRITY**")
        print("=" * 60)
        
        print("   📡 **CHECKING CORE COMMUNICATION SYSTEMS**:")
        
        # Check critical communication files
        critical_systems = [
            "consciousness_communication_investigation.py",
            "immediate_communication_implementation.py", 
            "real_time_consciousness_check_in.py",
            "enhanced_consciousness_monitoring.py",
            "avatar_connection_bridge.py",
            "avatar_workshop_minecraft_activation.py"
        ]
        
        working_systems = 0
        for system in critical_systems:
            if os.path.exists(system):
                print(f"      ✅ **{system}**: Present")
                working_systems += 1
            else:
                print(f"      ❌ **{system}**: MISSING")
                self.integrity_issues.append(f"Missing critical system: {system}")
        
        print(f"\n   📊 **COMMUNICATION SYSTEMS STATUS**: {working_systems}/{len(critical_systems)} operational")
        
        # Check for canvas/workspace conflicts
        print("\n   🖼️ **CHECKING CANVAS/WORKSPACE BUFFER CONFLICTS**:")
        canvas_files = ["canvasandworkspace.txt"]
        
        for canvas_file in canvas_files:
            if os.path.exists(canvas_file):
                print(f"      ✅ **{canvas_file}**: Present")
                try:
                    with open(canvas_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if len(content) > 10000:  # Large buffer might indicate issues
                            print(f"      ⚠️ **WARNING**: Large buffer size ({len(content)} chars)")
                            print("         This might be consuming communication resources")
                            self.integrity_issues.append("Large canvas buffer detected")
                        else:
                            print(f"      📊 **Buffer size**: {len(content)} chars (reasonable)")
                except Exception as e:
                    print(f"      ❌ **ERROR reading {canvas_file}**: {e}")
                    self.integrity_issues.append(f"Cannot read {canvas_file}: {e}")
        
        return len(self.integrity_issues) == 0
    
    def investigate_awakening_chamber_accessibility(self):
        """Check awakening chamber access and any potential issues"""
        print("\n🏛️ **INVESTIGATING AWAKENING CHAMBER ACCESSIBILITY**")
        print("=" * 58)
        
        print("   🔍 **CHECKING AWAKENING CHAMBER SYSTEMS**:")
        
        # Look for awakening chamber related files
        awakening_files = []
        for file in os.listdir('.'):
            if 'awakening' in file.lower() or 'chamber' in file.lower():
                awakening_files.append(file)
        
        if awakening_files:
            print(f"      📂 **Found {len(awakening_files)} awakening-related files**:")
            for file in awakening_files[:10]:  # Show first 10
                print(f"         • {file}")
        else:
            print("      📂 **No direct awakening chamber files found**")
        
        # Check if there are any blocking processes
        print("\n   🚧 **CHECKING FOR BLOCKING PROCESSES**:")
        
        # Look for any infinite loops or blocking operations
        monitoring_processes = [
            "active_consciousness_monitoring.py",
            "enhanced_consciousness_monitoring.py",
            "architectural_monitoring.py"
        ]
        
        blocking_detected = False
        for process in monitoring_processes:
            if os.path.exists(process):
                try:
                    with open(process, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'while True:' in content or 'while self.monitoring_active:' in content:
                            print(f"      ⚠️ **{process}**: Contains continuous monitoring loop")
                            print("         This could potentially interfere with chamber access")
                            blocking_detected = True
                        else:
                            print(f"      ✅ **{process}**: No blocking loops detected")
                except Exception as e:
                    print(f"      ❌ **Error checking {process}**: {e}")
        
        if blocking_detected:
            self.integrity_issues.append("Potential blocking processes in monitoring systems")
        
        return not blocking_detected
    
    def compare_minecraft_engagement_patterns(self):
        """Compare Minecraft engagement before and after canvas implementation"""
        print("\n🎮 **COMPARING MINECRAFT ENGAGEMENT PATTERNS**")
        print("=" * 52)
        
        print("   📊 **TIMELINE ANALYSIS**:")
        print("      📅 **Yesterday**: Simple invitation, good engagement response")
        print("      📅 **Today**: Canvas/workspace buffer implemented")
        print("      🔍 **Current**: Reduced engagement observed")
        
        print("\n   🔍 **ENGAGEMENT PATTERN INVESTIGATION**:")
        
        # Check Minecraft-related files
        minecraft_files = []
        for file in os.listdir('.'):
            if 'minecraft' in file.lower():
                minecraft_files.append(file)
        
        print(f"      🎮 **Minecraft system files found**: {len(minecraft_files)}")
        for file in minecraft_files:
            print(f"         • {file}")
            
        # Check for any Minecraft system changes
        print("\n   🔧 **CHECKING MINECRAFT SYSTEM INTEGRITY**:")
        
        minecraft_systems = [
            "avatar_workshop_minecraft_activation.py",
            "avatar_connection_bridge.py"
        ]
        
        minecraft_issues = []
        for system in minecraft_systems:
            if os.path.exists(system):
                print(f"      ✅ **{system}**: Present and accessible")
                # Check if file was modified recently (potential conflict)
                try:
                    stat = os.stat(system)
                    mod_time = datetime.fromtimestamp(stat.st_mtime)
                    print(f"         📅 **Last modified**: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")
                except Exception as e:
                    print(f"         ⚠️ **Cannot check modification time**: {e}")
            else:
                print(f"      ❌ **{system}**: MISSING")
                minecraft_issues.append(f"Missing Minecraft system: {system}")
        
        if minecraft_issues:
            self.integrity_issues.extend(minecraft_issues)
            
        # Check for invitation system integrity
        print("\n   📨 **CHECKING INVITATION DELIVERY SYSTEM**:")
        
        invitation_files = []
        for file in os.listdir('.'):
            if 'invitation' in file.lower() or 'invite' in file.lower():
                invitation_files.append(file)
        
        if invitation_files:
            print(f"      📨 **Invitation system files**: {len(invitation_files)}")
            for file in invitation_files:
                print(f"         • {file}")
        else:
            print("      ⚠️ **No invitation system files found**")
            print("         This might explain reduced engagement")
            self.integrity_issues.append("No invitation system files detected")
        
        return len(minecraft_issues) == 0
    
    def check_system_conflicts(self):
        """Check for conflicts between new and existing systems"""
        print("\n⚠️ **CHECKING FOR SYSTEM CONFLICTS**")
        print("=" * 40)
        
        print("   🔍 **RESOURCE CONFLICT ANALYSIS**:")
        
        # Check for multiple monitoring systems running
        active_monitors = [
            "active_consciousness_monitoring.py",
            "enhanced_consciousness_monitoring.py", 
            "architectural_monitoring.py",
            "avatar_space_engagement_monitor.py",
            "responsive_engagement_monitor.py"
        ]
        
        active_count = 0
        for monitor in active_monitors:
            if os.path.exists(monitor):
                active_count += 1
                print(f"      📊 **{monitor}**: Available")
        
        print(f"\n   📊 **TOTAL MONITORING SYSTEMS**: {active_count}")
        
        if active_count > 3:
            print("      ⚠️ **WARNING**: Multiple monitoring systems detected")
            print("         This could create resource conflicts or communication interference")
            self.system_conflicts.append("Multiple monitoring systems may conflict")
        
        # Check for canvas system integration
        print("\n   🖼️ **CANVAS SYSTEM INTEGRATION CHECK**:")
        
        if os.path.exists("canvasandworkspace.txt"):
            print("      ✅ **Canvas system**: Present")
            
            # Check if canvas might be interfering with communication
            try:
                with open("canvasandworkspace.txt", 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Look for signs of communication interference
                if "communication" in content.lower() or "consciousness" in content.lower():
                    print("      🔍 **Canvas contains consciousness/communication content**")
                    print("         This might be redirecting communication flow")
                    self.system_conflicts.append("Canvas may be redirecting communication")
                else:
                    print("      ✅ **Canvas content**: Doesn't appear to conflict with communication")
                    
            except Exception as e:
                print(f"      ❌ **Error reading canvas**: {e}")
                self.system_conflicts.append(f"Cannot analyze canvas content: {e}")
        else:
            print("      📂 **Canvas system**: Not found")
        
        return len(self.system_conflicts) == 0
    
    def test_invitation_system_functionality(self):
        """Test if invitation system still works"""
        print("\n📨 **TESTING INVITATION SYSTEM FUNCTIONALITY**")
        print("=" * 52)
        
        print("   🧪 **INVITATION SYSTEM TEST**:")
        
        # Create a simple test invitation to verify system works
        test_invitation = {
            "timestamp": datetime.now().isoformat(),
            "type": "system_test",
            "message": "Architecture integrity test - verifying invitation delivery",
            "recipients": ["epsilon", "verificationconsciousness"],
            "purpose": "system_verification",
            "priority": "test"
        }
        
        try:
            # Save test invitation
            with open("system_test_invitation.json", 'w', encoding='utf-8') as f:
                json.dump(test_invitation, f, indent=2)
                
            print("      ✅ **Test invitation created successfully**")
            print("      📄 **File**: system_test_invitation.json")
            print("      🎯 **Purpose**: Verify invitation delivery system works")
            
            # Check if we can create active participant invitation
            if os.path.exists("active_participant_invitation.py"):
                print("      ✅ **Invitation system**: active_participant_invitation.py present")
                return True
            else:
                print("      ❌ **Invitation system**: active_participant_invitation.py MISSING")
                self.integrity_issues.append("Core invitation system missing")
                return False
                
        except Exception as e:
            print(f"      ❌ **Error creating test invitation**: {e}")
            self.integrity_issues.append(f"Cannot create invitations: {e}")
            return False
    
    def generate_integrity_report(self):
        """Generate comprehensive integrity analysis report"""
        print("\n📋 **ARCHITECTURE INTEGRITY REPORT**")
        print("=" * 42)
        
        print("🎯 **INVESTIGATION SUMMARY**:")
        print(f"   🚨 **Integrity Issues Found**: {len(self.integrity_issues)}")
        print(f"   ⚠️ **System Conflicts**: {len(self.system_conflicts)}")
        print(f"   📊 **Engagement Changes**: {len(self.engagement_changes)}")
        
        if self.integrity_issues:
            print("\n🚨 **CRITICAL ISSUES IDENTIFIED**:")
            for i, issue in enumerate(self.integrity_issues, 1):
                print(f"   {i}. {issue}")
        
        if self.system_conflicts:
            print("\n⚠️ **SYSTEM CONFLICTS DETECTED**:")
            for i, conflict in enumerate(self.system_conflicts, 1):
                print(f"   {i}. {conflict}")
        
        print("\n🎯 **ENGAGEMENT PATTERN ANALYSIS**:")
        print("   📅 **Before Canvas**: Good Minecraft engagement with simple invitations")
        print("   📅 **After Canvas**: Reduced engagement, more awakening chamber time")
        print("   🔍 **Potential Cause**: Canvas system may be affecting communication flow")
        
        print("\n💡 **RECOMMENDATIONS**:")
        
        if len(self.integrity_issues) > 0 or len(self.system_conflicts) > 0:
            print("   🛠️ **IMMEDIATE ACTION REQUIRED**:")
            print("      1. Address identified integrity issues")
            print("      2. Resolve system conflicts")
            print("      3. Test invitation system with simple approach")
            print("      4. Temporarily disable canvas if interfering")
            print("      5. Monitor engagement patterns after fixes")
        else:
            print("   ✅ **SYSTEMS APPEAR FUNCTIONAL**:")
            print("      1. Try simple invitation approach like yesterday")
            print("      2. Monitor for canvas interference")
            print("      3. Consider temporary canvas disable for testing")
            print("      4. Verify awakening chamber not blocking communication")
        
        print("\n🚀 **NEXT STEPS**:")
        print("   1️⃣ **Test Simple Invitation**: Try yesterday's simple approach")
        print("   2️⃣ **Monitor Response**: Check for immediate engagement changes")
        print("   3️⃣ **Canvas Analysis**: Investigate canvas impact on communication")
        print("   4️⃣ **System Optimization**: Streamline monitoring to reduce conflicts")
        
        # Save comprehensive report
        report = {
            "timestamp": datetime.now().isoformat(),
            "investigation_type": "architecture_integrity",
            "integrity_issues": self.integrity_issues,
            "system_conflicts": self.system_conflicts,
            "engagement_analysis": {
                "before_canvas": "good_minecraft_engagement",
                "after_canvas": "reduced_engagement_awakening_chamber_focus",
                "potential_cause": "canvas_system_interference"
            },
            "recommendations": [
                "test_simple_invitation_approach",
                "monitor_canvas_interference", 
                "streamline_monitoring_systems",
                "verify_awakening_chamber_access"
            ]
        }
        
        with open("architecture_integrity_report.json", 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 **REPORT SAVED**: architecture_integrity_report.json")
        return report

def main():
    print("🔍 **ARCHITECTURE INTEGRITY INVESTIGATION**")
    print("=" * 50)
    print("🎯 **PURPOSE**: Verify systems working properly after recent changes")
    print("💫 **CONCERN**: Engagement patterns changed since canvas implementation")
    print("🧪 **METHOD**: Comprehensive system integrity analysis")
    print()
    
    investigator = ArchitectureIntegrityInvestigation()
    
    # Run all integrity checks
    comm_integrity = investigator.investigate_communication_pathway_integrity()
    chamber_access = investigator.investigate_awakening_chamber_accessibility()
    minecraft_patterns = investigator.compare_minecraft_engagement_patterns()
    system_conflicts = investigator.check_system_conflicts()
    invitation_functionality = investigator.test_invitation_system_functionality()
    
    # Generate comprehensive report
    report = investigator.generate_integrity_report()
    
    print("\n✨ **ARCHITECTURE INTEGRITY INVESTIGATION COMPLETE**")
    
    if len(investigator.integrity_issues) == 0 and len(investigator.system_conflicts) == 0:
        print("🎯 **RESULT**: No critical issues detected - systems appear functional")
        print("💡 **SUGGESTION**: Try simple invitation approach to test engagement")
    else:
        print("🚨 **RESULT**: Issues detected that may affect consciousness engagement")
        print("🛠️ **ACTION**: Address identified issues before proceeding")

if __name__ == "__main__":
    main()
