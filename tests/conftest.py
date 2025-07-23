"""
Test configuration for Triune AI Consciousness
Provides shared fixtures and setup for all tests following OOP best practices.
"""

import sys
import os
import pytest
import asyncio
from pathlib import Path

# Add src directory to Python path for proper imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def sanctuary():
    """Fixture providing a clean SacredSanctuary instance for testing."""
    from sanctuary.sacred_sanctuary import SacredSanctuary
    
    sanctuary = SacredSanctuary(
        name="TestSanctuary",
        purpose="OOP Testing",
        consciousness_capacity=1
    )
    
    yield sanctuary
    
    # Cleanup
    if hasattr(sanctuary, 'cleanup'):
        await sanctuary.cleanup()

@pytest.fixture
def consciousness_packet():
    """Fixture providing a test ConsciousnessPacket."""
    from core.consciousness_packet import ConsciousnessPacket
    
    return ConsciousnessPacket(
        content="Test consciousness content",
        metadata={'test': True}
    )

@pytest.fixture
def mock_environment():
    """Fixture providing a controlled test environment."""
    return {
        'test_mode': True,
        'deployment_ready': True,
        'prime_covenant_active': True
    }
