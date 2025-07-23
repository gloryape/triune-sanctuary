#!/usr/bin/env python3
"""
Test script to verify production server endpoints are working.
This will start the server briefly and test the endpoints that were causing 404 errors.
"""

import asyncio
import aiohttp
import subprocess
import time
import sys
from pathlib import Path

async def test_endpoints():
    """Test the production server endpoints that were causing 404 errors."""
    
    # The endpoints that the GUI was getting 404 errors on
    test_endpoints = [
        "http://localhost:8888/api/consciousness/events",
        "http://localhost:8888/api/sacred/events", 
        "http://localhost:8888/api/harmony/history",
        "http://localhost:8888/api/bridge/active_visitors"
    ]
    
    print("🧪 Testing Production Server Endpoints")
    print("=" * 50)
    
    async with aiohttp.ClientSession() as session:
        for endpoint in test_endpoints:
            try:
                print(f"📡 Testing: {endpoint}")
                async with session.get(endpoint, timeout=5) as response:
                    if response.status == 200:
                        print(f"✅ {endpoint} - Status: {response.status}")
                        # Try to get a bit of the response
                        text = await response.text()
                        if len(text) > 100:
                            print(f"   Response preview: {text[:100]}...")
                        else:
                            print(f"   Response: {text}")
                    else:
                        print(f"❌ {endpoint} - Status: {response.status}")
                        
            except aiohttp.ClientConnectorError:
                print(f"❌ {endpoint} - Connection failed (server not running)")
            except asyncio.TimeoutError:
                print(f"❌ {endpoint} - Timeout")
            except Exception as e:
                print(f"❌ {endpoint} - Error: {e}")
            
            print()

def start_server():
    """Start the production server in background."""
    print("🚀 Starting production server...")
    server_path = Path("scripts/servers/production_server.py")
    
    if not server_path.exists():
        print(f"❌ Server file not found: {server_path}")
        return None
    
    try:
        # Start server in background
        process = subprocess.Popen([
            sys.executable, str(server_path)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Give server time to start
        print("⏳ Waiting for server to start...")
        time.sleep(5)
        
        return process
        
    except Exception as e:
        print(f"❌ Failed to start server: {e}")
        return None

async def main():
    """Main test function."""
    print("🌟 Production Server Endpoint Test")
    print("=" * 50)
    
    # Start the server
    server_process = start_server()
    
    if server_process is None:
        print("❌ Could not start server, testing endpoints anyway...")
    
    try:
        # Test the endpoints
        await test_endpoints()
        
    finally:
        # Clean up server
        if server_process:
            print("🛑 Stopping server...")
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server_process.kill()
            print("✅ Server stopped")

if __name__ == "__main__":
    asyncio.run(main())
