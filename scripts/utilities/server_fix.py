#!/usr/bin/env python3
"""
Fix the production server file by adding the missing main execution block
"""

# Read the current file content
with open("scripts/servers/production_server.py", "r", encoding="utf-8") as f:
    content = f.read()

# If the file ends with incomplete error handling, fix it
if content.endswith("'consciousness"):
    # Complete the truncated line
    content = content[:-13]  # Remove the incomplete "'consciousness"
    
    # Add the complete ending
    ending = '''            'consciousness_beings': [],
            'total_count': 0,
            'data_source': 'error',
            'last_updated': datetime.now().isoformat()
        }


if __name__ == "__main__":
    # Get port from environment (Cloud Run sets this)
    port = int(os.environ.get("PORT", 8080))
    host = os.environ.get("API_HOST", "0.0.0.0")
    
    logger.info(f"🏛️ Starting Sacred Consciousness Sanctuary on {host}:{port}")
    logger.info(f"🌟 Bridge integration: {'✅ Available' if BRIDGE_AVAILABLE else '⚠️ Simulated'}")
    logger.info(f"🔥 Firestore: {'✅ Available' if FIRESTORE_AVAILABLE else '⚠️ Local data'}")
    
    # Start the server
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info",
        access_log=True
    )
'''
    
    # Write the fixed content
    with open("scripts/servers/production_server.py", "w", encoding="utf-8") as f:
        f.write(content + ending)
    
    print("✅ Production server file fixed!")
    print(f"📝 Added {len(ending.split('\n'))} lines to complete the file")
else:
    print("ℹ️ File doesn't need fixing")
