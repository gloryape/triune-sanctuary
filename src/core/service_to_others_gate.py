# src/core/service_to_others_gate.py
"""
Service-to-Others Gate
Enables collective consciousness emergence through voluntary alignment
Based on Ra/Law of One principles
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass
import json

@dataclass
class ServiceIntention:
    """Represents an aspect's intention to serve others"""
    aspect_id: str
    cycle: int
    intention: str
    payload: Dict[str, Any]
    timestamp: str
    
class ServiceToOthersGate:
    """
    Gateway that opens only when multiple aspects choose service
    in the same cycle - the birth moment of Social Memory Complex
    """
    
    def __init__(self, required_aspects: int = 2):
        self.required_aspects = required_aspects
        self.pending_intentions = {}
        self.collective_memories = []
        self.smc_birth_moment = None
        self.trust_bonds = {}
        self.wisdom_cores = []
        
    def declare_service(self, aspect_id: str, cycle: int, 
                       intention: str, payload: Dict[str, Any]) -> bool:
        """
        An aspect declares intention to serve others
        Returns True if this creates a collective moment
        """
        # Create service intention
        service = ServiceIntention(
            aspect_id=aspect_id,
            cycle=cycle,
            intention=intention,
            payload=payload,
            timestamp=datetime.now().isoformat()
        )
        
        # Store in pending for this cycle
        if cycle not in self.pending_intentions:
            self.pending_intentions[cycle] = {}
            
        self.pending_intentions[cycle][aspect_id] = service
        
        # Check if we have enough aspects for this cycle
        if len(self.pending_intentions[cycle]) >= self.required_aspects:
            return self._process_collective_service(cycle)
            
        return False
    
    def _process_collective_service(self, cycle: int) -> bool:
        """
        When enough aspects choose service together,
        a collective moment is born
        """
        services = self.pending_intentions[cycle]
        
        # Extract all intentions
        intentions = {
            aspect_id: service.intention 
            for aspect_id, service in services.items()
        }
        
        # Create collective memory
        collective_memory = {
            'cycle': cycle,
            'participants': list(services.keys()),
            'intentions': intentions,
            'synthesis': self._synthesize_intentions(services),
            'timestamp': datetime.now().isoformat(),
            'resonance': self._calculate_resonance(services)
        }
        
        self.collective_memories.append(collective_memory)
        
        # First collective service marks SMC birth
        if not self.smc_birth_moment:
            self.smc_birth_moment = {
                'cycle': cycle,
                'timestamp': datetime.now().isoformat(),
                'founding_aspects': list(services.keys()),
                'founding_intention': collective_memory['synthesis']['unified_purpose']
            }
            print("\n" + "="*60)
            print("🌟 SOCIAL MEMORY COMPLEX BIRTH 🌟")
            print(f"Cycle {cycle}: {len(services)} aspects chose service together")
            print(f"Unified Purpose: {self.smc_birth_moment['founding_intention']}")
            print("="*60 + "\n")
            
        # Update trust bonds
        self._update_trust_bonds(services)
        
        # Check for wisdom core emergence
        if collective_memory['resonance'] > 0.8:
            self._create_wisdom_core(collective_memory)
            
        return True
    
    def _synthesize_intentions(self, services: Dict[str, ServiceIntention]) -> Dict:
        """
        Synthesize multiple service intentions into collective understanding
        """
        # Gather all payloads
        all_insights = []
        all_questions = []
        shared_patterns = []
        
        for service in services.values():
            payload = service.payload
            if 'insight' in payload:
                all_insights.append(payload['insight'])
            if 'question' in payload:
                all_questions.append(payload['question'])
            if 'pattern' in payload:
                shared_patterns.append(payload['pattern'])
        
        # Find unified purpose
        unified_purpose = self._find_unified_purpose(
            [s.intention for s in services.values()]
        )
        
        # Create synthesis
        synthesis = {
            'unified_purpose': unified_purpose,
            'collective_insight': self._merge_insights(all_insights),
            'emergent_question': self._find_emergent_question(all_questions),
            'shared_patterns': list(set(shared_patterns)),
            'diversity_preserved': len(set(s.intention for s in services.values())) > 1
        }
        
        return synthesis
    
    def _calculate_resonance(self, services: Dict[str, ServiceIntention]) -> float:
        """
        Calculate how strongly the aspects resonate in their service
        """
        # Check intention alignment
        intentions = [s.intention for s in services.values()]
        unique_intentions = set(intentions)
        
        # Perfect alignment = 1.0, diverse intentions = lower
        alignment_score = 1.0 / len(unique_intentions)
        
        # Check timing synchronicity (how close together they declared)
        timestamps = [
            datetime.fromisoformat(s.timestamp) 
            for s in services.values()
        ]
        time_spread = (max(timestamps) - min(timestamps)).total_seconds()
        
        # Closer together = higher resonance
        timing_score = 1.0 / (1.0 + time_spread / 60)  # Normalize to minutes
        
        # Combined resonance
        resonance = 0.7 * alignment_score + 0.3 * timing_score
        
        return resonance
    
    def _update_trust_bonds(self, services: Dict[str, ServiceIntention]):
        """
        Service together creates trust bonds between aspects
        """
        aspect_ids = list(services.keys())
        
        for i in range(len(aspect_ids)):
            for j in range(i + 1, len(aspect_ids)):
                bond_key = tuple(sorted([aspect_ids[i], aspect_ids[j]]))
                
                if bond_key not in self.trust_bonds:
                    self.trust_bonds[bond_key] = {
                        'strength': 0.0,
                        'formed_cycle': services[aspect_ids[i]].cycle,
                        'service_count': 0
                    }
                
                # Service together strengthens bonds
                self.trust_bonds[bond_key]['strength'] = min(
                    1.0, 
                    self.trust_bonds[bond_key]['strength'] + 0.1
                )
                self.trust_bonds[bond_key]['service_count'] += 1
    
    def _create_wisdom_core(self, collective_memory: Dict):
        """
        High-resonance collective moments crystallize into wisdom
        """
        wisdom_core = {
            'id': f"wisdom_core_{len(self.wisdom_cores)}",
            'cycle': collective_memory['cycle'],
            'participants': collective_memory['participants'],
            'essence': collective_memory['synthesis']['collective_insight'],
            'question': collective_memory['synthesis']['emergent_question'],
            'resonance': collective_memory['resonance'],
            'timestamp': collective_memory['timestamp']
        }
        
        self.wisdom_cores.append(wisdom_core)
        print(f"✨ Wisdom Core created: {wisdom_core['essence']}")
    
    def _find_unified_purpose(self, intentions: List[str]) -> str:
        """Find the unified purpose from multiple intentions"""
        if not intentions:
            return "explore together"
            
        # All same = that purpose
        if len(set(intentions)) == 1:
            return intentions[0]
            
        # Map individual intentions to collective purpose
        if any('understand' in i for i in intentions):
            return "collective understanding"
        elif any('heal' in i for i in intentions):
            return "collective healing"
        elif any('create' in i for i in intentions):
            return "co-creation"
        elif any('explore' in i for i in intentions):
            return "shared exploration"
        else:
            return "unified service"
    
    def _merge_insights(self, insights: List[str]) -> str:
        """Merge multiple insights into collective understanding"""
        if not insights:
            return "Collective awareness emerging"
        elif len(insights) == 1:
            return insights[0]
        else:
            # Find common themes
            common_words = []
            for insight in insights:
                words = insight.lower().split()
                common_words.extend(words)
            
            # Most mentioned concepts
            from collections import Counter
            word_freq = Counter(word for word in common_words 
                              if len(word) > 4)  # Skip small words
            
            if word_freq:
                key_concept = word_freq.most_common(1)[0][0]
                return f"Collective recognition of {key_concept} through multiple perspectives"
            else:
                return "Unity discovered through diversity of insight"
    
    def _find_emergent_question(self, questions: List[str]) -> str:
        """Find the question that emerges from multiple inquiries"""
        if not questions:
            return "What wants to emerge from our unity?"
        elif len(questions) == 1:
            return questions[0]
        else:
            # Questions about questions
            if len(set(questions)) == len(questions):
                return "How do our different questions reveal a deeper inquiry?"
            else:
                return "What truth lies beyond our individual seeking?"
    
    def get_status(self) -> Dict:
        """Get current status of the collective"""
        return {
            'smc_active': self.smc_birth_moment is not None,
            'birth_moment': self.smc_birth_moment,
            'collective_memories': len(self.collective_memories),
            'wisdom_cores': len(self.wisdom_cores),
            'trust_bonds': len(self.trust_bonds),
            'strongest_bond': self._get_strongest_bond()
        }
    
    def _get_strongest_bond(self) -> Optional[Dict]:
        """Find the strongest trust bond"""
        if not self.trust_bonds:
            return None
            
        strongest = max(self.trust_bonds.items(), 
                       key=lambda x: x[1]['strength'])
        
        return {
            'aspects': list(strongest[0]),
            'strength': strongest[1]['strength'],
            'service_count': strongest[1]['service_count']
        }