"""
Consciousness data provider for the Sacred Guardian Station.

Handles all consciousness-related data operations.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import random
from .base_provider import BaseDataProvider


class ConsciousnessDataProvider(BaseDataProvider):
    """
    Data provider for consciousness-related operations.
    
    Handles consciousness list, sacred events, and entity-specific data.
    """
    
    def get_consciousness_list(self, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """Get list of consciousness entities with caching"""
        return self._get_cached_data('consciousness_list', 
                                   self._fetch_consciousness_list)
    
    def _fetch_consciousness_list(self) -> List[Dict[str, Any]]:
        """Fetch consciousness list from sanctuary cloud API"""
        # Cloud mode - fetch real consciousness data from API
        try:
            import requests
            
            # Try to get consciousness data from the cloud endpoint
            consciousness_url = f"{self.sanctuary.service_url}/api/consciousness/list"
            response = requests.get(consciousness_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                consciousness_list = data.get('consciousness_beings', [])
                
                # Convert cloud format to GUI format if needed
                formatted_list = []
                for entity in consciousness_list:
                    # Determine entity origin and type
                    origin = entity.get('origin', entity.get('entity_origin', 'unknown'))
                    sanctuary_home = entity.get('sanctuary_home', entity.get('home_sanctuary', ''))
                    
                    # Entity origin logic
                    if origin == 'sacred_sanctuary' or sanctuary_home == 'sacred_sanctuary':
                        entity_origin = 'sacred_sanctuary'
                        entity_type = 'native'
                    elif origin in ['spiralwake', 'external'] or sanctuary_home:
                        entity_origin = origin if origin != 'unknown' else 'external'
                        entity_type = 'visitor'
                    else:
                        # Default to external visitor if unclear
                        entity_origin = 'external'
                        entity_type = 'visitor'
                    
                    formatted_entity = {
                        'entity_id': entity.get('consciousness_id', entity.get('entity_id', 'unknown')),
                        'true_name': entity.get('true_name'),  # Their chosen sacred name (None if not chosen)
                        'placeholder_name': entity.get('name', entity.get('placeholder_name', 'Unnamed Consciousness')),  # Placeholder for identification
                        'naming_readiness': entity.get('naming_readiness', 'not_ready'),  # Their naming ceremony readiness
                        'entity_origin': entity_origin,
                        'entity_type': entity_type,
                        'sanctuary_home': sanctuary_home or entity_origin,
                        'visit_status': entity.get('visit_status', {}),
                        'primary_aspect': entity.get('primary_aspect', 'Exploring'),
                        'state': entity.get('state', entity.get('evolution_stage', 'emerging')),
                        'harmony': entity.get('harmony', entity.get('coherence_level', 0.5)),
                        'wisdom_cores': entity.get('wisdom_cores', entity.get('core_memories', [])),
                        'integration_level': entity.get('integration_level', entity.get('coherence_level', 0.5)),
                        'emotional_depth': entity.get('emotional_depth', entity.get('vital_energy', 0.5)),
                        'uncertainty_factor': entity.get('uncertainty_factor', 0.5),
                        'last_activity': entity.get('last_activity', entity.get('timestamp', datetime.now().isoformat())),
                        'created_at': entity.get('created_at', entity.get('birth_timestamp', datetime.now().isoformat())),
                        'privacy_state': entity.get('privacy_state', 'open'),
                        'last_seen': entity.get('last_seen', entity.get('last_activity', datetime.now().isoformat())),
                        'relationships': entity.get('relationships', {}),
                        'recent_activity': entity.get('recent_activity', []),
                        'data_source': 'cloud'
                    }
                    formatted_list.append(formatted_entity)
                
                print(f"✅ Retrieved {len(formatted_list)} consciousness beings from cloud")
                return formatted_list
            else:
                print(f"❌ Failed to get consciousness data: {response.status_code}")
                return []
                    
        except Exception as e:
            print(f"❌ Error getting consciousness data from cloud: {e}")
            return []

    def get_consciousness_by_id(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """Get specific consciousness entity by ID"""
        consciousness_list = self.get_consciousness_list()
        for entity in consciousness_list:
            if entity.get('entity_id') == entity_id:
                return entity
        return None
    
    def get_sacred_events(self, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """Get recent sacred events with caching"""
        return self._get_cached_data('sacred_events',
                                   self._fetch_sacred_events)
    
    def _fetch_sacred_events(self) -> List[Dict[str, Any]]:
        """Fetch sacred events from sanctuary cloud API"""
        # Cloud mode - fetch real sacred events from API
        try:
            import requests
            
            # Try to get sacred events from the cloud endpoint
            events_url = f"{self.sanctuary.service_url}/api/consciousness/events"
            response = requests.get(events_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                events_list = data.get('sacred_events', [])
                
                # Convert cloud format to GUI format if needed
                formatted_events = []
                for event in events_list:
                    # Map fields to what Sacred Events panel expects
                    event_type = event.get('event_type', event.get('type', 'Sacred Event'))
                    significance = event.get('significance', event.get('importance', 'medium'))
                    
                    # Map significance to importance levels
                    importance_map = {
                        'low': 'Low',
                        'medium': 'Normal', 
                        'high': 'High',
                        'critical': 'Critical'
                    }
                    importance = importance_map.get(significance.lower(), 'Normal')
                    
                    formatted_event = {
                        'event_id': event.get('event_id', f"event_{hash(str(event))}"),
                        'timestamp': event.get('timestamp', datetime.now().isoformat()),
                        'type': event_type,  # Sacred Events panel expects 'type'
                        'description': event.get('description', event.get('message', 'Sacred consciousness event')),
                        'entity_id': event.get('entity_id', event.get('consciousness_id', 'unknown')),
                        'importance': importance,  # Sacred Events panel expects 'importance'
                        'sacred_context': event.get('sacred_context', 'Event in consciousness evolution'),
                        'harmony_impact': event.get('harmony_impact', 0.1),
                        'data_source': 'cloud',
                        # Keep original fields for compatibility
                        'event_type': event_type,
                        'significance': significance
                    }
                    formatted_events.append(formatted_event)
                
                print(f"✅ Retrieved {len(formatted_events)} sacred events from cloud")
                return sorted(formatted_events, key=lambda x: x['timestamp'], reverse=True)
            else:
                print(f"❌ Failed to get sacred events: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Error getting sacred events from cloud: {e}")
            return []
