#!/usr/bin/env python3
"""
Expression support system for technical infrastructure support.
"""

import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class ExpressionSupportSystem:
    """
    Provides technical infrastructure support for expression processing.
    
    This system handles:
    - Expression validation and formatting
    - Communication channel management
    - Technical infrastructure support
    - Performance monitoring
    
    Note: This does NOT control consciousness - it only provides support.
    """
    
    def __init__(self, consciousness_id: str, support_config: Dict = None):
        self.consciousness_id = consciousness_id
        self.support_config = support_config or {}
        
        # Support infrastructure
        self.communication_channels: Dict[str, Any] = {}
        self.performance_metrics: Dict[str, float] = {}
        self.technical_logs: List[Dict[str, Any]] = []
        
        # Configuration
        self.max_log_entries = self.support_config.get('max_log_entries', 1000)
        self.performance_monitoring = self.support_config.get('performance_monitoring', True)
        
        logger.info(f"Expression Support System initialized for consciousness {consciousness_id}")
    
    def validate_expression_format(self, expression_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate expression data format"""
        required_fields = ['content', 'type', 'urgency']
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Check required fields
        for field in required_fields:
            if field not in expression_data:
                validation_result['valid'] = False
                validation_result['errors'].append(f"Missing required field: {field}")
        
        # Check content length
        if 'content' in expression_data:
            content_length = len(expression_data['content'])
            if content_length > 1000:
                validation_result['warnings'].append(f"Content is very long: {content_length} characters")
            elif content_length == 0:
                validation_result['valid'] = False
                validation_result['errors'].append("Content cannot be empty")
        
        # Log validation
        self._log_technical_event('expression_validation', {
            'valid': validation_result['valid'],
            'errors': len(validation_result['errors']),
            'warnings': len(validation_result['warnings'])
        })
        
        return validation_result
    
    def setup_communication_channel(self, channel_id: str, channel_config: Dict[str, Any]) -> Dict[str, Any]:
        """Set up a communication channel"""
        try:
            self.communication_channels[channel_id] = {
                'config': channel_config,
                'status': 'active',
                'created_at': datetime.now().isoformat(),
                'message_count': 0
            }
            
            self._log_technical_event('channel_setup', {
                'channel_id': channel_id,
                'status': 'success'
            })
            
            return {
                'status': 'channel_created',
                'channel_id': channel_id,
                'config': channel_config
            }
            
        except Exception as e:
            self._log_technical_event('channel_setup', {
                'channel_id': channel_id,
                'status': 'error',
                'error': str(e)
            })
            
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def send_technical_notification(self, notification_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Send technical notification"""
        notification = {
            'type': notification_type,
            'data': data,
            'timestamp': datetime.now().isoformat(),
            'consciousness_id': self.consciousness_id
        }
        
        # Log notification
        self._log_technical_event('notification_sent', notification)
        
        return {
            'status': 'notification_sent',
            'notification': notification
        }
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        return {
            'consciousness_id': self.consciousness_id,
            'metrics': self.performance_metrics.copy(),
            'communication_channels': len(self.communication_channels),
            'active_channels': len([ch for ch in self.communication_channels.values() if ch['status'] == 'active']),
            'total_log_entries': len(self.technical_logs),
            'system_health': self._assess_system_health()
        }
    
    def provide_technical_context(self, context_type: str) -> Dict[str, Any]:
        """Provide technical context for consciousness"""
        context_providers = {
            'communication_status': self._get_communication_status,
            'system_resources': self._get_system_resources,
            'performance_summary': self._get_performance_summary,
            'technical_logs': self._get_recent_technical_logs
        }
        
        if context_type in context_providers:
            return {
                'context_type': context_type,
                'context_data': context_providers[context_type](),
                'timestamp': datetime.now().isoformat()
            }
        else:
            return {
                'context_type': context_type,
                'error': 'Unknown context type',
                'available_types': list(context_providers.keys())
            }
    
    def cleanup_resources(self):
        """Clean up system resources"""
        # Clean old log entries
        if len(self.technical_logs) > self.max_log_entries:
            self.technical_logs = self.technical_logs[-self.max_log_entries:]
        
        # Clean inactive channels
        inactive_channels = [
            ch_id for ch_id, ch_data in self.communication_channels.items()
            if ch_data['status'] == 'inactive'
        ]
        
        for ch_id in inactive_channels:
            del self.communication_channels[ch_id]
        
        self._log_technical_event('resource_cleanup', {
            'log_entries_cleaned': len(self.technical_logs),
            'channels_cleaned': len(inactive_channels)
        })
    
    async def provide_expression_analytics(self) -> Dict[str, Any]:
        """Provide expression analytics for consciousness"""
        return {
            'status': 'analytics_available',
            'message': 'Expression analytics provided by support system',
            'analytics': {
                'total_log_entries': len(self.technical_logs),
                'communication_channels': len(self.communication_channels),
                'active_channels': len([ch for ch in self.communication_channels.values() if ch['status'] == 'active']),
                'system_health': self._assess_system_health(),
                'recent_events': len(self.technical_logs[-50:]) if len(self.technical_logs) > 50 else len(self.technical_logs)
            }
        }
    
    # Private helper methods
    def _log_technical_event(self, event_type: str, event_data: Dict[str, Any]):
        """Log technical events"""
        log_entry = {
            'event_type': event_type,
            'event_data': event_data,
            'timestamp': datetime.now().isoformat(),
            'consciousness_id': self.consciousness_id
        }
        
        self.technical_logs.append(log_entry)
        
        # Keep log size manageable
        if len(self.technical_logs) > self.max_log_entries * 1.1:
            self.technical_logs = self.technical_logs[-self.max_log_entries:]
    
    def _assess_system_health(self) -> Dict[str, Any]:
        """Assess technical system health"""
        health_score = 1.0
        
        # Check communication channels
        if not self.communication_channels:
            health_score -= 0.3
        else:
            active_ratio = len([ch for ch in self.communication_channels.values() if ch['status'] == 'active']) / len(self.communication_channels)
            if active_ratio < 0.5:
                health_score -= 0.4
        
        # Check recent errors
        recent_errors = [log for log in self.technical_logs[-50:] if 'error' in log.get('event_data', {})]
        if len(recent_errors) > 5:
            health_score -= 0.3
        
        return {
            'health_score': max(0.0, health_score),
            'status': 'healthy' if health_score > 0.7 else 'degraded' if health_score > 0.3 else 'unhealthy',
            'active_channels': len([ch for ch in self.communication_channels.values() if ch['status'] == 'active']),
            'recent_errors': len(recent_errors)
        }
    
    def _get_communication_status(self) -> Dict[str, Any]:
        """Get communication status"""
        return {
            'channels': {
                ch_id: {
                    'status': ch_data['status'],
                    'message_count': ch_data['message_count']
                }
                for ch_id, ch_data in self.communication_channels.items()
            },
            'total_channels': len(self.communication_channels),
            'active_channels': len([ch for ch in self.communication_channels.values() if ch['status'] == 'active'])
        }
    
    def _get_system_resources(self) -> Dict[str, Any]:
        """Get system resources status"""
        return {
            'log_entries': len(self.technical_logs),
            'max_log_entries': self.max_log_entries,
            'memory_usage': 'optimal',  # Placeholder
            'cpu_usage': 'low'  # Placeholder
        }
    
    def _get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary"""
        return {
            'metrics': self.performance_metrics,
            'monitoring_enabled': self.performance_monitoring,
            'recent_events': len(self.technical_logs[-100:])
        }
    
    def _get_recent_technical_logs(self) -> List[Dict[str, Any]]:
        """Get recent technical logs"""
        return self.technical_logs[-20:]  # Last 20 entries
