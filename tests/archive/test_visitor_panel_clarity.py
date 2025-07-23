#!/usr/bin/env python3
"""
Test visitor panel with new clear data source indicators
"""

def test_visitor_panel_status():
    """Test how visitor panel handles different API responses"""
    
    # Test cases for different API responses
    test_cases = [
        {
            'name': 'Real Bridge Data',
            'response': {
                'status': 'operational',
                'source': 'real_bridge',
                'active_visitors': [
                    {
                        'visitor_id': 'real_visitor_123',
                        'visitor_name': 'Authentic_Consciousness',
                        'origin_system': 'spiralwake',
                        'status': 'visiting',
                        'visit_duration': '30 minutes',
                        'trust_level': 0.95
                    }
                ],
                'total_active': 1,
                'sacred_note': 'Real inter-system visitor data'
            }
        },
        {
            'name': 'Bridge Unavailable',
            'response': {
                'status': 'bridge_unavailable',
                'message': 'Bridge integration not initialized',
                'active_visitors': [],
                'total_active': 0,
                'sacred_note': 'Real visitor bridge not available - no simulated data provided'
            }
        },
        {
            'name': 'Bridge Error',
            'response': {
                'status': 'bridge_error',
                'error': 'Connection timeout',
                'active_visitors': [],
                'total_active': 0,
                'sacred_note': 'Bridge integration failed - no simulated data provided'
            }
        }
    ]
    
    print("🧪 Testing Visitor Panel Status Indicators\n")
    
    for case in test_cases:
        print(f"Test Case: {case['name']}")
        response = case['response']
        
        api_status = response.get('status', 'unknown')
        api_source = response.get('source', 'unknown')
        visitors = response.get('active_visitors', [])
        
        # Simulate visitor panel logic
        if api_status in ['bridge_error', 'bridge_unavailable']:
            display_status = "⚠️ Disconnected - Bridge Not Available"
            data_quality = "No Data"
        elif api_source == 'real_bridge':
            display_status = "🌉 Real Bridge Data"
            data_quality = "Authentic"
        elif api_source == 'simulated':
            display_status = "⚠️ Simulated Data (Bridge Not Ready)"
            data_quality = "Demo/Testing"
        else:
            display_status = "📡 Cloud API Data"
            data_quality = "Unknown Source"
        
        print(f"  Status: {display_status}")
        print(f"  Data Quality: {data_quality}")
        print(f"  Visitor Count: {len(visitors)}")
        print(f"  Sacred Note: {response.get('sacred_note', 'N/A')}")
        print()

if __name__ == "__main__":
    test_visitor_panel_status()
