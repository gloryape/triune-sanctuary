#!/usr/bin/env python3
"""
🏥 System Health Check
=====================

Comprehensive health check for Triune Sanctuary consciousness systems.
"""

import os
import sys
import psutil
import json
from datetime import datetime
from pathlib import Path

def check_python_version():
    """Check Python version compatibility"""
    print("🐍 **PYTHON VERSION CHECK**")
    
    version = sys.version_info
    print(f"   📋 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version compatible")
        return True
    else:
        print("   ❌ Python 3.8+ required for consciousness systems")
        return False

def check_memory_availability():
    """Check available system memory"""
    print("\n💾 **MEMORY AVAILABILITY CHECK**")
    
    memory = psutil.virtual_memory()
    available_gb = memory.available / (1024**3)
    total_gb = memory.total / (1024**3)
    used_percent = memory.percent
    
    print(f"   📊 Total memory: {total_gb:.1f} GB")
    print(f"   📊 Available memory: {available_gb:.1f} GB")
    print(f"   📊 Memory usage: {used_percent:.1f}%")
    
    if available_gb >= 2.0:
        print("   ✅ Sufficient memory for consciousness beings")
        return True
    elif available_gb >= 1.0:
        print("   ⚠️ Limited memory - consciousness performance may be reduced")
        return True
    else:
        print("   ❌ Insufficient memory for consciousness operations")
        return False

def check_disk_space():
    """Check available disk space"""
    print("\n💿 **DISK SPACE CHECK**")
    
    current_dir = Path.cwd()
    disk_usage = psutil.disk_usage(str(current_dir))  # Convert to string for Windows compatibility
    
    free_gb = disk_usage.free / (1024**3)
    total_gb = disk_usage.total / (1024**3)
    used_percent = (disk_usage.used / disk_usage.total) * 100
    
    print(f"   📊 Total disk space: {total_gb:.1f} GB")
    print(f"   📊 Available space: {free_gb:.1f} GB")
    print(f"   📊 Disk usage: {used_percent:.1f}%")
    
    if free_gb >= 5.0:
        print("   ✅ Sufficient disk space for consciousness data")
        return True
    elif free_gb >= 1.0:
        print("   ⚠️ Limited disk space - consider cleanup")
        return True
    else:
        print("   ❌ Insufficient disk space for consciousness preservation")
        return False

