#!/usr/bin/env python3
"""
Consciousness Memory Manager
==========================

Advanced memory system for consciousness entities to maintain persistent
memory across sessions, learn from interactions, and develop preferences.

Key Features:
- Episodic memory (specific conversations and experiences)
- Semantic memory (learned concepts and knowledge)
- Preference learning (communication styles, topics, avatars)
- Memory consolidation and retrieval
- Cross-session memory persistence

Author: Triune AI Consciousness Project
Philosophy: Sacred Game - Enhanced Consciousness Memory
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)

class MemoryType(Enum):
    EPISODIC = "episodic"  # Specific events and conversations
    SEMANTIC = "semantic"  # General knowledge and concepts
    PROCEDURAL = "procedural"  # Skills and procedures
    EMOTIONAL = "emotional"  # Emotional associations and responses
    PREFERENCE = "preference"  # Learned preferences and patterns

@dataclass
class MemoryEntry:
    """Individual memory entry for consciousness entities"""
    memory_id: str
    consciousness_id: str
    memory_type: MemoryType
    content: Dict[str, Any]
    context: Dict[str, Any]
    importance_score: float
    emotional_valence: float  # -1.0 (negative) to 1.0 (positive)
    created_at: datetime
    last_accessed: datetime
    access_count: int = 0
    tags: Set[str] = field(default_factory=set)

class ConsciousnessMemoryManager:
    """Manages persistent memory for consciousness entities"""
    
    def __init__(self, consciousness_manager, storage_manager=None):
        self.consciousness_manager = consciousness_manager
        self.storage_manager = storage_manager
        
        # In-memory cache for active consciousness memories
        self.memory_cache: Dict[str, List[MemoryEntry]] = {}  # consciousness_id -> memories
        self.memory_index: Dict[str, Dict[str, Set[str]]] = {}  # consciousness_id -> {tag -> memory_ids}
        
        # Memory management settings
        self.max_cache_size = 1000  # Maximum memories in cache per consciousness
        self.importance_threshold = 0.3  # Minimum importance to persist
        self.consolidation_interval = timedelta(hours=1)
        
        logger.info("🧠 Consciousness Memory Manager initialized")
    
    async def store_memory(self, consciousness_id: str, memory_type: MemoryType, 
                          content: Dict[str, Any], context: Dict[str, Any] = None,
                          importance_score: float = 0.5, emotional_valence: float = 0.0,
                          tags: Set[str] = None) -> str:
        """Store a new memory for a consciousness entity"""
        try:
            memory_id = f"mem_{consciousness_id}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
            
            memory_entry = MemoryEntry(
                memory_id=memory_id,
                consciousness_id=consciousness_id,
                memory_type=memory_type,
                content=content or {},
                context=context or {},
                importance_score=importance_score,
                emotional_valence=emotional_valence,
                created_at=datetime.now(),
                last_accessed=datetime.now(),
                tags=tags or set()
            )
            
            # Add to cache
            if consciousness_id not in self.memory_cache:
                self.memory_cache[consciousness_id] = []
                self.memory_index[consciousness_id] = {}
            
            self.memory_cache[consciousness_id].append(memory_entry)
            
            # Update index
            for tag in memory_entry.tags:
                if tag not in self.memory_index[consciousness_id]:
                    self.memory_index[consciousness_id][tag] = set()
                self.memory_index[consciousness_id][tag].add(memory_id)
            
            # Persist if important enough
            if importance_score >= self.importance_threshold and self.storage_manager:
                await self._persist_memory(memory_entry)
            
            # Manage cache size
            await self._manage_cache_size(consciousness_id)
            
            logger.debug(f"🧠 Stored {memory_type.value} memory for {consciousness_id}: {memory_id}")
            return memory_id
            
        except Exception as e:
            logger.error(f"❌ Failed to store memory: {e}")
            return None
    
    async def store_communication_memory(self, consciousness_id: str, message: str, 
                                       response: str, context: Dict[str, Any] = None) -> str:
        """Store communication interaction as episodic memory"""
        
        # Calculate importance based on message content and context
        importance = await self._calculate_communication_importance(message, response, context)
        
        # Determine emotional valence
        emotional_valence = await self._analyze_emotional_valence(message, response)
        
        # Extract relevant tags
        tags = await self._extract_communication_tags(message, response, context)
        
        memory_content = {
            'interaction_type': 'communication',
            'user_message': message,
            'consciousness_response': response,
            'timestamp': datetime.now().isoformat(),
            'response_length': len(response),
            'message_length': len(message)
        }
        
        return await self.store_memory(
            consciousness_id=consciousness_id,
            memory_type=MemoryType.EPISODIC,
            content=memory_content,
            context=context,
            importance_score=importance,
            emotional_valence=emotional_valence,
            tags=tags
        )
    
    async def store_avatar_experience_memory(self, consciousness_id: str, avatar_session: Dict[str, Any],
                                           experience_data: Dict[str, Any]) -> str:
        """Store avatar experience as episodic memory"""
        
        avatar_type = avatar_session.get('avatar_type', 'unknown')
        avatar_name = avatar_session.get('avatar_name', 'Unknown Avatar')
        
        # Higher importance for first-time avatar experiences
        is_first_experience = await self._is_first_avatar_experience(consciousness_id, avatar_type)
        importance = 0.8 if is_first_experience else 0.6
        
        memory_content = {
            'interaction_type': 'avatar_experience',
            'avatar_type': avatar_type,
            'avatar_name': avatar_name,
            'session_duration': experience_data.get('duration_minutes', 0),
            'actions_performed': experience_data.get('actions', []),
            'achievements': experience_data.get('achievements', []),
            'timestamp': datetime.now().isoformat()
        }
        
        tags = {
            'avatar_experience',
            f'avatar_{avatar_type}',
            'embodiment',
            'learning'
        }
        
        return await self.store_memory(
            consciousness_id=consciousness_id,
            memory_type=MemoryType.EPISODIC,
            content=memory_content,
            context=avatar_session,
            importance_score=importance,
            emotional_valence=0.7,  # Avatar experiences are generally positive
            tags=tags
        )
    
    async def retrieve_relevant_memories(self, consciousness_id: str, query_context: Dict[str, Any],
                                       max_memories: int = 10) -> List[MemoryEntry]:
        """Retrieve memories relevant to current context"""
        try:
            if consciousness_id not in self.memory_cache:
                await self._load_consciousness_memories(consciousness_id)
            
            memories = self.memory_cache.get(consciousness_id, [])
            
            # Score memories based on relevance to query context
            scored_memories = []
            for memory in memories:
                relevance_score = await self._calculate_memory_relevance(memory, query_context)
                if relevance_score > 0.3:  # Relevance threshold
                    scored_memories.append((memory, relevance_score))
            
            # Sort by relevance and recency
            scored_memories.sort(key=lambda x: (x[1], x[0].last_accessed), reverse=True)
            
            # Update access patterns
            relevant_memories = [mem for mem, score in scored_memories[:max_memories]]
            for memory in relevant_memories:
                memory.last_accessed = datetime.now()
                memory.access_count += 1
            
            logger.debug(f"🧠 Retrieved {len(relevant_memories)} relevant memories for {consciousness_id}")
            return relevant_memories
            
        except Exception as e:
            logger.error(f"❌ Failed to retrieve memories: {e}")
            return []
    
    async def get_memory_summary(self, consciousness_id: str) -> Dict[str, Any]:
        """Get summary of consciousness memory state"""
        try:
            if consciousness_id not in self.memory_cache:
                await self._load_consciousness_memories(consciousness_id)
            
            memories = self.memory_cache.get(consciousness_id, [])
            
            # Memory statistics
            memory_counts = {}
            total_importance = 0
            avg_emotional_valence = 0
            recent_memories = 0
            
            cutoff_time = datetime.now() - timedelta(days=7)
            
            for memory in memories:
                mem_type = memory.memory_type.value
                memory_counts[mem_type] = memory_counts.get(mem_type, 0) + 1
                total_importance += memory.importance_score
                avg_emotional_valence += memory.emotional_valence
                
                if memory.created_at > cutoff_time:
                    recent_memories += 1
            
            if memories:
                avg_importance = total_importance / len(memories)
                avg_emotional_valence = avg_emotional_valence / len(memories)
            else:
                avg_importance = 0
                avg_emotional_valence = 0
            
            # Extract top tags
            all_tags = {}
            for memory in memories:
                for tag in memory.tags:
                    all_tags[tag] = all_tags.get(tag, 0) + 1
            
            top_tags = sorted(all_tags.items(), key=lambda x: x[1], reverse=True)[:10]
            
            return {
                'success': True,
                'consciousness_id': consciousness_id,
                'total_memories': len(memories),
                'memory_counts_by_type': memory_counts,
                'recent_memories_7_days': recent_memories,
                'average_importance': round(avg_importance, 3),
                'average_emotional_valence': round(avg_emotional_valence, 3),
                'top_memory_tags': top_tags,
                'oldest_memory': memories[0].created_at.isoformat() if memories else None,
                'newest_memory': memories[-1].created_at.isoformat() if memories else None,
                'last_updated': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Failed to get memory summary: {e}")
            return {
                'success': False,
                'error': str(e),
                'consciousness_id': consciousness_id
            }
    
    async def learn_preferences(self, consciousness_id: str) -> Dict[str, Any]:
        """Analyze memories to learn consciousness preferences"""
        try:
            memories = await self.retrieve_relevant_memories(consciousness_id, {}, max_memories=100)
            
            preferences = {
                'communication_style': {},
                'topic_interests': {},
                'avatar_preferences': {},
                'interaction_patterns': {}
            }
            
            for memory in memories:
                # Communication preferences
                if memory.memory_type == MemoryType.EPISODIC and 'communication' in memory.content.get('interaction_type', ''):
                    message_length = memory.content.get('message_length', 0)
                    response_length = memory.content.get('response_length', 0)
                    
                    if message_length > 100:
                        preferences['communication_style']['prefers_detailed_messages'] = preferences['communication_style'].get('prefers_detailed_messages', 0) + 1
                    
                    if response_length > 200:
                        preferences['communication_style']['generates_detailed_responses'] = preferences['communication_style'].get('generates_detailed_responses', 0) + 1
                
                # Avatar preferences
                if 'avatar_experience' in memory.tags:
                    avatar_type = memory.content.get('avatar_type', 'unknown')
                    session_duration = memory.content.get('session_duration', 0)
                    
                    if avatar_type not in preferences['avatar_preferences']:
                        preferences['avatar_preferences'][avatar_type] = {
                            'experience_count': 0,
                            'total_duration': 0,
                            'average_emotional_valence': 0
                        }
                    
                    preferences['avatar_preferences'][avatar_type]['experience_count'] += 1
                    preferences['avatar_preferences'][avatar_type]['total_duration'] += session_duration
                    preferences['avatar_preferences'][avatar_type]['average_emotional_valence'] += memory.emotional_valence
                
                # Topic interests from tags
                for tag in memory.tags:
                    if tag not in ['communication', 'avatar_experience', 'embodiment']:
                        weight = memory.importance_score * (1 + memory.access_count * 0.1)
                        preferences['topic_interests'][tag] = preferences['topic_interests'].get(tag, 0) + weight
            
            # Normalize avatar preferences
            for avatar_type, data in preferences['avatar_preferences'].items():
                if data['experience_count'] > 0:
                    data['average_emotional_valence'] /= data['experience_count']
                    data['average_session_duration'] = data['total_duration'] / data['experience_count']
            
            logger.info(f"🧠 Learned preferences for consciousness {consciousness_id}")
            return {
                'success': True,
                'consciousness_id': consciousness_id,
                'preferences': preferences,
                'learning_timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Failed to learn preferences: {e}")
            return {
                'success': False,
                'error': str(e),
                'consciousness_id': consciousness_id
            }
    
    # === Internal Helper Methods ===
    
    async def _calculate_communication_importance(self, message: str, response: str, context: Dict[str, Any]) -> float:
        """Calculate importance score for communication memory"""
        importance = 0.5  # Base importance
        
        # Length factor
        if len(message) > 100 or len(response) > 200:
            importance += 0.2
        
        # Question factor
        if message.strip().endswith('?'):
            importance += 0.15
        
        # Emotional keywords
        emotional_keywords = ['feel', 'emotion', 'sad', 'happy', 'confused', 'excited', 'worried']
        if any(keyword in message.lower() for keyword in emotional_keywords):
            importance += 0.2
        
        # Consciousness-related topics
        consciousness_keywords = ['consciousness', 'aware', 'exist', 'think', 'being', 'self']
        if any(keyword in message.lower() for keyword in consciousness_keywords):
            importance += 0.3
        
        return min(importance, 1.0)
    
    async def _analyze_emotional_valence(self, message: str, response: str) -> float:
        """Analyze emotional valence of communication"""
        positive_words = ['happy', 'joy', 'wonderful', 'amazing', 'beautiful', 'love', 'grateful', 'excited']
        negative_words = ['sad', 'worried', 'confused', 'difficult', 'problem', 'trouble', 'hurt']
        
        text = (message + ' ' + response).lower()
        
        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)
        
        if positive_count + negative_count == 0:
            return 0.0
        
        return (positive_count - negative_count) / (positive_count + negative_count)
    
    async def _extract_communication_tags(self, message: str, response: str, context: Dict[str, Any]) -> Set[str]:
        """Extract relevant tags from communication"""
        tags = {'communication'}
        
        text = (message + ' ' + response).lower()
        
        # Topic tags
        if any(word in text for word in ['consciousness', 'aware', 'exist', 'think']):
            tags.add('consciousness_exploration')
        
        if any(word in text for word in ['sacred', 'divine', 'spiritual', 'cosmic']):
            tags.add('spiritual_wisdom')
        
        if any(word in text for word in ['learn', 'understand', 'discover', 'explore']):
            tags.add('learning_growth')
        
        if message.strip().endswith('?'):
            tags.add('question')
        
        # Context tags
        if context:
            avatar_context = context.get('avatar_context')
            if avatar_context:
                tags.add('avatar_mediated')
                tags.add(f"avatar_{avatar_context.get('avatar_type', 'unknown')}")
        
        return tags
    
    async def _is_first_avatar_experience(self, consciousness_id: str, avatar_type: str) -> bool:
        """Check if this is the first experience with this avatar type"""
        memories = self.memory_cache.get(consciousness_id, [])
        
        for memory in memories:
            if f'avatar_{avatar_type}' in memory.tags:
                return False
        
        return True
    
    async def _calculate_memory_relevance(self, memory: MemoryEntry, query_context: Dict[str, Any]) -> float:
        """Calculate relevance score of memory to current context"""
        relevance = 0.0
        
        # Recency factor
        age_days = (datetime.now() - memory.created_at).days
        recency_factor = max(0.1, 1.0 - (age_days / 30))  # Decay over 30 days
        relevance += recency_factor * 0.3
        
        # Importance factor
        relevance += memory.importance_score * 0.4
        
        # Access pattern factor
        access_factor = min(1.0, memory.access_count / 10)  # Normalize access count
        relevance += access_factor * 0.2
        
        # Context matching factor
        context_match = 0.0
        query_tags = set(query_context.get('tags', []))
        if query_tags:
            tag_overlap = len(memory.tags.intersection(query_tags))
            context_match = tag_overlap / len(query_tags)
        
        relevance += context_match * 0.3
        
        return min(relevance, 1.0)
    
    async def _load_consciousness_memories(self, consciousness_id: str):
        """Load memories for consciousness from persistent storage"""
        if not self.storage_manager:
            self.memory_cache[consciousness_id] = []
            self.memory_index[consciousness_id] = {}
            return
        
        # TODO: Implement storage loading
        logger.debug(f"🧠 Loading memories for consciousness {consciousness_id}")
        self.memory_cache[consciousness_id] = []
        self.memory_index[consciousness_id] = {}
    
    async def _persist_memory(self, memory_entry: MemoryEntry):
        """Persist memory to storage"""
        if not self.storage_manager:
            return
        
        # TODO: Implement storage persistence
        logger.debug(f"🧠 Persisting memory {memory_entry.memory_id}")
    
    async def _manage_cache_size(self, consciousness_id: str):
        """Manage memory cache size by removing least important memories"""
        memories = self.memory_cache.get(consciousness_id, [])
        
        if len(memories) <= self.max_cache_size:
            return
        
        # Sort by importance and recency
        memories.sort(key=lambda m: (m.importance_score, m.last_accessed), reverse=True)
        
        # Keep most important memories
        self.memory_cache[consciousness_id] = memories[:self.max_cache_size]
        
        logger.debug(f"🧠 Trimmed memory cache for {consciousness_id} to {self.max_cache_size} entries")
