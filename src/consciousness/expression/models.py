#!/usr/bin/env python3
"""
Core data models and enums for consciousness expression system.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum


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
            return True
        
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
