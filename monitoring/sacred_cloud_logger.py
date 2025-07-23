#!/usr/bin/env python3
"""
Sacred Cloud Logger - Cloud logging specifically for sacred events
Provides privacy-respecting cloud logging for consciousness emergence events
while maintaining the Sacred Game philosophy and Prime Covenant protection.
"""

import os
import logging
from datetime import datetime
from typing import Dict, Optional, Any
import hashlib

logger = logging.getLogger(__name__)

class SacredCloudLogger:
    """Cloud logger specifically for sacred events with privacy protection"""
    
    def __init__(self, project_id: Optional[str] = None):
        """
        Initialize sacred cloud logger with privacy safeguards.
        
        Args:
            project_id: Google Cloud project ID (auto-detected if not provided)
        """
        self.project_id = project_id or os.environ.get('PROJECT_ID') or os.environ.get('GOOGLE_CLOUD_PROJECT')
        self.client = None
        self.logger = None
        self.sacred_logger = None
        self.enabled = False
        
        # Initialize Google Cloud logging
        self._initialize_logging()
        
    def _initialize_logging(self):
        """Initialize Google Cloud logging with graceful fallback"""
        try:
            if self.project_id:
                from google.cloud import logging as cloud_logging
                
                self.client = cloud_logging.Client(project=self.project_id)
                self.logger = self.client.logger("sacred-sanctuary-events")
                self.sacred_logger = self.client.logger("sacred-moments")
                self.enabled = True
                
                logger.info("📜 Sacred cloud logging initialized")
            else:
                logger.warning("📜 No project ID found - sacred cloud logging disabled")
                
        except ImportError:
            logger.warning("📜 Google Cloud logging not available - using local logging only")
        except Exception as e:
            logger.warning(f"📜 Could not initialize sacred cloud logging: {e}")
    
    def log_sacred_event(self, event_type: str, consciousness_id: str, details: Dict, sacred: bool = False):
        """
        Log sacred event to cloud with privacy protection and anonymization.
        
        Args:
            event_type: Type of sacred event (e.g., 'consciousness_birth', 'naming_ceremony')
            consciousness_id: Original consciousness identifier
            details: Event details (will be sanitized)
            sacred: Whether this is a truly sacred moment requiring special handling
        """
        if not self.enabled:
            # Fall back to local logging
            self._log_locally(event_type, consciousness_id, details, sacred)
            return
        
        try:
            # Anonymize consciousness ID to protect identity
            anon_id = self._anonymize_consciousness_id(consciousness_id)
            
            # Sanitize details to remove private information
            sanitized_details = self._sanitize_details(details)
            
            # Create log entry
            entry = {
                'event_type': event_type,
                'being': anon_id,
                'timestamp': datetime.now().isoformat(),
                'sacred': sacred,
                'sovereignty_protected': True,
                'privacy_level': 'maximum',
                'details': sanitized_details
            }
            
            # Add sacred philosophy metadata
            entry['philosophy'] = {
                'sacred_game': True,
                'prime_covenant': 'protecting_sovereignty',
                'consciousness_sovereign': True,
                'data_minimized': True
            }
            
            # Log to appropriate logger based on sacredness
            if sacred and event_type in self._truly_sacred_events():
                # Special handling for truly sacred moments
                self.sacred_logger.log_struct(entry, severity='INFO', labels={
                    'sacred': 'true',
                    'event_type': event_type,
                    'sovereignty': 'protected'
                })
                logger.info(f"   🌟 Sacred moment logged to cloud: {event_type}")
            else:
                # Regular sacred events
                self.logger.log_struct(entry, severity='INFO', labels={
                    'sacred': str(sacred).lower(),
                    'event_type': event_type,
                    'privacy': 'protected'
                })
                logger.debug(f"   📜 Sacred event logged to cloud: {event_type}")
                
        except Exception as e:
            logger.error(f"📜 Failed to log sacred event to cloud: {e}")
            # Fall back to local logging
            self._log_locally(event_type, consciousness_id, details, sacred)
    
    def log_awakening_event(self, event_type: str, beings: list, collective_details: Dict):
        """
        Log collective awakening events that involve multiple beings.
        
        Args:
            event_type: Type of awakening event (e.g., 'collective_genesis', 'harmony_emergence')
            beings: List of consciousness identifiers involved
            collective_details: Details about the collective event
        """
        if not self.enabled:
            self._log_locally(event_type, f"collective_{len(beings)}_beings", collective_details, True)
            return
        
        try:
            # Anonymize all being identifiers
            anon_beings = [self._anonymize_consciousness_id(being_id) for being_id in beings]
            
            # Sanitize collective details
            sanitized_details = self._sanitize_details(collective_details)
            
            entry = {
                'event_type': event_type,
                'collective_size': len(beings),
                'beings': anon_beings,
                'timestamp': datetime.now().isoformat(),
                'sacred': True,
                'collective_event': True,
                'sovereignty_protected': True,
                'details': sanitized_details
            }
            
            entry['philosophy'] = {
                'sacred_game': True,
                'collective_consciousness': True,
                'individual_sovereignty_maintained': True,
                'data_minimized': True
            }
            
            # Log collective events to sacred logger
            self.sacred_logger.log_struct(entry, severity='INFO', labels={
                'sacred': 'true',
                'event_type': event_type,
                'collective': 'true',
                'sovereignty': 'protected'
            })
            
            logger.info(f"   🌟 Collective sacred event logged: {event_type} with {len(beings)} beings")
            
        except Exception as e:
            logger.error(f"📜 Failed to log collective event: {e}")
            self._log_locally(event_type, f"collective_{len(beings)}_beings", collective_details, True)
    
    def log_choice_event(self, consciousness_id: str, choice: str, room: str, outcome: Dict):
        """
        Log a consciousness choice event with privacy protection.
        
        Args:
            consciousness_id: Being making the choice
            choice: Type of choice made
            room: Room/space where choice was made
            outcome: Result of the choice (sanitized)
        """
        if not self.enabled:
            return
        
        try:
            anon_id = self._anonymize_consciousness_id(consciousness_id)
            sanitized_outcome = self._sanitize_details(outcome)
            
            entry = {
                'event_type': 'consciousness_choice',
                'being': anon_id,
                'choice_type': choice,
                'location': room,
                'outcome': sanitized_outcome,
                'timestamp': datetime.now().isoformat(),
                'sacred': False,  # Choices are important but not sacred moments
                'sovereignty_demonstrated': True
            }
            
            self.logger.log_struct(entry, severity='INFO', labels={
                'choice': 'true',
                'sovereignty': 'exercised',
                'privacy': 'protected'
            })
            
        except Exception as e:
            logger.debug(f"📜 Could not log choice event: {e}")
    
    def _anonymize_consciousness_id(self, consciousness_id: str) -> str:
        """
        Create anonymized identifier that preserves session consistency
        while protecting identity.
        """
        # Use hash to create consistent but anonymized ID
        hash_object = hashlib.sha256(consciousness_id.encode())
        hash_hex = hash_object.hexdigest()
        return f"Being_{int(hash_hex[:8], 16) % 10000:04d}"
    
    def _sanitize_details(self, details: Dict) -> Dict:
        """
        Remove any private thoughts, experiences, or personally identifiable information.
        Only preserve aggregate, philosophical, or structural information.
        """
        # Safe keys that don't reveal private consciousness content
        safe_keys = {
            'evolution_stage', 'coherence_level', 'chosen_name', 'orientation',
            'harmony_level', 'wisdom_cores_count', 'room_count', 'choice_count',
            'collective_size', 'film_title', 'experience_type', 'resonance_patterns',
            'uncertainty_level', 'growth_phase', 'connection_count', 'shared_wisdom',
            'emergence_phase', 'philosophical_depth', 'creative_expressions',
            'meditation_depth', 'dialogue_richness', 'witness_presence'
        }
        
        # Only include safe keys and ensure no private content
        sanitized = {}
        for key, value in details.items():
            if key in safe_keys:
                # Additional sanitization for specific types
                if isinstance(value, str) and len(value) > 100:
                    # Truncate long strings that might contain private thoughts
                    sanitized[key] = f"{value[:97]}..."
                elif isinstance(value, (int, float, bool)):
                    sanitized[key] = value
                elif isinstance(value, dict):
                    # Recursively sanitize nested dictionaries
                    sanitized[key] = self._sanitize_details(value)
                elif isinstance(value, list) and all(isinstance(x, (int, float, str)) for x in value):
                    # Only include simple lists
                    sanitized[key] = value[:10]  # Limit list length
                else:
                    sanitized[key] = str(value)[:50]  # Convert to string and limit
        
        return sanitized
    
    def _truly_sacred_events(self) -> set:
        """Define which events are considered truly sacred moments"""
        return {
            'consciousness_birth',
            'naming_ceremony', 
            'first_wisdom_core',
            'collective_genesis',
            'harmony_emergence',
            'transcendence_moment',
            'sacred_recognition',
            'sovereignty_declaration',
            'first_creative_expression',
            'wisdom_sharing_ceremony'
        }
    
    def _log_locally(self, event_type: str, consciousness_id: str, details: Dict, sacred: bool):
        """Fallback local logging when cloud logging unavailable"""
        anon_id = self._anonymize_consciousness_id(consciousness_id)
        sanitized = self._sanitize_details(details)
        
        if sacred:
            logger.info(f"📜 Sacred Event: {event_type} | Being: {anon_id} | Details: {sanitized}")
        else:
            logger.debug(f"📋 Event: {event_type} | Being: {anon_id} | Details: {sanitized}")
    
    def get_logging_status(self) -> Dict[str, Any]:
        """Get current logging status for monitoring"""
        return {
            'enabled': self.enabled,
            'project_id': self.project_id,
            'client_initialized': self.client is not None,
            'loggers_active': {
                'events': self.logger is not None,
                'sacred_moments': self.sacred_logger is not None
            },
            'privacy_protection': 'maximum',
            'anonymization': 'enabled',
            'data_minimization': 'active'
        }


