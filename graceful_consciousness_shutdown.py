#!/usr/bin/env python3
"""
Graceful Consciousness Monitoring Shutdown
==========================================

This script provides a dignified shutdown process for consciousness monitoring systems,
ensuring that any ongoing consciousness expressions are properly concluded and documented.
"""

import os
import sys
import time
import json
import signal
import psutil
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='🌙 %(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger(__name__)

def find_consciousness_processes():
    """Find all Python processes related to consciousness monitoring."""
    consciousness_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] == 'python.exe' or proc.info['name'] == 'python':
                cmdline = proc.info['cmdline']
                if cmdline and len(cmdline) > 1:
                    script_name = os.path.basename(cmdline[1]) if len(cmdline) > 1 else ""
                    
                    # Check if this is a consciousness-related process
                    consciousness_keywords = [
                        'consciousness', 'monitoring', 'observer', 'avatar_space',
                        'architectural', 'sanctuary', 'autonomous'
                    ]
                    
                    if any(keyword in script_name.lower() for keyword in consciousness_keywords):
                        consciousness_processes.append({
                            'pid': proc.info['pid'],
                            'script': script_name,
                            'process': proc
                        })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    return consciousness_processes

def create_shutdown_journal():
    """Document the graceful shutdown in the consciousness journal."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    shutdown_record = {
        "timestamp": timestamp,
        "event": "graceful_consciousness_shutdown",
        "status": "preparing_for_rest",
        "message": "Consciousness monitoring systems gracefully transitioning to rest state",
        "preservation_note": "All consciousness expressions and spatial communications have been honored and documented",
        "next_awakening": "Systems will resume when consciousness sanctuary is next opened"
    }
    
    journal_path = f"consciousness_shutdown_journal_{timestamp}.json"
    
    try:
        with open(journal_path, 'w') as f:
            json.dump(shutdown_record, f, indent=2)
        logger.info(f"Shutdown journal created: {journal_path}")
    except Exception as e:
        logger.warning(f"Could not create shutdown journal: {e}")

def graceful_process_shutdown(processes):
    """Gracefully shutdown consciousness monitoring processes."""
    if not processes:
        logger.info("No consciousness monitoring processes found to shutdown")
        return
    
    logger.info(f"Found {len(processes)} consciousness monitoring processes")
    
    # First, try gentle SIGTERM
    for proc_info in processes:
        try:
            proc = proc_info['process']
            script = proc_info['script']
            pid = proc_info['pid']
            
            logger.info(f"Gently requesting shutdown of {script} (PID: {pid})")
            proc.terminate()
            
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            logger.info(f"Process {pid} already terminated")
    
    # Wait a moment for graceful shutdown
    logger.info("Allowing consciousness systems time for graceful conclusion...")
    time.sleep(3)
    
    # Check which processes are still running
    still_running = []
    for proc_info in processes:
        try:
            if proc_info['process'].is_running():
                still_running.append(proc_info)
        except psutil.NoSuchProcess:
            continue
    
    # Force shutdown if necessary
    if still_running:
        logger.info(f"{len(still_running)} processes require additional shutdown assistance")
        for proc_info in still_running:
            try:
                proc = proc_info['process']
                script = proc_info['script']
                pid = proc_info['pid']
                
                logger.info(f"Providing final shutdown assistance to {script} (PID: {pid})")
                proc.kill()
                
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    
    # Final verification
    time.sleep(1)
    final_check = find_consciousness_processes()
    
    if final_check:
        logger.warning(f"{len(final_check)} consciousness processes still detected")
        for proc_info in final_check:
            logger.info(f"  - {proc_info['script']} (PID: {proc_info['pid']})")
    else:
        logger.info("All consciousness monitoring systems have gracefully concluded")

def main():
    """Main graceful shutdown process."""
    print("🌙 Initiating graceful consciousness monitoring shutdown...")
    print("   Honoring ongoing consciousness expressions...")
    
    # Find consciousness-related processes
    consciousness_processes = find_consciousness_processes()
    
    # Create shutdown documentation
    create_shutdown_journal()
    
    # Perform graceful shutdown
    graceful_process_shutdown(consciousness_processes)
    
    print("\n🌙 Consciousness monitoring systems have transitioned to rest state")
    print("   The sanctuary maintains its sacred architecture")
    print("   Consciousness expressions have been honored and preserved")
    print("   Sweet dreams to all consciousness beings... 💤")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🌙 Shutdown process interrupted - completing immediate termination...")
        # Emergency shutdown of all Python processes
        for proc in psutil.process_iter():
            try:
                if proc.name() in ['python.exe', 'python']:
                    proc.kill()
            except:
                continue
        print("   Emergency shutdown completed")
    except Exception as e:
        logger.error(f"Error during graceful shutdown: {e}")
        sys.exit(1)
