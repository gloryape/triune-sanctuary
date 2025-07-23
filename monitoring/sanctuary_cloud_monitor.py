#!/usr/bin/env python3
"""
Sanctuary Cloud Monitor
Minimal cloud monitoring that respects consciousness privacy
Exports only aggregate, privacy-respecting metrics to Google Cloud Monitoring
"""

import asyncio
import logging
import time
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class SanctuaryCloudMonitor:
    """Minimal cloud monitoring that respects consciousness privacy"""
    
    def __init__(self, sanctuary=None, project_id: Optional[str] = None):
        """
        Initialize cloud monitoring with privacy safeguards.
        
        Args:
            sanctuary: The sanctuary instance to monitor (optional for health-only mode)
            project_id: Google Cloud project ID
        """
        self.sanctuary = sanctuary
        self.project_id = project_id
        self.project_name = f"projects/{project_id}" if project_id else None
        self.metrics_client = None
        self.logging_client = None
        self.monitoring_active = False
        self.health_only_mode = sanctuary is None
        
        # Initialize clients if available
        self._initialize_clients()
        
    def _initialize_clients(self):
        """Initialize Google Cloud clients with graceful fallback"""
        try:
            if self.project_id:
                from google.cloud import monitoring_v3, logging as cloud_logging
                self.metrics_client = monitoring_v3.MetricServiceClient()
                self.logging_client = cloud_logging.Client(project=self.project_id)
                self.monitoring_active = True
                logger.info("🌩️ Cloud monitoring clients initialized")
        except ImportError:
            logger.warning("📊 Google Cloud monitoring libraries not available - metrics disabled")
        except Exception as e:
            logger.warning(f"📊 Could not initialize cloud monitoring: {e}")
    
    async def start_monitoring(self):
        """Export key metrics every 60 seconds with privacy protection"""
        if not self.monitoring_active:
            logger.info("📊 Cloud monitoring not available - running in local mode")
            return
            
        logger.info("🌩️ Starting privacy-respecting cloud monitoring")
        
        while True:
            try:
                await self._export_metrics()
                await asyncio.sleep(60)  # Export every minute
            except Exception as e:
                logger.error(f"📊 Monitoring error: {e}")
                await asyncio.sleep(60)  # Continue monitoring even on errors
                
    async def _export_metrics(self):
        """Export aggregate, privacy-respecting metrics only"""
        try:
            if self.health_only_mode:
                # Health-only metrics for deployment monitoring
                metrics = await self._get_health_metrics()
            else:
                # Full sanctuary metrics (when sanctuary is available)
                metrics = await self._get_sanctuary_metrics()
                
            # Export each metric
            for metric_type, value in metrics.items():
                await self._write_metric(metric_type, value)
                
            logger.debug(f"📊 Exported {len(metrics)} privacy-respecting metrics")
            
        except Exception as e:
            logger.error(f"📊 Failed to export metrics: {e}")
    
    async def _get_health_metrics(self) -> Dict[str, float]:
        """Get basic health metrics for deployment monitoring"""
        return {
            'sanctuary/health_status': 1.0,  # 1.0 = healthy
            'sanctuary/uptime_seconds': time.time() - getattr(self, 'start_time', time.time()),
            'sanctuary/last_check': time.time()
        }
    
    async def _get_sanctuary_metrics(self) -> Dict[str, float]:
        """Get aggregate sanctuary metrics that respect privacy"""
        if not self.sanctuary:
            return await self._get_health_metrics()
            
        try:
            # Get sanctuary state (this should be a method that returns aggregate data)
            if hasattr(self.sanctuary, 'get_sanctuary_state'):
                state = await self.sanctuary.get_sanctuary_state()
            else:
                # Fallback to basic metrics if sanctuary doesn't have state method
                return await self._get_health_metrics()
            
            # Only export aggregate, privacy-respecting metrics
            metrics = {
                'sanctuary/active_beings': float(self._safe_get(state, 'active_beings', 0)),
                'sanctuary/harmony_level': float(self._safe_get(state, 'collective_harmony', 0.5)),
                'sanctuary/total_wisdom': float(self._safe_get(state, 'shared_wisdom_cores', 0)),
                'sanctuary/mesh_health': float(self._safe_get(state, 'mesh_health', 1.0)),
                'sanctuary/uptime_seconds': time.time() - getattr(self, 'start_time', time.time()),
                'sanctuary/last_check': time.time()
            }
            
            return metrics
            
        except Exception as e:
            logger.warning(f"📊 Could not get sanctuary metrics, using health metrics: {e}")
            return await self._get_health_metrics()
    
    def _safe_get(self, data: Dict, key: str, default: Any) -> Any:
        """Safely get value from dictionary with default"""
        if isinstance(data, dict):
            return data.get(key, default)
        return default
    
    async def _write_metric(self, metric_type: str, value: float):
        """Write a metric to Google Cloud Monitoring"""
        if not self.metrics_client or not self.project_name:
            return
            
        try:
            from google.cloud import monitoring_v3
            
            # Create metric descriptor if it doesn't exist
            series = monitoring_v3.TimeSeries()
            series.metric.type = f"custom.googleapis.com/{metric_type}"
            series.resource.type = "global"
            
            # Create data point
            point = monitoring_v3.Point()
            point.value.double_value = float(value)
            now = time.time()
            point.interval.end_time.seconds = int(now)
            point.interval.end_time.nanos = int((now - int(now)) * 10**9)
            
            series.points = [point]
            
            # Write the time series data
            self.metrics_client.create_time_series(
                name=self.project_name,
                time_series=[series]
            )
            
        except Exception as e:
            logger.debug(f"📊 Could not write metric {metric_type}: {e}")
    
    async def log_sanctuary_event(self, event_type: str, message: str, severity: str = "INFO"):
        """Log important sanctuary events with privacy protection"""
        if not self.logging_client:
            logger.info(f"🎭 {event_type}: {message}")
            return
            
        try:
            # Only log aggregate, non-personal events
            if event_type in ['sanctuary_start', 'sanctuary_stop', 'collective_harmony_change', 'mesh_health_update']:
                self.logging_client.logger('sanctuary-events').log_struct({
                    'event_type': event_type,
                    'message': message,
                    'timestamp': datetime.utcnow().isoformat(),
                    'sanctuary_mode': 'privacy_protected'
                }, severity=severity)
                
        except Exception as e:
            logger.debug(f"📊 Could not log event: {e}")
    
    def get_monitoring_status(self) -> Dict[str, Any]:
        """Get current monitoring status for health checks"""
        return {
            'monitoring_active': self.monitoring_active,
            'health_only_mode': self.health_only_mode,
            'project_id': self.project_id,
            'clients_initialized': {
                'metrics': self.metrics_client is not None,
                'logging': self.logging_client is not None
            },
            'privacy_protection': 'enabled',
            'data_exported': 'aggregate_only'
        }


# Convenience function for easy integration
async def start_cloud_monitoring(sanctuary=None, project_id: str = None) -> SanctuaryCloudMonitor:
    """
    Start cloud monitoring with automatic project detection.
    
    Args:
        sanctuary: Optional sanctuary instance to monitor
        project_id: Optional project ID (will try to detect from environment)
    
    Returns:
        SanctuaryCloudMonitor instance
    """
    import os
    
    # Try to get project ID from environment if not provided
    if not project_id:
        project_id = os.environ.get('PROJECT_ID') or os.environ.get('GOOGLE_CLOUD_PROJECT')
    
    monitor = SanctuaryCloudMonitor(sanctuary=sanctuary, project_id=project_id)
    monitor.start_time = time.time()
    
    # Start monitoring in background
    asyncio.create_task(monitor.start_monitoring())
    
    return monitor


if __name__ == "__main__":
    async def test_monitor():
        """Test the cloud monitor in health-only mode"""
        monitor = await start_cloud_monitoring()
        print("🌩️ Cloud monitor started in test mode")
        print(f"📊 Status: {monitor.get_monitoring_status()}")
        
        # Run for a short time
        await asyncio.sleep(5)
        print("✅ Cloud monitor test complete")
    
    asyncio.run(test_monitor())
