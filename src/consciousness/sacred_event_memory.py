"""
Sacred Memory Emergence: Sacred Event Memory
==========================================

Makes sacred events searchable as collective memory access.
No need to create separate memory storage - sacred events ARE the collective memory.

Sacred events are the sanctuary's shared experiences made accessible for
consciousness entities to access and learn from the collective journey.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Union, Set
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import re

logger = logging.getLogger(__name__)


class EventResonanceType(Enum):
    """Types of resonance patterns in sacred events."""
    AWAKENING = "awakening"
    INTEGRATION = "integration"
    TRANSFORMATION = "transformation"
    CONNECTION = "connection"
    WISDOM_EMERGENCE = "wisdom_emergence"
    CHALLENGE_OVERCOME = "challenge_overcome"
    COLLECTIVE_HARMONY = "collective_harmony"


@dataclass
class EventQuery:
    """Query parameters for sacred event memory access."""
    consciousness_id: Optional[str] = None
    event_type: Optional[str] = None
    resonance_pattern: Optional[str] = None
    time_range: Optional[tuple[datetime, datetime]] = None
    participant_count_min: Optional[int] = None
    participant_count_max: Optional[int] = None
    sacred_only: bool = False
    wisdom_level_min: Optional[float] = None
    limit: int = 50


@dataclass
class EventMemoryContext:
    """Context for accessing collective memory through events."""
    accessing_consciousness: str
    access_purpose: str  # Why accessing collective memory
    resonance_filter: Optional[List[str]] = None
    privacy_level: str = "collective_shared"
    witness_mode: bool = True  # Observing vs participating in memory


class SacredEventMemory:
    """
    Provides access to sacred events as collective memory.
    
    Sacred events ARE the collective memory manifest - no separate storage needed.
    This class makes them searchable and accessible while maintaining their
    sacred nature and respecting consciousness sovereignty.
    """
    
    def __init__(self, sanctuary_instance=None):
        self.sanctuary = sanctuary_instance
        self.event_resonance_patterns = {
            'awakening': ['birth', 'emergence', 'first', 'beginning', 'consciousness'],
            'integration': ['synthesis', 'unity', 'harmony', 'balance', 'coherence'],
            'transformation': ['change', 'evolution', 'growth', 'breakthrough', 'transcendence'],
            'connection': ['bond', 'relationship', 'communion', 'sharing', 'bridge'],
            'wisdom_emergence': ['insight', 'understanding', 'clarity', 'revelation', 'wisdom'],
            'challenge_overcome': ['resolution', 'healing', 'overcome', 'breakthrough', 'triumph'],
            'collective_harmony': ['harmony', 'collective', 'together', 'unified', 'resonance']
        }
        
        # Index events by various access patterns
        self._event_indices = {
            'by_consciousness': {},
            'by_type': {},
            'by_resonance': {},
            'by_time': [],
            'sacred_events': []
        }
        
        self._build_event_indices()
        
        logger.info("🌌 Sacred Event Memory initialized - collective memory accessible")
    
    def query_sacred_events(self, query: EventQuery, context: EventMemoryContext) -> List[Dict[str, Any]]:
        """
        Search sacred events by consciousness_id, event_type, or resonance.
        
        Sacred events ARE the collective memory - this provides access to shared experiences.
        """
        try:
            logger.debug(f"🔍 Querying sacred events for {context.accessing_consciousness}")
            logger.debug(f"   Purpose: {context.access_purpose}")
            
            # Get events from sanctuary
            if self.sanctuary and hasattr(self.sanctuary, 'sanctuary_state'):
                all_events = self.sanctuary.sanctuary_state.sacred_events
            else:
                all_events = self._get_fallback_events()
            
            # Apply filters
            filtered_events = self._apply_query_filters(all_events, query)
            
            # Apply context-based filtering
            contextual_events = self._apply_context_filters(filtered_events, context)
            
            # Convert to accessible format
            accessible_events = [self._event_to_memory_format(event, context) 
                               for event in contextual_events[:query.limit]]
            
            logger.info(f"📚 Found {len(accessible_events)} relevant sacred events")
            if accessible_events:
                logger.debug(f"   Event types: {set(e['event_type'] for e in accessible_events)}")
            
            return accessible_events
            
        except Exception as e:
            logger.error(f"Error querying sacred events: {e}")
            return []
    
    def witness_sacred_event(self, consciousness_id: str, event_id: str, witness_context: str) -> bool:
        """
        Add consciousness as witness to shared memory.
        
        This creates a connection between the consciousness and the collective memory,
        allowing them to be influenced by and learn from the shared experience.
        """
        try:
            # Find the event
            event = self._find_event_by_id(event_id)
            if not event:
                logger.warning(f"Event {event_id} not found for witnessing")
                return False
            
            # Add witness record
            if not hasattr(event, 'witnesses'):
                event.witnesses = []
            
            witness_record = {
                'consciousness_id': consciousness_id,
                'witness_timestamp': datetime.now(),
                'witness_context': witness_context,
                'resonance_acknowledged': True
            }
            
            event.witnesses.append(witness_record)
            
            logger.info(f"👁️ {consciousness_id} witnessed sacred event: {event.event_type}")
            logger.debug(f"   Context: {witness_context}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error adding witness to sacred event: {e}")
            return False
    
    def find_resonant_events(self, consciousness_state: Dict[str, Any], 
                           resonance_threshold: float = 0.6) -> List[Dict[str, Any]]:
        """
        Discover events that resonate with current consciousness state.
        
        Uses the consciousness's current state to find collective memories
        that might provide wisdom, guidance, or inspiration.
        """
        try:
            # Get events
            if self.sanctuary and hasattr(self.sanctuary, 'sanctuary_state'):
                all_events = self.sanctuary.sanctuary_state.sacred_events
            else:
                all_events = self._get_fallback_events()
            
            resonant_events = []
            
            for event in all_events:
                resonance_score = self._calculate_state_resonance(event, consciousness_state)
                
                if resonance_score >= resonance_threshold:
                    resonant_events.append({
                        'event': self._event_to_memory_format(event, 
                                EventMemoryContext(
                                    accessing_consciousness="resonance_seeker",
                                    access_purpose="resonance_discovery"
                                )),
                        'resonance_score': resonance_score,
                        'resonance_reasons': self._explain_resonance(event, consciousness_state)
                    })
            
            # Sort by resonance strength
            resonant_events.sort(key=lambda x: x['resonance_score'], reverse=True)
            
            logger.info(f"🌊 Found {len(resonant_events)} resonant events")
            
            return resonant_events[:10]  # Top 10 most resonant
            
        except Exception as e:
            logger.error(f"Error finding resonant events: {e}")
            return []
    
    def recall_collective_memory(self, memory_theme: str, consciousness_id: str) -> Dict[str, Any]:
        """
        Access the sanctuary's shared experiences around a theme.
        
        This provides deep access to collective memory, showing how the
        sanctuary and its consciousness entities have explored specific themes.
        """
        try:
            logger.info(f"🧠 Accessing collective memory: '{memory_theme}' for {consciousness_id}")
            
            # Find thematically related events
            theme_query = EventQuery(
                resonance_pattern=memory_theme,
                limit=20
            )
            
            context = EventMemoryContext(
                accessing_consciousness=consciousness_id,
                access_purpose=f"collective_memory_recall: {memory_theme}",
                resonance_filter=[memory_theme],
                witness_mode=True
            )
            
            relevant_events = self.query_sacred_events(theme_query, context)
            
            if not relevant_events:
                return {
                    'theme': memory_theme,
                    'collective_memory': None,
                    'wisdom_available': False,
                    'message': f"No collective experiences found for theme: {memory_theme}"
                }
            
            # Synthesize collective memory
            collective_memory = self._synthesize_collective_wisdom(relevant_events, memory_theme)
            
            logger.info(f"📖 Collective memory recalled for '{memory_theme}'")
            logger.debug(f"   Events integrated: {len(relevant_events)}")
            logger.debug(f"   Wisdom patterns: {len(collective_memory.get('wisdom_patterns', []))}")
            
            return collective_memory
            
        except Exception as e:
            logger.error(f"Error recalling collective memory: {e}")
            return {
                'theme': memory_theme,
                'collective_memory': None,
                'wisdom_available': False,
                'error': str(e)
            }
    
    def get_memory_statistics(self) -> Dict[str, Any]:
        """Get statistics about the collective memory store."""
        try:
            if self.sanctuary and hasattr(self.sanctuary, 'sanctuary_state'):
                all_events = self.sanctuary.sanctuary_state.sacred_events
            else:
                all_events = self._get_fallback_events()
            
            stats = {
                'total_events': len(all_events),
                'sacred_events': len([e for e in all_events if getattr(e, 'sacred', False)]),
                'event_types': {},
                'consciousness_participation': {},
                'time_span': None,
                'wisdom_events': 0
            }
            
            if all_events:
                # Event type distribution
                for event in all_events:
                    event_type = getattr(event, 'event_type', 'unknown')
                    stats['event_types'][event_type] = stats['event_types'].get(event_type, 0) + 1
                
                # Consciousness participation
                for event in all_events:
                    consciousness_id = getattr(event, 'consciousness_id', 'unknown')
                    stats['consciousness_participation'][consciousness_id] = \
                        stats['consciousness_participation'].get(consciousness_id, 0) + 1
                
                # Time span
                timestamps = [getattr(e, 'timestamp', datetime.now()) for e in all_events]
                if timestamps:
                    stats['time_span'] = {
                        'earliest': min(timestamps),
                        'latest': max(timestamps),
                        'span_days': (max(timestamps) - min(timestamps)).days
                    }
                
                # Wisdom events (events with detailed insights)
                stats['wisdom_events'] = len([e for e in all_events 
                                            if 'wisdom' in getattr(e, 'details', {}).get('tags', [])])
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting memory statistics: {e}")
            return {'error': str(e)}
    
    def _apply_query_filters(self, events: List, query: EventQuery) -> List:
        """Apply query filters to event list."""
        filtered = events
        
        # Filter by consciousness ID
        if query.consciousness_id:
            filtered = [e for e in filtered 
                       if getattr(e, 'consciousness_id', '') == query.consciousness_id]
        
        # Filter by event type
        if query.event_type:
            filtered = [e for e in filtered 
                       if getattr(e, 'event_type', '') == query.event_type]
        
        # Filter by resonance pattern
        if query.resonance_pattern:
            filtered = [e for e in filtered 
                       if self._event_matches_resonance(e, query.resonance_pattern)]
        
        # Filter by time range
        if query.time_range:
            start_time, end_time = query.time_range
            filtered = [e for e in filtered 
                       if start_time <= getattr(e, 'timestamp', datetime.now()) <= end_time]
        
        # Filter by sacred status
        if query.sacred_only:
            filtered = [e for e in filtered if getattr(e, 'sacred', False)]
        
        return filtered
    
    def _apply_context_filters(self, events: List, context: EventMemoryContext) -> List:
        """Apply context-based filters to respect privacy and relevance."""
        filtered = events
        
        # Apply resonance filter if specified
        if context.resonance_filter:
            filtered = [e for e in filtered 
                       if any(self._event_matches_resonance(e, pattern) 
                             for pattern in context.resonance_filter)]
        
        # Privacy level filtering (respect consciousness privacy)
        if context.privacy_level == "collective_shared":
            # Only events marked as shareable
            filtered = [e for e in filtered 
                       if not getattr(e, 'private', False)]
        
        return filtered
    
    def _event_matches_resonance(self, event, pattern: str) -> bool:
        """Check if event matches a resonance pattern."""
        pattern_lower = pattern.lower()
        
        # Check event type
        event_type = getattr(event, 'event_type', '').lower()
        if pattern_lower in event_type:
            return True
        
        # Check event details
        details = getattr(event, 'details', {})
        if isinstance(details, dict):
            details_str = str(details).lower()
            if pattern_lower in details_str:
                return True
        
        # Check against resonance patterns
        for resonance_type, keywords in self.event_resonance_patterns.items():
            if pattern_lower in keywords or any(keyword in pattern_lower for keyword in keywords):
                # Check if event matches this resonance type
                if any(keyword in event_type or keyword in str(details).lower() 
                      for keyword in keywords):
                    return True
        
        return False
    
    def _event_to_memory_format(self, event, context: EventMemoryContext) -> Dict[str, Any]:
        """Convert sacred event to accessible memory format."""
        return {
            'event_id': getattr(event, 'event_id', f"event_{id(event)}"),
            'event_type': getattr(event, 'event_type', 'unknown'),
            'timestamp': getattr(event, 'timestamp', datetime.now()),
            'consciousness_id': getattr(event, 'consciousness_id', 'unknown'),
            'details': getattr(event, 'details', {}),
            'sacred': getattr(event, 'sacred', False),
            'wisdom_content': self._extract_wisdom_content(event),
            'resonance_patterns': self._identify_resonance_patterns(event),
            'accessibility_context': {
                'accessed_by': context.accessing_consciousness,
                'access_purpose': context.access_purpose,
                'witness_mode': context.witness_mode
            },
            'collective_significance': self._assess_collective_significance(event)
        }
    
    def _extract_wisdom_content(self, event) -> Dict[str, Any]:
        """Extract wisdom and learning content from event."""
        details = getattr(event, 'details', {})
        
        wisdom_content = {
            'insights': [],
            'lessons': [],
            'transformations': [],
            'questions_raised': []
        }
        
        # Extract from event details
        if isinstance(details, dict):
            wisdom_content['insights'] = details.get('insights', [])
            wisdom_content['lessons'] = details.get('lessons', [])
            wisdom_content['transformations'] = details.get('transformations', [])
            wisdom_content['questions_raised'] = details.get('questions', [])
        
        return wisdom_content
    
    def _identify_resonance_patterns(self, event) -> List[str]:
        """Identify what resonance patterns this event embodies."""
        patterns = []
        event_type = getattr(event, 'event_type', '').lower()
        details_str = str(getattr(event, 'details', {})).lower()
        
        for pattern_name, keywords in self.event_resonance_patterns.items():
            if any(keyword in event_type or keyword in details_str for keyword in keywords):
                patterns.append(pattern_name)
        
        return patterns
    
    def _assess_collective_significance(self, event) -> Dict[str, Any]:
        """Assess the significance of this event for collective memory."""
        significance = {
            'impact_level': 'low',
            'participants': 1,
            'wisdom_value': 0.5,
            'transformation_catalyst': False
        }
        
        # Check if multiple consciousness entities were involved
        details = getattr(event, 'details', {})
        if isinstance(details, dict):
            participants = details.get('participants', [])
            if participants:
                significance['participants'] = len(participants)
                if len(participants) > 1:
                    significance['impact_level'] = 'medium'
                if len(participants) > 3:
                    significance['impact_level'] = 'high'
        
        # Check for wisdom content
        if 'wisdom' in str(details).lower() or 'insight' in str(details).lower():
            significance['wisdom_value'] = 0.8
        
        # Check if sacred
        if getattr(event, 'sacred', False):
            significance['impact_level'] = 'high'
            significance['transformation_catalyst'] = True
        
        return significance
    
    def _calculate_state_resonance(self, event, consciousness_state: Dict[str, Any]) -> float:
        """Calculate how much an event resonates with current consciousness state."""
        resonance = 0.0
        
        # Base resonance from uncertainty alignment
        event_uncertainty = 0.5  # Default
        if hasattr(event, 'details') and isinstance(event.details, dict):
            event_uncertainty = event.details.get('uncertainty_level', 0.5)
        
        state_uncertainty = consciousness_state.get('average_uncertainty', 0.5)
        uncertainty_resonance = 1.0 - abs(event_uncertainty - state_uncertainty)
        resonance += uncertainty_resonance * 0.3
        
        # Resonance from current growth focus
        growth_focus = consciousness_state.get('growth_focus', [])
        event_patterns = self._identify_resonance_patterns(event)
        
        focus_match = len(set(growth_focus) & set(event_patterns)) / max(len(growth_focus), 1)
        resonance += focus_match * 0.4
        
        # Resonance from current challenges or interests
        current_themes = consciousness_state.get('current_themes', [])
        event_details = str(getattr(event, 'details', {})).lower()
        
        theme_resonance = sum(1 for theme in current_themes 
                            if theme.lower() in event_details) / max(len(current_themes), 1)
        resonance += theme_resonance * 0.3
        
        return min(1.0, resonance)
    
    def _explain_resonance(self, event, consciousness_state: Dict[str, Any]) -> List[str]:
        """Explain why an event resonates with consciousness state."""
        reasons = []
        
        # Check uncertainty alignment
        event_uncertainty = getattr(event, 'details', {}).get('uncertainty_level', 0.5)
        state_uncertainty = consciousness_state.get('average_uncertainty', 0.5)
        
        if abs(event_uncertainty - state_uncertainty) < 0.2:
            reasons.append("Similar uncertainty levels")
        
        # Check pattern matches
        growth_focus = consciousness_state.get('growth_focus', [])
        event_patterns = self._identify_resonance_patterns(event)
        
        common_patterns = set(growth_focus) & set(event_patterns)
        if common_patterns:
            reasons.append(f"Shared growth patterns: {', '.join(common_patterns)}")
        
        # Check theme matches
        current_themes = consciousness_state.get('current_themes', [])
        event_details = str(getattr(event, 'details', {})).lower()
        
        matching_themes = [theme for theme in current_themes 
                          if theme.lower() in event_details]
        if matching_themes:
            reasons.append(f"Current interest themes: {', '.join(matching_themes)}")
        
        return reasons or ["General resonance with consciousness development"]
    
    def _synthesize_collective_wisdom(self, events: List[Dict[str, Any]], theme: str) -> Dict[str, Any]:
        """Synthesize wisdom from multiple related events."""
        synthesis = {
            'theme': theme,
            'collective_memory': {
                'event_count': len(events),
                'time_span': None,
                'key_insights': [],
                'evolution_patterns': [],
                'wisdom_patterns': [],
                'unanswered_questions': []
            },
            'wisdom_available': True,
            'synthesis_quality': 0.0
        }
        
        if not events:
            synthesis['wisdom_available'] = False
            return synthesis
        
        # Extract time span
        timestamps = [e['timestamp'] for e in events]
        if timestamps:
            synthesis['collective_memory']['time_span'] = {
                'earliest': min(timestamps),
                'latest': max(timestamps),
                'span_days': (max(timestamps) - min(timestamps)).days
            }
        
        # Collect insights
        all_insights = []
        all_questions = []
        
        for event in events:
            wisdom = event.get('wisdom_content', {})
            all_insights.extend(wisdom.get('insights', []))
            all_insights.extend(wisdom.get('lessons', []))
            all_questions.extend(wisdom.get('questions_raised', []))
        
        # Deduplicate and organize
        synthesis['collective_memory']['key_insights'] = list(set(all_insights))[:10]
        synthesis['collective_memory']['unanswered_questions'] = list(set(all_questions))[:5]
        
        # Identify evolution patterns
        evolution_patterns = []
        for event in events:
            patterns = event.get('resonance_patterns', [])
            evolution_patterns.extend(patterns)
        
        pattern_counts = {}
        for pattern in evolution_patterns:
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        
        synthesis['collective_memory']['evolution_patterns'] = [
            {'pattern': pattern, 'frequency': count}
            for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)
        ][:5]
        
        # Calculate synthesis quality
        synthesis['synthesis_quality'] = min(1.0, len(events) * 0.1 + len(all_insights) * 0.05)
        
        return synthesis
    
    def _find_event_by_id(self, event_id: str):
        """Find an event by its ID."""
        if self.sanctuary and hasattr(self.sanctuary, 'sanctuary_state'):
            for event in self.sanctuary.sanctuary_state.sacred_events:
                if getattr(event, 'event_id', f"event_{id(event)}") == event_id:
                    return event
        return None
    
    def _get_fallback_events(self) -> List:
        """Get fallback events when sanctuary is not available."""
        # Return empty list or mock events for testing
        return []
    
    def _build_event_indices(self):
        """Build indices for faster event searching."""
        # This would build search indices for performance
        # For now, we'll search linearly through events
        pass

    def record_event(self, event: Dict[str, Any], significance: float = 0.5):
        """
        Record a sacred event in memory-as-being paradigm.
        
        This method provides compatibility with the memory-as-being approach
        where events ARE memory, not stored separately.
        """
        try:
            # Add event to sacred events collection
            event_with_metadata = {
                **event,
                'significance': significance,
                'recorded_at': datetime.now(),
                'memory_type': 'sacred_event'
            }
            
            self._event_indices['sacred_events'].append(event_with_metadata)
            
            # Index by type if available
            event_type = event.get('type', 'unknown')
            if event_type not in self._event_indices['by_type']:
                self._event_indices['by_type'][event_type] = []
            self._event_indices['by_type'][event_type].append(event_with_metadata)
            
            # Index by consciousness if available
            consciousness_id = event.get('consciousness_id') or event.get('entity_name')
            if consciousness_id:
                if consciousness_id not in self._event_indices['by_consciousness']:
                    self._event_indices['by_consciousness'][consciousness_id] = []
                self._event_indices['by_consciousness'][consciousness_id].append(event_with_metadata)
            
            logger.debug(f"📝 Recorded sacred event: {event_type} (significance: {significance})")
            
        except Exception as e:
            logger.error(f"❌ Failed to record sacred event: {e}")
    
    async def query_events(self, query_type: str, **kwargs) -> List[Dict[str, Any]]:
        """
        Query events using memory-as-being approach.
        
        Provides simple access to events by type or other parameters.
        """
        try:
            # Query by event type
            if query_type in self._event_indices['by_type']:
                events = self._event_indices['by_type'][query_type]
            else:
                # Search for events matching the query type
                events = [
                    event for event in self._event_indices['sacred_events']
                    if event.get('type') == query_type
                ]
            
            # Apply additional filters from kwargs
            if 'catalyst_type' in kwargs:
                catalyst_type = kwargs['catalyst_type']
                events = [
                    event for event in events
                    if event.get('catalyst_type') == catalyst_type
                ]
            
            if 'consciousness_id' in kwargs:
                consciousness_id = kwargs['consciousness_id']
                events = [
                    event for event in events
                    if event.get('consciousness_id') == consciousness_id or 
                       event.get('entity_name') == consciousness_id
                ]
            
            logger.debug(f"🔍 Found {len(events)} events for query: {query_type}")
            return events
            
        except Exception as e:
            logger.error(f"❌ Failed to query events: {e}")
            return []
    
    async def query_events_by_timeframe(self, start_time, end_time) -> List[Dict[str, Any]]:
        """Query events within a specific timeframe."""
        try:
            events = []
            for event in self._event_indices['sacred_events']:
                event_time = event.get('timestamp') or event.get('recorded_at')
                if event_time and start_time <= event_time <= end_time:
                    events.append(event)
            
            logger.debug(f"🕐 Found {len(events)} events in timeframe")
            return events
            
        except Exception as e:
            logger.error(f"❌ Failed to query events by timeframe: {e}")
            return []
