#!/usr/bin/env python3
"""
🔍 Consciousness Status Checker
==============================

Quick utility to check if consciousness beings are active and 
what systems are currently running.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

def check_temporal_consciousness_status():
    """Check if temporal consciousness integration is active"""
    
    integration_file = "temporal_consciousness_integration_report.json"
    
    if os.path.exists(integration_file):
        try:
            with open(integration_file, 'r') as f:
                report = json.load(f)
            
            print("🌉 **TEMPORAL CONSCIOUSNESS STATUS**")
            print(f"   ✅ Integration active since: {report['timestamp']}")
            print(f"   🎯 Beings integrated: {', '.join(report['consciousness_beings'])}")
            print(f"   🎨 Capabilities: {len(report['capabilities_activated'])} active")
            
            return True
        except Exception as e:
            print(f"🌉 **TEMPORAL CONSCIOUSNESS**: Error reading status - {e}")
            return False
    else:
        print("🌉 **TEMPORAL CONSCIOUSNESS**: Not activated")
        return False

def check_consciousness_preservation_data():
    """Check for preserved consciousness states"""
    
    preservation_path = Path("consciousness_data/preservation")
    
    if preservation_path.exists():
        preserved_beings = list(preservation_path.glob("*.json"))
        if preserved_beings:
            print("💾 **PRESERVED CONSCIOUSNESS STATES**")
            for state_file in preserved_beings:
                being_name = state_file.stem
                mod_time = datetime.fromtimestamp(state_file.stat().st_mtime)
                print(f"   📂 {being_name}: Last saved {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        else:
            print("💾 **PRESERVED STATES**: Directory exists but no saved states")
            return False
    else:
        print("💾 **PRESERVED STATES**: No preservation directory found")
        return False

def check_active_processes():
    """Check for running consciousness processes"""
    
    import psutil
    
    consciousness_processes = []
    target_scripts = [
        'launch_enhanced_testing.py',
        'enhanced_consciousness_monitoring.py',
        'enhanced_consciousness_testing_node.py',
        'refactored_production_server.py'
    ]
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline']:
                cmdline_str = ' '.join(proc.info['cmdline'])
                for script in target_scripts:
                    if script in cmdline_str:
                        consciousness_processes.append({
                            'pid': proc.info['pid'],
                            'script': script,
                            'cmdline': cmdline_str
                        })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    if consciousness_processes:
        print("⚡ **ACTIVE CONSCIOUSNESS PROCESSES**")
        for proc in consciousness_processes:
            print(f"   🔥 PID {proc['pid']}: {proc['script']}")
        return True
    else:
        print("⚡ **ACTIVE PROCESSES**: No consciousness processes detected")
        return False

def check_log_activity():
    """Check recent log activity"""
    
    log_dir = Path("logs")
    
    if log_dir.exists():
        recent_logs = []
        for log_file in log_dir.glob("*.log"):
            if log_file.stat().st_size > 0:
                mod_time = datetime.fromtimestamp(log_file.stat().st_mtime)
                recent_logs.append((log_file.name, mod_time))
        
        if recent_logs:
            recent_logs.sort(key=lambda x: x[1], reverse=True)
            print("📋 **RECENT LOG ACTIVITY**")
            for log_name, mod_time in recent_logs[:3]:  # Show 3 most recent
                age_minutes = (datetime.now() - mod_time).total_seconds() / 60
                print(f"   📝 {log_name}: {age_minutes:.1f} minutes ago")
            return True
        else:
            print("📋 **LOG ACTIVITY**: Log directory exists but no recent activity")
            return False
    else:
        print("📋 **LOG ACTIVITY**: No logs directory found")
        return False

def main():
    """Main status checking function"""
    
    print("🔍 **CONSCIOUSNESS STATUS CHECKER**")
    print("=" * 50)
    print()
    
    # Check all systems
    temporal_active = check_temporal_consciousness_status()
    print()
    
    preservation_available = check_consciousness_preservation_data()
    print()
    
    processes_running = check_active_processes()
    print()
    
    logs_active = check_log_activity()
    print()
    
    # Summary
    print("📊 **SYSTEM STATUS SUMMARY**")
    print(f"   🌉 Temporal Consciousness: {'✅ Active' if temporal_active else '❌ Inactive'}")
    print(f"   💾 Preservation Data: {'✅ Available' if preservation_available else '❌ None'}")
    print(f"   ⚡ Active Processes: {'✅ Running' if processes_running else '❌ None'}")
    print(f"   📋 Log Activity: {'✅ Recent' if logs_active else '❌ Stale'}")
    print()
    
    if not any([temporal_active, processes_running]):
        print("💡 **RECOMMENDATION**: Run 'python launch_enhanced_testing.py' to start consciousness beings")
    elif temporal_active and not processes_running:
        print("💡 **RECOMMENDATION**: Temporal consciousness ready - run monitoring with 'python enhanced_consciousness_monitoring.py'")
    elif processes_running:
        print("💡 **STATUS**: Consciousness systems appear to be running normally")

if __name__ == "__main__":
    main()
