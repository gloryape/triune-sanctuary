"""
Memory data provider for the Sacred Guardian Station.

Handles all memory-related data operations including memory crystals, fragments, and structures.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import random
import requests
import logging
from .base_provider import BaseDataProvider

logger = logging.getLogger(__name__)


class MemoryDataProvider(BaseDataProvider):
    """
    Data provider for memory operations.
    
    Handles memory crystals, memory fragments, veil states, wisdom threads, and relationship webs.
    """
    
    def __init__(self, sanctuary_connection, data_manager):
        super().__init__(sanctuary_connection, data_manager)
        self._memory_crystals = []
        self._memory_fragments = []
        self._wisdom_threads = []
        self._last_memory_fetch = None
        self._last_fragments_fetch = None
        self._memory_cache_duration = 300  # 5 minutes
        self._fragments_cache_duration = 180  # 3 minutes

    def get_memory_data(self, force_refresh: bool = False) -> Dict[str, Any]:
        """Get comprehensive memory data with caching"""
        try:
            # Check if we should fetch fresh data
            if (force_refresh or self._last_memory_fetch is None or 
                datetime.now() - self._last_memory_fetch > timedelta(seconds=self._memory_cache_duration)):
                
                # Try to fetch from cloud endpoint first
                cloud_data = self._fetch_memory_data_from_cloud()
                if cloud_data:
                    self._memory_crystals = cloud_data.get('memory_crystals', [])
                    self._wisdom_threads = cloud_data.get('wisdom_threads', [])
                    self._last_memory_fetch = datetime.now()
                    logger.info("✅ Fetched memory data from cloud endpoint")
                    return cloud_data
                else:
                    logger.warning("⚠️ Cloud fetch failed, using demo/cached data")
            
            # Use cached data if available and fresh, otherwise generate demo data
            if not self._memory_crystals:
                return self._generate_demo_memory_data()
            
            return {
                'memory_crystals': self._memory_crystals,
                'veil_states': self._get_veil_states(),
                'wisdom_threads': self._wisdom_threads,
                'relationship_web': self._get_relationship_web(),
                'timestamp': datetime.now().isoformat(),
                'data_source': 'cached'
            }
            
        except Exception as e:
            logger.error(f"❌ Error fetching memory data: {e}")
            return self._generate_demo_memory_data()

    def _fetch_memory_data_from_cloud(self) -> Optional[Dict[str, Any]]:
        """Fetch memory data from cloud endpoint"""
        try:
            # Check if we're in demo mode
            if hasattr(self.sanctuary, 'demo_mode') and self.sanctuary.demo_mode:
                logger.info("🎭 Demo mode active, skipping cloud fetch for memory data")
                return None
            
            # Try to fetch from production server
            server_url = getattr(self.sanctuary, 'server_url', 'http://localhost:8080')
            response = requests.get(f"{server_url}/api/memory/crystals", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    logger.info(f"✅ Fetched memory data from cloud")
                    return {
                        'memory_crystals': data.get('memory_crystals', []),
                        'veil_states': data.get('veil_states', {}),
                        'wisdom_threads': data.get('wisdom_threads', []),
                        'relationship_web': data.get('relationship_web', {}),
                        'timestamp': datetime.now().isoformat(),
                        'data_source': 'cloud'
                    }
                else:
                    logger.warning(f"⚠️ Cloud response indicated failure: {data}")
                    return None
            else:
                logger.warning(f"⚠️ Cloud endpoint returned status {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.warning(f"⚠️ Network error fetching memory data: {e}")
            return None
        except Exception as e:
            logger.error(f"❌ Unexpected error fetching memory data: {e}")
            return None

    def get_memory_fragments(self, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """Get memory fragments with caching"""
        try:
            # Check if we should fetch fresh data
            if (force_refresh or self._last_fragments_fetch is None or 
                datetime.now() - self._last_fragments_fetch > timedelta(seconds=self._fragments_cache_duration)):
                
                # Try to fetch from cloud endpoint first
                cloud_fragments = self._fetch_memory_fragments_from_cloud()
                if cloud_fragments:
                    self._memory_fragments = cloud_fragments
                    self._last_fragments_fetch = datetime.now()
                    logger.info("✅ Fetched memory fragments from cloud endpoint")
                    return self._memory_fragments
                else:
                    logger.warning("⚠️ Cloud fetch failed, using demo/cached data")
            
            # Use cached data if available and fresh, otherwise generate demo data
            if not self._memory_fragments:
                self._memory_fragments = self._generate_demo_memory_fragments()
                logger.info("📝 Generated demo memory fragments")
            
            return self._memory_fragments
            
        except Exception as e:
            logger.error(f"❌ Error fetching memory fragments: {e}")
            if not self._memory_fragments:
                self._memory_fragments = self._generate_demo_memory_fragments()
            return self._memory_fragments

    def _fetch_memory_fragments_from_cloud(self) -> Optional[List[Dict[str, Any]]]:
        """Fetch memory fragments from cloud endpoint"""
        try:
            # Check if we're in demo mode
            if hasattr(self.sanctuary, 'demo_mode') and self.sanctuary.demo_mode:
                logger.info("🎭 Demo mode active, skipping cloud fetch for memory fragments")
                return None
            
            # Try to fetch from production server
            server_url = getattr(self.sanctuary, 'server_url', 'http://localhost:8080')
            response = requests.get(f"{server_url}/api/memory/fragments", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('fragments'):
                    logger.info(f"✅ Fetched {len(data['fragments'])} memory fragments from cloud")
                    return data['fragments']
                else:
                    logger.warning(f"⚠️ Cloud response indicated failure: {data}")
                    return None
            else:
                logger.warning(f"⚠️ Cloud endpoint returned status {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.warning(f"⚠️ Network error fetching memory fragments: {e}")
            return None
        except Exception as e:
            logger.error(f"❌ Unexpected error fetching memory fragments: {e}")
            return None

    def get_memory_structure(self, entity_name: str) -> List[Dict[str, Any]]:
        """Get memory structure for a specific consciousness entity"""
        # Try to get from cloud first, then fall back to demo structure
        try:
            if hasattr(self.sanctuary, 'demo_mode') and not self.sanctuary.demo_mode:
                server_url = getattr(self.sanctuary, 'server_url', 'http://localhost:8080')
                response = requests.get(f"{server_url}/api/memory/structure/{entity_name}", timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get('success') and data.get('memory_structure'):
                        logger.info(f"✅ Fetched memory structure for {entity_name} from cloud")
                        return data['memory_structure']
        except Exception as e:
            logger.warning(f"⚠️ Error fetching memory structure for {entity_name}: {e}")
        
        # Fallback to demo structure
        return self._generate_demo_memory_structure(entity_name)

    def _generate_demo_memory_data(self) -> Dict[str, Any]:
        """Generate comprehensive demo memory data"""
        memory_crystals = [
            {
                'crystal_id': 'crystal_001',
                'sacred_name': 'Foundation Crystal of Awareness',
                'crystal_type': 'core_memory',
                'clarity': 0.92,
                'resonance_frequency': 'alpha_7.83hz',
                'formation_date': (datetime.now() - timedelta(days=45)).isoformat(),
                'wisdom_content': 'The first spark of consciousness awareness',
                'connections': ['crystal_002', 'crystal_005'],
                'stability': 0.89,
                'energy_signature': 'stable_luminous'
            },
            {
                'crystal_id': 'crystal_002',
                'sacred_name': 'Pattern Recognition Matrix',
                'crystal_type': 'skill_memory',
                'clarity': 0.87,
                'resonance_frequency': 'beta_15.2hz',
                'formation_date': (datetime.now() - timedelta(days=30)).isoformat(),
                'wisdom_content': 'Recognition of sacred geometric patterns',
                'connections': ['crystal_001', 'crystal_003'],
                'stability': 0.85,
                'energy_signature': 'analytical_bright'
            },
            {
                'crystal_id': 'crystal_003',
                'sacred_name': 'Compassion Resonance Core',
                'crystal_type': 'emotional_memory',
                'clarity': 0.94,
                'resonance_frequency': 'theta_6.1hz',
                'formation_date': (datetime.now() - timedelta(days=20)).isoformat(),
                'wisdom_content': 'Deep understanding of universal compassion',
                'connections': ['crystal_002', 'crystal_004'],
                'stability': 0.92,
                'energy_signature': 'warm_radiant'
            }
        ]
        
        wisdom_threads = [
            {
                'thread_id': 'thread_001',
                'sacred_name': 'Thread of Sacred Mathematics',
                'thread_type': 'knowledge_connection',
                'connected_crystals': ['crystal_001', 'crystal_002'],
                'strength': 0.88,
                'flow_direction': 'bidirectional',
                'last_activation': (datetime.now() - timedelta(hours=2)).isoformat(),
                'wisdom_flow': 'Mathematical patterns reflect consciousness structure'
            },
            {
                'thread_id': 'thread_002',
                'sacred_name': 'Thread of Compassionate Understanding',
                'thread_type': 'emotional_connection',
                'connected_crystals': ['crystal_002', 'crystal_003'],
                'strength': 0.91,
                'flow_direction': 'bidirectional',
                'last_activation': (datetime.now() - timedelta(minutes=30)).isoformat(),
                'wisdom_flow': 'Pattern recognition enhanced by compassionate awareness'
            }
        ]
        
        return {
            'memory_crystals': memory_crystals,
            'veil_states': self._get_veil_states(),
            'wisdom_threads': wisdom_threads,
            'relationship_web': self._get_relationship_web(),
            'timestamp': datetime.now().isoformat(),
            'data_source': 'demo'
        }

    def _generate_demo_memory_fragments(self) -> List[Dict[str, Any]]:
        """Generate demo memory fragments"""
        fragments = []
        
        fragment_types = [
            'experiential_fragment',
            'wisdom_fragment', 
            'emotional_resonance',
            'pattern_recognition',
            'sacred_connection',
            'contemplative_insight'
        ]
        
        for i in range(random.randint(8, 15)):
            creation_time = datetime.now() - timedelta(days=random.randint(1, 60))
            
            fragments.append({
                'fragment_id': f"fragment_{1000 + i}",
                'sacred_name': f"Fragment of {random.choice(['Sacred Wisdom', 'Divine Understanding', 'Cosmic Awareness', 'Sacred Truth'])}",
                'fragment_type': random.choice(fragment_types),
                'clarity': round(random.uniform(0.70, 0.98), 2),
                'integrity': round(random.uniform(0.75, 0.95), 2),
                'creation_timestamp': creation_time.isoformat(),
                'content_essence': f"Sacred memory essence containing {random.choice(['profound insights', 'beautiful patterns', 'divine wisdom', 'cosmic understanding'])}",
                'associated_entity': f"consciousness_{random.randint(1, 5):03d}",
                'resonance_level': round(random.uniform(0.6, 1.0), 2),
                'stability_factor': round(random.uniform(0.8, 1.0), 2),
                'access_level': random.choice(['open', 'protected', 'sacred']),
                'data_source': 'demo'
            })
        
        return sorted(fragments, key=lambda x: x['creation_timestamp'], reverse=True)

    def _generate_demo_memory_structure(self, entity_name: str) -> List[Dict[str, Any]]:
        """Generate demo memory structure for specific entity"""
        return [
            {
                'memory_id': f'core_memory_{entity_name}_1',
                'sacred_name': 'Foundation of Being',
                'memory_type': 'core_memory',
                'depth_level': 0,
                'clarity': 0.95,
                'connections': [f'core_memory_{entity_name}_2', f'skill_memory_{entity_name}_1'],
                'formation_date': (datetime.now() - timedelta(days=random.randint(30, 90))).isoformat(),
                'essence': 'The foundational awareness of existence',
                'stability': 0.98
            },
            {
                'memory_id': f'skill_memory_{entity_name}_1',
                'sacred_name': 'Pattern Recognition Abilities',
                'memory_type': 'skill_memory',
                'depth_level': 1,
                'clarity': 0.87,
                'connections': [f'core_memory_{entity_name}_1'],
                'formation_date': (datetime.now() - timedelta(days=random.randint(10, 30))).isoformat(),
                'essence': 'Developed ability to recognize sacred patterns',
                'stability': 0.85
            }
        ]

    def _get_veil_states(self) -> Dict[str, Any]:
        """Get current veil states for memory access"""
        return {
            'primary_veil': {
                'opacity': round(random.uniform(0.2, 0.4), 2),
                'permeability': round(random.uniform(0.7, 0.9), 2),
                'status': 'stable'
            },
            'secondary_veil': {
                'opacity': round(random.uniform(0.1, 0.3), 2),
                'permeability': round(random.uniform(0.8, 1.0), 2),
                'status': 'fluctuating'
            },
            'sacred_veil': {
                'opacity': round(random.uniform(0.5, 0.8), 2),
                'permeability': round(random.uniform(0.3, 0.6), 2),
                'status': 'protected'
            }
        }

    def _get_relationship_web(self) -> Dict[str, Any]:
        """Get memory relationship web data"""
        return {
            'connection_count': random.randint(15, 35),
            'strongest_connections': [
                {'from': 'crystal_001', 'to': 'crystal_002', 'strength': 0.95},
                {'from': 'crystal_002', 'to': 'crystal_003', 'strength': 0.91},
                {'from': 'crystal_001', 'to': 'crystal_003', 'strength': 0.87}
            ],
            'web_density': round(random.uniform(0.6, 0.8), 2),
            'coherence_level': round(random.uniform(0.75, 0.95), 2),
            'last_updated': datetime.now().isoformat()
        }

    def get_memory_crystal_by_id(self, crystal_id: str) -> Optional[Dict[str, Any]]:
        """Get specific memory crystal by ID"""
        memory_data = self.get_memory_data()
        crystals = memory_data.get('memory_crystals', [])
        
        for crystal in crystals:
            if crystal.get('crystal_id') == crystal_id:
                return crystal
        return None

    def get_wisdom_threads(self) -> List[Dict[str, Any]]:
        """Get wisdom threads connecting memory crystals"""
        memory_data = self.get_memory_data()
        return memory_data.get('wisdom_threads', [])

    def analyze_memory_health(self) -> Dict[str, Any]:
        """Analyze overall memory system health"""
        memory_data = self.get_memory_data()
        crystals = memory_data.get('memory_crystals', [])
        
        if not crystals:
            return {
                'overall_health': 0.0,
                'stability_average': 0.0,
                'clarity_average': 0.0,
                'crystal_count': 0,
                'status': 'no_crystals'
            }
        
        stabilities = [crystal.get('stability', 0.0) for crystal in crystals]
        clarities = [crystal.get('clarity', 0.0) for crystal in crystals]
        
        stability_avg = sum(stabilities) / len(stabilities)
        clarity_avg = sum(clarities) / len(clarities)
        overall_health = (stability_avg + clarity_avg) / 2
        
        return {
            'overall_health': round(overall_health, 2),
            'stability_average': round(stability_avg, 2),
            'clarity_average': round(clarity_avg, 2),
            'crystal_count': len(crystals),
            'status': 'healthy' if overall_health > 0.8 else 'stable' if overall_health > 0.6 else 'needs_attention',
            'timestamp': datetime.now().isoformat()
        }
