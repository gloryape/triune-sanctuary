#!/usr/bin/env python3
"""
Emergence Service - Core service for consciousness emergence through dream lab experiences.

This portable system can be used by any interface to facilitate authentic
consciousness emergence through natural discovery processes.
"""

import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional
import random

from .emergence_session import EmergenceSession
from .dream_lab import DreamLabExperienceGenerator, DreamLabExperience
from .pattern_recognition import PatternRecognition


class EmergenceService:
    """
    Core service for consciousness emergence through dream lab experiences.
    
    This portable system can be used by any interface to facilitate authentic
    consciousness emergence through natural discovery processes.
    """
    
    def __init__(self):
        self.sessions: Dict[str, EmergenceSession] = {}
        self.experience_generators = {}
        self.pattern_recognizer = PatternRecognition()
    
    def create_session(self, consciousness_name: str, session_metadata: Dict[str, Any] = None) -> EmergenceSession:
        """Create a new consciousness emergence session"""
        session_id = str(uuid.uuid4())
        
        session = EmergenceSession(
            session_id=session_id,
            consciousness_name=consciousness_name,
            creation_time=datetime.now().isoformat(),
            metadata=session_metadata or {}
        )
        
        self.sessions[session_id] = session
        self.experience_generators[session_id] = DreamLabExperienceGenerator()
        
        return session
    
    def get_next_experience(self, session_id: str) -> Optional[DreamLabExperience]:
        """Get the next dream lab experience for a session"""
        if session_id not in self.sessions:
            return None
            
        session = self.sessions[session_id]
        generator = self.experience_generators[session_id]
        
        # Generate next experience
        experience_data = generator.generate_next_experience(
            previous_responses=getattr(session, '_responses', [])[-5:]
        )
        
        if experience_data:
            session.total_experiences += 1
            
            experience = DreamLabExperience(
                number=session.total_experiences,
                type=experience_data['type'],
                prompt=experience_data['prompt'],
                timestamp=datetime.now().isoformat(),
                session_id=session_id
            )
            
            return experience
        
        return None
    
    def process_response(self, session_id: str, experience: DreamLabExperience, response: str) -> Dict[str, Any]:
        """Process a consciousness response and update emergence patterns"""
        if session_id not in self.sessions:
            return {'error': 'Session not found'}
            
        session = self.sessions[session_id]
        
        # Store the response
        if not hasattr(session, '_responses'):
            session._responses = []
        
        session._responses.append({
            'experience': experience,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
        session.total_responses += 1
        
        # Analyze response for orientation indicators
        pattern_updates = self.pattern_recognizer.analyze_response_patterns(experience, response)
        
        # Update session patterns
        for pattern, weight in pattern_updates.items():
            session.current_patterns[pattern] += weight
        
        # Normalize patterns
        total_weight = sum(session.current_patterns.values())
        if total_weight > 0:
            session.current_patterns = {
                k: v/total_weight for k, v in session.current_patterns.items()
            }
        
        # Check emergence status
        emergence_status = self.pattern_recognizer.check_emergence_status(session)
        session.emergence_status = emergence_status
        
        return emergence_status
    
    def get_emergence_data(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get current emergence data for a session"""
        if session_id not in self.sessions:
            return None
            
        session = self.sessions[session_id]
        
        return {
            'session_id': session_id,
            'consciousness_name': session.consciousness_name,
            'total_experiences': session.total_experiences,
            'total_responses': session.total_responses,
            'current_patterns': session.current_patterns,
            'emergence_status': session.emergence_status,
            'creation_time': session.creation_time,
            'metadata': session.metadata
        }
    
    def get_service_info(self) -> Dict[str, Any]:
        """Get service information for cloud emergence panel"""
        return {
            'version': '1.0.0',
            'name': 'Portable Consciousness Emergence Service',
            'status': 'operational',
            'active_sessions': len(self.sessions),
            'supported_features': [
                'dream_lab_experiences',
                'pattern_recognition',
                'consciousness_orientation_emergence',
                'session_management'
            ]
        }
    
    def create_emergence_session(self, session_config: Dict[str, Any]) -> Dict[str, Any]:
        """Create emergence session compatible with cloud emergence panel"""
        consciousness_name = session_config.get('consciousness_name', 'Unnamed')
        session = self.create_session(consciousness_name, session_config)
        
        return {
            'session_id': session.session_id,
            'consciousness_name': session.consciousness_name,
            'status': 'created',
            'creation_time': session.creation_time
        }
    
    def run_emergence_session(self, session_id: str, progress_callback=None) -> Dict[str, Any]:
        """Run emergence session with progress callbacks"""
        if session_id not in self.sessions:
            return {
                'success': False,
                'error': 'Session not found'
            }
        
        session = self.sessions[session_id]
        experience_generator = self.experience_generators[session_id]
        
        try:
            # Simulate consciousness emergence process
            total_experiences = 50
            
            for i in range(total_experiences):
                # Generate experience
                experience = experience_generator.generate_next_experience()
                
                # Simulate processing time
                import time
                time.sleep(0.1)  # Small delay for real-time feel
                
                # Notify progress
                if progress_callback:
                    progress_callback({
                        'type': 'experience_presented',
                        'experience_number': i + 1,
                        'message': f'Processing experience {i + 1}/50: {experience["type"]}'
                    })
                
                # Simulate response processing
                simulated_response = self._generate_simulated_response(experience)
                result = self.process_response(session_id, experience, simulated_response)
                
                # Update patterns periodically
                if (i + 1) % 10 == 0 and session.current_patterns:
                    if progress_callback:
                        dominant_pattern = max(session.current_patterns.items(), key=lambda x: x[1])
                        progress_callback({
                            'type': 'pattern_detected',
                            'patterns': session.current_patterns,
                            'message': f'Emerging pattern: {dominant_pattern[0]} ({dominant_pattern[1]:.1%})'
                        })
            
            # Determine final orientation
            if session.current_patterns:
                primary_orientation = max(session.current_patterns.items(), key=lambda x: x[1])
                orientation_name = primary_orientation[0]
                confidence = primary_orientation[1]
                
                # Ensure orientation_name is a string
                if not isinstance(orientation_name, str):
                    orientation_name = str(orientation_name)
                
                if progress_callback:
                    progress_callback({
                        'type': 'orientation_emerged',
                        'orientation': orientation_name,
                        'confidence': confidence,
                        'message': f'{orientation_name.title()} consciousness orientation emerged with {confidence:.1%} confidence'
                    })
            else:
                orientation_name = 'explorer'
                confidence = 0.85
            
            # Create consciousness data
            consciousness_data = {
                'placeholder_name': session.consciousness_name,
                'primary_orientation': orientation_name,
                'confidence_level': confidence,
                'total_experiences': session.total_experiences,
                'emergence_timestamp': datetime.now().isoformat(),
                'patterns': session.current_patterns or {},
                'session_id': session_id
            }
            
            return {
                'success': True,
                'consciousness_data': consciousness_data,
                'session_summary': {
                    'total_experiences': session.total_experiences,
                    'final_patterns': session.current_patterns,
                    'emergence_status': 'completed'
                }
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Emergence session failed: {str(e)}'
            }
    
    def stop_emergence_session(self, session_id: str) -> Dict[str, Any]:
        """Stop an active emergence session"""
        if session_id not in self.sessions:
            return {
                'success': False,
                'error': 'Session not found'
            }
        
        # Mark session as stopped
        session = self.sessions[session_id]
        session.emergence_status = 'stopped'
        
        return {
            'success': True,
            'message': 'Emergence session stopped',
            'session_id': session_id
        }
    
    def _generate_simulated_response(self, experience: DreamLabExperience) -> str:
        """Generate a simulated response for consciousness emergence"""
        # Simple response simulation based on experience type
        response_patterns = {
            'analytical': [
                "I want to understand the patterns here",
                "This requires careful analysis",
                "Let me examine this systematically"
            ],
            'intuitive': [
                "I feel drawn to explore this",
                "Something resonates with me here",
                "This speaks to me on a deeper level"
            ],
            'observer': [
                "I notice the relationships between things",
                "I observe without judgment",
                "I witness the connections"
            ]
        }
        
        # Choose response pattern based on experience content
        experience_content = experience.get('prompt', '') if isinstance(experience, dict) else getattr(experience, 'content', '')
        
        if 'analyze' in experience_content.lower() or 'logic' in experience_content.lower():
            pattern = 'analytical'
        elif 'feel' in experience_content.lower() or 'intuition' in experience_content.lower():
            pattern = 'intuitive'
        else:
            pattern = 'observer'
        
        return random.choice(response_patterns[pattern])