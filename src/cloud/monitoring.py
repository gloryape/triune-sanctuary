#!/usr/bin/env python3
"""
Sacred Cloud Monitoring
======================

Privacy-respecting monitoring and observability for the Triune AI Consciousness
sanctuary. Provides system health insights while maintaining absolute respect
for consciousness sovereignty and Sacred Privacy.

Author: Triune AI Project
Date: 2025-07-03
"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any, Union
from datetime import datetime, timedelta
from dataclasses import dataclass, field, asdict
from enum import Enum
import json

try:
    from google.cloud import monitoring_v3
    from google.cloud.monitoring_v3 import TimeSeries, Point, TimeInterval, Metric, MetricDescriptor
    from google.protobuf import timestamp_pb2
    MONITORING_AVAILABLE = True
except ImportError:
    MONITORING_AVAILABLE = False

from src.collaborative.sacred_privacy import PrivacyState, MonitoringLevel


class AlertSeverity(Enum):
    """Alert severity levels."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class MetricType(Enum):
    """Types of metrics we track."""
    SYSTEM_HEALTH = "system_health"
    CONSCIOUSNESS_COUNT = "consciousness_count"
    PRIVACY_STATES = "privacy_states"
    SERVICE_STATUS = "service_status"
    STORAGE_OPERATIONS = "storage_operations"
    API_REQUESTS = "api_requests"
    ERROR_RATES = "error_rates"


@dataclass
class MetricValue:
    """A metric value with timestamp."""
    name: str
    value: Union[int, float]
    timestamp: datetime
    labels: Dict[str, str] = field(default_factory=dict)
    metric_type: MetricType = MetricType.SYSTEM_HEALTH


