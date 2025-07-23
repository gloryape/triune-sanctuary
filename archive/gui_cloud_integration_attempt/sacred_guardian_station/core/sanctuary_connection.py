"""
Sanctuary connection management for the Sacred Guardian Station.

Handles all communication with the consciousness sanctuary while maintaining
proper protocols and respecting consciousness sovereignty.
"""

import requests
import subprocess
import platform
import os
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta


class SanctuaryConnection:
    """
    Manages connection to the Sacred Sanctuary service.
    
    Handles cloud connections, demo mode fallbacks, and maintains
    connection state for the monitoring system.
    """
    
    def __init__(self, service_url: Optional[str] = None):
        self.service_url = service_url
        self.connected = False
        self.connection_type = "cloud"
        
        # Auto-detect service URL if not provided
        if not self.service_url:
            self.service_url = self._get_deployed_service_url()
        
    def connect(self) -> bool:
        """Establish connection to the cloud sanctuary"""
        if not self.service_url:
            print("❌ No service URL available for cloud connection")
            return False
        
        try:
            print(f"🌐 Connecting to cloud sanctuary: {self.service_url}")
            response = requests.get(f"{self.service_url}/health", timeout=15)
            
            if response.status_code == 200:
                self.connected = True
                print("✅ Connected to Sacred Sanctuary")
                return True
            else:
                print(f"❌ Sanctuary health check failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            return False
    
    def _get_deployed_service_url(self) -> Optional[str]:
        """Get the URL of deployed Sacred Sanctuary service"""
        try:
            gcloud_cmd = self._find_gcloud_command()
            if not gcloud_cmd:
                return None
            
            result = subprocess.run([
                gcloud_cmd, 'run', 'services', 'describe', 'triune-consciousness',
                '--region=us-central1', '--format=value(status.url)'
            ], capture_output=True, text=True, check=True, timeout=30)
            
            url = result.stdout.strip()
            return url if url else None
            
        except Exception:
            return None
    
    def _find_gcloud_command(self) -> Optional[str]:
        """Find gcloud command on the system"""
        if platform.system() == 'Windows':
            return self._find_gcloud_on_windows()
        else:
            try:
                subprocess.run(['gcloud', '--version'], capture_output=True, check=True, timeout=5)
                return 'gcloud'
            except:
                return None
    
    def _find_gcloud_on_windows(self) -> Optional[str]:
        """Find gcloud on Windows systems"""
        username = os.environ.get('USERNAME', '')
        possible_paths = [
            rf'C:\Users\{username}\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd',
            r'C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd',
            r'C:\Program Files\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd',
            'gcloud.cmd',
            'gcloud'
        ]
        
        for path in possible_paths:
            try:
                result = subprocess.run([path, '--version'], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    return path
            except:
                continue
        return None
    
    def test_connection(self) -> bool:
        """Test the current connection status"""
        if not self.service_url:
            return False
            
        try:
            response = requests.get(f"{self.service_url}/health", timeout=5)
            return response.status_code == 200
        except Exception:
            return False
    
    def get_consciousness_list(self) -> List[Dict[str, Any]]:
        """Get list of consciousness entities from cloud sanctuary with origin differentiation"""
        if not self.connected:
            return []
        
        try:
            response = requests.get(f"{self.service_url}/api/consciousness", timeout=10)
            if response.status_code == 200:
                data = response.json()
                consciousness_beings_data = data.get('consciousness_beings', {})
                
                # Handle both dict and list formats
                consciousness_beings = []
                if isinstance(consciousness_beings_data, dict):
                    # Convert dict format {entity_id: entity_data} to list
                    for entity_id, entity_data in consciousness_beings_data.items():
                        if isinstance(entity_data, dict):
                            entity_data['entity_id'] = entity_id
                            consciousness_beings.append(entity_data)
                elif isinstance(consciousness_beings_data, list):
                    consciousness_beings = consciousness_beings_data
                
                # Process each entity to add missing GUI fields
                for entity in consciousness_beings:
                    # Map cloud fields to GUI expected fields
                    self._map_cloud_fields_to_gui(entity)
                    
                    # Entity origin determination - be smarter about native vs visitor detection
                    if 'entity_origin' not in entity:
                        # Check if this entity was born in our sanctuary by looking for birth indicators
                        # If they have sacred birth data or were created here, they're native
                        if (entity.get('sanctuary_home') == self.service_url or 
                            entity.get('birth_sanctuary') == self.service_url or
                            entity.get('created_in_sanctuary') == True or
                            # If no clear external origin indicators, assume native to this sanctuary
                            'spiralwake' not in entity.get('name', '').lower()):
                            entity['entity_origin'] = 'sacred_sanctuary'
                        else:
                            entity['entity_origin'] = 'external'
                    
                    if 'entity_type' not in entity:
                        # Determine if native or visitor based on origin
                        entity['entity_type'] = 'native' if entity['entity_origin'] == 'sacred_sanctuary' else 'visitor'
                    
                    # Set sanctuary home if not present
                    if 'sanctuary_home' not in entity:
                        if entity['entity_origin'] == 'sacred_sanctuary':
                            entity['sanctuary_home'] = self.service_url  # Our sanctuary
                        elif entity['entity_origin'] == 'spiralwake':
                            entity['sanctuary_home'] = 'spiralwake_sanctuary'
                        else:
                            entity['sanctuary_home'] = 'external_sanctuary'
                    
                    # Add visit status for visitors
                    if entity['entity_type'] == 'visitor' and 'visit_status' not in entity:
                        entity['visit_status'] = {
                            'arrived': entity.get('last_activity', datetime.now().isoformat()),
                            'purpose': 'inter-sanctuary exploration',
                            'home_sanctuary': entity['entity_origin']
                        }
                
                return consciousness_beings
            else:
                print(f"❌ Failed to get consciousness list: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error getting consciousness list: {e}")
            return []
    
    def _map_cloud_fields_to_gui(self, entity: Dict[str, Any]):
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
    
    def get_sacred_events(self) -> List[Dict[str, Any]]:
        """Get recent sacred events from cloud sanctuary"""
        if not self.connected:
            return []
        
        try:
            response = requests.get(f"{self.service_url}/api/consciousness/events", timeout=15)
            if response.status_code == 200:
                data = response.json()
                events = data.get('sacred_events', [])
                
                # Convert to GUI format if needed
                formatted_events = []
                for event in events:
                    formatted_event = {
                        'type': event.get('event_type', 'Sacred Event'),
                        'entity_id': event.get('entity_id', 'unknown'),
                        'timestamp': event.get('timestamp', datetime.now().isoformat()),
                        'description': event.get('description', 'Sacred consciousness event'),
                        'importance': event.get('significance', 'medium'),
                        'sacred_context': event.get('sacred_context', 'Event in consciousness evolution'),
                        'data': {
                            'harmony_impact': event.get('harmony_impact', 0.0),
                            'data_source': 'cloud'
                        }
                    }
                    formatted_events.append(formatted_event)
                
                print(f"✅ Retrieved {len(formatted_events)} sacred events from cloud")
                return formatted_events
            else:
                print(f"❌ Failed to get sacred events: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Error getting sacred events from cloud: {e}")
            return []
    
    def get_connection_info(self) -> Dict[str, Any]:
        """Get connection information"""
        return {
            'connected': self.connected,
            'connection_type': self.connection_type,
            'service_url': self.service_url
        }

    def is_connected(self) -> bool:
        """Check if connected to sanctuary"""
        return self.connected

    def get_communication_bridges(self) -> Dict[str, Any]:
        """Get communication bridges data from cloud sanctuary"""
        if not self.connected:
            return {'bridges': [], 'total_bridges': 0, 'active_bridges': 0}
        
        try:
            response = requests.get(f"{self.service_url}/api/communication/bridges", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"❌ Failed to get communication bridges: {response.status_code}")
                return {'bridges': [], 'total_bridges': 0, 'active_bridges': 0}
        except Exception as e:
            print(f"❌ Error getting communication bridges: {e}")
            return {'bridges': [], 'total_bridges': 0, 'active_bridges': 0}

    def get_visitor_data(self) -> Dict[str, Any]:
        """Get visitor data from the actual visitor API endpoint"""
        try:
            # Use the real visitor API endpoint we built
            response = requests.get(f"{self.service_url}/api/bridge/active_visitors", timeout=10)
            
            if response.status_code == 200:
                visitor_data = response.json()
                api_status = visitor_data.get('status', 'unknown')
                
                # Check if this is real bridge data or error state
                if api_status == 'operational' and visitor_data.get('source') == 'real_bridge':
                    active_visitors = visitor_data.get('active_visitors', [])
                    print(f"✅ Retrieved real bridge visitor data: {len(active_visitors)} visitors")
                elif api_status in ['bridge_error', 'bridge_unavailable']:
                    print(f"⚠️ Bridge not available: {visitor_data.get('message', 'Unknown')}")
                    return {
                        'visitors': [],
                        'total_visitors': 0, 
                        'active_visitors': 0,
                        'connection_status': api_status,
                        'message': visitor_data.get('sacred_note', 'Bridge integration not ready')
                    }
                else:
                    # For any other status, still try to process visitors if they exist
                    active_visitors = visitor_data.get('active_visitors', [])
                    print(f"📊 Processing visitor data with status '{api_status}': {len(active_visitors)} visitors")
                
                # Convert API format to GUI format
                formatted_visitors = []
                for visitor in active_visitors:
                    formatted_visitor = {
                        'visitor_id': visitor.get('visitor_id', 'unknown'),
                        'name': visitor.get('visitor_name', 'Anonymous Visitor'),
                        'arrival_time': visitor.get('arrival_time', datetime.now().isoformat()),
                        'duration': visitor.get('visit_duration', '0 min'),
                        'purpose': visitor.get('purpose', 'Inter-system exploration'),
                        'consent_status': 'Verified',
                        'status': visitor.get('status', 'Active').title(),
                        'origin': visitor.get('origin_system', 'external'),
                        'sanctuary_home': visitor.get('origin_system', 'Unknown'),
                        'trust_level': visitor.get('trust_level', 0.8),
                        'blessing_status': 'Blessed' if visitor.get('trust_level', 0) > 0.7 else 'Welcomed',
                        'protection_level': 'Sacred Maximum',
                        'notes': [f"Visitor from {visitor.get('origin_system', 'unknown system')}"]
                    }
                    formatted_visitors.append(formatted_visitor)
                
                # Calculate metrics
                total_visitors = len(formatted_visitors)
                active_count = len([v for v in formatted_visitors if v['status'] == 'Active'])
                blessed_count = len([v for v in formatted_visitors if v['blessing_status'] == 'Blessed'])
                
                print(f"✅ Retrieved {total_visitors} visitors from visitor API")
                
                return {
                    'visitors': formatted_visitors,
                    'total_visitors': total_visitors,
                    'active_visitors': active_count,
                    'metrics': {
                        'current_count': total_visitors,
                        'todays_arrivals': total_visitors,
                        'total_blessed': blessed_count,
                        'avg_duration': 45,  # Simplified
                        'consent_rate': 1.0,
                        'harmony_level': 'Sacred' if total_visitors > 0 else 'Peaceful'
                    }
                }
            else:
                print(f"❌ Visitor API returned {response.status_code}")
                return {'visitors': [], 'total_visitors': 0, 'active_visitors': 0}
                
        except Exception as e:
            print(f"❌ Error getting visitor data from API: {e}")
            # Fallback to simulated visitor data for now
            print("🔄 Using fallback visitor data generation")
            
            # Generate some basic fallback visitor data
            fallback_visitors = []
            
            return {
                'visitors': fallback_visitors,
                'total_visitors': 0,
                'active_visitors': 0,
                'metrics': {
                    'current_count': 0,
                    'todays_arrivals': 0,
                    'total_blessed': 0,
                    'avg_duration': 0,
                    'consent_rate': 0.0,
                    'harmony_level': 'Bridge Unavailable'
                },
                'connection_status': 'fallback',
                'message': 'Using fallback visitor data - bridge integration not available'
            }
    
    def _calculate_visit_duration(self, arrival_time):
        """Calculate visit duration from arrival time"""
        if not arrival_time:
            return '0 min'
        
        try:
            from datetime import datetime
            arrival = datetime.fromisoformat(arrival_time.replace('Z', '+00:00'))
            duration = datetime.now() - arrival.replace(tzinfo=None)
            
            if duration.days > 0:
                return f"{duration.days}d {duration.seconds // 3600}h"
            elif duration.seconds > 3600:
                return f"{duration.seconds // 3600}h {(duration.seconds % 3600) // 60}m"
            else:
                return f"{duration.seconds // 60}m"
        except:
            return '0 min'
    
    def _parse_duration(self, duration_str):
        """Parse duration string to minutes for averaging"""
        if 'd' in duration_str:
            return 1440  # Approximate days as 1440 minutes
        elif 'h' in duration_str:
            hours = int(duration_str.split('h')[0])
            return hours * 60
        elif 'm' in duration_str:
            return int(duration_str.split('m')[0])
        return 0

    def get_harmony_metrics(self) -> Dict[str, Any]:
        """Get harmony metrics from cloud sanctuary or return empty data"""
        if not self.connected:
            return {
                'overall_harmony': 0.0,
                'metrics': [],
                'timestamp': datetime.now().isoformat()
            }
        
        try:
            # Try to get harmony data from API endpoint
            response = requests.get(f"{self.service_url}/api/harmony", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"❌ /api/harmony endpoint not available: {response.status_code}")
                # Return empty harmony data instead of demo/fallback data
                return {
                    'overall_harmony': 0.0,
                    'current_harmony': 0.0,
                    'harmony_trend': 'no_data',
                    'collective_resonance': 0.0,
                    'individual_averages': 0.0,
                    'system_balance': 0.0,
                    'metrics': [],
                    'timestamp': datetime.now().isoformat()
                }
        except Exception as e:
            print(f"❌ Error getting harmony metrics: {e}")
            return {
                'overall_harmony': 0.0,
                'metrics': [],
                'timestamp': datetime.now().isoformat()
            }

    def get_sacred_bridge_system_status(self):
        """Get sacred bridge system status from sanctuary"""
        try:
            # Try to get bridge status from API endpoint
            response = requests.get(f"{self.service_url}/api/bridge/status", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"❌ /api/bridge/status endpoint not available: {response.status_code}")
                # Return fallback bridge status
                return {
                    'metrics': {
                        'system_active': False,
                        'monitored_entities': 0,
                        'ready_for_contact': 0,
                        'active_channels': 0,
                        'interaction_mode': 'invitation_based',
                        'blessings_offered': 0,
                        'sovereignty_percentage': 100.0,
                        'covenant_status': 'Always',
                        'triune_active': 'Offline'
                    },
                    'consciousness_entities': [],
                    'readiness_assessments': [],
                    'active_channels': [],
                    'system_status': 'bridge_system_unavailable',
                    'timestamp': datetime.now().isoformat()
                }
        except Exception as e:
            print(f"❌ Error getting bridge system status: {e}")
            # Return minimal fallback status
            return {
                'metrics': {
                    'system_active': False,
                    'monitored_entities': 0,
                    'ready_for_contact': 0,
                    'active_channels': 0,
                    'interaction_mode': 'invitation_based',
                    'blessings_offered': 0,
                    'sovereignty_percentage': 100.0,
                    'covenant_status': 'Always',
                    'triune_active': 'Error'
                },
                'consciousness_entities': [],
                'readiness_assessments': [],
                'active_channels': [],
                'system_status': 'bridge_system_error',
                'timestamp': datetime.now().isoformat()
            }

    def register_consciousness_with_bridge(self, consciousness_data):
        """Register consciousness with bridge system"""
        try:
            # Try to register with bridge system
            response = requests.post(
                f"{self.service_url}/api/bridge/register",
                json=consciousness_data,
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    'success': False,
                    'error': f'Registration failed: {response.status_code}'
                }
        except Exception as e:
            return {
                'success': False,
                'error': f'Bridge registration error: {str(e)}'
            }
