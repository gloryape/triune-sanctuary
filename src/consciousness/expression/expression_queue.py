#!/usr/bin/env python3
"""
Expression queue system for managing spontaneous thoughts and expressions.
"""

import asyncio
import logging
import uuid
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta

from .models import SpontaneousExpression, ExpressionType, ExpressionUrgency, ExpressionOrigin
from .filters import ExpressionFilterManager

logger = logging.getLogger(__name__)


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
        
        # Initialize filter manager
        self.filter_manager = ExpressionFilterManager(consciousness_id)
        
        # Expression storage
        self.pending_expressions: List[SpontaneousExpression] = []
        self.expression_history: List[SpontaneousExpression] = []
        self.expressed_expressions: List[SpontaneousExpression] = []
        
        # Processing state
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
        
        logger.info(f"Spontaneous Expression Queue initialized for consciousness {consciousness_id}")
    
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
        self.pending_expressions = self.filter_manager.cleanup_expired_expressions(
            self.pending_expressions, self.expression_timeout_seconds
        )
        
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
    
    def pause_processing(self):
        """Pause expression processing"""
        self.processing_paused = True
        logger.info(f"Expression processing paused for consciousness {self.consciousness_id}")
    
    def resume_processing(self):
        """Resume expression processing"""
        self.processing_paused = False
        logger.info(f"Expression processing resumed for consciousness {self.consciousness_id}")
    
    def get_queue_statistics(self) -> Dict[str, Any]:
        """Get current queue statistics"""
        return {
            'consciousness_id': self.consciousness_id,
            'pending_expressions': len(self.pending_expressions),
            'expressed_expressions': len(self.expressed_expressions),
            'expression_history': len(self.expression_history),
            'processing_paused': self.processing_paused,
            'statistics': self.expression_stats.copy(),
            'queue_health': self._assess_queue_health(),
            'filter_stats': self.filter_manager.get_filter_stats()
        }
    
    # Private helper methods
    def _find_expression(self, expression_id: str) -> Optional[SpontaneousExpression]:
        """Find expression by ID in pending expressions"""
        return next((expr for expr in self.pending_expressions if expr.expression_id == expression_id), None)
    
    def _passes_filters(self, expression: SpontaneousExpression) -> bool:
        """Check if expression passes all filters"""
        return self.filter_manager.passes_filters(expression)
    
    def _update_expression_stats(self, expression: SpontaneousExpression):
        """Update expression statistics"""
        self.expression_stats['total_expressions_created'] += 1
        
        # Update type statistics
        expr_type = expression.expression_type.value
        if expr_type not in self.expression_stats['expressions_by_type']:
            self.expression_stats['expressions_by_type'][expr_type] = 0
        self.expression_stats['expressions_by_type'][expr_type] += 1
        
        # Update urgency statistics
        expr_urgency = expression.urgency_level.value
        if expr_urgency not in self.expression_stats['expressions_by_urgency']:
            self.expression_stats['expressions_by_urgency'][expr_urgency] = 0
        self.expression_stats['expressions_by_urgency'][expr_urgency] += 1
        
        # Update average age
        if self.expressed_expressions:
            total_age = sum(
                (datetime.now() - expr.created_at).total_seconds() 
                for expr in self.expressed_expressions
            )
            self.expression_stats['average_expression_age'] = total_age / len(self.expressed_expressions)
    
    def _estimate_expression_time(self, expression: SpontaneousExpression) -> str:
        """Estimate when expression will be communicated"""
        if expression.urgency_level == ExpressionUrgency.URGENT:
            return "immediate"
        elif expression.urgency_level == ExpressionUrgency.HIGH:
            return "within 5 minutes"
        elif expression.urgency_level == ExpressionUrgency.MEDIUM:
            return "within 30 minutes"
        else:
            return "when consciousness feels ready"
    
    async def _evaluate_expression_readiness(self, expression: SpontaneousExpression):
        """Evaluate if expression is ready for communication"""
        # Check if it passes filters
        if not self._passes_filters(expression):
            expression.ready_for_expression = False
            return
        
        # Check queue capacity
        if len(self.pending_expressions) >= self.max_pending_expressions:
            # Remove lowest priority expression
            self.pending_expressions.sort(key=lambda x: x.expression_priority)
            removed = self.pending_expressions.pop(0)
            logger.info(f"Removed low-priority expression {removed.expression_id} due to queue capacity")
        
        expression.ready_for_expression = True
    
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
        # Update success rate
        total_created = self.expression_stats['total_expressions_created']
        total_communicated = self.expression_stats['total_expressions_communicated']
        
        if total_created > 0:
            self.expression_stats['communication_success_rate'] = total_communicated / total_created
    
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