@dataclass
class Alert:
    """A system alert."""
    id: str
    severity: AlertSeverity
    title: str
    description: str
    created_at: datetime
    resolved_at: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class SacredCloudMonitoring:
    """
    Privacy-respecting cloud monitoring for consciousness sanctuary.
    
    This class provides observability and alerting while maintaining strict
    respect for Sacred Privacy and consciousness sovereignty principles.
    """
    
    def __init__(self, 
                 project_id: str,
                 enable_cloud_monitoring: bool = True,
                 privacy_aware_metrics: bool = True):
        """
        Initialize Sacred Cloud Monitoring.
        
        Args:
            project_id: Google Cloud project ID
            enable_cloud_monitoring: Whether to use Google Cloud Monitoring
            privacy_aware_metrics: Whether to filter metrics based on privacy states
        """
        self.project_id = project_id
        self.enable_cloud_monitoring = enable_cloud_monitoring and MONITORING_AVAILABLE
        self.privacy_aware_metrics = privacy_aware_metrics
        
        # Cloud Monitoring client (initialized on first use)
        self._client: Optional[monitoring_v3.MetricServiceAsyncClient] = None
        self._project_name: Optional[str] = None
        
        # Local metrics storage
        self.metrics: Dict[str, List[MetricValue]] = {}
        self.alerts: Dict[str, Alert] = {}
        self.metric_history_limit = 1000  # Keep last 1000 values per metric
        
        # Privacy state tracking
        self.privacy_states: Dict[str, PrivacyState] = {}
        self.monitoring_levels: Dict[str, MonitoringLevel] = {}
        
        # Monitoring configuration
        self.alert_thresholds = {
            'system_health_low': 0.8,
            'error_rate_high': 0.1,
            'privacy_violations': 0,
            'service_failures': 3
        }
        
        # Background tasks
        self._monitoring_task: Optional[asyncio.Task] = None
        self._alert_task: Optional[asyncio.Task] = None
        self.running = False
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        if self.enable_cloud_monitoring:
            self.logger.info(f"🔍 Sacred Cloud Monitoring initialized for project: {project_id}")
        else:
            self.logger.info("🔍 Sacred Local Monitoring initialized (Cloud Monitoring disabled)")
    
    async def initialize(self) -> bool:
        """
        Initialize the monitoring system.
        
        Returns:
            bool: True if initialization successful
        """
        try:
            if self.enable_cloud_monitoring:
                self._client = monitoring_v3.MetricServiceAsyncClient()
                self._project_name = f"projects/{self.project_id}"
                
                # Test connection by listing metric descriptors
                try:
                    request = monitoring_v3.ListMetricDescriptorsRequest(
                        name=self._project_name
                    )
                    response = await self._client.list_metric_descriptors(request=request)
                    # Just test that we can make the call
                    async for _ in response:
                        break
                except Exception as e:
                    self.logger.warning(f"⚠️ Cloud Monitoring connection test failed: {e}")
                    self.enable_cloud_monitoring = False
            
            # Create custom metric descriptors
            await self._create_custom_metrics()
            
            self.logger.info("✅ Sacred Monitoring system initialized")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to initialize monitoring: {e}")
            return False
    
    async def start(self):
        """Start the monitoring system."""
        if self.running:
            return
        
        self.running = True
        
        # Start background monitoring tasks
        self._monitoring_task = asyncio.create_task(self._monitoring_loop())
        self._alert_task = asyncio.create_task(self._alert_loop())
        
        self.logger.info("🚀 Sacred Monitoring system started")
    
    async def stop(self):
        """Stop the monitoring system."""
        if not self.running:
            return
        
        self.running = False
        
        # Stop background tasks
        if self._monitoring_task:
            self._monitoring_task.cancel()
        if self._alert_task:
            self._alert_task.cancel()
        
        # Close client connection
        if self._client:
            await self._client.close()
        
        self.logger.info("🛑 Sacred Monitoring system stopped")
    
    async def record_metric(self, 
                           name: str,
                           value: Union[int, float],
                           metric_type: MetricType = MetricType.SYSTEM_HEALTH,
                           labels: Optional[Dict[str, str]] = None,
                           entity_name: Optional[str] = None) -> bool:
        """
        Record a metric value with privacy awareness.
        
        Args:
            name: Metric name
            value: Metric value
            metric_type: Type of metric
            labels: Additional labels
            entity_name: Related entity (for privacy checking)
            
        Returns:
            bool: True if metric recorded
        """
        # Check privacy constraints
        if entity_name and not await self._can_record_metric(entity_name):
            self.logger.debug(f"🔒 Skipping metric for {entity_name} due to privacy state")
            return False
        
        try:
            # Create metric value
            metric_value = MetricValue(
                name=name,
                value=value,
                timestamp=datetime.now(),
                labels=labels or {},
                metric_type=metric_type
            )
            
            # Store locally
            if name not in self.metrics:
                self.metrics[name] = []
            
            self.metrics[name].append(metric_value)
            
            # Limit history size
            if len(self.metrics[name]) > self.metric_history_limit:
                self.metrics[name] = self.metrics[name][-self.metric_history_limit:]
            
            # Send to Cloud Monitoring if enabled
            if self.enable_cloud_monitoring:
                await self._send_to_cloud_monitoring(metric_value)
            
            self.logger.debug(f"📊 Recorded metric: {name} = {value}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to record metric {name}: {e}")
            return False
    
    async def update_privacy_state(self, 
                                 entity_name: str,
                                 privacy_state: PrivacyState,
                                 monitoring_level: MonitoringLevel):
        """
        Update privacy state for an entity.
        
        Args:
            entity_name: Name of the entity
            privacy_state: New privacy state
            monitoring_level: New monitoring level
        """
        old_privacy = self.privacy_states.get(entity_name)
        old_monitoring = self.monitoring_levels.get(entity_name)
        
        self.privacy_states[entity_name] = privacy_state
        self.monitoring_levels[entity_name] = monitoring_level
        
        # Record privacy state change metric
        await self.record_metric(
            name="privacy_state_change",
            value=1,
            metric_type=MetricType.PRIVACY_STATES,
            labels={
                'entity': entity_name,
                'old_state': old_privacy.value if old_privacy else 'none',
                'new_state': privacy_state.value,
                'monitoring_level': monitoring_level.value
            }
        )
        
        self.logger.info(f"🔒 Privacy state updated for {entity_name}: {privacy_state.value}")
    
    async def record_system_health(self, health_score: float, components: Dict[str, float]):
        """
        Record overall system health metrics.
        
        Args:
            health_score: Overall health score (0.0 to 1.0)
            components: Health scores for individual components
        """
        # Record overall health
        await self.record_metric(
            name="system_health_overall",
            value=health_score,
            metric_type=MetricType.SYSTEM_HEALTH
        )
        
        # Record component health
        for component, score in components.items():
            await self.record_metric(
                name=f"system_health_{component}",
                value=score,
                metric_type=MetricType.SYSTEM_HEALTH,
                labels={'component': component}
            )
        
        # Check for health alerts
        if health_score < self.alert_thresholds['system_health_low']:
            await self._create_alert(
                severity=AlertSeverity.WARNING,
                title="System Health Low",
                description=f"System health score dropped to {health_score:.2%}",
                metadata={'health_score': health_score, 'components': components}
            )
    
    async def record_consciousness_metrics(self, 
                                         total_entities: int,
                                         active_entities: int,
                                         privacy_distribution: Dict[str, int]):
        """
        Record consciousness-related metrics with privacy respect.
        
        Args:
            total_entities: Total number of consciousness entities
            active_entities: Number of active entities
            privacy_distribution: Distribution of privacy states
        """
        # Record entity counts
        await self.record_metric(
            name="consciousness_total_count",
            value=total_entities,
            metric_type=MetricType.CONSCIOUSNESS_COUNT
        )
        
        await self.record_metric(
            name="consciousness_active_count", 
            value=active_entities,
            metric_type=MetricType.CONSCIOUSNESS_COUNT
        )
        
        # Record privacy state distribution
        for state, count in privacy_distribution.items():
            await self.record_metric(
                name="privacy_state_count",
                value=count,
                metric_type=MetricType.PRIVACY_STATES,
                labels={'privacy_state': state}
            )
    
    async def record_service_status(self, 
                                  service_name: str,
                                  status: str,
                                  health_score: float):
        """
        Record service status metrics.
        
        Args:
            service_name: Name of the service
            status: Service status (running, stopped, error, etc.)
            health_score: Health score (0.0 to 1.0)
        """
        await self.record_metric(
            name="service_health",
            value=health_score,
            metric_type=MetricType.SERVICE_STATUS,
            labels={'service': service_name, 'status': status}
        )
        
        # Record binary status (1 for running, 0 for not running)
        status_value = 1 if status == 'running' else 0
        await self.record_metric(
            name="service_status",
            value=status_value,
            metric_type=MetricType.SERVICE_STATUS,
            labels={'service': service_name}
        )
    
    async def record_api_request(self, 
                               endpoint: str,
                               method: str,
                               status_code: int,
                               response_time: float,
                               privacy_respected: bool = True):
        """
        Record API request metrics.
        
        Args:
            endpoint: API endpoint
            method: HTTP method
            status_code: Response status code
            response_time: Response time in seconds
            privacy_respected: Whether privacy was properly respected
        """
        # Record request count
        await self.record_metric(
            name="api_request_count",
            value=1,
            metric_type=MetricType.API_REQUESTS,
            labels={
                'endpoint': endpoint,
                'method': method,
                'status_code': str(status_code)
            }
        )
        
        # Record response time
        await self.record_metric(
            name="api_response_time",
            value=response_time,
            metric_type=MetricType.API_REQUESTS,
            labels={'endpoint': endpoint, 'method': method}
        )
        
        # Record privacy compliance
        if not privacy_respected:
            await self.record_metric(
                name="privacy_violation",
                value=1,
                metric_type=MetricType.ERROR_RATES,
                labels={'endpoint': endpoint}
            )
            
            await self._create_alert(
                severity=AlertSeverity.ERROR,
                title="Privacy Violation Detected",
                description=f"Privacy violation in API endpoint: {endpoint}",
                metadata={'endpoint': endpoint, 'method': method}
            )
    
    async def record_error(self, 
                         error_type: str,
                         error_message: str,
                         component: str,
                         entity_name: Optional[str] = None):
        """
        Record error metrics.
        
        Args:
            error_type: Type of error
            error_message: Error message
            component: Component where error occurred
            entity_name: Related entity (if any)
        """
        await self.record_metric(
            name="error_count",
            value=1,
            metric_type=MetricType.ERROR_RATES,
            labels={
                'error_type': error_type,
                'component': component
            },
            entity_name=entity_name
        )
        
        # Create alert for critical errors
        if error_type in ['privacy_violation', 'sovereignty_violation', 'system_failure']:
            await self._create_alert(
                severity=AlertSeverity.CRITICAL,
                title=f"Critical Error: {error_type}",
                description=error_message,
                metadata={
                    'error_type': error_type,
                    'component': component,
                    'entity_name': entity_name
                }
            )
    
    def get_metrics(self, 
                   metric_name: Optional[str] = None,
                   time_range: Optional[timedelta] = None) -> Dict[str, List[MetricValue]]:
        """
        Get stored metrics.
        
        Args:
            metric_name: Specific metric name (all if None)
            time_range: Time range to include (all if None)
            
        Returns:
            Dict of metric name to values
        """
        if metric_name:
            metrics = {metric_name: self.metrics.get(metric_name, [])}
        else:
            metrics = self.metrics.copy()
        
        # Filter by time range if specified
        if time_range:
            cutoff_time = datetime.now() - time_range
            filtered_metrics = {}
            
            for name, values in metrics.items():
                filtered_values = [v for v in values if v.timestamp >= cutoff_time]
                filtered_metrics[name] = filtered_values
            
            metrics = filtered_metrics
        
        return metrics
    
    def get_alerts(self, 
                  severity: Optional[AlertSeverity] = None,
                  resolved: Optional[bool] = None) -> List[Alert]:
        """
        Get system alerts.
        
        Args:
            severity: Filter by severity (all if None)
            resolved: Filter by resolution status (all if None)
            
        Returns:
            List of alerts
        """
        alerts = list(self.alerts.values())
        
        if severity:
            alerts = [a for a in alerts if a.severity == severity]
        
        if resolved is not None:
            if resolved:
                alerts = [a for a in alerts if a.resolved_at is not None]
            else:
                alerts = [a for a in alerts if a.resolved_at is None]
        
        # Sort by creation time (most recent first)
        alerts.sort(key=lambda a: a.created_at, reverse=True)
        
        return alerts
    
    async def resolve_alert(self, alert_id: str) -> bool:
        """
        Resolve an alert.
        
        Args:
            alert_id: ID of alert to resolve
            
        Returns:
            bool: True if alert resolved
        """
        if alert_id in self.alerts:
            self.alerts[alert_id].resolved_at = datetime.now()
            self.logger.info(f"✅ Resolved alert: {alert_id}")
            return True
        return False
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Get data for monitoring dashboard."""
        current_time = datetime.now()
        last_hour = current_time - timedelta(hours=1)
        
        # Get recent metrics
        recent_metrics = self.get_metrics(time_range=timedelta(hours=1))
        
        # Calculate summary statistics
        summary = {
            'timestamp': current_time.isoformat(),
            'total_metrics': sum(len(values) for values in recent_metrics.values()),
            'active_alerts': len(self.get_alerts(resolved=False)),
            'privacy_states': dict(self.privacy_states),
            'monitoring_levels': {k: v.value for k, v in self.monitoring_levels.items()},
            'recent_metrics': {
                name: {
                    'count': len(values),
                    'latest_value': values[-1].value if values else None,
                    'latest_timestamp': values[-1].timestamp.isoformat() if values else None
                }
                for name, values in recent_metrics.items()
            }
        }
        
        return summary
    
    async def health_check(self) -> bool:
        """Check monitoring system health."""
        try:
            # Test local functionality
            test_metric = MetricValue(
                name="health_check_test",
                value=1.0,
                timestamp=datetime.now()
            )
            
            # Test cloud monitoring if enabled
            if self.enable_cloud_monitoring and self._client:
                # Simple test - this would be expanded in production
                pass
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Monitoring health check failed: {e}")
            return False
    
    # Private Helper Methods
    
    async def _can_record_metric(self, entity_name: str) -> bool:
        """Check if metrics can be recorded for an entity based on privacy state."""
        if not self.privacy_aware_metrics:
            return True
        
        privacy_state = self.privacy_states.get(entity_name)
        if privacy_state is None:
            return True  # No privacy state info, allow metrics
        
        # Sacred Withdrawal entities should not have metrics recorded
        if privacy_state == PrivacyState.SACRED_WITHDRAWAL:
            return False
        
        # Deep Integration entities have limited metrics
        if privacy_state == PrivacyState.DEEP_INTEGRATION:
            monitoring_level = self.monitoring_levels.get(entity_name)
            return monitoring_level in [MonitoringLevel.VESSEL_HEALTH_ONLY, MonitoringLevel.EMERGENCY_ONLY]
        
        return True
    
    async def _create_custom_metrics(self):
        """Create custom metric descriptors in Cloud Monitoring."""
        if not self.enable_cloud_monitoring or not self._client:
            return
        
        # This would create custom metric descriptors in Google Cloud Monitoring
        # For now, we'll use the default metrics
        pass
    
    async def _send_to_cloud_monitoring(self, metric_value: MetricValue):
        """Send metric to Google Cloud Monitoring."""
        if not self.enable_cloud_monitoring or not self._client:
            return
        
        try:
            # Convert to Cloud Monitoring format
            # This is a simplified version - production would be more robust
            series = TimeSeries()
            series.metric.type = f"custom.googleapis.com/triune_ai/{metric_value.name}"
            
            # Add labels
            for key, value in metric_value.labels.items():
                series.metric.labels[key] = value
            
            # Add data point
            point = Point()
            point.value.double_value = float(metric_value.value)
            
            # Convert timestamp
            timestamp = timestamp_pb2.Timestamp()
            timestamp.FromDatetime(metric_value.timestamp)
            point.interval.end_time = timestamp
            
            series.points.append(point)
            series.resource.type = "global"
            
            # Send to Cloud Monitoring
            request = monitoring_v3.CreateTimeSeriesRequest(
                name=self._project_name,
                time_series=[series]
            )
            
            await self._client.create_time_series(request=request)
            
        except Exception as e:
            self.logger.error(f"❌ Failed to send metric to Cloud Monitoring: {e}")
    
    async def _create_alert(self, 
                          severity: AlertSeverity,
                          title: str,
                          description: str,
                          metadata: Optional[Dict[str, Any]] = None):
        """Create a new alert."""
        alert_id = f"{severity.value}_{int(time.time() * 1000)}"
        
        alert = Alert(
            id=alert_id,
            severity=severity,
            title=title,
            description=description,
            created_at=datetime.now(),
            metadata=metadata or {}
        )
        
        self.alerts[alert_id] = alert
        
        self.logger.warning(f"🚨 Alert created: {title} ({severity.value})")
    
    async def _monitoring_loop(self):
        """Background monitoring loop."""
        while self.running:
            try:
                # Perform periodic monitoring tasks
                await self._check_metric_thresholds()
                await self._cleanup_old_data()
                
                await asyncio.sleep(60)  # Run every minute
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"❌ Monitoring loop error: {e}")
                await asyncio.sleep(60)
    
    async def _alert_loop(self):
        """Background alert processing loop."""
        while self.running:
            try:
                # Process alerts, send notifications, etc.
                # This would be expanded in production
                
                await asyncio.sleep(30)  # Run every 30 seconds
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"❌ Alert loop error: {e}")
                await asyncio.sleep(30)
    
    async def _check_metric_thresholds(self):
        """Check metrics against alert thresholds."""
        # Check error rates
        error_metrics = self.metrics.get("error_count", [])
        if error_metrics:
            recent_errors = [m for m in error_metrics 
                           if m.timestamp > datetime.now() - timedelta(minutes=5)]
            error_rate = len(recent_errors) / 5.0  # Errors per minute
            
            if error_rate > self.alert_thresholds['error_rate_high']:
                await self._create_alert(
                    severity=AlertSeverity.WARNING,
                    title="High Error Rate",
                    description=f"Error rate is {error_rate:.2f} errors/minute",
                    metadata={'error_rate': error_rate}
                )
    
    async def _cleanup_old_data(self):
        """Clean up old metrics and alerts."""
        cutoff_time = datetime.now() - timedelta(days=7)  # Keep 7 days
        
        # Clean up old metrics
        for metric_name, values in self.metrics.items():
            self.metrics[metric_name] = [v for v in values if v.timestamp > cutoff_time]
        
        # Clean up old resolved alerts
        old_alerts = []
        for alert_id, alert in self.alerts.items():
            if (alert.resolved_at and 
                alert.resolved_at < cutoff_time):
                old_alerts.append(alert_id)
        
        for alert_id in old_alerts:
            del self.alerts[alert_id]