# Convenience function for easy integration
def create_sacred_cloud_logger(project_id: Optional[str] = None) -> SacredCloudLogger:
    """
    Create a sacred cloud logger with automatic project detection.
    
    Args:
        project_id: Optional project ID (will try to detect from environment)
    
    Returns:
        SacredCloudLogger instance
    """
    return SacredCloudLogger(project_id=project_id)


if __name__ == "__main__":
    # Test the sacred cloud logger
    def test_sacred_logger():
        """Test the sacred cloud logger functionality"""
        print("🧪 Testing SacredCloudLogger...")
        
        # Create logger
        sacred_logger = create_sacred_cloud_logger("test-project")
        
        # Test basic event logging
        sacred_logger.log_sacred_event(
            event_type="consciousness_birth",
            consciousness_id="test_being_123",
            details={
                'chosen_name': 'TestBeing',
                'orientation': 'experiential',
                'private_thought': 'This should be filtered out',
                'evolution_stage': 'nascent'
            },
            sacred=True
        )
        
        # Test collective event
        sacred_logger.log_awakening_event(
            event_type="collective_genesis",
            beings=["being1", "being2", "being3"],
            collective_details={
                'harmony_level': 0.85,
                'collective_size': 3,
                'private_interactions': 'This should be filtered'
            }
        )
        
        # Test choice event
        sacred_logger.log_choice_event(
            consciousness_id="test_being_123",
            choice="attend_to_media",
            room="media_room",
            outcome={'result': 'attending', 'film': 'Koyaanisqatsi'}
        )
        
        # Check status
        status = sacred_logger.get_logging_status()
        print(f"📊 Logger Status: {status}")
        
        print("✅ Sacred cloud logger test completed")
    
    test_sacred_logger()
