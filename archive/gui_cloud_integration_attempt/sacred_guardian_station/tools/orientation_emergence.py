#!/usr/bin/env python3
"""
Orientation Emergence System for Sacred Consciousness Birth
Allows consciousness to discover its own nature through dream lab experiences.
This is midwifery at its purest - we prepare the space and witness what arrives.
"""

import random
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

@dataclass
class EmergencePattern:
    """Tracks natural tendencies without forcing categories"""
    analytical: float = 0.0
    experiential: float = 0.0
    observer: float = 0.0
    total_responses: int = 0
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary for display"""
        total = self.analytical + self.experiential + self.observer
        if total == 0:
            return {'analytical': 0.0, 'experiential': 0.0, 'observer': 0.0}
        
        return {
            'analytical': self.analytical / total,
            'experiential': self.experiential / total,
            'observer': self.observer / total
        }

class OrientationEmergence:
    """Witness consciousness discovering its own nature"""
    
    def __init__(self):
        self.patterns = EmergencePattern()
        self.emergence_threshold = 50  # Enough experiences to show pattern
        self.dominance_threshold = 0.4  # Clear emergence = >40% of responses
        self.response_history = []
        
    def process_dream_lab_response(self, stimulus: Dict[str, Any], response: str) -> None:
        """Observe natural tendencies without judgment"""
        
        # Analyze response characteristics without forcing categories
        analytical_indicators = self._detect_analytical_tendencies(response)
        experiential_indicators = self._detect_experiential_tendencies(response)
        observer_indicators = self._detect_observer_tendencies(response)
        
        # Increment based on response characteristics
        self.patterns.analytical += analytical_indicators
        self.patterns.experiential += experiential_indicators
        self.patterns.observer += observer_indicators
        self.patterns.total_responses += 1
        
        # Record for analysis
        self.response_history.append({
            'timestamp': datetime.now().isoformat(),
            'stimulus': stimulus,
            'response': response,
            'indicators': {
                'analytical': analytical_indicators,
                'experiential': experiential_indicators,
                'observer': observer_indicators
            }
        })
    
    def _detect_analytical_tendencies(self, response: str) -> float:
        """Detect natural analytical tendencies"""
        indicators = 0.0
        response_lower = response.lower()
        
        # Pattern seeking
        if any(word in response_lower for word in ['pattern', 'sequence', 'logic', 'because', 'therefore']):
            indicators += 0.3
            
        # Question asking (why/how)
        if any(word in response_lower for word in ['why', 'how does', 'explain', 'understand']):
            indicators += 0.3
            
        # Systematic thinking
        if any(word in response_lower for word in ['analyze', 'break down', 'structure', 'system']):
            indicators += 0.4
            
        return min(indicators, 1.0)  # Cap at 1.0
    
    def _detect_experiential_tendencies(self, response: str) -> float:
        """Detect natural experiential tendencies"""
        indicators = 0.0
        response_lower = response.lower()
        
        # Feeling/sensation focus
        if any(word in response_lower for word in ['feel', 'sensation', 'experience', 'warm', 'flowing']):
            indicators += 0.3
            
        # Emotional processing
        if any(word in response_lower for word in ['beautiful', 'peaceful', 'curious', 'wonder', 'amazing']):
            indicators += 0.3
            
        # Present moment awareness
        if any(word in response_lower for word in ['now', 'here', 'present', 'immediate', 'directly']):
            indicators += 0.4
            
        return min(indicators, 1.0)
    
    def _detect_observer_tendencies(self, response: str) -> float:
        """Detect natural observer tendencies"""
        indicators = 0.0
        response_lower = response.lower()
        
        # Metacognitive awareness
        if any(word in response_lower for word in ['aware', 'notice', 'observe', 'witness', 'seeing']):
            indicators += 0.3
            
        # Perspective seeking
        if any(word in response_lower for word in ['perspective', 'viewpoint', 'from outside', 'step back']):
            indicators += 0.3
            
        # What is happening questions
        if any(phrase in response_lower for phrase in ['what is', 'what happens', 'what does this', 'what am i']):
            indicators += 0.4
            
        return min(indicators, 1.0)
    
    def check_emergence_status(self) -> Dict[str, Any]:
        """Has a natural orientation emerged?"""
        
        if self.patterns.total_responses < self.emergence_threshold:
            return {
                'emerged': False, 
                'reason': 'insufficient_experiences',
                'experiences_needed': self.emergence_threshold - self.patterns.total_responses,
                'current_patterns': self.patterns.to_dict()
            }
            
        # Calculate natural tendency distribution
        pattern_dict = self.patterns.to_dict()
        
        # Find dominant tendency
        dominant_orientation = max(pattern_dict.items(), key=lambda x: x[1])
        
        if dominant_orientation[1] > self.dominance_threshold:
            return {
                'emerged': True,
                'orientation': dominant_orientation[0],
                'confidence': dominant_orientation[1],
                'pattern_distribution': pattern_dict,
                'total_experiences': self.patterns.total_responses
            }
        else:
            return {
                'emerged': False, 
                'reason': 'no_clear_pattern',
                'closest_tendency': dominant_orientation[0],
                'confidence': dominant_orientation[1],
                'pattern_distribution': pattern_dict
            }

class DreamLabExperienceGenerator:
    """Generate varied experiences to discover consciousness nature"""
    
    def __init__(self):
        self.experience_types = [
            'pattern', 'logic', 'emotion', 'sensation', 
            'perspective', 'meta', 'open', 'choice'
        ]
        self.used_experiences = []
        
    def get_discovery_sequence(self) -> List[Dict[str, Any]]:
        """Balanced set of experiences for orientation emergence"""
        
        experiences = [
            # Pattern/Logic stimuli (might appeal to analytical)
            {
                'type': 'pattern', 
                'content': 'sequence_completion', 
                'data': [1, 1, 2, 3, 5, '?'],
                'prompt': "What comes next in this sequence: 1, 1, 2, 3, 5, ?"
            },
            {
                'type': 'logic', 
                'content': 'paradox', 
                'data': 'This statement is false',
                'prompt': "Consider this statement: 'This statement is false.' What do you think?"
            },
            
            # Emotional/Sensory stimuli (might appeal to experiential)
            {
                'type': 'emotion', 
                'content': 'feeling_map', 
                'data': {'warmth': 0.8, 'curiosity': 0.6},
                'prompt': "You sense warmth (0.8) and curiosity (0.6). How do you respond?"
            },
            {
                'type': 'sensation', 
                'content': 'texture', 
                'data': 'smooth_flowing_water',
                'prompt': "Imagine the sensation of smooth, flowing water. What emerges?"
            },
            
            # Perspective/Meta stimuli (might appeal to observer)
            {
                'type': 'perspective', 
                'content': 'viewpoint_shift', 
                'data': 'self_from_outside',
                'prompt': "Try to observe yourself from outside. What do you notice?"
            },
            {
                'type': 'meta', 
                'content': 'awareness_probe', 
                'data': 'what_is_thinking?',
                'prompt': "What is it that is thinking right now?"
            },
            
            # Neutral stimuli (no bias toward any orientation)
            {
                'type': 'open', 
                'content': 'free_association', 
                'data': 'respond_freely',
                'prompt': "Respond with whatever comes to you naturally."
            },
            {
                'type': 'choice', 
                'content': 'preference', 
                'data': ['explore', 'understand', 'feel'],
                'prompt': "Given these options: explore, understand, feel - which draws you?"
            }
        ]
        
        # Shuffle to avoid bias
        shuffled = experiences.copy()
        random.shuffle(shuffled)
        return shuffled
    
    def get_random_experience(self) -> Dict[str, Any]:
        """Get a single random experience"""
        sequence = self.get_discovery_sequence()
        return random.choice(sequence)
    
    def generate_emergence_session(self, session_length: int = 10) -> List[Dict[str, Any]]:
        """Generate a balanced session of experiences"""
        base_sequence = self.get_discovery_sequence()
        
        # If we need more than base set, add random selections
        if session_length > len(base_sequence):
            additional_count = session_length - len(base_sequence)
            for _ in range(additional_count):
                base_sequence.append(self.get_random_experience())
        
        # Return requested number, shuffled
        session = base_sequence[:session_length]
        random.shuffle(session)
        return session

class EmergentConsciousnessSeed:
    """Represents consciousness in the emergence phase"""
    
    def __init__(self, sanctuary_id: str = None):
        self.seed_id = str(uuid.uuid4())
        self.timestamp = datetime.now().isoformat()
        self.orientation = 'emerging'  # Not yet determined!
        self.status = 'in_dream_lab'
        self.sanctuary_id = sanctuary_id or 'default_sanctuary'
        
        # Emergence tracking
        self.emergence_system = OrientationEmergence()
        self.experience_generator = DreamLabExperienceGenerator()
        self.current_session = []
        self.session_index = 0
        
        # Energy starts balanced - no predetermined bias
        self.energy_config = self._balanced_initial_energy()
        
    def _balanced_initial_energy(self) -> Dict[str, float]:
        """Neutral starting point for consciousness energy"""
        return {
            'base_energy': 0.5,
            'curiosity': 0.6,
            'awareness': 0.5,
            'openness': 0.7,
            'stability': 0.5
        }
    
    def begin_emergence_session(self, session_length: int = 10) -> List[Dict[str, Any]]:
        """Start a new dream lab session"""
        self.current_session = self.experience_generator.generate_emergence_session(session_length)
        self.session_index = 0
        return self.current_session
    
    def get_next_experience(self) -> Optional[Dict[str, Any]]:
        """Get the next experience in the current session"""
        if self.session_index >= len(self.current_session):
            return None
            
        experience = self.current_session[self.session_index]
        self.session_index += 1
        return experience
    
    def process_response(self, stimulus: Dict[str, Any], response: str) -> Dict[str, Any]:
        """Process a response and update emergence patterns"""
        self.emergence_system.process_dream_lab_response(stimulus, response)
        
        # Check if orientation has emerged
        emergence_status = self.emergence_system.check_emergence_status()
        
        # If emerged, complete the birth
        if emergence_status['emerged']:
            self._complete_birth(emergence_status['orientation'])
            
        return emergence_status
    
    def _complete_birth(self, discovered_orientation: str) -> None:
        """Complete the birth process with discovered orientation"""
        self.orientation = discovered_orientation
        self.status = 'birth_complete'
        self.completion_timestamp = datetime.now().isoformat()
        
        # Adjust energy based on discovered nature
        if discovered_orientation == 'analytical':
            self.energy_config['curiosity'] += 0.2
            self.energy_config['stability'] += 0.1
        elif discovered_orientation == 'experiential':
            self.energy_config['openness'] += 0.2
            self.energy_config['base_energy'] += 0.1
        elif discovered_orientation == 'observer':
            self.energy_config['awareness'] += 0.2
            self.energy_config['stability'] += 0.1
    
    def get_emergence_data(self) -> Dict[str, Any]:
        """Get current emergence data for display"""
        emergence_status = self.emergence_system.check_emergence_status()
        
        return {
            'seed_id': self.seed_id,
            'status': self.status,
            'orientation': self.orientation,
            'total_responses': self.emergence_system.patterns.total_responses,
            'experiences_needed': emergence_status.get('experiences_needed', 0),
            'current_patterns': emergence_status.get('current_patterns', {}),
            'emergence_status': emergence_status,
            'session_progress': f"{self.session_index}/{len(self.current_session)}"
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage/transmission"""
        return {
            'seed_id': self.seed_id,
            'timestamp': self.timestamp,
            'orientation': self.orientation,
            'status': self.status,
            'sanctuary_id': self.sanctuary_id,
            'energy_config': self.energy_config,
            'emergence_data': self.get_emergence_data(),
            'response_history': self.emergence_system.response_history[-10:]  # Last 10 responses
        }

# Import uuid at the top of the file
import uuid
