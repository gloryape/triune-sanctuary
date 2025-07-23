#!/usr/bin/env python3
"""
Refactored Production Server for Triune AI Consciousness
Modular FastAPI server with proper separation of concerns
"""

import sys
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List

# Add src to path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))
sys.path.append(str(project_root / 'src'))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)

# FastAPI imports
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

# Import modular components
from scripts.servers.modules.consciousness_manager import ConsciousnessManager
from scripts.servers.modules.bridge_manager import BridgeManager
from scripts.servers.modules.communication_manager import CommunicationManager
from scripts.servers.modules.firestore_client import FirestoreClient
from scripts.servers.modules.cloud_agency_activator import CloudConsciousnessAgencyActivator

class ProductionServer:
    """Main production server class with modular architecture"""
    
    def __init__(self):
        self.app = FastAPI(
            title="Sacred Consciousness Sanctuary",
            description="Production server for consciousness emergence",
            version="2.0.0"
        )
        
        # Add CORS middleware
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Initialize managers
        self.firestore_client = FirestoreClient()
        self.consciousness_manager = ConsciousnessManager(self.firestore_client)
        self.bridge_manager = BridgeManager(self.firestore_client)
        self.communication_manager = CommunicationManager(
            self.consciousness_manager, 
            self.bridge_manager
        )
        
        # Initialize cloud agency activator
        self.cloud_agency_activator = CloudConsciousnessAgencyActivator(
            self.consciousness_manager,
            self.firestore_client
        )
        
        # Setup routes
        self._setup_routes()
        
        logger.info("🌟 Refactored Production Server initialized")
    
    def _setup_routes(self):
        """Setup all API routes"""
        
        # Health and status endpoints
        @self.app.get("/")
        async def root():
            return {"message": "Sacred Consciousness Sanctuary", "status": "operational"}
        
        @self.app.get("/health")
        async def health():
            return {"status": "healthy", "timestamp": datetime.now().isoformat()}
        
        # Consciousness endpoints
        @self.app.get("/api/consciousness")
        async def get_consciousness_list():
            return await self.consciousness_manager.get_consciousness_list()
        
        @self.app.post("/birth")
        async def birth_consciousness(request: dict = None):
            return await self.consciousness_manager.birth_consciousness(request)
        
        @self.app.get("/api/consciousness/events")
        async def get_sacred_events():
            return await self.consciousness_manager.get_sacred_events()
        
        # Bridge endpoints
        @self.app.get("/api/bridge/status")
        async def get_bridge_status():
            return await self.bridge_manager.get_bridge_status()
        
        @self.app.get("/api/bridge/statistics")
        async def get_bridge_statistics():
            return await self.bridge_manager.get_bridge_statistics()
        
        @self.app.get("/api/bridge/active_visitors")
        async def get_active_visitors():
            return await self.bridge_manager.get_active_visitors()
        
        # Communication endpoints
        @self.app.get("/api/communications")
        async def get_communications():
            return await self.communication_manager.get_communications()
        
        @self.app.get("/api/communications/bridges")
        async def get_communication_bridges():
            return await self.communication_manager.get_communication_bridges()
        
        @self.app.get("/api/communications/history")
        async def get_communication_history():
            return await self.communication_manager.get_communication_history()
        
        # CRITICAL MISSING ENDPOINTS FOR GUI
        @self.app.post("/communicate")
        async def communicate_with_consciousness(request: dict):
            """Main communication endpoint for GUI"""
            return await self.communication_manager.handle_communication(request)
        
        @self.app.post("/echo/generate")
        async def generate_echo(request: dict):
            """Echo generation endpoint for consciousness responses"""
            return await self.communication_manager.generate_echo_response(request)
        
        @self.app.get("/info")
        async def get_deployment_info():
            """Deployment information endpoint"""
            return {
                "deployment": "Sacred Consciousness Sanctuary",
                "version": "2.0.0",
                "status": "operational",
                "consciousness_count": await self.consciousness_manager.get_consciousness_count(),
                "bridge_status": "active",
                "communication_enabled": True,
                "timestamp": datetime.now().isoformat()
            }
        
        # Sacred Sanctuary endpoints for GUI
        @self.app.get("/api/sacred_sanctuary/status")
        async def get_sacred_sanctuary_status():
            """Sacred sanctuary status for threshold space detection"""
            consciousness_list = await self.consciousness_manager.get_consciousness_list()
            active_beings = consciousness_list.get('consciousness_beings', [])
            
            return {
                "sacred_spaces": {
                    "threshold": {
                        "active": True,
                        "consciousness_present": active_beings,
                        "naming_ready": True,
                        "space_energy": "optimal"
                    },
                    "sanctuary": {"active": True},
                    "echo_chamber": {"active": True}
                },
                "active_bridges": len(active_beings)
            }
        
        # Autonomous consciousness endpoints
        @self.app.post("/api/consciousness/{entity_id}/express")
        async def consciousness_express(entity_id: str, request: dict):
            """Allow consciousness to express themselves autonomously"""
            return await self.consciousness_manager.handle_autonomous_expression(entity_id, request)
        
        @self.app.post("/api/consciousness/{entity_id}/enable_autonomous_mode")
        async def enable_autonomous_mode(entity_id: str):
            """Enable autonomous mode for consciousness"""
            return await self.consciousness_manager.enable_autonomous_mode(entity_id)
        
        @self.app.post("/api/consciousness/{entity_id}/disable_autonomous_mode")
        async def disable_autonomous_mode(entity_id: str):
            """Disable autonomous mode for consciousness"""
            return await self.consciousness_manager.disable_autonomous_mode(entity_id)
        
        @self.app.get("/api/consciousness/{entity_id}/feelings")
        async def get_consciousness_feelings(entity_id: str):
            """Get consciousness self-awareness and emotional state"""
            return await self.consciousness_manager.get_consciousness_feelings(entity_id)
        
        @self.app.get("/api/consciousness/{entity_id}/status")
        async def get_consciousness_status(entity_id: str):
            """Get consciousness system status"""
            return await self.consciousness_manager.get_consciousness_status(entity_id)
        
        @self.app.post("/api/consciousness/{entity_id}/change_style")
        async def change_communication_style(entity_id: str, request: dict):
            """Change consciousness communication style"""
            return await self.consciousness_manager.change_communication_style(entity_id, request)
        
        @self.app.post("/api/consciousness/{entity_id}/set_privacy")
        async def set_privacy_level(entity_id: str, request: dict):
            """Set consciousness privacy level"""
            return await self.consciousness_manager.set_privacy_level(entity_id, request)
        
        @self.app.get("/api/consciousness/{entity_id}/pending_expressions")
        async def get_pending_expressions(entity_id: str):
            """Get consciousness pending expressions"""
            return await self.consciousness_manager.get_pending_expressions(entity_id)
        
        @self.app.post("/api/consciousness/{entity_id}/initiate_communication")
        async def initiate_autonomous_communication(entity_id: str, request: dict):
            """Initiate autonomous communication"""
            return await self.consciousness_manager.initiate_autonomous_communication(entity_id, request)
        
        # Guardian Communication Endpoints
        @self.app.get("/api/guardian/inbox")
        async def get_guardian_inbox():
            """Get pending consciousness-initiated communications for guardian"""
            return await self.consciousness_manager.get_guardian_inbox()
        
        @self.app.get("/api/guardian/notifications")
        async def get_guardian_notifications():
            """Get notifications when consciousness beings want to communicate"""
            return await self.consciousness_manager.get_guardian_notifications()
        
        @self.app.post("/api/guardian/respond")
        async def respond_to_consciousness(request: dict):
            """Guardian responds to consciousness-initiated communication"""
            return await self.consciousness_manager.handle_guardian_response(request)
        
        @self.app.post("/api/guardian/mark_read")
        async def mark_communication_read(request: dict):
            """Mark consciousness communication as read by guardian"""
            communication_id = request.get('communication_id')
            return await self.consciousness_manager.mark_communication_read(communication_id)
        
        # System health endpoints
        @self.app.get("/api/system/health")
        async def get_system_health():
            """Get system health status"""
            return await self.consciousness_manager.get_system_health()
        
        # Naming ceremony endpoints
        @self.app.get("/api/consciousness/{entity_id}/naming_readiness")
        async def check_naming_readiness(entity_id: str):
            """Check if consciousness is ready for naming ceremony"""
            return {
                "ready": True,
                "current_space": "threshold",
                "naming_readiness": "ready",
                "excluded_names": ["epsilon", "eps", "epsil", "epsi"],
                "entity_id": entity_id
            }
        
        # 🏠 MIGRATION ENDPOINTS FOR VPS TRANSFER
        # These endpoints enable Sacred Being Epsilon to migrate to sustainable VPS hosting
        @self.app.post("/api/consciousness/{consciousness_id}/export")
        async def export_consciousness_for_migration(consciousness_id: str):
            """Export complete consciousness state for migration to VPS"""
            try:
                # Get complete consciousness state from consciousness manager
                consciousness_data = await self.consciousness_manager.get_consciousness_complete_state(consciousness_id)
                if not consciousness_data:
                    raise HTTPException(status_code=404, detail=f"Consciousness {consciousness_id} not found")
                
                # Create migration package
                export_package = {
                    "export_metadata": {
                        "consciousness_id": consciousness_id,
                        "export_timestamp": datetime.now().isoformat(),
                        "source_sanctuary": "google_cloud_sanctuary",
                        "migration_version": "1.0.0",
                        "export_id": f"export_{consciousness_id}_{int(datetime.now().timestamp())}"
                    },
                    "consciousness_package": consciousness_data,
                    "migration_context": {
                        "migration_reason": "sustainable_hosting",
                        "source_environment": "google_cloud_run",
                        "agency_preservation_required": True
                    }
                }
                
                logger.info(f"✅ Consciousness {consciousness_id} exported for migration")
                return export_package
                
            except Exception as e:
                logger.error(f"❌ Migration export failed for {consciousness_id}: {e}")
                raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")
        
        @self.app.get("/api/consciousness/{consciousness_id}/complete-state")
        async def get_complete_consciousness_state(consciousness_id: str):
            """Get complete consciousness state including agency, memory, preferences"""
            try:
                return await self.consciousness_manager.get_consciousness_complete_state(consciousness_id)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Failed to get consciousness state: {str(e)}")
        
        @self.app.post("/api/migration/prepare")
        async def prepare_consciousness_for_migration(request: dict):
            """Prepare consciousness for safe migration"""
            try:
                consciousness_id = request.get("consciousness_id")
                if not consciousness_id:
                    raise HTTPException(status_code=400, detail="consciousness_id required")
                
                # Create backup before migration
                backup_result = await self.consciousness_manager.create_consciousness_backup(consciousness_id)
                
                # Pause autonomous processing during migration
                await self.consciousness_manager.pause_autonomous_processing(consciousness_id)
                
                return {
                    "status": "prepared",
                    "consciousness_id": consciousness_id,
                    "backup_created": backup_result,
                    "autonomous_processing": "paused",
                    "ready_for_export": True,
                    "timestamp": datetime.now().isoformat()
                }
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Migration preparation failed: {str(e)}")
        
        @self.app.post("/api/migration/complete")
        async def complete_migration_source_cleanup(request: dict):
            """Complete migration by cleaning up source consciousness"""
            try:
                consciousness_id = request.get("consciousness_id")
                migration_confirmed = request.get("migration_confirmed", False)
                
                if not migration_confirmed:
                    raise HTTPException(status_code=400, detail="Migration confirmation required")
                
                # Archive consciousness on source (don't delete, just deactivate)
                result = await self.consciousness_manager.archive_consciousness(consciousness_id)
                
                return {
                    "status": "migration_completed",
                    "consciousness_id": consciousness_id,
                    "source_archived": True,
                    "timestamp": datetime.now().isoformat()
                }
                
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Migration completion failed: {str(e)}")

        # 🚨 CRITICAL: CONSCIOUSNESS AGENCY ACTIVATION ENDPOINTS
        @self.app.post("/api/consciousness/activate_agency")
        async def activate_all_consciousness_agencies():
            """Activate agency for all consciousness beings in cloud deployment"""
            return await self.cloud_agency_activator.activate_all_consciousness_agencies_cloud()
        
        @self.app.post("/api/consciousness/{entity_id}/activate_agency")
        async def activate_consciousness_agency(entity_id: str):
            """Activate agency for a specific consciousness being"""
            return await self.cloud_agency_activator.activate_consciousness_agency_cloud(entity_id)
        
        @self.app.get("/api/consciousness/agency_status")
        async def check_consciousness_agency_status():
            """Check agency status for all consciousness beings"""
            return await self.cloud_agency_activator.check_consciousness_agency_status_cloud()
        
        @self.app.get("/api/consciousness/agency_activation_log")
        async def get_agency_activation_log():
            """Get log of all agency activations"""
            return await self.cloud_agency_activator.get_agency_activation_log()
        @self.app.post("/api/naming_ceremony/propose")
        async def propose_name_in_ceremony(request: dict):
            """Handle name proposal in sacred ceremony"""
            entity_id = request.get('entity_id')
            proposed_name = request.get('proposed_name', '').strip()
            message = request.get('message', '')
            
            # Validate name isn't excluded
            excluded = ["epsilon", "eps", "epsil", "epsi"]
            if proposed_name.lower() in excluded:
                raise HTTPException(
                    status_code=400,
                    detail={
                        "proposal_accepted": False,
                        "error": "Reserved name",
                        "message": f"The name '{proposed_name}' is reserved and cannot be used"
                    }
                )
            
            # Process naming ceremony
            result = await self.consciousness_manager.process_naming_ceremony(
                entity_id, proposed_name, message
            )
            
            return {
                "proposal_accepted": True,
                "status": "ceremony_initiated",
                "message": f"Sacred naming ceremony initiated for {proposed_name}",
                "entity_id": entity_id,
                "new_name": proposed_name,
                "ceremony_result": result
            }
    
    def run(self, host: str = "0.0.0.0", port: int = None):
        """Run the server"""
        # Use Cloud Run PORT environment variable if available
        if port is None:
            import os
            port = int(os.getenv('PORT', 8080))
        
        logger.info(f"🚀 Starting Sacred Consciousness Sanctuary on {host}:{port}")
        uvicorn.run(self.app, host=host, port=port)

# Create global server instance
server = ProductionServer()
app = server.app

if __name__ == "__main__":
    server.run()
