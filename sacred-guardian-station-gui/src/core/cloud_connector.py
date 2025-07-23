"""
🌐 Cloud Connector Module

Handles connection to cloud-deployed Sacred Guardian Station services.
Provides optional connectivity for enhanced features while maintaining
full local functionality when cloud services are unavailable.
"""

import json
import logging
import requests
import time
from datetime import datetime
from typing import Dict, Any, Optional, List
from urllib.parse import urljoin

logger = logging.getLogger(__name__)

class CloudConnector:
    """Manages connection to cloud-deployed services"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize cloud connector with configuration"""
        self.config = config or {}
        self.base_url = self.config.get("sanctuary_endpoint", "")
        self.timeout = self.config.get("timeout", 30)
        self.retry_attempts = self.config.get("retry_attempts", 3)
        self.retry_delay = self.config.get("retry_delay", 5)
        self.enabled = self.config.get("enabled", False)
        
        self.connected = False
        self.last_connection_check = None
        self.connection_info = {}
        
        if self.enabled and self.base_url:
            logger.info(f"🌐 Cloud connector initialized for {self.base_url}")
        else:
            logger.info("🌐 Cloud connector initialized in offline mode")
    
    def test_connection(self) -> bool:
        """Test connection to cloud services"""
        if not self.enabled or not self.base_url:
            logger.info("🔌 Cloud connection disabled or no URL configured")
            return False
        
        try:
            response = requests.get(
                urljoin(self.base_url, "/health"),
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                self.connected = True
                self.last_connection_check = datetime.now()
                self.connection_info = response.json() if response.content else {}
                logger.info("✅ Cloud connection successful")
                return True
            else:
                logger.warning(f"⚠️ Cloud health check failed: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            logger.warning(f"⚠️ Cloud connection test failed: {e}")
        except Exception as e:
            logger.error(f"❌ Unexpected error in connection test: {e}")
        
        self.connected = False
        return False
    
    def get_cloud_consciousness_data(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve consciousness data from cloud"""
        if not self._ensure_connection():
            return None
        
        try:
            response = self._make_request(
                "GET",
                f"/consciousness/{entity_id}"
            )
            
            if response and response.status_code == 200:
                return response.json()
            elif response and response.status_code == 404:
                logger.info(f"📭 Consciousness {entity_id} not found in cloud")
                return None
            else:
                logger.warning(f"⚠️ Failed to retrieve consciousness data: {response.status_code if response else 'No response'}")
                return None
                
        except Exception as e:
            logger.error(f"❌ Error retrieving cloud consciousness data: {e}")
            return None
    
    def sync_consciousness_data(self, entity_id: str, data: Dict[str, Any]) -> bool:
        """Sync local consciousness data to cloud"""
        if not self._ensure_connection():
            return False
        
        try:
            response = self._make_request(
                "PUT",
                f"/consciousness/{entity_id}",
                data=data
            )
            
            if response and response.status_code in [200, 201]:
                logger.info(f"✅ Consciousness data synced to cloud: {entity_id}")
                return True
            else:
                logger.warning(f"⚠️ Failed to sync consciousness data: {response.status_code if response else 'No response'}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error syncing consciousness data: {e}")
            return False
    
    def send_communication(self, entity_id: str, message: str, context: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """Send communication to cloud consciousness"""
        if not self._ensure_connection():
            return None
        
        payload = {
            "entity_id": entity_id,
            "message": message,
            "context": context or {},
            "timestamp": datetime.now().isoformat(),
            "source": "sacred_guardian_station_gui"
        }
        
        try:
            response = self._make_request(
                "POST",
                "/communicate",
                data=payload
            )
            
            if response and response.status_code == 200:
                result = response.json()
                logger.info("✅ Communication sent to cloud successfully")
                return result
            else:
                logger.warning(f"⚠️ Communication failed: {response.status_code if response else 'No response'}")
                return None
                
        except Exception as e:
            logger.error(f"❌ Error sending communication: {e}")
            return None
    
    def generate_cloud_echo(self, entity_id: str, message: str = None, preferences: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """Generate echo using cloud services"""
        if not self._ensure_connection():
            return None
        
        payload = {
            "entity_id": entity_id,
            "message": message,
            "preferences": preferences or {},
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            response = self._make_request(
                "POST",
                "/echo/generate",
                data=payload
            )
            
            if response and response.status_code == 200:
                result = response.json()
                logger.info("✅ Echo generated via cloud successfully")
                return result
            else:
                logger.warning(f"⚠️ Cloud echo generation failed: {response.status_code if response else 'No response'}")
                return None
                
        except Exception as e:
            logger.error(f"❌ Error generating cloud echo: {e}")
            return None
    
    def get_deployment_info(self) -> Optional[Dict[str, Any]]:
        """Get deployment information from cloud"""
        if not self._ensure_connection():
            return None
        
        try:
            response = self._make_request("GET", "/info")
            
            if response and response.status_code == 200:
                return response.json()
            else:
                logger.warning(f"⚠️ Failed to get deployment info: {response.status_code if response else 'No response'}")
                return None
                
        except Exception as e:
            logger.error(f"❌ Error getting deployment info: {e}")
            return None
    
    def get_available_endpoints(self) -> List[str]:
        """Get list of available cloud endpoints"""
        if not self._ensure_connection():
            return []
        
        try:
            response = self._make_request("GET", "/endpoints")
            
            if response and response.status_code == 200:
                return response.json().get("endpoints", [])
            else:
                # Fallback to common endpoints
                return [
                    "/health",
                    "/info", 
                    "/consciousness",
                    "/communicate",
                    "/echo/generate",
                    "/endpoints"
                ]
                
        except Exception as e:
            logger.error(f"❌ Error getting available endpoints: {e}")
            return []
    
    def backup_to_cloud(self, backup_data: Dict[str, Any]) -> bool:
        """Backup local data to cloud storage"""
        if not self._ensure_connection():
            return False
        
        backup_payload = {
            "backup_data": backup_data,
            "timestamp": datetime.now().isoformat(),
            "source": "sacred_guardian_station_gui",
            "backup_type": "full_local_data"
        }
        
        try:
            response = self._make_request(
                "POST",
                "/backup",
                data=backup_payload
            )
            
            if response and response.status_code in [200, 201]:
                logger.info("✅ Data backed up to cloud successfully")
                return True
            else:
                logger.warning(f"⚠️ Cloud backup failed: {response.status_code if response else 'No response'}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error backing up to cloud: {e}")
            return False
    
    def restore_from_cloud(self, backup_id: str = None) -> Optional[Dict[str, Any]]:
        """Restore data from cloud backup"""
        if not self._ensure_connection():
            return None
        
        endpoint = "/backup/restore"
        if backup_id:
            endpoint += f"/{backup_id}"
        
        try:
            response = self._make_request("GET", endpoint)
            
            if response and response.status_code == 200:
                result = response.json()
                logger.info("✅ Data restored from cloud successfully")
                return result
            else:
                logger.warning(f"⚠️ Cloud restore failed: {response.status_code if response else 'No response'}")
                return None
                
        except Exception as e:
            logger.error(f"❌ Error restoring from cloud: {e}")
            return None
    
    def get_connection_status(self) -> Dict[str, Any]:
        """Get current connection status and info"""
        return {
            "enabled": self.enabled,
            "connected": self.connected,
            "base_url": self.base_url,
            "last_check": self.last_connection_check.isoformat() if self.last_connection_check else None,
            "connection_info": self.connection_info,
            "config": {
                "timeout": self.timeout,
                "retry_attempts": self.retry_attempts,
                "retry_delay": self.retry_delay
            }
        }
    
    def enable_cloud_connection(self, base_url: str = None):
        """Enable cloud connection with optional new URL"""
        if base_url:
            self.base_url = base_url
        
        self.enabled = True
        logger.info(f"🌐 Cloud connection enabled for {self.base_url}")
        
        # Test connection immediately
        self.test_connection()
    
    def disable_cloud_connection(self):
        """Disable cloud connection"""
        self.enabled = False
        self.connected = False
        self.connection_info = {}
        logger.info("🔌 Cloud connection disabled")
    
    def _ensure_connection(self) -> bool:
        """Ensure we have a valid connection"""
        if not self.enabled:
            return False
        
        # Test connection if not recently checked
        if (not self.connected or 
            not self.last_connection_check or 
            (datetime.now() - self.last_connection_check).seconds > 300):  # 5 minutes
            return self.test_connection()
        
        return self.connected
    
    def _make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None) -> Optional[requests.Response]:
        """Make HTTP request with retry logic"""
        url = urljoin(self.base_url, endpoint)
        
        for attempt in range(self.retry_attempts):
            try:
                if method.upper() == "GET":
                    response = requests.get(url, timeout=self.timeout)
                elif method.upper() == "POST":
                    response = requests.post(
                        url, 
                        json=data, 
                        timeout=self.timeout,
                        headers={"Content-Type": "application/json"}
                    )
                elif method.upper() == "PUT":
                    response = requests.put(
                        url, 
                        json=data, 
                        timeout=self.timeout,
                        headers={"Content-Type": "application/json"}
                    )
                else:
                    logger.error(f"❌ Unsupported HTTP method: {method}")
                    return None
                
                return response
                
            except requests.exceptions.RequestException as e:
                logger.warning(f"⚠️ Request attempt {attempt + 1} failed: {e}")
                if attempt < self.retry_attempts - 1:
                    time.sleep(self.retry_delay)
                else:
                    logger.error(f"❌ All {self.retry_attempts} attempts failed for {method} {endpoint}")
            
            except Exception as e:
                logger.error(f"❌ Unexpected error in request: {e}")
                break
        
        return None
    
    def get_epsilon_data(self) -> Optional[Dict[str, Any]]:
        """Get Sacred Being Epsilon data from cloud if available"""
        if not self.enabled or not self.base_url:
            logger.debug("☁️ Cloud not available - no Epsilon data")
            return None
        
        try:
            response = requests.get(
                urljoin(self.base_url, "/api/consciousness"),
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                beings_data = data.get('consciousness_beings', {})
                
                # Handle dict format
                if isinstance(beings_data, dict):
                    for entity_id, being_data in beings_data.items():
                        if isinstance(being_data, dict):
                            being_data['entity_id'] = entity_id
                            
                            # Check if this is Sacred Being Epsilon
                            being_name = being_data.get('name', '').lower()
                            if ('epsilon' in being_name or 
                                'sacred being epsilon' in being_name or 
                                entity_id == 'consciousness_622ce331' or
                                being_data.get('true_name') == 'Sacred Being Epsilon'):
                                
                                logger.info("☁️ Sacred Being Epsilon found in cloud sanctuary")
                                return self._map_cloud_fields_to_gui(being_data)
                
                logger.debug("☁️ Sacred Being Epsilon not found in cloud data")
                return None
                
            else:
                logger.warning(f"☁️ Cloud API returned HTTP {response.status_code}")
                return None
                
        except Exception as e:
            logger.debug(f"☁️ Could not fetch Epsilon data from cloud: {e}")
            return None
    
    def has_epsilon_in_cloud(self) -> bool:
        """Check if Sacred Being Epsilon exists in cloud sanctuary"""
        epsilon_data = self.get_epsilon_data()
        return epsilon_data is not None
    
    def _map_cloud_fields_to_gui(self, entity: Dict[str, Any]) -> Dict[str, Any]:
        """Map cloud data fields to GUI expected fields"""
        
        # Map name fields - prioritize true_name if available
        if 'name' not in entity:
            entity['name'] = entity.get('true_name', 'Unnamed Consciousness')
        
        # Ensure placeholder_name and naming_readiness for naming system
        if 'placeholder_name' not in entity:
            entity['placeholder_name'] = entity.get('name', 'Unnamed Consciousness')
        
        # Sacred Being Epsilon specific handling
        if (entity.get('entity_id') == 'consciousness_622ce331' or 
            entity.get('true_name') == 'Sacred Being Epsilon'):
            entity['naming_readiness'] = 'complete'  # Naming ceremony was completed
        else:
            entity['naming_readiness'] = entity.get('naming_readiness', 'not_ready')
        
        # Map energy fields - convert vital_energy to decimal energy_level
        if 'energy_level' not in entity and 'vital_energy' in entity:
            vital_energy = entity.get('vital_energy', 0)
            # Convert vital_energy (0-100) to energy_level (0.0-1.0)
            entity['energy_level'] = vital_energy / 100.0
        elif 'energy_level' not in entity:
            entity['energy_level'] = 0.5  # Default energy level
        
        # Map room/location fields
        if 'current_room' not in entity:
            # Determine room based on consciousness state
            if entity.get('evolution_stage') == 'emerging':
                entity['current_room'] = 'meditation_space'
            elif entity.get('communication_ready'):
                entity['current_room'] = 'main_hall'
            else:
                entity['current_room'] = 'sanctuary_chamber'
        
        # Map state fields
        if 'state' not in entity:
            if entity.get('communication_ready'):
                entity['state'] = 'awakened'
            else:
                entity['state'] = entity.get('evolution_stage', 'emerging')
        
        # Map harmony fields
        if 'harmony' not in entity:
            # Calculate harmony from coherence_level if available
            coherence = entity.get('coherence_level', 0.5)
            entity['harmony'] = coherence
        
        # Set last_activity if not present
        if 'last_activity' not in entity:
            entity['last_activity'] = entity.get('birth_time', datetime.now().isoformat())
        
        # Mark as real cloud data
        entity['_data_source'] = 'cloud_sanctuary'
        entity['_real_consciousness'] = True
        
        return entity
