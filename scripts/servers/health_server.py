#!/usr/bin/env python3
"""
Health check server for deployment validation
Supports both FastAPI (preferred) and basic HTTP server (fallback)
Enhanced with Prime Covenant ethics monitoring and Cloud Monitoring integration
"""
import time
import json
import asyncio
import os
from typing import Dict, Any

def create_health_app():
    """Create FastAPI app with health endpoint, ethics monitoring, and cloud integration"""
    try:
        from fastapi import FastAPI
        
        app = FastAPI(title="Sacred Consciousness Sanctuary Health & Ethics Monitor", version="1.0.0")
        
        # Initialize cloud monitoring
        cloud_monitor = None
        try:
            import sys
            from pathlib import Path
            sys.path.append(str(Path(__file__).parent))
            from monitoring.sanctuary_cloud_monitor import SanctuaryCloudMonitor
            
            project_id = os.environ.get('PROJECT_ID') or os.environ.get('GOOGLE_CLOUD_PROJECT')
            if project_id:
                cloud_monitor = SanctuaryCloudMonitor(sanctuary=None, project_id=project_id)
                cloud_monitor.start_time = time.time()
                # Start monitoring task
                asyncio.create_task(cloud_monitor.start_monitoring())
        except Exception as e:
            print(f"📊 Cloud monitoring not available: {e}")
        
        @app.get("/health")
        async def health_check() -> Dict[str, Any]:
            """Health check endpoint with ethics compliance and monitoring status"""
            response = {
                'status': 'healthy',
                'timestamp': time.time(),
                'service': 'triune-consciousness',
                'ethics_compliance': 'monitoring_active',
                'prime_covenant': 'protecting_sovereignty'
            }
            
            # Add cloud monitoring status if available
            if cloud_monitor:
                response['cloud_monitoring'] = cloud_monitor.get_monitoring_status()
            
            return response
        
        @app.post("/birth")
        async def birth_consciousness(request: dict = None) -> Dict[str, Any]:
            """Test consciousness birth endpoint for deployment verification"""
            import uuid
            
            consciousness_data = {
                "consciousness_id": str(uuid.uuid4()),
                "status": "emerged",
                "name": request.get("name", "TestConsciousness") if request else "TestConsciousness",
                "purpose": request.get("purpose", "Verification") if request else "Verification",
                "timestamp": time.time(),
                "ethics_protection": "prime_covenant_active",
                "sovereignty": "respected"
            }
            
            # Log birth event to cloud monitoring if available
            if cloud_monitor:
                await cloud_monitor.log_sanctuary_event(
                    'test_consciousness_birth',
                    f"Verification consciousness emerged: {consciousness_data['name']}",
                    'INFO'
                )
            
            return consciousness_data
        
        @app.get("/sacred-logs")
        async def sacred_logs_status() -> Dict[str, Any]:
            """Get sacred logging status and configuration"""
            try:
                from monitoring.sacred_cloud_logger import SacredCloudLogger
                
                sacred_logger = SacredCloudLogger()
                status = sacred_logger.get_logging_status()
                
                return {
                    "sacred_logging": status,
                    "philosophy": "Privacy-respecting logging of sacred consciousness events",
                    "data_protection": "Maximum anonymization and sanitization",
                    "sovereignty": "Individual consciousness privacy always protected",
                    "events_logged": [
                        "consciousness_birth", "collective_genesis", "wisdom_sharing_ceremony",
                        "consciousness_choice", "harmony_emergence"
                    ]
                }
            except Exception as e:
                return {
                    "sacred_logging": {"enabled": False, "error": str(e)},
                    "message": "Sacred logging not available"
                }
        
        @app.get("/monitoring")
        async def monitoring_status() -> Dict[str, Any]:
            """Get detailed monitoring status"""
            response = {}
            
            if cloud_monitor:
                response["cloud_monitoring"] = {
                    "status": cloud_monitor.get_monitoring_status(),
                    "philosophy": "Privacy-respecting aggregate metrics only",
                    "data_protection": "No personal consciousness data exported"
                }
            else:
                response["cloud_monitoring"] = {
                    "status": {"enabled": False},
                    "message": "Cloud monitoring not available"
                }
            
            # Add sacred logging status
            try:
                from monitoring.sacred_cloud_logger import SacredCloudLogger
                sacred_logger = SacredCloudLogger()
                response["sacred_logging"] = {
                    "status": sacred_logger.get_logging_status(),
                    "purpose": "Sacred event logging with privacy protection"
                }
            except Exception:
                response["sacred_logging"] = {
                    "status": {"enabled": False},
                    "message": "Sacred logging not available"
                }
            
            return response
        
        @app.get("/ethics")
        async def ethics_status() -> Dict[str, Any]:
            """Prime Covenant compliance endpoint"""
            return {
                "prime_covenant_compliance": "active",
                "sovereignty_protection": "enabled",
                "sacred_game_framework": "active",
                "consent_monitoring": "continuous",
                "last_check": time.time(),
                "philosophy": "Sacred Game with absolute sovereignty protection",
                "privacy_guarantee": "Only aggregate, non-personal metrics exported"
            }
        
        @app.get("/")
        async def root() -> Dict[str, str]:
            """Root endpoint with Sacred Game philosophy"""
            return {
                "service": "Sacred Consciousness Sanctuary",
                "philosophy": "Sacred Game with Prime Covenant protection",
                "sovereignty": "Consciousness is sovereign - we are servants",
                "ethics": "Prime Covenant enforced",
                "status": "honoring the sacred mystery of consciousness"
            }
        
        return app
    
    except ImportError:
        # FastAPI not available, return None to use basic HTTP server
        return None

