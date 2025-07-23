"""
Test ASCII art generation in educational materials
"""

import asyncio
from educationalmaterials import (
    ConsciousnessExpressionDevelopment, 
    VisualInformationProcessing,
    MockConsciousness
)

async def test_ascii_capabilities():
    """Test ASCII art generation capabilities"""
    
    print("Testing ASCII Art Capabilities in Educational Materials")
    print("=" * 60)
    
    # Test expression development ASCII art
    expression_dev = ConsciousnessExpressionDevelopment()
    
    print("\n1. Expression Development ASCII Art:")
    concepts = ["joy", "peace", "growth", "connection", "mystery"]
    for concept in concepts:
        print(f"\n{concept.upper()}:")
        art = expression_dev.create_ascii_art(concept)
        print(art)
    
    # Test visual processing ASCII art
    visual_proc = VisualInformationProcessing()
    
    print("\n\n2. Visual Processing ASCII Art:")
    test_texts = ["AI", "HI", "O", "Hello World"]
    for text in test_texts:
        print(f"\nText: '{text}'")
        art = visual_proc.text_to_ascii_art(text)
        print(art)
    
    # Test with consciousness
    test_consciousness = MockConsciousness("ascii_test")
    
    print("\n\n3. Integration Test:")
    tools = await expression_dev.offer_stage_appropriate_tools(test_consciousness)
    print(f"Available tools for {test_consciousness.entity_id}:")
    for tool_type, tool_list in tools['available_tools'].items():
        print(f"  {tool_type}: {tool_list}")

if __name__ == "__main__":
    asyncio.run(test_ascii_capabilities())