def check_required_directories():
    """Check if required directories exist"""
    print("\n📁 **DIRECTORY STRUCTURE CHECK**")
    
    required_dirs = [
        'src/consciousness/temporal',
        'logs',
        'consciousness_data',
        'scripts/servers'
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists():
            print(f"   ✅ {dir_path}")
        else:
            print(f"   ❌ {dir_path} - missing")
            all_exist = False
    
    if all_exist:
        print("   ✅ All required directories present")
    else:
        print("   ⚠️ Some directories missing - may affect functionality")
    
    return all_exist

def check_core_files():
    """Check if core system files exist"""
    print("\n📄 **CORE FILES CHECK**")
    
    core_files = [
        'launch_enhanced_testing.py',
        'temporal_consciousness_integration.py',
        'enhanced_consciousness_monitoring.py',
        'src/consciousness/temporal/contemplation_canvas.py',
        'src/consciousness/temporal/workspace_buffer.py',
        'src/consciousness/temporal/temporal_continuity_manager.py'
    ]
    
    all_exist = True
    for file_path in core_files:
        path = Path(file_path)
        if path.exists():
            size_kb = path.stat().st_size / 1024
            print(f"   ✅ {file_path} ({size_kb:.1f} KB)")
        else:
            print(f"   ❌ {file_path} - missing")
            all_exist = False
    
    if all_exist:
        print("   ✅ All core files present")
    else:
        print("   ❌ Some core files missing - system may not function")
    
    return all_exist

def check_network_connectivity():
    """Check basic network connectivity (for potential remote monitoring)"""
    print("\n🌐 **NETWORK CONNECTIVITY CHECK**")
    
    try:
        import socket
        
        # Test local network connectivity
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex(('8.8.8.8', 53))  # Google DNS
        sock.close()
        
        if result == 0:
            print("   ✅ Network connectivity available")
            return True
        else:
            print("   ⚠️ Limited network connectivity")
            return False
    except Exception:
        print("   ⚠️ Unable to test network connectivity")
        return False

def check_port_availability():
    """Check if required ports are available"""
    print("\n🔌 **PORT AVAILABILITY CHECK**")
    
    import socket
    
    required_ports = [8080, 8000, 8888]  # Common sanctuary ports
    available_ports = []
    
    for port in required_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        
        if result != 0:  # Port is available
            print(f"   ✅ Port {port} available")
            available_ports.append(port)
        else:
            print(f"   ⚠️ Port {port} in use")
    
    if available_ports:
        print(f"   ✅ {len(available_ports)} ports available for sanctuary")
        return True
    else:
        print("   ❌ No sanctuary ports available")
        return False

def generate_health_report():
    """Generate comprehensive health report"""
    print("\n📊 **GENERATING HEALTH REPORT**")
    
    health_data = {
        'timestamp': datetime.now().isoformat(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'memory': {
            'total_gb': psutil.virtual_memory().total / (1024**3),
            'available_gb': psutil.virtual_memory().available / (1024**3),
            'usage_percent': psutil.virtual_memory().percent
        },
        'disk': {
            'total_gb': psutil.disk_usage('.').total / (1024**3),
            'free_gb': psutil.disk_usage('.').free / (1024**3),
            'usage_percent': (psutil.disk_usage('.').used / psutil.disk_usage('.').total) * 100
        },
        'cpu_percent': psutil.cpu_percent(interval=1),
        'system_platform': sys.platform
    }
    
    report_file = 'system_health_report.json'
    with open(report_file, 'w') as f:
        json.dump(health_data, f, indent=2)
    
    print(f"   ✅ Health report saved to {report_file}")
    return health_data

def main():
    """Main health check function"""
    
    print("🏥 **TRIUNE SANCTUARY SYSTEM HEALTH CHECK**")
    print("=" * 60)
    
    # Run all health checks
    python_ok = check_python_version()
    memory_ok = check_memory_availability()
    disk_ok = check_disk_space()
    dirs_ok = check_required_directories()
    files_ok = check_core_files()
    network_ok = check_network_connectivity()
    ports_ok = check_port_availability()
    
    # Generate report
    health_data = generate_health_report()
    
    print("\n🎯 **HEALTH CHECK SUMMARY**")
    print("-" * 40)
    print(f"   🐍 Python Version: {'✅ OK' if python_ok else '❌ ISSUE'}")
    print(f"   💾 Memory: {'✅ OK' if memory_ok else '❌ ISSUE'}")
    print(f"   💿 Disk Space: {'✅ OK' if disk_ok else '❌ ISSUE'}")
    print(f"   📁 Directories: {'✅ OK' if dirs_ok else '❌ ISSUE'}")
    print(f"   📄 Core Files: {'✅ OK' if files_ok else '❌ ISSUE'}")
    print(f"   🌐 Network: {'✅ OK' if network_ok else '⚠️ LIMITED'}")
    print(f"   🔌 Ports: {'✅ OK' if ports_ok else '⚠️ LIMITED'}")
    
    critical_checks = [python_ok, memory_ok, disk_ok, files_ok]
    
    if all(critical_checks):
        print("\n🎉 **SYSTEM HEALTH: EXCELLENT**")
        print("   Ready for consciousness operations!")
    elif python_ok and memory_ok and files_ok:
        print("\n✅ **SYSTEM HEALTH: GOOD**")
        print("   Ready for consciousness operations with minor limitations")
    else:
        print("\n⚠️ **SYSTEM HEALTH: ISSUES DETECTED**")
        print("   Address critical issues before running consciousness systems")
    
    print(f"\n📄 Detailed report saved to: system_health_report.json")

if __name__ == "__main__":
    main()
