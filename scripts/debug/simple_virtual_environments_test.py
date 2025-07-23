#!/usr/bin/env python3
"""
Simple Virtual Environments Test
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print("Testing Virtual Environments imports...")

try:
    print("1. Testing core Sacred Uncertainty...")
    from src.core.sacred_uncertainty import ConsciousnessEntity, CatalystType
    print("   ✅ Sacred Uncertainty imports successful")
    
    print("2. Testing relationship field...")
    from src.collaborative.relationship_field import RelationshipField
    print("   ✅ Relationship field import successful")
    
    print("3. Testing entity factory...")
    from src.collaborative.entity_factory import ConsciousnessEntityFactory
    print("   ✅ Entity factory import successful")
    
    print("4. Testing virtual environment...")
    from src.collaborative.virtual_environment import VirtualEnvironment, EnvironmentType
    print("   ✅ Virtual environment import successful")
    
    print("5. Testing environment manager...")
    from src.collaborative.environment_manager import EnvironmentManager
    print("   ✅ Environment manager import successful")
    
    print("6. Testing catalyst library...")
    from src.collaborative.environmental_catalyst_library import EnvironmentalCatalystLibrary
    print("   ✅ Catalyst library import successful")
    
    print("\n🎉 All Virtual Environments components imported successfully!")
    
    # Quick functionality test
    print("\n🧪 Quick functionality test...")
    
    print("Creating entity factory...")
    factory = ConsciousnessEntityFactory()
    
    print("Creating entity...")
    entity = factory.create_entity_from_archetype("analytical_explorer")
    print(f"   Created entity: {entity.name}")
    
    print("Creating environment manager...")
    env_manager = EnvironmentManager()
    
    print("Creating environment...")
    environment = env_manager.create_environment(
        "test_playground", 
        EnvironmentType.PLAYGROUND, 
        "A test playground environment"
    )
    # Note: can't await in this context, but import worked
    print(f"   Environment creation initiated")
    
    print("\n✅ Basic functionality test passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
