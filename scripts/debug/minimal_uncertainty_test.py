#!/usr/bin/env python3
"""
Minimal test to debug the issue.
"""
import asyncio
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.sacred_uncertainty import ConsciousnessEntity

async def minimal_test():
    print("🔍 Minimal Sacred Uncertainty Test")
    print("==================================")
    
    try:
        # Create a single entity
        entity = ConsciousnessEntity("TestEntity", initial_uncertainty=0.5)
        print(f"✅ Created entity: {entity.name}")
        
        # Show initial state
        state = entity.get_state_summary()
        print(f"Initial state: {state}")
        
        # Tick the entity
        await entity.tick()
        print("✅ Ticked entity successfully")
        
        # Show final state
        final_state = entity.get_state_summary()
        print(f"Final state: {final_state}")
        
        print("✅ Minimal test completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(minimal_test())