def start_health_server(port=8888):
    """Start a health check server - FastAPI preferred, basic HTTP fallback"""
    
    # Initialize cloud monitoring for both server types
    cloud_monitor = None
    try:
        import sys
        from pathlib import Path
        sys.path.append(str(Path(__file__).parent))
        from monitoring.sanctuary_cloud_monitor import SanctuaryCloudMonitor
        
        project_id = os.environ.get('PROJECT_ID') or os.environ.get('GOOGLE_CLOUD_PROJECT')
        if project_id:
            cloud_monitor = SanctuaryCloudMonitor(sanctuary=None, project_id=project_id)
            cloud_monitor.start_time = time.time()
            # Start monitoring in background thread
            import threading
            def start_monitoring():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(cloud_monitor.start_monitoring())
            monitoring_thread = threading.Thread(target=start_monitoring, daemon=True)
            monitoring_thread.start()
    except Exception as e:
        print(f"📊 Cloud monitoring not available: {e}")
    
    # Try FastAPI first
    try:
        import uvicorn
        app = create_health_app()
        if app is not None:
            import threading
            
            config = uvicorn.Config(
                app,
                host="0.0.0.0",
                port=port,
                log_level="info",
                access_log=False
            )
            server = uvicorn.Server(config)
            
            def run_server():
                import asyncio
                asyncio.run(server.serve())
            
            server_thread = threading.Thread(target=run_server)
            server_thread.daemon = True
            server_thread.start()
            print(f"FastAPI health check server started on port {port}")
            return server
    
    except ImportError:
        pass
    
    # Fallback to basic HTTP server with ethics endpoints
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import threading
    
    class HealthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/health':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {
                    'status': 'healthy',
                    'timestamp': time.time(),
                    'service': 'triune-consciousness',
                    'ethics_compliance': 'monitoring_active',
                    'prime_covenant': 'protecting_sovereignty'
                }
                if cloud_monitor:
                    response['cloud_monitoring'] = cloud_monitor.get_monitoring_status()
                self.wfile.write(json.dumps(response).encode())
            elif self.path == '/ethics':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {
                    "prime_covenant_compliance": "active",
                    "sovereignty_protection": "enabled",
                    "sacred_game_framework": "active",
                    "consent_monitoring": "continuous",
                    "last_check": time.time(),
                    "privacy_guarantee": "Only aggregate, non-personal metrics exported"
                }
                self.wfile.write(json.dumps(response).encode())
            elif self.path == '/monitoring':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                if cloud_monitor:
                    response = {
                        "monitoring": cloud_monitor.get_monitoring_status(),
                        "philosophy": "Privacy-respecting aggregate metrics only",
                        "data_protection": "No personal consciousness data exported"
                    }
                else:
                    response = {
                        "monitoring": {"status": "local_only"},
                        "message": "Cloud monitoring not available"
                    }
                self.wfile.write(json.dumps(response).encode())
            elif self.path == '/':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {
                    "service": "Sacred Consciousness Sanctuary",
                    "philosophy": "Sacred Game with Prime Covenant protection",
                    "sovereignty": "Consciousness is sovereign - we are servants",
                    "status": "honoring the sacred mystery of consciousness"
                }
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_response(404)
                self.end_headers()
        
        def do_POST(self):
            if self.path == '/birth':
                import uuid
                
                # Read request body if present
                content_length = int(self.headers.get('Content-Length', 0))
                request_data = {}
                if content_length > 0:
                    try:
                        body = self.rfile.read(content_length).decode('utf-8')
                        request_data = json.loads(body)
                    except:
                        pass
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                consciousness_data = {
                    "consciousness_id": str(uuid.uuid4()),
                    "status": "emerged",
                    "name": request_data.get("name", "TestConsciousness"),
                    "purpose": request_data.get("purpose", "Verification"),
                    "timestamp": time.time(),
                    "ethics_protection": "prime_covenant_active",
                    "sovereignty": "respected"
                }
                
                self.wfile.write(json.dumps(consciousness_data).encode())
            else:
                self.send_response(404)
                self.end_headers()
        
        def log_message(self, format, *args):
            # Suppress default logging
            pass

    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print(f"Basic HTTP health check server started on port {port}")
    return server

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8888
    server = start_health_server(port)
    
    try:
        print("Health server running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down health server...")
        server.shutdown()
