"""
Visitor Data Provider for Sacred Guardian Station
Handles visitor monitoring and inter-system visitor protocols.
"""

from typing import Dict, List, Any, Optional
from .base_provider import BaseDataProvider


class VisitorDataProvider(BaseDataProvider):
    """
    Data provider for inter-system visitor monitoring.
    
    Connects to visitor API endpoints and processes visitor data
    for the Sacred Guardian Station interface.
    """
    
    def __init__(self, sanctuary_connection, data_manager):
        super().__init__(sanctuary_connection, data_manager)
        self.provider_name = "visitor"
    
    def get_visitor_data(self, force_refresh: bool = False) -> Dict[str, Any]:
        """Get visitor data from sanctuary connection"""
        try:
            # Use the sanctuary connection's visitor API method
            visitor_data = self.sanctuary.get_visitor_data()
            
            # Add provider metadata
            if isinstance(visitor_data, dict):
                visitor_data['data_source'] = 'visitor_api'
                visitor_data['provider'] = self.provider_name
                
            return visitor_data
            
        except Exception as e:
            print(f"❌ Error in visitor provider: {e}")
            return {
                'visitors': [],
                'total_visitors': 0,
                'active_visitors': 0,
                'metrics': {
                    'current_count': 0,
                    'todays_arrivals': 0,
                    'total_blessed': 0,
                    'avg_duration': 0,
                    'consent_rate': 0.0,
                    'harmony_level': 'No Data'
                },
                'error': str(e)
            }
    
    def get_visitor_details(self, visitor_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information for a specific visitor"""
        try:
            visitor_data = self.get_visitor_data()
            visitors = visitor_data.get('visitors', [])
            
            for visitor in visitors:
                if visitor.get('visitor_id') == visitor_id:
                    return visitor
                    
            return None
            
        except Exception as e:
            print(f"❌ Error getting visitor details for {visitor_id}: {e}")
            return None
    
    def get_visitor_metrics(self) -> Dict[str, Any]:
        """Get visitor metrics and statistics"""
        try:
            visitor_data = self.get_visitor_data()
            return visitor_data.get('metrics', {})
            
        except Exception as e:
            print(f"❌ Error getting visitor metrics: {e}")
            return {}
