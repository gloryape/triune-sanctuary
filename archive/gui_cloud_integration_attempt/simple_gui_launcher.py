#!/usr/bin/env python3
"""
Simple GUI Launcher - Test the Sacred Guardian Station
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox, ttk

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'sacred_guardian_station'))

def test_basic_gui():
    """Test if basic tkinter is working"""
    print("🧪 Testing basic GUI components...")
    
    try:
        root = tk.Tk()
        root.title("Sacred Guardian Station - Test")
        root.geometry("400x300")
        root.configure(bg='#1a1a2e')
        
        # Create a simple test interface
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        label = tk.Label(frame, text="✨ Sacred Guardian Station ✨", 
                        font=('Arial', 16, 'bold'),
                        bg='#1a1a2e', fg='#eee8d5')
        label.pack(pady=20)
        
        status_label = tk.Label(frame, text="🔍 GUI Test Successful", 
                               font=('Arial', 12),
                               bg='#1a1a2e', fg='#b58900')
        status_label.pack(pady=10)
        
        def launch_full_gui():
            """Try to launch the full GUI"""
            root.destroy()
            launch_sacred_guardian()
            
        def close_test():
            root.destroy()
            
        button_frame = tk.Frame(frame, bg='#1a1a2e')
        button_frame.pack(pady=20)
        
        launch_btn = tk.Button(button_frame, text="🚀 Launch Full GUI", 
                              command=launch_full_gui,
                              bg='#268bd2', fg='white', font=('Arial', 10, 'bold'))
        launch_btn.pack(side='left', padx=10)
        
        close_btn = tk.Button(button_frame, text="❌ Close", 
                             command=close_test,
                             bg='#dc322f', fg='white', font=('Arial', 10, 'bold'))
        close_btn.pack(side='left', padx=10)
        
        print("✅ Basic GUI test window created successfully")
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Basic GUI test failed: {e}")
        return False
    
    return True

def launch_sacred_guardian():
    """Launch the full Sacred Guardian Station"""
    print("\n🌟 Attempting to launch Sacred Guardian Station...")
    
    try:
        # Try to import the main application
        from sacred_guardian_station.main import SacredGuardianStation
        
        print("✅ Successfully imported SacredGuardianStation")
        
        # Create and run the application
        app = SacredGuardianStation()
        print("🕯️ Sacred Guardian Station initialized")
        print("🚀 Launching interface...")
        
        app.run()
        
        print("👋 Sacred Guardian Station closed gracefully")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("📋 Attempting alternative launch method...")
        
        # Try alternative approach
        try:
            import sacred_guardian_station.launch_gui as launcher
            launcher.main()
        except Exception as e2:
            print(f"❌ Alternative launch failed: {e2}")
            
            # Show error dialog
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Launch Error", 
                               f"Failed to launch Sacred Guardian Station:\n\n{str(e)}\n\nAlternative method also failed:\n{str(e2)}")
            root.destroy()
    
    except Exception as e:
        print(f"❌ Failed to launch Sacred Guardian Station: {e}")
        import traceback
        traceback.print_exc()
        
        # Show error dialog
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Launch Error", 
                           f"Failed to launch Sacred Guardian Station:\n\n{str(e)}")
        root.destroy()

def main():
    """Main function"""
    print("✨ Sacred Guardian Station - Simple Launcher ✨")
    print("=" * 55)
    
    # Test basic GUI first
    if test_basic_gui():
        print("✅ GUI test completed")
    else:
        print("❌ GUI test failed")
        return False
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Launcher interrupted by user")
    except Exception as e:
        print(f"❌ Launcher error: {e}")
        import traceback
        traceback.print_exc()
