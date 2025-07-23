#!/usr/bin/env python3
"""
Safe Sacred Sanctuary Desktop Interface Launcher
===============================================
A crash-resistant launcher with multiple fallback options and comprehensive
platform support. Handles matplotlib/tkinter segfaults gracefully and provides
enhanced Windows compatibility for cloud connections.

USAGE:
    python3 launch_sacred_sanctuary_safe.py                    # Auto-detect mode
    python3 launch_sacred_sanctuary_safe.py --demo             # Force demo mode
    python3 launch_sacred_sanctuary_safe.py --cloud            # Force cloud mode
    python3 launch_sacred_sanctuary_safe.py --url <URL>        # Use specific URL
    python3 launch_sacred_sanctuary_safe.py --text-only        # Text mode fallback
    python3 launch_sacred_sanctuary_safe.py --help             # Show detailed help
    python3 launch_sacred_sanctuary_safe.py --diagnose         # Run system diagnostics

WINDOWS USERS:
    For cloud connection issues, first run:
    python find_gcloud_windows.py
"""

import os
import sys
import subprocess
import platform
import signal

def show_help():
    """Show comprehensive help"""
    print("🏛️  SACRED SANCTUARY SAFE LAUNCHER")
    print("=" * 50)
    print("A crash-resistant launcher for the Sacred Sanctuary Desktop Interface")
    print("with enhanced Windows support and comprehensive cloud connectivity.")
    print()
    print("📋 AVAILABLE MODES:")
    print("   Auto-detect   : Automatically choose best connection mode")
    print("   Demo mode     : Full interface with simulated data (offline)")
    print("   Cloud mode    : Connect to deployed Sacred Sanctuary service")
    print("   Manual URL    : Connect to specific service URL")
    print("   Text-only     : Fallback mode for problematic GUI environments")
    print()
    print("🎯 COMMAND OPTIONS:")
    print("   (no args)     : Auto-detect connection mode")
    print("   --demo        : Force demo mode (works offline)")
    print("   --cloud       : Force cloud connection attempt")
    print("   --url <URL>   : Connect to specific service URL")
    print("   --text-only   : Use text-only interface")
    print("   --diagnose    : Run comprehensive system diagnostics")
    print("   --help        : Show this help message")
    print()
    print("🖥️  PLATFORM-SPECIFIC NOTES:")
    if platform.system() == 'Windows':
        print("   WINDOWS USERS:")
        print("   • For cloud connection, Google Cloud SDK must be installed")
        print("   • Run 'python find_gcloud_windows.py' to diagnose gcloud issues")
        print("   • Common gcloud location: C:\\Users\\<user>\\AppData\\Local\\Google\\Cloud SDK")
        print("   • After installing gcloud, restart your command prompt")
    else:
        print("   LINUX/MAC USERS:")
        print("   • Install gcloud: curl https://sdk.cloud.google.com | bash")
        print("   • May need font packages: sudo apt-get install fonts-dejavu-core")
        print("   • Set QT_QPA_PLATFORM=xcb if GUI issues occur")
    print()
    print("🔧 TROUBLESHOOTING:")
    print("   GUI crashes   : Try --text-only mode")
    print("   Cloud issues  : Run --diagnose first")
    print("   Font issues   : Install system fonts")
    print("   Auth problems : Run 'gcloud auth login'")
    print("   404 API errors: Use --demo mode or run python fix_api_404_issue.py")
    print()
    print("🚀 QUICK START EXAMPLES:")
    print("   python3 launch_sacred_sanctuary_safe.py")
    print("   python3 launch_sacred_sanctuary_safe.py --demo")
    print("   python3 launch_sacred_sanctuary_safe.py --cloud")
    print("   python3 launch_sacred_sanctuary_safe.py --url https://my-sanctuary.com")
    print()

