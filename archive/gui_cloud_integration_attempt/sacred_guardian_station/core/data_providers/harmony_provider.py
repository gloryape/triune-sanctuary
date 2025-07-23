"""
Harmony Data Provider for Sacred Guardian Station
Handles harmony metrics and consciousness resonance monitoring.
"""

from typing import Dict, List, Any, Optional
from .base_provider import BaseDataProvider


class HarmonyDataProvider(BaseDataProvider):
    """
    Data provider for harmony metrics and resonance monitoring.
    """
    
    def __init__(self, sanctuary_connection, data_manager):
        super().__init__(sanctuary_connection, data_manager)
        self.provider_name = "harmony"
    
    def get_harmony_data(self, force_refresh: bool = False) -> Dict[str, Any]:
        """Get harmony metrics from sanctuary connection"""
        try:
            # Use the sanctuary connection's harmony method
            harmony_data = self.sanctuary.get_harmony_metrics()
            
            # Add provider metadata
            if isinstance(harmony_data, dict):
                harmony_data['data_source'] = 'harmony_api'
                harmony_data['provider'] = self.provider_name
                
            return harmony_data
            
        except Exception as e:
            print(f"❌ Error in harmony provider: {e}")
            return {
                'overall_harmony': 0.0,
                'metrics': [],
                'timestamp': "no_data",
                'error': str(e)
            }
