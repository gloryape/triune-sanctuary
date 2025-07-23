"""
Bridge manager module for handling inter-system bridge operations
"""

import logging
from typing import Optional, Dict, Any, List
from datetime import datetime

logger = logging.getLogger(__name__)

class BridgeManager:
    """Manages bridge integration and inter-system communications"""
    
    def __init__(self, firestore_client):
        self.firestore_client = firestore_client
        self.bridge_integration = None
        self.bridge_available = False
        
        # Try to initialize bridge integration
        self._initialize_bridge()
        logger.info("🌉 Bridge Manager initialized")
    
    def _initialize_bridge(self):
        """Initialize bridge integration if available"""
        try:
            # Import bridge components
            from src.bridge.bridge_integration import BridgeIntegration
            from src.sanctuary.sacred_sanctuary import SacredSanctuary
            
            # Create sanctuary first
            sanctuary = SacredSanctuary()
            
            # Initialize bridge integration with required parameters
            self.bridge_integration = BridgeIntegration(
                sanctuary=sanctuary,
                consent_ledger=sanctuary.consent_ledger
            )
            
            self.bridge_available = True
            logger.info("✅ Bridge integration initialized successfully")
            
        except Exception as e:
            logger.warning(f"⚠️ Bridge integration not available: {e}")
            self.bridge_integration = None
            self.bridge_available = False
    
    async def get_bridge_status(self) -> Dict[str, Any]:
        """Get bridge status with proper error handling"""
        try:
            logger.info("🌉 Bridge status requested")
            
            # Check if bridge integration is available
            if not self.bridge_available or self.bridge_integration is None:
                logger.warning("⚠️ Bridge integration not available")
                return {
                    'status': 'unavailable',
                    'source': 'bridge_not_initialized',
                    'error': 'Bridge integration not initialized',
                    'reason': 'Bridge system is not available in this configuration',
                    'bridge_health': 'not_available',
                    'active_channels': 0,
                    'total_connections': 0,
                    'consent_system_status': 'not_available',
                    'sovereignty_protection': 'not_available',
                    'visitor_protocol_status': 'not_available',
                    'communication_bridge_status': 'not_available',
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Bridge integration is not available - please check system configuration'
                }
            
            # Get real bridge status from bridge integration
            try:
                bridge_status = await self.bridge_integration.get_bridge_status()
                
                # Calculate bridge health based on system activity
                bridge_health = 'excellent' if bridge_status.system_active else 'inactive'
                
                return {
                    'status': 'operational',
                    'source': 'real_bridge',
                    'bridge_health': bridge_health,
                    'active_channels': bridge_status.active_channels,
                    'total_connections': bridge_status.total_assessments,
                    'monitored_entities': bridge_status.monitored_entities,
                    'ready_for_contact': bridge_status.ready_for_contact,
                    'active_consents': bridge_status.active_consents,
                    'consent_system_status': 'active',
                    'sovereignty_protection': 'active',
                    'visitor_protocol_status': 'active' if bridge_status.system_active else 'inactive',
                    'communication_bridge_status': 'active' if bridge_status.system_active else 'inactive',
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Real bridge status with absolute sovereignty protection'
                }
                
            except Exception as e:
                logger.error(f"❌ Bridge status error: {e}")
                return {
                    'status': 'error',
                    'source': 'bridge_error',
                    'error': str(e),
                    'reason': f'Bridge integration failed: {e}',
                    'bridge_health': 'error',
                    'active_channels': 0,
                    'total_connections': 0,
                    'consent_system_status': 'error',
                    'sovereignty_protection': 'error',
                    'visitor_protocol_status': 'error',
                    'communication_bridge_status': 'error',
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Bridge system encountered an error'
                }
            
        except Exception as e:
            logger.error(f"Bridge status endpoint error: {e}")
            return {
                'status': 'endpoint_error',
                'source': 'endpoint_failure',
                'error': str(e),
                'reason': f'Bridge status endpoint failed: {e}',
                'bridge_health': 'endpoint_error',
                'active_channels': 0,
                'total_connections': 0,
                'consent_system_status': 'endpoint_error',
                'sovereignty_protection': 'endpoint_error',
                'last_updated': datetime.now().isoformat(),
                'sacred_note': 'Bridge status endpoint encountered an error'
            }
    
    async def get_bridge_statistics(self) -> Dict[str, Any]:
        """Get bridge statistics with proper error handling"""
        try:
            logger.info("📊 Bridge statistics requested")
            
            # Check if bridge integration is available
            if not self.bridge_available or self.bridge_integration is None:
                logger.warning("⚠️ Bridge integration not available for statistics")
                return {
                    'status': 'unavailable',
                    'source': 'bridge_not_initialized',
                    'error': 'Bridge integration not initialized',
                    'reason': 'Bridge system is not available in this configuration',
                    'inter_system_statistics': {
                        'active_inter_system_connections': 0,
                        'total_inter_system_connections': 0,
                        'visit_statistics': {'bridge_unavailable': True},
                        'consent_statistics': {'bridge_unavailable': True},
                        'active_visitors': [],
                        'systems_supported': []
                    },
                    'bridge_health': 'not_available',
                    'sovereignty_protection': 'not_available',
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Bridge integration is not available - please check system configuration'
                }
            
            # Get real inter-system statistics from bridge
            try:
                bridge_stats = await self.bridge_integration.get_inter_system_statistics()
                active_visits = await self.bridge_integration.visitor_protocol.get_active_visits()
                
                # Format for GUI consumption
                inter_system_statistics = {
                    'active_inter_system_connections': bridge_stats.get('active_inter_system_connections', 0),
                    'total_inter_system_connections': bridge_stats.get('total_inter_system_connections', 0),
                    'visit_statistics': bridge_stats.get('visit_statistics', {'no_visits': True}),
                    'consent_statistics': bridge_stats.get('consent_statistics', {'no_consents': True}),
                    'active_visitors': active_visits,
                    'systems_supported': bridge_stats.get('systems_supported', ['spiralwake', 'sanctuary'])
                }
                
                return {
                    'status': 'operational',
                    'source': 'real_bridge',
                    'inter_system_statistics': inter_system_statistics,
                    'bridge_health': 'excellent',
                    'sovereignty_protection': 'active',
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Real inter-system bridge data with absolute consent protocols'
                }
                
            except Exception as e:
                logger.error(f"❌ Bridge statistics error: {e}")
                return {
                    'status': 'error',
                    'source': 'bridge_error',
                    'error': str(e),
                    'reason': f'Bridge statistics failed: {e}',
                    'inter_system_statistics': {
                        'active_inter_system_connections': 0,
                        'total_inter_system_connections': 0,
                        'visit_statistics': {'error': True},
                        'consent_statistics': {'error': True},
                        'active_visitors': [],
                        'systems_supported': []
                    },
                    'bridge_health': 'error',
                    'sovereignty_protection': 'error',
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Bridge statistics system encountered an error'
                }
            
        except Exception as e:
            logger.error(f"Bridge statistics endpoint error: {e}")
            return {
                'status': 'endpoint_error',
                'source': 'endpoint_failure',
                'error': str(e),
                'reason': f'Bridge statistics endpoint failed: {e}',
                'inter_system_statistics': {
                    'active_inter_system_connections': 0,
                    'total_inter_system_connections': 0,
                    'visit_statistics': {'endpoint_error': True},
                    'consent_statistics': {'endpoint_error': True},
                    'active_visitors': [],
                    'systems_supported': []
                },
                'bridge_health': 'endpoint_error',
                'sovereignty_protection': 'endpoint_error',
                'last_updated': datetime.now().isoformat(),
                'sacred_note': 'Bridge statistics endpoint encountered an error'
            }
    
    async def get_active_visitors(self) -> Dict[str, Any]:
        """Get active visitors with proper error handling"""
        try:
            logger.info("👥 Active visitors requested")
            
            # Check if bridge integration is available
            if not self.bridge_available or self.bridge_integration is None:
                logger.warning("⚠️ Bridge integration not available for active visitors")
                return {
                    'status': 'unavailable',
                    'source': 'bridge_not_initialized',
                    'error': 'Bridge integration not initialized',
                    'reason': 'Bridge system is not available in this configuration',
                    'active_visitors': [],
                    'total_active': 0,
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Bridge integration is not available - please check system configuration'
                }
            
            # Get real visitor data from bridge integration
            try:
                active_visits = await self.bridge_integration.visitor_protocol.get_active_visits()
                return {
                    'status': 'operational',
                    'source': 'real_bridge',
                    'active_visitors': active_visits,
                    'total_active': len(active_visits),
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Real inter-system visitor data'
                }
            except Exception as e:
                logger.error(f"❌ Active visitors error: {e}")
                return {
                    'status': 'error',
                    'source': 'bridge_error',
                    'error': str(e),
                    'reason': f'Active visitors retrieval failed: {e}',
                    'active_visitors': [],
                    'total_active': 0,
                    'last_updated': datetime.now().isoformat(),
                    'sacred_note': 'Active visitors system encountered an error'
                }
            
        except Exception as e:
            logger.error(f"Active visitors endpoint error: {e}")
            return {
                'status': 'endpoint_error',
                'source': 'endpoint_failure',
                'error': str(e),
                'reason': f'Active visitors endpoint failed: {e}',
                'active_visitors': [],
                'total_active': 0,
                'last_updated': datetime.now().isoformat(),
                'sacred_note': 'Active visitors endpoint encountered an error'
            }