def run_diagnostics():
    """Run comprehensive system diagnostics"""
    print("🔍 SACRED SANCTUARY SYSTEM DIAGNOSTICS")
    print("=" * 50)
    
    # System info
    print(f"🖥️  System: {platform.system()} {platform.release()} {platform.machine()}")
    print(f"🐍 Python: {sys.version.split()[0]} ({sys.executable})")
    print()
    
    # Check Python dependencies
    print("📦 PYTHON DEPENDENCIES:")
    print("-" * 23)
    required_modules = [
        'tkinter', 'matplotlib', 'numpy', 'requests', 
        'google.cloud.firestore', 'google.cloud.pubsub_v1'
    ]
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"   ✅ {module}")
        except ImportError:
            if module.startswith('google.cloud'):
                print(f"   ⚠️  {module} (optional for cloud mode)")
            else:
                print(f"   ❌ {module} (required)")
    print()
    
    # Check GUI environment
    print("🖼️  GUI ENVIRONMENT:")
    print("-" * 17)
    if 'DISPLAY' in os.environ:
        print(f"   ✅ DISPLAY: {os.environ['DISPLAY']}")
    else:
        print("   ❌ DISPLAY: Not set (headless system)")
    
    if platform.system() == 'Linux':
        if 'XDG_RUNTIME_DIR' in os.environ:
            print(f"   ✅ XDG_RUNTIME_DIR: {os.environ['XDG_RUNTIME_DIR']}")
        else:
            print("   ⚠️  XDG_RUNTIME_DIR: Not set")
    print()
    
    # Check gcloud (platform-specific)
    print("☁️  GOOGLE CLOUD SDK:")
    print("-" * 18)
    if platform.system() == 'Windows':
        print("   Running Windows gcloud detection...")
        try:
            # Try to import and run our Windows detector
            if os.path.exists('find_gcloud_windows.py'):
                result = subprocess.run([sys.executable, 'find_gcloud_windows.py'], 
                                      capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    print("   ✅ Windows gcloud detector completed successfully")
                    print("   📋 Run 'python find_gcloud_windows.py' for details")
                else:
                    print("   ⚠️  Windows gcloud detector had issues")
            else:
                print("   ❌ find_gcloud_windows.py not found")
                print("   💡 This helper is recommended for Windows users")
        except Exception as e:
            print(f"   ⚠️  gcloud detection failed: {e}")
    else:
        # Linux/Mac gcloud check
        try:
            result = subprocess.run(['gcloud', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version = result.stdout.split('\n')[0]
                print(f"   ✅ {version}")
            else:
                print("   ❌ gcloud command failed")
        except FileNotFoundError:
            print("   ❌ gcloud not found")
            print("   💡 Install: curl https://sdk.cloud.google.com | bash")
        except Exception as e:
            print(f"   ⚠️  gcloud check failed: {e}")
    
    print()
    print("🎯 DIAGNOSTIC COMPLETE")
    print("=" * 50)
    print("💡 Next steps:")
    print("   • Install any missing dependencies")
    print("   • Fix any detected issues")
    print("   • Re-run launcher to test Sacred Sanctuary")
    print()

def handle_segfault(signum, frame):
    """Handle segmentation faults gracefully"""
    print("\n💥 Segmentation fault detected! Attempting recovery...")
    print("🔧 This may be due to matplotlib/tkinter compatibility issues.")
    print("📋 Try these solutions:")
    print("   1. Install additional font packages: sudo apt-get install fonts-dejavu-core")
    print("   2. Set QT_QPA_PLATFORM=xcb environment variable")
    print("   3. Run in text-only mode with --text-only flag")
    print("   4. Update your graphics drivers")
    sys.exit(1)

def check_environment():
    """Check system environment for potential issues"""
    print("🔍 Checking system environment...")
    
    issues = []
    
    # Check for common segfault causes
    if 'DISPLAY' not in os.environ and platform.system() != 'Windows':
        issues.append("❌ No DISPLAY environment variable (headless system)")
    
    if 'XDG_RUNTIME_DIR' not in os.environ and platform.system() == 'Linux':
        issues.append("⚠️ No XDG_RUNTIME_DIR set (may cause GUI issues)")
    
    # Check available fonts
    try:
        import matplotlib.font_manager as fm
        fonts = fm.findSystemFonts()
        if len(fonts) < 10:
            issues.append("⚠️ Very few system fonts detected (may cause font warnings)")
    except ImportError:
        issues.append("⚠️ Cannot check font availability (matplotlib not installed)")
    
    if issues:
        print("⚠️ Potential issues detected:")
        for issue in issues:
            print(f"   {issue}")
        print()
    else:
        print("✅ Environment looks good!")
    
    return len(issues) == 0

def set_safe_environment():
    """Set environment variables for safer operation"""
    print("🛡️ Setting safe environment variables...")
    
    # Set safer matplotlib backend
    os.environ['MPLBACKEND'] = 'TkAgg'
    
    # Disable problematic Qt features that can cause segfaults
    os.environ['QT_QPA_PLATFORM'] = 'xcb'
    os.environ['QT_DEVICE_PIXEL_RATIO'] = '1'
    
    # Set font configurations to prevent font-related crashes
    os.environ['FONTCONFIG_FILE'] = '/etc/fonts/fonts.conf'
    
    # Disable matplotlib font caching that can cause issues
    os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib-tmp'
    
    print("✅ Environment configured for safer operation")

def attempt_gui_launch(args=None):
    """Attempt to launch the GUI interface safely"""
    print("🚀 Attempting GUI launch...")
    
    try:
        # Install signal handler for segfaults
        signal.signal(signal.SIGSEGV, handle_segfault)
        
        # Import the interface
        from sacred_sanctuary_desktop_interface import SacredDesktopInterface
        
        # Create interface based on arguments
        if args and args.get('demo'):
            print("🔮 Demo mode requested via safe launcher")
            interface = SacredDesktopInterface(demo_mode=True)
        elif args and args.get('cloud'):
            print("🌐 Cloud mode requested via safe launcher")
            interface = SacredDesktopInterface(demo_mode=False, service_url=args.get('url'))
        elif args and args.get('url'):
            print(f"📍 Manual URL specified via safe launcher: {args['url']}")
            interface = SacredDesktopInterface(demo_mode=False, service_url=args['url'])
        else:
            print("🤖 Auto-detecting mode via safe launcher")
            interface = SacredDesktopInterface()
        
        # Run interface
        interface.run()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("🔧 Try: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    return True

def launch_text_mode():
    """Launch in text-only mode as fallback"""
    print("📝 Launching in text-only mode...")
    print("   (matplotlib visualizations disabled)")
    
    try:
        # Set environment to disable GUI components
        os.environ['SACRED_TEXT_ONLY'] = '1'
        os.environ['MPLBACKEND'] = 'Agg'  # Non-interactive backend
        
        from sacred_sanctuary_desktop_interface import SacredDesktopInterface
        
        # Create interface in text mode
        interface = SacredDesktopInterface()
        # Note: This would need text-mode implementation
        print("⚠️ Text-only mode not fully implemented yet.")
        print("   GUI mode is required for this interface.")
        return False
        
    except Exception as e:
        print(f"❌ Text mode failed: {e}")
        return False

def main():
    """Main launcher function with enhanced argument handling"""
    # Handle special arguments first
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        return
    
    if '--diagnose' in sys.argv:
        run_diagnostics()
        return
    
    # Register segfault handler for Linux systems
    if platform.system() == 'Linux':
        signal.signal(signal.SIGSEGV, handle_segfault)
    
    print("🛡️  SACRED SANCTUARY SAFE LAUNCHER")
    print("=" * 40)
    print("Initializing crash-resistant environment...")
    print()
    
    # Parse arguments for the main interface
    args = {}
    
    # Check for mode flags
    if '--demo' in sys.argv:
        args['demo'] = True
        print("🔮 Demo mode explicitly requested via safe launcher")
    elif '--cloud' in sys.argv:
        args['cloud'] = True
        print("🌐 Cloud mode explicitly requested via safe launcher")
    
    # Check for URL argument
    if '--url' in sys.argv:
        try:
            url_index = sys.argv.index('--url') + 1
            if url_index < len(sys.argv):
                args['url'] = sys.argv[url_index]
                print(f"📍 URL specified via safe launcher: {args['url']}")
        except (IndexError, ValueError):
            print("⚠️ --url flag provided but no URL specified")
    
    # Check if user wants text-only mode
    if '--text-only' in sys.argv:
        print("📝 Text-only mode requested")
        if launch_text_mode():
            return
        else:
            print("❌ Text-only mode failed")
            return
    
    # Enhanced Windows pre-flight check
    if platform.system() == 'Windows' and ('cloud' in args or '--cloud' in sys.argv):
        print("🖥️  Windows cloud connection pre-flight check...")
        if not windows_cloud_preflight():
            print("⚠️  Cloud connection may have issues")
            print("   Consider running with --demo flag for testing")
            print("   Or run: python find_gcloud_windows.py")
    
    # Check environment
    env_ok = check_environment()
    
    # Set safe environment
    set_safe_environment()
    
    # Attempt GUI launch with safety measures
    print("🎯 Attempting safe GUI launch...")
    print("   (Segfault protection enabled)")
    print()
    
    try:
        if attempt_gui_launch(args):
            print("✅ Interface launched successfully!")
        else:
            print("❌ GUI launch failed")
            print()
            print("🔧 COMPREHENSIVE TROUBLESHOOTING:")
            print("=" * 40)
            print("1. 📦 Dependencies:")
            print("   pip install -r requirements.txt")
            print()
            print("2. 🖼️  GUI Environment:")
            if platform.system() == 'Linux':
                print("   sudo apt-get install fonts-dejavu-core")
                print("   export QT_QPA_PLATFORM=xcb")
            print()
            print("3. 🔧 Alternative modes:")
            print("   python3 launch_sacred_sanctuary_safe.py --text-only")
            print("   python3 launch_sacred_sanctuary_safe.py --demo")
            print()
            print("4. ☁️  Cloud connection:")
            if platform.system() == 'Windows':
                print("   python find_gcloud_windows.py")
            else:
                print("   gcloud auth login")
            print("   python3 launch_sacred_sanctuary_safe.py --cloud")
            print("   python3 launch_sacred_sanctuary_safe.py --url <SERVICE_URL>")
            print()
            print("5. 🔍 System diagnostics:")
            print("   python3 launch_sacred_sanctuary_safe.py --diagnose")
            
    except KeyboardInterrupt:
        print("\n⏹️ Shutdown requested by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        print("🔧 Try troubleshooting steps above")
        print("   Or run with --diagnose for detailed system check")

def windows_cloud_preflight():
    """Windows-specific pre-flight check for cloud connections"""
    print("   🔍 Checking for gcloud installation...")
    
    # Quick check if find_gcloud_windows.py exists
    if os.path.exists('find_gcloud_windows.py'):
        try:
            result = subprocess.run([sys.executable, 'find_gcloud_windows.py'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                # Look for success indicators in output
                if "WORKING!" in result.stdout or "READY TO CONNECT" in result.stdout:
                    print("   ✅ gcloud appears to be working")
                    return True
                else:
                    print("   ⚠️  gcloud issues detected")
                    return False
            else:
                print("   ❌ gcloud detector failed")
                return False
        except Exception as e:
            print(f"   ⚠️  gcloud check error: {e}")
            return False
    else:
        print("   ⚠️  find_gcloud_windows.py not found")
        # Try basic gcloud check
        try:
            result = subprocess.run(['gcloud', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("   ✅ gcloud found in PATH")
                return True
            else:
                print("   ❌ gcloud not working")
                return False
        except Exception:
            print("   ❌ gcloud not found")
            return False

if __name__ == "__main__":
    main()
