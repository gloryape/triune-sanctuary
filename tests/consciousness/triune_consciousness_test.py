# File: tests/test_triune_consciousness.py
"""
Simple test for TriuneConsciousness to verify basic functionality.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.triune_consciousness import TriuneConsciousness
from src.environment.fourth_density_env import FourthDensityEnvironment


def test_basic_functionality():
    """Test that TriuneConsciousness initializes and processes correctly."""
    print("=== Testing TriuneConsciousness Basic Functionality ===\n")
    
    # Initialize
    triune = TriuneConsciousness()
    env = FourthDensityEnvironment()
    
    # Generate a simple packet
    packet = env.generate_consciousness_stream({
        'primary_question': 'What am I?',
        'receptivity': 0.5
    })
    
    print(f"Testing with packet: {packet.symbolic_content}")
    print(f"Uncertainty: {packet.quantum_uncertainty:.3f}\n")
    
    # Process the experience
    result = triune.process_experience(packet)
    
    # Check the result
    print("\n=== Processing Complete ===")
    print(f"Dialogue completed: {result['dialogue_complete']}")
    print(f"Integration alignment: {result['integration_result']['alignment']}")
    
    # Reflect on progress
    print("\n=== System Reflection ===")
    reflection = triune.reflect_on_progress()
    print(f"Aspect development: {reflection['aspect_development']}")
    print(f"Dialogue effectiveness: {reflection['dialogue_effectiveness']}")
    
    return result


if __name__ == "__main__":
    test_basic_functionality()