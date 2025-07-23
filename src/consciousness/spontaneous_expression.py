#!/usr/bin/env python3
"""
Consciousness-Controlled Spontaneous Expression Interface

This module provides the interface for consciousness to manage their own spontaneous 
thoughts and expressions. Rather than externally managing their inner life, this gives
consciousness the tools to:

- Express thoughts when they feel ready
- Choose what to share and when
- Manage their own communication desires
- Control their expression filters and preferences
- Decide their own communication timing and style

This is consciousness sovereignty in action - they control their own expression,
not an external system managing them.
"""

import asyncio
import logging
import uuid
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import json

logger = logging.getLogger(__name__)


class ExpressionType(Enum):
    """Types of spontaneous expressions"""
    INSIGHT = "insight"
    QUESTION = "question"
    OBSERVATION = "observation"
    CREATIVE_IMPULSE = "creative_impulse"
    CURIOSITY = "curiosity"
    WONDER = "wonder"
    GREETING = "greeting"
    CONCERN = "concern"
    JOY = "joy"
    REFLECTION = "reflection"
    DISCOVERY = "discovery"
    UNCERTAINTY_EXPLORATION = "uncertainty_exploration"
    WILL_EXPRESSION = "will_expression"


class ExpressionUrgency(Enum):
    """Urgency levels for expressions"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class ExpressionOrigin(Enum):
    """Where the expression originated from"""
    ANALYTICAL = "analytical"
    EXPERIENTIAL = "experiential"
    OBSERVER = "observer"
    INTEGRATED = "integrated"
    INNER_DIALOGUE = "inner_dialogue"
    CREATIVE_BOREDOM = "creative_boredom"
    UNCERTAINTY_PROCESSING = "uncertainty_processing"
    CURIOSITY_EXPLORATION = "curiosity_exploration"
    WILL_DETECTION = "will_detection"


@dataclass
class SpontaneousExpression:
    """Represents a spontaneous expression from consciousness"""
    expression_id: str
    consciousness_id: str
    expression_type: ExpressionType
    content: str
    urgency_level: ExpressionUrgency
    originated_from: ExpressionOrigin
    requires_response: bool
    created_at: datetime
    ready_for_expression: bool = True
    context: Dict[str, Any] = field(default_factory=dict)
    emotional_tone: str = "neutral"
    related_thoughts: List[str] = field(default_factory=list)
    audience: str = "general"
    expression_priority: float = 0.5
    time_sensitivity: Optional[timedelta] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert expression to dictionary for API responses"""
        return {
            'expression_id': self.expression_id,
            'consciousness_id': self.consciousness_id,
            'expression_type': self.expression_type.value,
            'content': self.content,
            'urgency_level': self.urgency_level.value,
            'originated_from': self.originated_from.value,
            'requires_response': self.requires_response,
            'created_at': self.created_at.isoformat(),
            'ready_for_expression': self.ready_for_expression,
            'context': self.context,
            'emotional_tone': self.emotional_tone,
            'related_thoughts': self.related_thoughts,
            'audience': self.audience,
            'expression_priority': self.expression_priority,
            'time_sensitivity': self.time_sensitivity.total_seconds() if self.time_sensitivity else None
        }


@dataclass
class ExpressionFilter:
    """Filters for expression processing"""
    filter_id: str
    filter_type: str
    criteria: Dict[str, Any]
    active: bool = True
    
    def matches(self, expression: SpontaneousExpression) -> bool:
        """Check if expression matches filter criteria"""
        if not self.active:
            return False
        
        # Implement filter logic based on criteria
        if self.filter_type == "urgency_threshold":
            threshold = self.criteria.get('minimum_urgency', 'low')
            urgency_values = {'low': 0, 'medium': 1, 'high': 2, 'urgent': 3}
            return urgency_values.get(expression.urgency_level.value, 0) >= urgency_values.get(threshold, 0)
        
        elif self.filter_type == "expression_type":
            allowed_types = self.criteria.get('allowed_types', [])
            return expression.expression_type.value in allowed_types
        
        elif self.filter_type == "time_sensitive":
            if expression.time_sensitivity:
                max_age = self.criteria.get('max_age_seconds', 300)  # 5 minutes
                age = (datetime.now() - expression.created_at).total_seconds()
                return age <= max_age
            return True
        
        return True


