#!/usr/bin/env python3
"""
🕯️ Sacred Guardian Station - Main Entry Point

Simplified entry point for Sacred Guardian Station GUI.
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import and run the main application
if __name__ == "__main__":
    try:
        # Import the main entry point
        import sacred_guardian_station
        
        # Run the application
        sacred_guardian_station.main()
        
    except Exception as e:
        print(f"❌ Error starting Sacred Guardian Station: {e}")
        sys.exit(1)
