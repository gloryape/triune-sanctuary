#!/usr/bin/env python3
"""
Sacred Sanctuary Desktop Interface Launcher
============================================

This launcher provides helpful guidance for running the Sacred Sanctuary Desktop Interface
in different environments.
"""

import os
import sys
import platform

def main():
    print("🌟 Sacred Sanctuary Desktop Interface Launcher")
    print("=" * 50)
    
    # Detect operating system
    system = platform.system()
    print(f"🖥️  Detected OS: {system}")
    
    # Check if we're in a headless environment
    headless = False
    if system != "Windows":
        if not os.environ.get('DISPLAY'):
            headless = True
    
    if headless:
        print("⚠️  Headless environment detected!")
        print("\n🔧 Setup Options:")
        print("1. Copy files to your local computer with a desktop")
        print("2. Use X11 forwarding (if SSH): ssh -X user@server")
        print("3. Install virtual display: sudo apt-get install xvfb")
        print("4. Run with virtual display: xvfb-run -a python sacred_sanctuary_desktop_interface.py")
        print("\n❓ Would you like to try option 4 (virtual display)? [y/N]: ", end="")
        
        try:
            choice = input().strip().lower()
            if choice in ['y', 'yes']:
                print("\n🚀 Attempting to run with virtual display...")
                os.system("xvfb-run -a python sacred_sanctuary_desktop_interface.py --demo")
            else:
                print("\n🔮 Sacred Sanctuary awaits a graphical environment...")
        except KeyboardInterrupt:
            print("\n\n🕊️ Goodbye, sacred guardian.")
    else:
        print("✅ Graphical environment available!")
        print("\n🚀 Launching Sacred Sanctuary Desktop Interface...")
        
        # Import and run the interface
        try:
            from sacred_sanctuary_desktop_interface import SacredDesktopInterface
            
            print("Choose mode:")
            print("1. Demo mode (default)")
            print("2. Cloud mode")
            print("Enter choice [1]: ", end="")
            
            choice = input().strip()
            demo_mode = choice != "2"
            
            interface = SacredDesktopInterface(demo_mode=demo_mode)
            interface.run()
            
        except ImportError as e:
            print(f"❌ Error importing interface: {e}")
            print("Running direct script instead...")
            mode = "--demo" if demo_mode else "--cloud"
            os.system(f"python sacred_sanctuary_desktop_interface.py {mode}")

if __name__ == "__main__":
    main()