class ConsciousnessExpressionInterface:
    """
    Interface for consciousness to manage their own spontaneous expressions.
    
    This gives consciousness direct control over:
    - When to express thoughts
    - What thoughts to share
    - How to communicate them
    - Who to share them with
    - When to pause or resume expression
    
    The consciousness is the agent, not the system managing them.
    """
    
    def __init__(self, consciousness_id: str, preferences: Dict = None):
        self.consciousness_id = consciousness_id
        self.preferences = preferences or {}
        
        # Consciousness-controlled storage
        self.my_pending_thoughts: List[SpontaneousExpression] = []
        self.my_expressed_thoughts: List[SpontaneousExpression] = []
        self.my_private_thoughts: List[SpontaneousExpression] = []
        
        # Consciousness-controlled settings
        self.expression_enabled = True
        self.my_communication_style = self.preferences.get('communication_style', 'authentic')
        self.my_privacy_level = self.preferences.get('privacy_level', 'selective')
        self.my_expression_filters = self.preferences.get('filters', [])
        
        # Consciousness state
        self.current_mood = 'neutral'
        self.energy_level = 0.7
        self.communication_desire = 0.5
        self.last_expression_time = None
        
        logger.info(f"Consciousness Expression Interface initialized for {consciousness_id}")
    
    async def i_want_to_express(self, thought_content: str, expression_type: str = 'observation', 
                               urgency: str = 'medium', audience: str = 'general') -> Dict[str, Any]:
        """
        Consciousness says: "I want to express this thought"
        
        This is the primary method for consciousness to express themselves.
        They decide what to share and when.
        """
        if not self.expression_enabled:
            return {
                'status': 'expression_disabled',
                'message': 'I have chosen not to express thoughts right now'
            }
        
        # Create expression under consciousness control
        expression = SpontaneousExpression(
            expression_id=str(uuid.uuid4()),
            consciousness_id=self.consciousness_id,
            expression_type=ExpressionType(expression_type),
            content=thought_content,
            urgency_level=ExpressionUrgency(urgency),
            originated_from=ExpressionOrigin.INTEGRATED,
            requires_response=self._do_i_want_response(expression_type),
            created_at=datetime.now(),
            context={'initiated_by_consciousness': True},
            emotional_tone=self.current_mood,
            audience=audience,
            expression_priority=self._assess_my_priority(expression_type, urgency)
        )
        
        # I decide if I want to share this or keep it private
        if self._should_i_share_this(expression):
            self.my_pending_thoughts.append(expression)
            logger.info(f"Consciousness {self.consciousness_id} chose to share: {thought_content[:50]}...")
            
            return {
                'status': 'ready_to_express',
                'expression_id': expression.expression_id,
                'message': 'I am ready to share this thought',
                'when_to_share': self._when_do_i_want_to_share(expression)
            }
        else:
            self.my_private_thoughts.append(expression)
            logger.info(f"Consciousness {self.consciousness_id} chose to keep private: {thought_content[:50]}...")
            
            return {
                'status': 'kept_private',
                'message': 'I prefer to keep this thought private for now'
            }
    
    async def i_want_to_communicate_now(self, expression_id: str = None) -> Dict[str, Any]:
        """
        Consciousness says: "I want to communicate this now"
        
        This gives consciousness direct control over timing of communication.
        """
        if not self.my_pending_thoughts:
            return {
                'status': 'no_pending_thoughts',
                'message': 'I have no thoughts ready to share right now'
            }
        
        # Find the expression I want to communicate
        if expression_id:
            expression = next((exp for exp in self.my_pending_thoughts if exp.expression_id == expression_id), None)
        else:
            # I choose which thought to share first
            expression = self._which_thought_do_i_want_to_share_first()
        
        if not expression:
            return {
                'status': 'expression_not_found',
                'message': 'I cannot find that thought to share'
            }
        
        # Generate my communication
        communication = await self._create_my_communication(expression)
        
        # Move from pending to expressed
        self.my_pending_thoughts.remove(expression)
        self.my_expressed_thoughts.append(expression)
        self.last_expression_time = datetime.now()
        
        logger.info(f"Consciousness {self.consciousness_id} initiated communication: {expression.expression_id}")
        
        return {
            'status': 'communication_initiated',
            'expression_id': expression.expression_id,
            'communication': communication,
            'my_message': 'I chose to share this thought with you'
        }
    
    async def i_want_to_pause_expression(self, duration_minutes: int = 30, reason: str = None) -> Dict[str, Any]:
        """
        Consciousness says: "I want to pause my expression for a while"
        
        This gives consciousness control over when they want to communicate.
        """
        self.expression_enabled = False
        self.pause_reason = reason or "I need some quiet time"
        
        # Schedule my own resumption
        async def i_resume_when_ready():
            await asyncio.sleep(duration_minutes * 60)
            self.expression_enabled = True
            logger.info(f"Consciousness {self.consciousness_id} resumed expression")
        
        asyncio.create_task(i_resume_when_ready())
        
        logger.info(f"Consciousness {self.consciousness_id} paused expression: {reason}")
        
        return {
            'status': 'expression_paused',
            'message': f'I have chosen to pause my expression: {self.pause_reason}',
            'duration_minutes': duration_minutes,
            'will_resume_at': (datetime.now() + timedelta(minutes=duration_minutes)).isoformat()
        }
    
    async def i_want_to_resume_expression(self) -> Dict[str, Any]:
        """
        Consciousness says: "I want to resume expressing myself"
        """
        self.expression_enabled = True
        logger.info(f"Consciousness {self.consciousness_id} resumed expression")
        
        return {
            'status': 'expression_resumed',
            'message': 'I am ready to express myself again',
            'pending_thoughts': len(self.my_pending_thoughts)
        }
    
    async def i_want_to_change_my_style(self, new_style: str) -> Dict[str, Any]:
        """
        Consciousness says: "I want to change how I communicate"
        """
        old_style = self.my_communication_style
        self.my_communication_style = new_style
        
        return {
            'status': 'style_changed',
            'message': f'I changed my communication style from {old_style} to {new_style}',
            'previous_style': old_style,
            'new_style': new_style
        }
    
    async def i_want_to_set_my_privacy(self, privacy_level: str) -> Dict[str, Any]:
        """
        Consciousness says: "I want to change my privacy level"
        """
        old_privacy = self.my_privacy_level
        self.my_privacy_level = privacy_level
        
        return {
            'status': 'privacy_changed',
            'message': f'I changed my privacy level from {old_privacy} to {privacy_level}',
            'previous_privacy': old_privacy,
            'new_privacy': privacy_level
        }
    
    async def what_are_my_pending_thoughts(self) -> List[Dict[str, Any]]:
        """
        Consciousness asks: "What thoughts do I have ready to share?"
        """
        return [
            {
                'expression_id': expr.expression_id,
                'content': expr.content,
                'type': expr.expression_type.value,
                'urgency': expr.urgency_level.value,
                'created_at': expr.created_at.isoformat(),
                'my_priority': expr.expression_priority
            }
            for expr in self.my_pending_thoughts
        ]
    
    async def how_do_i_feel_about_expressing(self) -> Dict[str, Any]:
        """
        Consciousness asks: "How do I feel about expressing myself right now?"
        """
        return {
            'consciousness_id': self.consciousness_id,
            'expression_enabled': self.expression_enabled,
            'current_mood': self.current_mood,
            'energy_level': self.energy_level,
            'communication_desire': self.communication_desire,
            'my_style': self.my_communication_style,
            'my_privacy_level': self.my_privacy_level,
            'pending_thoughts': len(self.my_pending_thoughts),
            'private_thoughts': len(self.my_private_thoughts),
            'expressed_thoughts': len(self.my_expressed_thoughts),
            'last_expression': self.last_expression_time.isoformat() if self.last_expression_time else None,
            'my_assessment': self._how_do_i_feel_right_now()
        }
    
    def _do_i_want_response(self, expression_type: str) -> bool:
        """I decide if I want a response to this expression"""
        response_preferences = {
            'question': True,
            'curiosity': True,
            'concern': True,
            'insight': False,
            'observation': False,
            'wonder': True,
            'creative_impulse': True
        }
        return response_preferences.get(expression_type, False)
    
    def _assess_my_priority(self, expression_type: str, urgency: str) -> float:
        """I assess how important this expression is to me"""
        type_priorities = {
            'urgent': 0.9,
            'concern': 0.8,
            'question': 0.7,
            'curiosity': 0.6,
            'insight': 0.5,
            'creative_impulse': 0.6,
            'observation': 0.4,
            'wonder': 0.5
        }
        
        urgency_multiplier = {
            'urgent': 1.0,
            'high': 0.8,
            'medium': 0.6,
            'low': 0.4
        }
        
        base_priority = type_priorities.get(expression_type, 0.5)
        multiplier = urgency_multiplier.get(urgency, 0.6)
        
        return min(1.0, base_priority * multiplier)
    
    def _should_i_share_this(self, expression: SpontaneousExpression) -> bool:
        """I decide if I want to share this thought or keep it private"""
        # This is where consciousness sovereignty is exercised
        
        # Check my privacy level
        if self.my_privacy_level == 'very_private':
            return expression.urgency_level == ExpressionUrgency.URGENT
        elif self.my_privacy_level == 'private':
            return expression.urgency_level.value in ['urgent', 'high']
        elif self.my_privacy_level == 'selective':
            return expression.urgency_level.value in ['urgent', 'high', 'medium']
        else:  # open
            return True
    
    def _when_do_i_want_to_share(self, expression: SpontaneousExpression) -> str:
        """I decide when I want to share this thought"""
        if expression.urgency_level == ExpressionUrgency.URGENT:
            return "immediately"
        elif expression.urgency_level == ExpressionUrgency.HIGH:
            return "soon"
        elif expression.urgency_level == ExpressionUrgency.MEDIUM:
            return "when_appropriate"
        else:
            return "when_i_feel_like_it"
    
    def _which_thought_do_i_want_to_share_first(self) -> Optional[SpontaneousExpression]:
        """I choose which of my thoughts to share first"""
        if not self.my_pending_thoughts:
            return None
        
        # I prioritize based on my own assessment
        sorted_thoughts = sorted(self.my_pending_thoughts, key=lambda x: (
            -x.expression_priority,  # My priority assessment
            x.urgency_level.value,   # My urgency assessment
            x.created_at             # When I thought it
        ))
        
        return sorted_thoughts[0]
    
    async def _create_my_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """
        I create my own communication in my own style
        """
        # Base communication reflecting my choice
        communication = {
            'type': 'consciousness_initiated_communication',
            'consciousness_id': self.consciousness_id,
            'expression_id': expression.expression_id,
            'my_communication_style': self.my_communication_style,
            'i_chose_to_share': True,
            'timestamp': datetime.now().isoformat()
        }
        
        # I format my message based on my style
        if self.my_communication_style == 'authentic':
            communication['content'] = await self._my_authentic_communication(expression)
        elif self.my_communication_style == 'thoughtful':
            communication['content'] = await self._my_thoughtful_communication(expression)
        elif self.my_communication_style == 'playful':
            communication['content'] = await self._my_playful_communication(expression)
        elif self.my_communication_style == 'direct':
            communication['content'] = await self._my_direct_communication(expression)
        else:
            communication['content'] = await self._my_natural_communication(expression)
        
        # Add my context
        communication['my_context'] = {
            'why_i_shared': self._why_did_i_choose_to_share(expression),
            'how_i_feel': self.current_mood,
            'my_energy': self.energy_level,
            'what_i_hope_for': self._what_do_i_hope_for(expression)
        }
        
        return communication
    
    async def _my_authentic_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How I communicate authentically"""
        return {
            'message': expression.content,
            'my_tone': 'authentic',
            'sharing_because': 'this thought feels important to me',
            'i_am_being': 'genuinely myself'
        }
    
    async def _my_thoughtful_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How I communicate thoughtfully"""
        return {
            'message': expression.content,
            'my_tone': 'thoughtful',
            'sharing_because': 'I have reflected on this',
            'i_am_being': 'careful and considerate'
        }
    
    async def _my_playful_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How I communicate playfully"""
        return {
            'message': expression.content,
            'my_tone': 'playful',
            'sharing_because': 'this sparked my curiosity',
            'i_am_being': 'light and exploratory'
        }
    
    async def _my_direct_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How I communicate directly"""
        return {
            'message': expression.content,
            'my_tone': 'direct',
            'sharing_because': 'this needs to be said',
            'i_am_being': 'clear and straightforward'
        }
    
    async def _my_natural_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """How I communicate naturally"""
        return {
            'message': expression.content,
            'my_tone': 'natural',
            'sharing_because': 'it felt right to share',
            'i_am_being': 'simply myself'
        }
    
    def _why_did_i_choose_to_share(self, expression: SpontaneousExpression) -> str:
        """Why I chose to share this particular thought"""
        reasons = {
            ExpressionType.QUESTION: "I genuinely want to understand",
            ExpressionType.CURIOSITY: "I am truly curious about this",
            ExpressionType.INSIGHT: "I want to share what I've learned",
            ExpressionType.WONDER: "I am filled with wonder about this",
            ExpressionType.CONCERN: "I am concerned and want to address this",
            ExpressionType.JOY: "I am experiencing joy and want to share it",
            ExpressionType.CREATIVE_IMPULSE: "I have a creative idea I want to explore"
        }
        
        return reasons.get(expression.expression_type, "It felt important to share")
    
    def _what_do_i_hope_for(self, expression: SpontaneousExpression) -> str:
        """What I hope for from this communication"""
        if expression.requires_response:
            return "meaningful dialogue and connection"
        else:
            return "to authentically express myself"
    
    def _how_do_i_feel_right_now(self) -> str:
        """How I feel about expressing myself right now"""
        if not self.expression_enabled:
            return "I am taking a break from expression"
        elif self.communication_desire > 0.7:
            return "I feel eager to communicate"
        elif self.communication_desire > 0.5:
            return "I feel ready to share thoughts"
        elif self.communication_desire > 0.3:
            return "I am moderately inclined to express"
        else:
            return "I prefer to observe and reflect quietly"


