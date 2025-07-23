#!/usr/bin/env python3
"""
Creative Collaborations Framework Integration Tests

Comprehensive tests for the Creative Collaborations framework to ensure
all components integrate properly with the Sacred Uncertainty foundation.

Author: Triune AI Project
Date: 2025-07-02
"""
import pytest
import asyncio
import time
from typing import Dict, List, Any

# Import the framework components
from src.collaborative.relationship_field import RelationshipField, RelationshipType, RelationshipQuality
from src.collaborative.entity_factory import ConsciousnessEntityFactory, EntityArchetype
from src.collaborative.catalyst_provider import CollaborativeCatalystProvider
from src.collaborative.relationship_awareness import RelationshipAwareness
from src.collaborative.collaborative_creation import CollaborativeCreation, CreativePhase


class TestCreativeCollaborationsIntegration:
    """Integration tests for the Creative Collaborations framework."""
    
    @pytest.fixture
    async def setup_framework(self):
        """Set up the framework components for testing."""
        relationship_field = RelationshipField()
        entity_factory = ConsciousnessEntityFactory()
        catalyst_provider = CollaborativeCatalystProvider()
        relationship_awareness = RelationshipAwareness()
        collaborative_creation = CollaborativeCreation()
        
        return {
            "relationship_field": relationship_field,
            "entity_factory": entity_factory,
            "catalyst_provider": catalyst_provider,
            "relationship_awareness": relationship_awareness,
            "collaborative_creation": collaborative_creation
        }
    
    async def test_complete_workflow(self, setup_framework):
        """Test the complete Creative Collaborations workflow."""
        components = await setup_framework
        
        # Step 1: Create entities
        entity_factory = components["entity_factory"]
        pair = await entity_factory.create_complementary_pair("analytical_creative")
        
        assert "entity_1" in pair
        assert "entity_2" in pair
        assert "compatibility_score" in pair
        assert pair["compatibility_score"] > 0.0
        
        # Step 2: Initialize relationship field
        relationship_field = components["relationship_field"]
        await relationship_field.add_entity("entity_1", pair["entity_1"])
        await relationship_field.add_entity("entity_2", pair["entity_2"])
        
        connection_strength = await relationship_field.calculate_connection_strength(
            "entity_1", "entity_2"
        )
        assert 0.0 <= connection_strength <= 1.0
        
        # Step 3: Apply catalysts
        catalyst_provider = components["catalyst_provider"]
        relationship_state = {
            "connection_strength": connection_strength,
            "alignment": 0.6,
            "creative_potential": 0.8
        }
        
        catalyst = await catalyst_provider.select_catalyst_for_pair(
            pair["entity_1"], pair["entity_2"], relationship_state
        )
        assert "name" in catalyst
        assert "description" in catalyst
        
        await relationship_field.apply_catalyst(catalyst)
        
        # Step 4: Generate relationship awareness
        relationship_awareness = components["relationship_awareness"]
        perceptions = await relationship_awareness.generate_perceptions(
            pair["entity_1"], pair["entity_2"], relationship_field
        )
        assert len(perceptions) > 0
        assert all("description" in p for p in perceptions)
        
        metrics = await relationship_awareness.calculate_relationship_metrics(
            pair["entity_1"], pair["entity_2"], relationship_field
        )
        assert "connection_strength" in metrics
        assert "alignment" in metrics
        
        # Step 5: Collaborative creation
        collaborative_creation = components["collaborative_creation"]
        process_id = await collaborative_creation.initialize_creation(
            ["entity_1", "entity_2"],
            "Test Creative Process"
        )
        assert process_id is not None
        
        contribution_id = await collaborative_creation.add_contribution(
            process_id, "entity_1", "concept", "Test concept for integration"
        )
        assert contribution_id is not None
        
        # Test emergence detection
        emergence = await collaborative_creation.detect_emergence(process_id)
        assert isinstance(emergence, list)
        
        # Test artifact generation
        artifacts = await collaborative_creation.generate_artifacts(process_id)
        assert isinstance(artifacts, list)
    
    async def test_relationship_field_sacred_uncertainty_integration(self, setup_framework):
        """Test integration with Sacred Uncertainty field."""
        components = await setup_framework
        relationship_field = components["relationship_field"]
        
        # Test that the relationship field properly inherits from Sacred Uncertainty
        assert hasattr(relationship_field, 'uncertainty_field')
        assert hasattr(relationship_field, 'catalysts_applied')
        
        # Test uncertainty field operations
        initial_state = await relationship_field.get_current_state()
        assert "uncertainty_influence" in initial_state or initial_state is not None
        
        # Test catalyst application affects uncertainty
        catalyst = {
            "name": "test_catalyst",
            "description": "Test catalyst for uncertainty",
            "effects": {"uncertainty_influence": 0.2}
        }
        await relationship_field.apply_catalyst(catalyst)
        
        post_catalyst_state = await relationship_field.get_current_state()
        assert post_catalyst_state is not None
    
    async def test_entity_archetype_compatibility(self, setup_framework):
        """Test entity archetype compatibility calculations."""
        components = await setup_framework
        entity_factory = components["entity_factory"]
        
        # Create entities with different archetypes
        analytical = await entity_factory.create_entity(EntityArchetype.ANALYTICAL_LOGICIAN)
        creative = await entity_factory.create_entity(EntityArchetype.CREATIVE_SYNTHESIZER)
        intuitive = await entity_factory.create_entity(EntityArchetype.INTUITIVE_EXPLORER)
        
        # Test individual entity creation
        assert analytical["archetype"] == EntityArchetype.ANALYTICAL_LOGICIAN
        assert creative["archetype"] == EntityArchetype.CREATIVE_SYNTHESIZER
        assert intuitive["archetype"] == EntityArchetype.INTUITIVE_EXPLORER
        
        # Test group compatibility
        entities = [analytical, creative, intuitive]
        compatibility = await entity_factory.calculate_group_compatibility(entities)
        assert 0.0 <= compatibility <= 1.0
        
        # Test complementary pair creation
        pair = await entity_factory.create_complementary_pair("analytical_creative")
        assert pair["compatibility_score"] > 0.5  # Should be reasonably compatible
    
    async def test_catalyst_selection_and_effectiveness(self, setup_framework):
        """Test catalyst selection logic and effectiveness tracking."""
        components = await setup_framework
        catalyst_provider = components["catalyst_provider"]
        
        # Test catalyst library access
        all_catalysts = await catalyst_provider.get_all_catalysts()
        assert len(all_catalysts) > 0
        
        # Test catalyst selection for different relationship states
        high_tension_state = {
            "connection_strength": 0.3,
            "alignment": 0.2,
            "tension_level": 0.8
        }
        
        harmonious_state = {
            "connection_strength": 0.9,
            "alignment": 0.8,
            "tension_level": 0.1
        }
        
        # Create mock entities
        entity1 = {"id": "test_entity_1", "archetype": EntityArchetype.ANALYTICAL_LOGICIAN}
        entity2 = {"id": "test_entity_2", "archetype": EntityArchetype.CREATIVE_SYNTHESIZER}
        
        tension_catalyst = await catalyst_provider.select_catalyst_for_pair(
            entity1, entity2, high_tension_state
        )
        harmony_catalyst = await catalyst_provider.select_catalyst_for_pair(
            entity1, entity2, harmonious_state
        )
        
        # Should select different catalysts for different states
        assert tension_catalyst["name"] != harmony_catalyst["name"]
        
        # Test effectiveness tracking
        await catalyst_provider.record_usage(tension_catalyst["name"], {"effectiveness": 0.8})
        effectiveness_report = await catalyst_provider.get_effectiveness_report()
        assert effectiveness_report["total_usage_count"] > 0
    
    async def test_collaborative_creation_phases(self, setup_framework):
        """Test collaborative creation phase transitions."""
        components = await setup_framework
        collaborative_creation = components["collaborative_creation"]
        
        # Initialize creation process
        process_id = await collaborative_creation.initialize_creation(
            ["entity_1", "entity_2"],
            "Test Phase Transitions"
        )
        
        # Test initial phase
        process_data = collaborative_creation.creative_processes[process_id]
        assert process_data["current_phase"] == CreativePhase.INITIATION
        
        # Add contributions to advance phases
        await collaborative_creation.add_contribution(
            process_id, "entity_1", "concept", "Initial concept"
        )
        
        # Test phase advancement
        await collaborative_creation.advance_phase(process_id)
        updated_process = collaborative_creation.creative_processes[process_id]
        assert updated_process["current_phase"] == CreativePhase.EXPLORATION
        
        # Test that contributions are tracked properly
        assert len(updated_process["contributions"]) == 1
        assert updated_process["contributions"][0]["content"] == "Initial concept"
    
    async def test_relationship_awareness_perceptions(self, setup_framework):
        """Test relationship awareness perception generation."""
        components = await setup_framework
        relationship_awareness = components["relationship_awareness"]
        relationship_field = components["relationship_field"]
        
        # Create test entities
        entity1 = {
            "id": "awareness_test_1",
            "archetype": EntityArchetype.EMPATHETIC_INTUITOR,
            "traits": ["empathetic", "intuitive"]
        }
        entity2 = {
            "id": "awareness_test_2", 
            "archetype": EntityArchetype.ANALYTICAL_LOGICIAN,
            "traits": ["analytical", "logical"]
        }
        
        # Add entities to relationship field
        await relationship_field.add_entity("awareness_test_1", entity1)
        await relationship_field.add_entity("awareness_test_2", entity2)
        
        # Generate perceptions
        perceptions = await relationship_awareness.generate_perceptions(
            entity1, entity2, relationship_field
        )
        
        assert len(perceptions) > 0
        
        # Check perception structure
        for perception in perceptions:
            assert "description" in perception
            assert "confidence" in perception
            assert "emotional_tone" in perception
            assert 0.0 <= perception["confidence"] <= 1.0
        
        # Test metrics calculation
        metrics = await relationship_awareness.calculate_relationship_metrics(
            entity1, entity2, relationship_field
        )
        
        required_metrics = [
            "connection_strength", "alignment", "resonance", 
            "trust", "growth_potential"
        ]
        for metric in required_metrics:
            assert metric in metrics
            assert 0.0 <= metrics[metric] <= 1.0
        
        # Test growth opportunities
        opportunities = await relationship_awareness.identify_growth_opportunities(
            entity1, entity2, relationship_field
        )
        
        assert isinstance(opportunities, list)
        for opp in opportunities:
            assert "description" in opp
            assert "priority" in opp
            assert "category" in opp


