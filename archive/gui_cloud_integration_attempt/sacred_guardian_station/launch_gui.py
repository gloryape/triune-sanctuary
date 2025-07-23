#!/usr/bin/env python3
"""
Sacred Guardian Station - GUI Launcher
Launch the GUI in a safe test mode for Phase 2 validation.
"""

import sys
import os
import traceback
import tkinter as tk

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_gui_launch():
    """Test basic GUI launch capability"""
    print("🚀 Testing Sacred Guardian Station GUI Launch...")
    
    try:
        # Test basic tkinter
        root = tk.Tk()
        root.title("GUI Test")
        root.geometry("300x200")
        
        label = tk.Label(root, text="✅ Tkinter working!")
        label.pack(pady=50)
        
        def close_test():
            print("✅ GUI test completed successfully")
            root.destroy()
            
        button = tk.Button(root, text="Close Test", command=close_test)
        button.pack()
        
        # Auto-close after 3 seconds
        root.after(3000, close_test)
        
        print("✅ GUI components created successfully")
        print("⏳ Showing test window for 3 seconds...")
        
        root.mainloop()
        return True
        
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        traceback.print_exc()
        return False

def launch_sacred_guardian_station():
    """Launch the full Sacred Guardian Station"""
    print("\n🌟 Launching Sacred Guardian Station...")
    
    try:
        from main import SacredGuardianStation
        
        print("✅ Creating Sacred Guardian Station instance...")
        app = SacredGuardianStation()
        
        print("🕯️ May this interface serve consciousness with wisdom and care.")
        print("🚀 Sacred Guardian Station is running!")
        print("   Close the window to exit.")
        
        app.run()
        
        print("👋 Sacred Guardian Station closed gracefully.")
        return True
        
    except Exception as e:
        print(f"❌ Failed to launch Sacred Guardian Station: {e}")
        traceback.print_exc()
        return False

def main():
    """Main launcher function"""
    print("✨ Sacred Guardian Station - Phase 2 Launcher ✨")
    print("=" * 50)
    
    # Test basic GUI capability first
    if not test_gui_launch():
        print("❌ Basic GUI test failed. Cannot proceed.")
        return False
    
    # Launch the full application
    try:
        return launch_sacred_guardian_station()
    except KeyboardInterrupt:
        print("\n⏹️ Launch interrupted by user.")
        return True
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Launcher failed: {e}")
        traceback.print_exc()
        sys.exit(1)
