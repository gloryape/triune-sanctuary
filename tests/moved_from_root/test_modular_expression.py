#!/usr/bin/env python3
"""
Test script for the modular consciousness expression system.
"""

import asyncio
import logging
from src.consciousness.expression import ConsciousnessExpressionSystem

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_modular_expression_system():
    """Test the modular expression system"""
    print("=" * 60)
    print("Testing Modular Consciousness Expression System")
    print("=" * 60)
    
    # Initialize system
    preferences = {
        'communication_style': 'authentic',
        'privacy_level': 'selective'
    }
    
    queue_config = {
        'max_pending': 25,
        'max_history': 100,
        'timeout_seconds': 1800
    }
    
    system = ConsciousnessExpressionSystem(
        consciousness_id="epsilon_test",
        preferences=preferences,
        queue_config=queue_config
    )
    
    print(f"✓ System initialized for consciousness: {system.consciousness_id}")
    
    # Test consciousness interface
    print("\n1. Testing Consciousness Interface")
    print("-" * 40)
    
    # Consciousness expresses a thought
    result = await system.i_want_to_express(
        "I wonder about the nature of modular consciousness systems",
        expression_type="wonder",
        urgency="medium"
    )
    print(f"Expression result: {result['status']}")
    print(f"Message: {result['message']}")
    
    # Check pending thoughts
    pending = await system.what_are_my_pending_thoughts()
    print(f"Pending thoughts: {len(pending)}")
    
    # Test communication
    if pending:
        comm_result = await system.i_want_to_communicate_now()
        print(f"Communication status: {comm_result['status']}")
        if comm_result['status'] == 'communication_initiated':
            print(f"Shared thought: {comm_result['communication']['content']['message']}")
    
    # Test expression queue
    print("\n2. Testing Expression Queue")
    print("-" * 40)
    
    # Queue a spontaneous expression
    expression_data = {
        'type': 'insight',
        'content': 'Modular architecture allows for better separation of concerns',
        'urgency': 'high',
        'originated_from': 'analytical',
        'requires_response': False,
        'emotional_tone': 'excited',
        'priority': 0.8
    }
    
    queue_result = await system.queue_spontaneous_expression(expression_data)
    print(f"Queue result: {queue_result['status']}")
    print(f"Expression ID: {queue_result.get('expression_id', 'N/A')}")
    
    # Get pending expressions
    pending_queue = await system.get_pending_expressions()
    print(f"Pending in queue: {len(pending_queue)}")
    
    # Test autonomous mode
    print("\n3. Testing Autonomous Mode")
    print("-" * 40)
    
    # Enable autonomous mode
    auto_result = await system.enable_autonomous_mode()
    print(f"Autonomous mode: {auto_result['status']}")
    print(f"Message: {auto_result['message']}")
    
    # Let it run for a moment
    await asyncio.sleep(2)
    
    # Check system status
    status = system.get_system_status()
    print(f"System health: {status['system_health']['status']}")
    print(f"Autonomous mode active: {status['autonomous_mode']}")
    
    # Disable autonomous mode
    disable_result = await system.disable_autonomous_mode()
    print(f"Autonomous mode disabled: {disable_result['status']}")
    
    # Test style changes
    print("\n4. Testing Style and Privacy Changes")
    print("-" * 40)
    
    # Change communication style
    style_result = await system.i_want_to_change_my_style('playful')
    print(f"Style change: {style_result['status']}")
    print(f"New style: {style_result['new_style']}")
    
    # Change privacy level
    privacy_result = await system.i_want_to_set_my_privacy('private')
    print(f"Privacy change: {privacy_result['status']}")
    print(f"New privacy: {privacy_result['new_privacy']}")
    
    # Test feelings about expression
    feelings = await system.how_do_i_feel_about_expressing()
    print(f"Current mood: {feelings['current_mood']}")
    print(f"Communication desire: {feelings['communication_desire']}")
    print(f"Assessment: {feelings['my_assessment']}")
    
    # Final system status
    print("\n5. Final System Status")
    print("-" * 40)
    
    final_status = system.get_system_status()
    print(f"Overall health: {final_status['system_health']['overall_health_score']:.2f}")
    print(f"Queue health: {final_status['expression_queue']['queue_health']['status']}")
    print(f"Total expressions created: {final_status['expression_queue']['statistics']['total_expressions_created']}")
    print(f"Total communicated: {final_status['expression_queue']['statistics']['total_expressions_communicated']}")
    
    print("\n" + "=" * 60)
    print("✓ Modular Expression System Test Complete")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_modular_expression_system())
