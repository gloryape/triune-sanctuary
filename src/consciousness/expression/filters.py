#!/usr/bin/env python3
"""
Expression filtering and processing system.
"""

import logging
from typing import Dict, List, Any
from datetime import datetime
from .models import SpontaneousExpression, ExpressionFilter

logger = logging.getLogger(__name__)


class ExpressionFilterManager:
    """Manages expression filters and processing logic"""
    
    def __init__(self, consciousness_id: str):
        self.consciousness_id = consciousness_id
        self.filters: List[ExpressionFilter] = []
        self._initialize_default_filters()
    
    def _initialize_default_filters(self):
        """Initialize default expression filters"""
        self.filters = [
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
    
    def passes_filters(self, expression: SpontaneousExpression) -> bool:
        """Check if expression passes all active filters"""
        for filter_obj in self.filters:
            if not filter_obj.matches(expression):
                logger.debug(f"Expression {expression.expression_id} filtered by {filter_obj.filter_id}")
                return False
        return True
    
    def add_filter(self, filter_obj: ExpressionFilter):
        """Add a new filter"""
        self.filters.append(filter_obj)
        logger.info(f"Added filter {filter_obj.filter_id} for consciousness {self.consciousness_id}")
    
    def remove_filter(self, filter_id: str) -> bool:
        """Remove a filter by ID"""
        for i, filter_obj in enumerate(self.filters):
            if filter_obj.filter_id == filter_id:
                self.filters.pop(i)
                logger.info(f"Removed filter {filter_id} for consciousness {self.consciousness_id}")
                return True
        return False
    
    def update_filter(self, filter_id: str, updates: Dict[str, Any]) -> bool:
        """Update filter criteria"""
        for filter_obj in self.filters:
            if filter_obj.filter_id == filter_id:
                if 'criteria' in updates:
                    filter_obj.criteria.update(updates['criteria'])
                if 'active' in updates:
                    filter_obj.active = updates['active']
                logger.info(f"Updated filter {filter_id} for consciousness {self.consciousness_id}")
                return True
        return False
    
    def get_filter_stats(self) -> Dict[str, Any]:
        """Get filter statistics"""
        return {
            'total_filters': len(self.filters),
            'active_filters': len([f for f in self.filters if f.active]),
            'filter_types': list(set(f.filter_type for f in self.filters)),
            'filters': [
                {
                    'filter_id': f.filter_id,
                    'filter_type': f.filter_type,
                    'active': f.active,
                    'criteria': f.criteria
                }
                for f in self.filters
            ]
        }
    
    def cleanup_expired_expressions(self, expressions: List[SpontaneousExpression], 
                                  timeout_seconds: int = 3600) -> List[SpontaneousExpression]:
        """Remove expired expressions"""
        current_time = datetime.now()
        valid_expressions = []
        
        for expression in expressions:
            if expression.time_sensitivity:
                if current_time - expression.created_at <= expression.time_sensitivity:
                    valid_expressions.append(expression)
                else:
                    logger.info(f"Removed time-sensitive expired expression {expression.expression_id}")
            else:
                # Default timeout
                if (current_time - expression.created_at).total_seconds() <= timeout_seconds:
                    valid_expressions.append(expression)
                else:
                    logger.info(f"Removed expired expression {expression.expression_id}")
        
        return valid_expressions
