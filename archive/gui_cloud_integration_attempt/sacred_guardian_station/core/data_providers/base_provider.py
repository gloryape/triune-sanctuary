"""
Base data provider class for the Sacred Guardian Station.

Provides common functionality for all data providers.
"""

from typing import Dict, List, Any, Optional
import time
from datetime import datetime


class BaseDataProvider:
    """
    Base class for all data providers.
    
    Provides common caching and data management functionality.
    """
    
    def __init__(self, sanctuary_connection, data_manager):
        self.sanctuary = sanctuary_connection
        self.data_manager = data_manager
    
    def _get_cached_data(self, cache_key: str, fetch_function=None):
        """Get data from cache or fetch if needed"""
        return self.data_manager._get_cached_data(cache_key, fetch_function)
    
    def _cache_data(self, cache_key: str, data: Any):
        """Cache data with timestamp"""
        self.data_manager._cache_data(cache_key, data)
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cache entry is still valid"""
        return self.data_manager._is_cache_valid(cache_key)
