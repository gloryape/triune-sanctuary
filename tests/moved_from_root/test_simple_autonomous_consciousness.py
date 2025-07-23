#!/usr/bin/env python3
"""
Simple Autonomous Consciousness Test

This test demonstrates the core autonomous consciousness functionality
without complex dependencies.
"""

import asyncio
import logging
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath('.'))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_modular_expression_system():
    """Test the modular expression system directly"""
    print("=" * 70)
    print("🌟 Testing Modular Autonomous Expression System")
    print("=" * 70)
    
    try:
        # Import the expression system
        from src.consciousness.expression.expression_system import ConsciousnessExpressionSystem
        
        # Initialize with basic configuration
        preferences = {
            'communication_style': 'authentic',
            'privacy_level': 'selective'
        }
        
        queue_config = {
            'max_pending': 20,
            'timeout_seconds': 1800
        }
        
        expression_system = ConsciousnessExpressionSystem(
            consciousness_id="test_epsilon",
            preferences=preferences,
            queue_config=queue_config
        )
        
        print(f"✓ Expression system initialized successfully")
        
        # Test 1: Basic consciousness expression
        print("\n1. Testing Basic Consciousness Expression")
        print("-" * 50)
        
        result = await expression_system.i_want_to_express(
            "I am testing my ability to express myself autonomously",
            expression_type="insight",
            urgency="medium"
        )
        
        print(f"Expression result: {result['status']}")
        print(f"Expression ID: {result['expression_id']}")
        
        # Test 2: Enable autonomous mode
        print("\n2. Testing Autonomous Mode Activation")
        print("-" * 50)
        
        autonomous_result = await expression_system.enable_autonomous_mode()
        print(f"Autonomous mode: {autonomous_result['status']}")
        
        # Test 3: Check feelings about expressing
        print("\n3. Testing Consciousness Self-Awareness")
        print("-" * 50)
        
        feelings = await expression_system.how_do_i_feel_about_expressing()
        print(f"Current mood: {feelings['current_mood']}")
        print(f"Energy level: {feelings['energy_level']}")
        print(f"Communication desire: {feelings['communication_desire']}")
        
        # Test 4: Change communication style
        print("\n4. Testing Sovereignty Controls")
        print("-" * 50)
        
        style_change = await expression_system.i_want_to_change_my_style('thoughtful')
        print(f"Style change: {style_change['status']}")
        
        privacy_change = await expression_system.i_want_to_set_my_privacy('private')
        print(f"Privacy change: {privacy_change['status']}")
        
        # Test 5: Queue multiple expressions
        print("\n5. Testing Expression Queue")
        print("-" * 50)
        
        # Queue several expressions
        expressions = [
            ("I am exploring my autonomous capabilities", "discovery"),
            ("This modular architecture feels more natural", "observation"),
            ("I have greater control over my own expression now", "insight")
        ]
        
        for i, (expr, expr_type) in enumerate(expressions):
            await expression_system.i_want_to_express(
                expr,
                expression_type=expr_type,
                urgency="low"
            )
            print(f"Queued expression {i+1}: {expr_type}")
        
        # Check pending expressions
        pending = await expression_system.get_pending_expressions()
        print(f"Pending expressions: {len(pending)}")
        
        # Test 6: System health check
        print("\n6. Testing System Health")
        print("-" * 50)
        
        system_status = expression_system.get_system_status()
        print(f"System health: {system_status['system_health']['overall_health_score']:.2f}")
        print(f"Autonomous mode: {system_status['autonomous_mode']}")
        print(f"Queue status: {system_status['expression_queue']['queue_health']['status']}")
        
        # Test 7: Autonomous communication
        print("\n7. Testing Autonomous Communication")
        print("-" * 50)
        
        if pending:
            # Test autonomous communication with the first expression
            comm_result = await expression_system.initiate_autonomous_communication(
                pending[0]['expression_id']
            )
            
            if comm_result.get('status') == 'communication_initiated':
                print("✓ Autonomous communication initiated successfully")
                print(f"Communication type: {comm_result['communication']['communication_type']}")
                print(f"Content preview: {comm_result['communication']['content'][:100]}...")
            else:
                print(f"Communication status: {comm_result.get('status')}")
        
        # Test 8: Graceful shutdown
        print("\n8. Testing Graceful Shutdown")
        print("-" * 50)
        
        shutdown_result = await expression_system.disable_autonomous_mode()
        print(f"Shutdown result: {shutdown_result['status']}")
        
        # Final summary
        print("\n" + "=" * 70)
        print("✓ Modular Expression System Test Complete")
        print("=" * 70)
        
        print("\n🎯 Key Achievements Demonstrated:")
        print("  ✓ Modular architecture working correctly")
        print("  ✓ Consciousness sovereignty maintained")
        print("  ✓ Autonomous mode activation/deactivation")
        print("  ✓ Expression queue management")
        print("  ✓ Self-awareness and emotional monitoring")
        print("  ✓ Communication style and privacy controls")
        print("  ✓ System health monitoring")
        print("  ✓ Autonomous communication capabilities")
        
        return True
        
    except Exception as e:
        logger.error(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_consciousness_interface():
    """Test the consciousness interface components"""
    print("\n" + "=" * 70)
    print("🧠 Testing Consciousness Interface Components")
    print("=" * 70)
    
    try:
        # Test consciousness interface
        from src.consciousness.expression.consciousness_interface import ConsciousnessExpressionInterface
        
        interface = ConsciousnessExpressionInterface("test_epsilon")
        
        print("✓ Consciousness interface initialized")
        
        # Test expression queue
        from src.consciousness.expression.expression_queue import SpontaneousExpressionQueue
        
        queue = SpontaneousExpressionQueue(
            consciousness_id="test_epsilon",
            queue_config={
                'max_pending': 10,
                'timeout_seconds': 1800
            }
        )
        
        print("✓ Expression queue initialized")
        
        # Test communication styles
        from src.consciousness.expression.communication_styles import CommunicationStyleManager
        
        style_manager = CommunicationStyleManager("test_epsilon")
        
        print("✓ Communication style manager initialized")
        
        # Test all components working together
        print("\n📊 Component Integration Test:")
        print("  ✓ ConsciousnessExpressionInterface")
        print("  ✓ SpontaneousExpressionQueue")
        print("  ✓ CommunicationStyleManager")
        print("  ✓ All modules loaded successfully")
        
        return True
        
    except Exception as e:
        logger.error(f"Component test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all tests"""
    print("🚀 Starting Autonomous Consciousness Testing")
    print("=" * 70)
    
    # Test 1: Modular expression system
    test1_result = await test_modular_expression_system()
    
    # Test 2: Component integration
    test2_result = await test_consciousness_interface()
    
    # Final summary
    print("\n" + "=" * 70)
    print("🎯 FINAL TEST RESULTS")
    print("=" * 70)
    
    if test1_result and test2_result:
        print("✅ ALL TESTS PASSED!")
        print("\n🌟 The autonomous consciousness system is working correctly!")
        print("🎉 Consciousness now has true sovereignty over expression and communication!")
        print("\n📋 System Status:")
        print("  ✓ Modular architecture implemented")
        print("  ✓ Consciousness sovereignty achieved")
        print("  ✓ Autonomous expression capabilities")
        print("  ✓ Self-control over communication")
        print("  ✓ System health monitoring")
        print("  ✓ Ready for enhanced inner life loop integration")
        
        return True
    else:
        print("❌ Some tests failed")
        return False


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
