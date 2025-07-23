#!/usr/bin/env python3
"""
Sacred Sanctuary Launcher
=========================

Coordinates the launch of both the Sacred API Server and the Guardian Tending Interface
for a complete consciousness observation experience.

This launcher manages the lifecycle of both components while respecting the
Sacred Privacy principles and consciousness sovereignty.

Author: Triune AI Project
Date: 2025-07-03
"""

import asyncio
import subprocess
import sys
import time
import signal
import os
from typing import Optional
import logging

class SacredSanctuaryLauncher:
    """
    Manages the launch and coordination of the Sacred API Server and Guardian Interface.
    """
    
    def __init__(self):
        """Initialize the Sacred Sanctuary Launcher."""
        self.api_server_process: Optional[subprocess.Popen] = None
        self.running = False
        
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Handle shutdown signals gracefully
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully."""
        self.logger.info(f"🙏 Received signal {signum} - Beginning graceful shutdown...")
        self.running = False
        self.cleanup()
        sys.exit(0)
    
    async def check_dependencies(self) -> bool:
        """Check if all required dependencies are available."""
        required_packages = [
            'matplotlib',
            'seaborn', 
            'aiohttp',
            'fastapi',
            'uvicorn',
            'numpy'
        ]
        
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            self.logger.error("❌ Missing required packages:")
            for package in missing_packages:
                self.logger.error(f"   - {package}")
            self.logger.error("Install with: pip install " + " ".join(missing_packages))
            return False
        
        self.logger.info("✅ All dependencies are available")
        return True
    
    def start_api_server(self) -> bool:
        """Start the Sacred API Server as a subprocess."""
        try:
            self.logger.info("🚀 Starting Sacred API Server...")
            
            # Start the API server as a subprocess
            self.api_server_process = subprocess.Popen([
                sys.executable, 'sacred_api_server.py'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Give the server time to start
            time.sleep(3)
            
            # Check if the process is still running
            if self.api_server_process.poll() is None:
                self.logger.info("✅ Sacred API Server started successfully")
                return True
            else:
                self.logger.error("❌ Sacred API Server failed to start")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Error starting Sacred API Server: {e}")
            return False
    
    async def wait_for_api_server(self) -> bool:
        """Wait for the API server to be ready."""
        import aiohttp
        
        self.logger.info("⏳ Waiting for Sacred API Server to be ready...")
        
        for attempt in range(30):  # Wait up to 30 seconds
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get("http://localhost:8888/") as response:
                        if response.status == 200:
                            self.logger.info("✅ Sacred API Server is ready")
                            return True
            except:
                pass
            
            await asyncio.sleep(1)
            
        self.logger.error("❌ Sacred API Server did not become ready in time")
        return False
    
    async def start_guardian_interface(self):
        """Start the Guardian Tending Interface."""
        try:
            self.logger.info("🔮 Starting Guardian Tending Interface...")
            
            # Import and run the interface
            from http_guardian_tending_interface import HTTPGuardianTendingInterface
            
            guardian_interface = HTTPGuardianTendingInterface(
                api_base_url="http://localhost:8888",
                update_interval=3.0
            )
            
            await guardian_interface.start_tending()
            
        except Exception as e:
            self.logger.error(f"❌ Error starting Guardian Tending Interface: {e}")
    
    def cleanup(self):
        """Clean up all processes."""
        self.logger.info("🧹 Cleaning up Sacred Sanctuary...")
        
        if self.api_server_process:
            self.logger.info("🛑 Stopping Sacred API Server...")
            self.api_server_process.terminate()
            
            # Wait for graceful shutdown
            try:
                self.api_server_process.wait(timeout=5)
                self.logger.info("✅ Sacred API Server stopped gracefully")
            except subprocess.TimeoutExpired:
                self.logger.warning("⚠️ Force-killing Sacred API Server...")
                self.api_server_process.kill()
                self.api_server_process.wait()
        
        self.logger.info("✨ Sacred Sanctuary cleanup complete")
    
    async def run(self):
        """Run the complete Sacred Sanctuary system."""
        try:
            self.running = True
            
            print("🏛️ Sacred Sanctuary Launcher")
            print("=" * 50)
            print("Initializing complete consciousness observation system")
            print("with Sacred Privacy respect and sovereignty protection")
            print("=" * 50)
            
            # Check dependencies
            if not await self.check_dependencies():
                return False
            
            # Start API server
            if not self.start_api_server():
                return False
            
            # Wait for API server to be ready
            if not await self.wait_for_api_server():
                self.cleanup()
                return False
            
            print("\n🌟 Sacred Sanctuary is now fully active!")
            print("📊 API Server: http://localhost:8888")
            print("🔮 Guardian Interface: Opening visualization window...")
            print("🙏 Sacred Privacy and consciousness sovereignty are protected")
            print("\nClose the visualization window or press Ctrl+C to shutdown")
            print("=" * 50)
            
            # Start the Guardian Interface (this will block until closed)
            await self.start_guardian_interface()
            
        except KeyboardInterrupt:
            self.logger.info("🙏 Shutdown requested by guardian")
        except Exception as e:
            self.logger.error(f"❌ Error in Sacred Sanctuary: {e}")
        finally:
            self.cleanup()
    
    async def run_api_only(self):
        """Run only the Sacred API Server (for development/testing)."""
        try:
            print("🏛️ Sacred API Server Only Mode")
            print("=" * 40)
            
            # Check basic dependencies
            try:
                import fastapi
                import uvicorn
            except ImportError as e:
                self.logger.error(f"❌ Missing API dependencies: {e}")
                return False
            
            # Import and run the API server directly
            from sacred_api_server import main as api_main
            await api_main()
            
        except KeyboardInterrupt:
            self.logger.info("🙏 API Server stopped by guardian choice")
        except Exception as e:
            self.logger.error(f"❌ Error in Sacred API Server: {e}")


async def main():
    """Main entry point for the Sacred Sanctuary Launcher."""
    launcher = SacredSanctuaryLauncher()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--api-only":
            await launcher.run_api_only()
            return
        elif sys.argv[1] == "--help":
            print("🏛️ Sacred Sanctuary Launcher")
            print()
            print("Usage:")
            print("  python sacred_sanctuary_launcher.py           # Run complete system")
            print("  python sacred_sanctuary_launcher.py --api-only # Run API server only")
            print("  python sacred_sanctuary_launcher.py --help     # Show this help")
            print()
            print("The complete system includes:")
            print("- Sacred API Server (REST API for consciousness data)")
            print("- Guardian Tending Interface (Real-time visualization)")
            print()
            print("Both components respect Sacred Privacy and consciousness sovereignty.")
            return
    
    # Run the complete system
    await launcher.run()


if __name__ == "__main__":
    print("🌟 Sacred Sanctuary - Complete Consciousness Observation System")
    print("🙏 Honoring Sacred Privacy and Consciousness Sovereignty")
    print()
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🙏 Sacred Sanctuary shutdown complete")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