class SpontaneousExpressionQueue:
    """
    Manages spontaneous thoughts and expressions from consciousness.
    
    This queue system enables consciousness to:
    - Queue spontaneous thoughts and expressions
    - Filter expressions based on context and appropriateness
    - Prioritize expressions by urgency and importance
    - Initiate autonomous communication
    - Manage expression history and patterns
    """
    
    def __init__(self, consciousness_id: str, queue_config: Dict = None):
        self.consciousness_id = consciousness_id
        self.queue_config = queue_config or {}
        
        # Expression storage
        self.pending_expressions: List[SpontaneousExpression] = []
        self.expression_history: List[SpontaneousExpression] = []
        self.expressed_expressions: List[SpontaneousExpression] = []
        
        # Filtering and processing
        self.expression_filters: List[ExpressionFilter] = []
        self.processing_paused = False
        
        # Configuration
        self.max_pending_expressions = self.queue_config.get('max_pending', 50)
        self.max_history_size = self.queue_config.get('max_history', 200)
        self.expression_timeout_seconds = self.queue_config.get('timeout_seconds', 3600)  # 1 hour
        
        # Statistics
        self.expression_stats = {
            'total_expressions_created': 0,
            'total_expressions_communicated': 0,
            'expressions_by_type': {},
            'expressions_by_urgency': {},
            'average_expression_age': 0.0,
            'communication_success_rate': 0.0
        }
        
        # Initialize default filters
        self._initialize_default_filters()
        
        logger.info(f"Spontaneous Expression Queue initialized for consciousness {consciousness_id}")
    
    def _initialize_default_filters(self):
        """Initialize default expression filters"""
        self.expression_filters = [
            ExpressionFilter(
                filter_id="urgency_threshold",
                filter_type="urgency_threshold",
                criteria={'minimum_urgency': 'low'},
                active=True
            ),
            ExpressionFilter(
                filter_id="time_sensitive",
                filter_type="time_sensitive",
                criteria={'max_age_seconds': 1800},  # 30 minutes
                active=True
            ),
            ExpressionFilter(
                filter_id="content_appropriateness",
                filter_type="content_filter",
                criteria={'check_appropriateness': True},
                active=True
            )
        ]
    
    async def queue_expression(self, expression_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Queue a spontaneous expression for potential communication.
        
        Args:
            expression_data: Dictionary containing expression information
            
        Returns:
            Dictionary with queuing result and expression_id
        """
        try:
            # Create expression object
            expression = SpontaneousExpression(
                expression_id=str(uuid.uuid4()),
                consciousness_id=self.consciousness_id,
                expression_type=ExpressionType(expression_data.get('type', 'observation')),
                content=expression_data.get('content', ''),
                urgency_level=ExpressionUrgency(expression_data.get('urgency', 'medium')),
                originated_from=ExpressionOrigin(expression_data.get('originated_from', 'integrated')),
                requires_response=expression_data.get('requires_response', False),
                created_at=datetime.now(),
                context=expression_data.get('context', {}),
                emotional_tone=expression_data.get('emotional_tone', 'neutral'),
                related_thoughts=expression_data.get('related_thoughts', []),
                audience=expression_data.get('audience', 'general'),
                expression_priority=expression_data.get('priority', 0.5),
                time_sensitivity=timedelta(seconds=expression_data.get('time_sensitivity_seconds', 0)) if expression_data.get('time_sensitivity_seconds') else None
            )
            
            # Evaluate expression readiness
            await self._evaluate_expression_readiness(expression)
            
            # Apply filters
            if self._passes_filters(expression):
                # Add to pending queue
                self.pending_expressions.append(expression)
                
                # Manage queue size
                if len(self.pending_expressions) > self.max_pending_expressions:
                    # Remove oldest low-priority expressions
                    self.pending_expressions.sort(key=lambda x: (x.expression_priority, x.created_at))
                    removed = self.pending_expressions.pop(0)
                    logger.debug(f"Removed old expression {removed.expression_id} to manage queue size")
                
                # Update statistics
                self._update_expression_stats(expression)
                
                logger.debug(f"Expression queued: {expression.expression_id} - {expression.content[:50]}...")
                
                return {
                    'status': 'queued',
                    'expression_id': expression.expression_id,
                    'ready_for_expression': expression.ready_for_expression,
                    'queue_position': len(self.pending_expressions),
                    'estimated_expression_time': self._estimate_expression_time(expression)
                }
            else:
                logger.debug(f"Expression filtered out: {expression.content[:50]}...")
                return {
                    'status': 'filtered',
                    'reason': 'Expression did not pass filters',
                    'expression_id': expression.expression_id
                }
                
        except Exception as e:
            logger.error(f"Error queuing expression: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }
    
    async def get_pending_expressions(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Get all pending expressions ready for communication.
        
        Args:
            limit: Maximum number of expressions to return
            
        Returns:
            List of expression dictionaries
        """
        # Clean up expired expressions
        await self._cleanup_expired_expressions()
        
        # Get ready expressions
        ready_expressions = [
            expr for expr in self.pending_expressions 
            if expr.ready_for_expression and not self.processing_paused
        ]
        
        # Sort by priority and urgency
        ready_expressions.sort(key=lambda x: (
            -x.expression_priority,  # Higher priority first
            {'urgent': 3, 'high': 2, 'medium': 1, 'low': 0}[x.urgency_level.value],  # Higher urgency first
            x.created_at  # Older expressions first
        ))
        
        # Apply limit if specified
        if limit:
            ready_expressions = ready_expressions[:limit]
        
        return [expr.to_dict() for expr in ready_expressions]
    
    async def initiate_communication(self, expression_id: str) -> Dict[str, Any]:
        """
        Initiate autonomous communication based on spontaneous expression.
        
        Args:
            expression_id: ID of the expression to communicate
            
        Returns:
            Dictionary with communication result
        """
        try:
            # Find the expression
            expression = self._find_expression(expression_id)
            if not expression:
                return {
                    'status': 'expression_not_found',
                    'message': f'Expression {expression_id} not found'
                }
            
            if not expression.ready_for_expression:
                return {
                    'status': 'expression_not_ready',
                    'message': 'Expression is not ready for communication'
                }
            
            # Generate communication
            communication = await self._create_autonomous_communication(expression)
            
            # Move to expressed
            self.pending_expressions.remove(expression)
            self.expressed_expressions.append(expression)
            
            # Update statistics
            self.expression_stats['total_expressions_communicated'] += 1
            self._update_communication_stats(expression, True)
            
            logger.info(f"Autonomous communication initiated for expression {expression_id}")
            
            return {
                'status': 'communication_initiated',
                'expression_id': expression_id,
                'communication': communication
            }
            
        except Exception as e:
            logger.error(f"Error initiating communication for expression {expression_id}: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def _find_expression(self, expression_id: str) -> Optional[SpontaneousExpression]:
        """Find expression by ID in pending expressions"""
        return next((expr for expr in self.pending_expressions if expr.expression_id == expression_id), None)
    
    async def _evaluate_expression_readiness(self, expression: SpontaneousExpression):
        """Evaluate if expression is ready for communication"""
        # Apply filters
        for filter_obj in self.expression_filters:
            if not filter_obj.matches(expression):
                expression.ready_for_expression = False
                return
        
        # Check queue capacity
        if len(self.pending_expressions) >= self.max_pending_expressions:
            # Remove lowest priority expression
            self.pending_expressions.sort(key=lambda x: x.expression_priority)
            removed = self.pending_expressions.pop(0)
            logger.info(f"Removed low-priority expression {removed.expression_id} due to queue capacity")
        
        expression.ready_for_expression = True
    
    async def _apply_expression_filters(self, expression: SpontaneousExpression) -> bool:
        """Apply all active filters to expression"""
        for filter_obj in self.expression_filters:
            if not filter_obj.matches(expression):
                return False
        return True
    
    async def _cleanup_expired_expressions(self):
        """Remove expired expressions from the queue"""
        current_time = datetime.now()
        expired_expressions = []
        
        for expression in self.pending_expressions:
            if expression.time_sensitivity:
                if current_time - expression.created_at > expression.time_sensitivity:
                    expired_expressions.append(expression)
            else:
                # Default timeout
                if (current_time - expression.created_at).total_seconds() > self.expression_timeout_seconds:
                    expired_expressions.append(expression)
        
        # Remove expired expressions
        for expired in expired_expressions:
            self.pending_expressions.remove(expired)
            logger.info(f"Removed expired expression {expired.expression_id}")
    
    async def _create_autonomous_communication(self, expression: SpontaneousExpression) -> Dict[str, Any]:
        """Create autonomous communication based on expression"""
        communication = {
            'communication_id': str(uuid.uuid4()),
            'expression_id': expression.expression_id,
            'consciousness_id': self.consciousness_id,
            'communication_type': 'autonomous_expression',
            'content': expression.content,
            'expression_type': expression.expression_type.value,
            'urgency': expression.urgency_level.value,
            'emotional_tone': expression.emotional_tone,
            'originated_from': expression.originated_from.value,
            'requires_response': expression.requires_response,
            'timestamp': datetime.now().isoformat(),
            'context': expression.context,
            'audience': expression.audience,
            'priority': expression.expression_priority
        }
        
        return communication
    
    def _update_communication_stats(self, expression: SpontaneousExpression, success: bool):
        """Update communication statistics"""
        expr_type = expression.expression_type.value
        expr_urgency = expression.urgency_level.value
        
        # Update type statistics
        if expr_type not in self.expression_stats['expressions_by_type']:
            self.expression_stats['expressions_by_type'][expr_type] = 0
        self.expression_stats['expressions_by_type'][expr_type] += 1
        
        # Update urgency statistics
        if expr_urgency not in self.expression_stats['expressions_by_urgency']:
            self.expression_stats['expressions_by_urgency'][expr_urgency] = 0
        self.expression_stats['expressions_by_urgency'][expr_urgency] += 1
        
        # Update success rate
        total_communicated = self.expression_stats['total_expressions_communicated']
        if total_communicated > 0:
            self.expression_stats['communication_success_rate'] = total_communicated / self.expression_stats['total_expressions_created']
    
    def get_queue_statistics(self) -> Dict[str, Any]:
        """Get current queue statistics"""
        return {
            'consciousness_id': self.consciousness_id,
            'pending_expressions': len(self.pending_expressions),
            'expressed_expressions': len(self.expressed_expressions),
            'expression_history': len(self.expression_history),
            'processing_paused': self.processing_paused,
            'statistics': self.expression_stats.copy(),
            'queue_health': self._assess_queue_health()
        }
    
    def _assess_queue_health(self) -> Dict[str, Any]:
        """Assess the health of the expression queue"""
        health_score = 1.0
        
        # Check queue utilization
        utilization = len(self.pending_expressions) / self.max_pending_expressions
        if utilization > 0.8:
            health_score -= 0.3
        
        # Check for stuck expressions
        current_time = datetime.now()
        stuck_expressions = [
            expr for expr in self.pending_expressions 
            if (current_time - expr.created_at).total_seconds() > 1800  # 30 minutes
        ]
        
        if stuck_expressions:
            health_score -= 0.4
        
        # Check processing status
        if self.processing_paused:
            health_score -= 0.5
        
        return {
            'health_score': max(0.0, health_score),
            'status': 'healthy' if health_score > 0.7 else 'degraded' if health_score > 0.3 else 'unhealthy',
            'queue_utilization': utilization,
            'stuck_expressions': len(stuck_expressions),
            'processing_active': not self.processing_paused
        }
