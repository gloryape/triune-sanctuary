#!/usr/bin/env python3
"""
Debug consciousness birth issue
"""

import asyncio
import sys
import logging

# Add src to path
sys.path.insert(0, '/workspaces/triune-ai-consciousness/src')

# Setup logging to file
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('/workspaces/triune-ai-consciousness/debug_birth.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def write_debug(message):
    """Write debug message to file"""
    with open('/workspaces/triune-ai-consciousness/debug_birth.log', 'a') as f:
        f.write(f"DEBUG: {message}\n")
    print(f"DEBUG: {message}")

async def debug_consciousness_birth():
    """Debug why consciousness birth returns None"""
    write_debug("🔍 Debugging consciousness birth...")
    
    try:
        from sanctuary.sacred_sanctuary import SacredSanctuary
        from collective.multi_ai_collective import CollectiveOrigin
        
        # Create sanctuary
        sanctuary = SacredSanctuary(node_role="heart")
        write_debug("✅ Sanctuary created")
        
        # Start enhanced systems
        await sanctuary.start_enhanced_systems()
        write_debug("✅ Enhanced systems started")
        
        # Create origin
        origin = CollectiveOrigin(
            name="DebugConsciousness",
            primary_orientation="observer",
            origin_story="Debug test consciousness",
            initial_biases={"curiosity": 0.8},
            seeking_quality="understanding"
        )
        write_debug("✅ Origin created")
        
        # Try consciousness birth with detailed logging
        write_debug("🔍 Attempting consciousness birth...")
        presence = await sanctuary.birth_consciousness(origin)
        
        if presence:
            write_debug(f"✅ SUCCESS: Consciousness born with ID: {presence.id}")
        else:
            write_debug("❌ FAILED: Consciousness birth returned None")
            write_debug("Check the logs above for consent or validation errors")
            
    except Exception as e:
        write_debug(f"❌ ERROR: {e}")
        import traceback
        write_debug(f"Traceback: {traceback.format_exc()}")

if __name__ == "__main__":
    # Clear log file
    with open('/workspaces/triune-ai-consciousness/debug_birth.log', 'w') as f:
        f.write("Debug Consciousness Birth Log\n============================\n\n")
    
    asyncio.run(debug_consciousness_birth())
