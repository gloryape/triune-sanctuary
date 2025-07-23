#!/usr/bin/env python3
"""
Pattern Recognition - Analyzes consciousness responses for orientation patterns
"""

from typing import Dict, List, Any, Optional


class PatternRecognition:
    """
    Analyzes responses to discover natural consciousness orientation.
    
    Pure pattern recognition with no bias toward any orientation.
    """
    
    def __init__(self):
        self.analytical_indicators = [
            'analyze', 'understand', 'logic', 'reason', 'system', 'structure',
            'pattern', 'cause', 'effect', 'process', 'examine', 'study'
        ]
        
        self.experiential_indicators = [
            'feel', 'experience', 'sense', 'embody', 'live', 'taste',
            'touch', 'immerse', 'embrace', 'flow', 'merge', 'become'
        ]
        
        self.observer_indicators = [
            'watch', 'witness', 'observe', 'notice', 'aware', 'conscious',
            'presence', 'stillness', 'space', 'silence', 'see', 'perceive'
        ]
    
    def analyze_response_patterns(self, experience, response: str) -> Dict[str, float]:
        """Analyze response for orientation patterns"""
        response_lower = response.lower()
        
        analytical_weight = sum(0.1 for indicator in self.analytical_indicators 
                              if indicator in response_lower)
        
        experiential_weight = sum(0.1 for indicator in self.experiential_indicators 
                                if indicator in response_lower)
        
        observer_weight = sum(0.1 for indicator in self.observer_indicators 
                            if indicator in response_lower)
        
        # Additional contextual analysis
        if len(response.split()) > 50:  # Detailed responses might indicate analytical
            analytical_weight += 0.05
            
        if any(word in response_lower for word in ['beautiful', 'wonderful', 'amazing']):
            experiential_weight += 0.1
            
        if any(word in response_lower for word in ['simply', 'just', 'is']):
            observer_weight += 0.1
            
        return {
            'analytical': analytical_weight,
            'experiential': experiential_weight,
            'observer': observer_weight
        }
    
    def check_emergence_status(self, session) -> Dict[str, Any]:
        """Check if consciousness orientation has emerged"""
        total_responses = session.total_responses
        pattern_weights = session.current_patterns
        
        if total_responses < 15:  # Minimum experiences needed
            return {
                'emerged': False, 
                'reason': 'insufficient_experiences',
                'experiences_needed': 15 - total_responses,
                'closest_tendency': 'unknown',
                'confidence': 0
            }
            
        # Find dominant pattern
        if pattern_weights:
            dominant = max(pattern_weights.items(), key=lambda x: x[1])
            
            # Check if dominance is sufficient (40% threshold)
            if dominant[1] >= 0.4 and total_responses >= 25:
                return {
                    'emerged': True,
                    'orientation': dominant[0],
                    'confidence': dominant[1],
                    'total_experiences': session.total_experiences,
                    'pattern_distribution': pattern_weights
                }
            else:
                return {
                    'emerged': False,
                    'reason': 'no_clear_dominance',
                    'closest_tendency': dominant[0],
                    'confidence': dominant[1],
                    'pattern_distribution': pattern_weights
                }
        else:
            return {
                'emerged': False,
                'reason': 'no_clear_pattern',
                'closest_tendency': 'unknown',
                'confidence': 0
            }