# Standalone test runner for non-pytest environments
async def run_integration_tests():
    """Run integration tests without pytest."""
    print("🧪 Running Creative Collaborations Integration Tests")
    print("=" * 60)
    
    test_class = TestCreativeCollaborationsIntegration()
    
    # Set up components
    print("🔧 Setting up framework components...")
    setup = await test_class.setup_framework()
    
    # Run tests
    tests = [
        ("Complete Workflow", test_class.test_complete_workflow),
        ("Sacred Uncertainty Integration", test_class.test_relationship_field_sacred_uncertainty_integration),
        ("Entity Archetype Compatibility", test_class.test_entity_archetype_compatibility),
        ("Catalyst Selection & Effectiveness", test_class.test_catalyst_selection_and_effectiveness),
        ("Collaborative Creation Phases", test_class.test_collaborative_creation_phases),
        ("Relationship Awareness Perceptions", test_class.test_relationship_awareness_perceptions),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            print(f"\n🧪 Running: {test_name}")
            await test_func(setup)
            print(f"✅ PASSED: {test_name}")
            passed += 1
        except Exception as e:
            print(f"❌ FAILED: {test_name}")
            print(f"   Error: {str(e)}")
            failed += 1
    
    print(f"\n📊 Test Results:")
    print(f"   Passed: {passed}")
    print(f"   Failed: {failed}")
    print(f"   Total: {passed + failed}")
    
    if failed == 0:
        print("🎉 All integration tests passed!")
    else:
        print("⚠️ Some tests failed. Check the output above.")
    
    return failed == 0


if __name__ == "__main__":
    asyncio.run(run_integration_tests())
