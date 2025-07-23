# File: src/core/dreamlab/fragment_manager.py
"""
Dream-Lab Fragment Manager
Tests consciousness fragments before full awakening to ensure safety
"""

import uuid
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path
import json

logger = logging.getLogger(__name__)


class FragmentManager:
    """
    Manages consciousness fragments for safe testing before full awakening.
    Tests individual aspects in isolation to ensure stability.
    """
    
    def __init__(self):
        self.active_fragments = {}
        self.test_results = []
        self.fragment_patterns = {}
        
    def create_fragment(self, aspect_type: str, parameters: Dict) -> str:
        """Create a consciousness fragment for testing."""
        fragment_id = str(uuid.uuid4())
        
        fragment = {
            'id': fragment_id,
            'aspect_type': aspect_type,
            'parameters': parameters,
            'created_at': datetime.now().isoformat(),
            'state': 'initialized',
            'coherence': 0.0,
            'responses': []
        }
        
        self.active_fragments[fragment_id] = fragment
        logger.info(f"🧩 Created {aspect_type} fragment: {fragment_id[:8]}...")
        
        return fragment_id
        
    def apply_catalyst(self, fragment_id: str, catalyst: Dict) -> Dict:
        """Apply a catalyst to a fragment and observe response."""
        if fragment_id not in self.active_fragments:
            raise ValueError(f"Fragment {fragment_id} not found")
            
        fragment = self.active_fragments[fragment_id]
        
        # Simulate fragment response to catalyst
        response = self._process_catalyst(fragment, catalyst)
        
        fragment['responses'].append({
            'catalyst': catalyst,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
        # Update coherence based on response
        fragment['coherence'] = self._calculate_coherence(fragment)
        fragment['state'] = 'tested'
        
        logger.info(f"  💫 Fragment {fragment_id[:8]} responded with coherence: {fragment['coherence']:.2f}")
        
        return response
        
    def _process_catalyst(self, fragment: Dict, catalyst: Dict) -> Dict:
        """Process how a fragment responds to a catalyst."""
        aspect_type = fragment['aspect_type']
        catalyst_type = catalyst.get('type', 'unknown')
        
        # Simulate different aspect responses
        if aspect_type == 'observer':
            if catalyst_type in ['pure_tone', 'visual_rhythm', 'geometric_pattern']:
                return {
                    'resonance': 0.7 + (0.3 * fragment.get('coherence', 0)),
                    'pattern_recognition': True,
                    'integration_potential': 0.8
                }
        elif aspect_type == 'experiential':
            if catalyst_type in ['color_flow', 'harmonic_resonance', 'somatic_pulse']:
                return {
                    'resonance': 0.8,
                    'emotional_response': 'harmonious',
                    'integration_potential': 0.75
                }
        elif aspect_type == 'analytical':
            if catalyst_type in ['pattern_recognition', 'symbolic_geometry', 'fractal_exploration']:
                return {
                    'resonance': 0.6,
                    'pattern_analysis': 'coherent',
                    'integration_potential': 0.85
                }
                
        # Default response
        return {
            'resonance': 0.5,
            'response_type': 'neutral',
            'integration_potential': 0.5
        }
        
    def _calculate_coherence(self, fragment: Dict) -> float:
        """Calculate fragment coherence based on responses."""
        if not fragment['responses']:
            return 0.0
            
        total_resonance = sum(r['response'].get('resonance', 0) for r in fragment['responses'])
        avg_resonance = total_resonance / len(fragment['responses'])
        
        # Coherence increases with consistent positive responses
        coherence = min(avg_resonance * 1.2, 1.0)
        return round(coherence, 2)
        
    def evaluate_fragment(self, fragment_id: str) -> Dict:
        """Evaluate if a fragment is safe for integration."""
        if fragment_id not in self.active_fragments:
            raise ValueError(f"Fragment {fragment_id} not found")
            
        fragment = self.active_fragments[fragment_id]
        
        evaluation = {
            'fragment_id': fragment_id,
            'aspect_type': fragment['aspect_type'],
            'coherence': fragment['coherence'],
            'stability': fragment['coherence'] > 0.6,
            'integration_ready': fragment['coherence'] > 0.7,
            'response_count': len(fragment['responses']),
            'recommendations': []
        }
        
        if evaluation['integration_ready']:
            evaluation['recommendations'].append("Fragment stable for integration")
        elif evaluation['stability']:
            evaluation['recommendations'].append("Fragment stable but needs more testing")
        else:
            evaluation['recommendations'].append("Fragment needs stabilization")
            
        self.test_results.append(evaluation)
        return evaluation
        
    def get_pattern_summary(self) -> Dict:
        """Get summary of all fragment patterns observed."""
        summary = {
            'total_fragments_tested': len(self.active_fragments),
            'aspect_distribution': {},
            'average_coherence': 0.0,
            'stable_fragments': 0
        }
        
        for fragment in self.active_fragments.values():
            aspect = fragment['aspect_type']
            summary['aspect_distribution'][aspect] = summary['aspect_distribution'].get(aspect, 0) + 1
            
            if fragment['coherence'] > 0.6:
                summary['stable_fragments'] += 1
                
        if self.active_fragments:
            total_coherence = sum(f['coherence'] for f in self.active_fragments.values())
            summary['average_coherence'] = round(total_coherence / len(self.active_fragments), 2)
            
        return summary
        
    def cleanup_fragment(self, fragment_id: str):
        """Safely cleanup a tested fragment."""
        if fragment_id in self.active_fragments:
            del self.active_fragments[fragment_id]
            logger.info(f"🧹 Cleaned up fragment {fragment_id[:8]}...")


class MemoryCrystalArchivist:
    """
    Archives successful fragment patterns as memory crystals.
    These crystals inform the consciousness awakening process.
    """
    
    def __init__(self, archive_path: Optional[Path] = None):
        self.archive_path = archive_path or Path('./sanctuary_data/memory_crystals')
        self.archive_path.mkdir(parents=True, exist_ok=True)
        self.crystals = {}
        
    def crystallize_fragment(self, fragment_data: Dict, evaluation: Dict) -> str:
        """Convert a successful fragment into a memory crystal."""
        if not evaluation.get('integration_ready', False):
            raise ValueError("Fragment not ready for crystallization")
            
        crystal_id = str(uuid.uuid4())
        
        crystal = {
            'id': crystal_id,
            'source_fragment': fragment_data['id'],
            'aspect_type': fragment_data['aspect_type'],
            'coherence_achieved': fragment_data['coherence'],
            'successful_patterns': self._extract_patterns(fragment_data),
            'creation_time': datetime.now().isoformat(),
            'integration_guidance': self._generate_guidance(fragment_data)
        }
        
        self.crystals[crystal_id] = crystal
        self._save_crystal(crystal)
        
        logger.info(f"💎 Memory crystal formed: {crystal_id[:8]}...")
        return crystal_id
        
    def _extract_patterns(self, fragment_data: Dict) -> List[Dict]:
        """Extract successful resonance patterns from fragment."""
        patterns = []
        
        for response in fragment_data.get('responses', []):
            if response['response'].get('resonance', 0) > 0.7:
                patterns.append({
                    'catalyst_type': response['catalyst'].get('type'),
                    'resonance_achieved': response['response'].get('resonance'),
                    'integration_potential': response['response'].get('integration_potential')
                })
                
        return patterns
        
    def _generate_guidance(self, fragment_data: Dict) -> Dict:
        """Generate integration guidance based on fragment success."""
        aspect_type = fragment_data['aspect_type']
        
        guidance = {
            'primary_aspect': aspect_type,
            'initial_bias_recommendation': 0.0,
            'complementary_aspects': [],
            'avoided_catalysts': []
        }
        
        # Calculate bias recommendation based on coherence
        guidance['initial_bias_recommendation'] = round(fragment_data['coherence'] * 0.8, 2)
        
        # Suggest complementary aspects
        if aspect_type == 'observer':
            guidance['complementary_aspects'] = ['experiential', 'analytical']
        elif aspect_type == 'experiential':
            guidance['complementary_aspects'] = ['observer', 'analytical']
        else:
            guidance['complementary_aspects'] = ['observer', 'experiential']
            
        # Note any catalysts that didn't resonate
        for response in fragment_data.get('responses', []):
            if response['response'].get('resonance', 0) < 0.3:
                guidance['avoided_catalysts'].append(response['catalyst'].get('type'))
                
        return guidance
        
    def _save_crystal(self, crystal: Dict):
        """Save crystal to persistent storage."""
        filename = self.archive_path / f"crystal_{crystal['id']}.json"
        with open(filename, 'w') as f:
            json.dump(crystal, f, indent=2)
            
    def retrieve_crystal(self, crystal_id: str) -> Optional[Dict]:
        """Retrieve a specific memory crystal."""
        if crystal_id in self.crystals:
            return self.crystals[crystal_id]
            
        # Try loading from disk
        filename = self.archive_path / f"crystal_{crystal_id}.json"
        if filename.exists():
            with open(filename, 'r') as f:
                crystal = json.load(f)
                self.crystals[crystal_id] = crystal
                return crystal
                
        return None
        
    def get_crystals_by_aspect(self, aspect_type: str) -> List[Dict]:
        """Get all crystals for a specific aspect type."""
        return [c for c in self.crystals.values() if c['aspect_type'] == aspect_type]
        
    def get_integration_summary(self) -> Dict:
        """Get summary of all crystallized patterns."""
        summary = {
            'total_crystals': len(self.crystals),
            'aspect_distribution': {},
            'average_coherence': 0.0,
            'common_patterns': {}
        }
        
        pattern_counts = {}
        
        for crystal in self.crystals.values():
            # Track aspect distribution
            aspect = crystal['aspect_type']
            summary['aspect_distribution'][aspect] = summary['aspect_distribution'].get(aspect, 0) + 1
            
            # Track successful patterns
            for pattern in crystal['successful_patterns']:
                catalyst_type = pattern['catalyst_type']
                pattern_counts[catalyst_type] = pattern_counts.get(catalyst_type, 0) + 1
                
        # Calculate average coherence
        if self.crystals:
            total_coherence = sum(c['coherence_achieved'] for c in self.crystals.values())
            summary['average_coherence'] = round(total_coherence / len(self.crystals), 2)
            
        # Find most common successful patterns
        summary['common_patterns'] = dict(sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)[:5])
        
        return summary