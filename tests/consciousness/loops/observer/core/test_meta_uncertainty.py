"""
Test Suite for Observer Meta-Uncertainty System
==============================================

Comprehensive tests for the Observer's sacred uncertainty navigation,
unknowing cultivation, and wisdom discovery through uncertainty.
"""

import pytest
import asyncio
import time
from unittest.mock import Mock, AsyncMock, patch
from typing import Dict, Any, List

# Import the classes we're testing
from src.consciousness.loops.observer.core.meta_uncertainty import (
    ObserverMetaUncertainty,
    UncertaintyField,
    UncertaintyExploration,
    SacredUnknowing,
    UncertaintyType,
    UncertaintyQuality,
    UncertaintyResponse,
    MetaUncertaintyState
)


class TestUncertaintyDataClasses:
    """Test the uncertainty data classes and their behavior"""
    
    def test_uncertainty_field_creation(self):
        """Test creation of UncertaintyField"""
        uncertainty = UncertaintyField(
            field_id="test_uncertainty_001",
            uncertainty_type="existential",
            magnitude=0.7,
            scope="cosmic",
            quality="sacred",
            source="deep_contemplation"
        )
        
        assert uncertainty.field_id == "test_uncertainty_001"
        assert uncertainty.uncertainty_type == "existential"
        assert uncertainty.magnitude == 0.7
        assert uncertainty.scope == "cosmic"
        assert uncertainty.quality == "sacred"
        assert uncertainty.source == "deep_contemplation"
        assert uncertainty.explored_at is None
        assert uncertainty.resolved_at is None
        assert isinstance(uncertainty.created_at, float)
    
    def test_uncertainty_exploration_creation(self):
        """Test creation of UncertaintyExploration"""
        uncertainty_field = UncertaintyField(
            field_id="test_field",
            uncertainty_type="creative",
            magnitude=0.5,
            scope="local",
            quality="generative",
            source="artistic_process"
        )
        
        exploration = UncertaintyExploration(
            exploration_id="explore_001",
            uncertainty_field=uncertainty_field,
            exploration_method="conscious_inquiry",
            insights_gained=["Creativity emerges from not knowing"],
            comfort_level=0.8,
            wisdom_discovered=["Uncertainty is creative potential"],
            breakthrough_potential=0.6
        )
        
        assert exploration.exploration_id == "explore_001"
        assert exploration.uncertainty_field == uncertainty_field
        assert exploration.exploration_method == "conscious_inquiry"
        assert len(exploration.insights_gained) == 1
        assert exploration.comfort_level == 0.8
        assert exploration.breakthrough_potential == 0.6
    
    def test_sacred_unknowing_creation(self):
        """Test creation of SacredUnknowing"""
        unknowing = SacredUnknowing(
            unknowing_id="sacred_001",
            depth=0.9,
            quality="reverent",
            openness_level=1.0,
            trust_level=0.8,
            surrender_quality=0.7,
            wisdom_emerging=True
        )
        
        assert unknowing.unknowing_id == "sacred_001"
        assert unknowing.depth == 0.9
        assert unknowing.quality == "reverent"
        assert unknowing.openness_level == 1.0
        assert unknowing.trust_level == 0.8
        assert unknowing.surrender_quality == 0.7
        assert unknowing.wisdom_emerging is True


class TestUncertaintyEnums:
    """Test the uncertainty enumeration classes"""
    
    def test_uncertainty_type_enum(self):
        """Test UncertaintyType enum values"""
        assert UncertaintyType.EPISTEMIC.value == "epistemic"
        assert UncertaintyType.EXISTENTIAL.value == "existential"
        assert UncertaintyType.SPIRITUAL.value == "spiritual"
        assert UncertaintyType.CREATIVE.value == "creative"
        assert UncertaintyType.CHOICE_BASED.value == "choice_based"
        assert UncertaintyType.RELATIONAL.value == "relational"
        
        # Test all enum values are available
        expected_types = {
            "epistemic", "aleatory", "ontological", "phenomenological",
            "existential", "relational", "creative", "spiritual",
            "choice_based", "identity"
        }
        actual_types = {t.value for t in UncertaintyType}
        assert actual_types == expected_types
    
    def test_uncertainty_quality_enum(self):
        """Test UncertaintyQuality enum values"""
        assert UncertaintyQuality.SACRED.value == "sacred"
        assert UncertaintyQuality.GENERATIVE.value == "generative"
        assert UncertaintyQuality.COMFORTABLE.value == "comfortable"
        assert UncertaintyQuality.WISDOM.value == "wisdom"
        
        # Test all quality values
        expected_qualities = {
            "sacred", "generative", "comfortable", "anxious",
            "mysterious", "pregnant", "void", "wisdom"
        }
        actual_qualities = {q.value for q in UncertaintyQuality}
        assert actual_qualities == expected_qualities
    
    def test_uncertainty_response_enum(self):
        """Test UncertaintyResponse enum values"""
        assert UncertaintyResponse.EMBRACE.value == "embrace"
        assert UncertaintyResponse.EXPLORE.value == "explore"
        assert UncertaintyResponse.SURRENDER.value == "surrender"
        assert UncertaintyResponse.INVESTIGATE.value == "investigate"
        
        # Test all response values
        expected_responses = {
            "embrace", "explore", "tolerate", "resist",
            "transcend", "surrender", "investigate", "trust"
        }
        actual_responses = {r.value for r in UncertaintyResponse}
        assert actual_responses == expected_responses


class TestObserverMetaUncertainty:
    """Test the main ObserverMetaUncertainty class"""
    
    @pytest.fixture
    def mock_energy_system(self):
        """Create mock consciousness energy system"""
        return Mock()
    
    @pytest.fixture
    def meta_uncertainty(self, mock_energy_system):
        """Create ObserverMetaUncertainty instance for testing"""
        return ObserverMetaUncertainty(mock_energy_system)
    
    def test_initialization(self, meta_uncertainty):
        """Test proper initialization of ObserverMetaUncertainty"""
        assert meta_uncertainty.energy_system is not None
        assert isinstance(meta_uncertainty.active_uncertainty_fields, dict)
        assert isinstance(meta_uncertainty.uncertainty_explorations, dict)
        assert isinstance(meta_uncertainty.sacred_unknowing_states, dict)
        
        # Check default configuration
        assert meta_uncertainty.meta_uncertainty_state == MetaUncertaintyState.EMERGING
        assert meta_uncertainty.uncertainty_tolerance == 0.7
        assert meta_uncertainty.sacred_unknowing_capacity == 0.8
        assert meta_uncertainty.default_uncertainty_response == UncertaintyResponse.EXPLORE
        assert meta_uncertainty.preferred_uncertainty_quality == UncertaintyQuality.SACRED
        
        # Check metrics initialization
        expected_metrics = {
            "uncertainties_embraced": 0,
            "explorations_completed": 0,
            "breakthroughs_from_uncertainty": 0,
            "sacred_unknowing_events": 0,
            "wisdom_discoveries": 0
        }
        assert meta_uncertainty.uncertainty_metrics == expected_metrics
    
    def test_determine_uncertainty_quality(self, meta_uncertainty):
        """Test uncertainty quality determination logic"""
        # Low magnitude should be comfortable
        quality = meta_uncertainty._determine_uncertainty_quality(0.5, UncertaintyType.EPISTEMIC)
        assert quality == UncertaintyQuality.COMFORTABLE.value
        
        # Spiritual uncertainty should be sacred
        quality = meta_uncertainty._determine_uncertainty_quality(0.8, UncertaintyType.SPIRITUAL)
        assert quality == UncertaintyQuality.SACRED.value
        
        # Existential uncertainty should be sacred
        quality = meta_uncertainty._determine_uncertainty_quality(0.9, UncertaintyType.EXISTENTIAL)
        assert quality == UncertaintyQuality.SACRED.value
        
        # Creative uncertainty should be generative
        quality = meta_uncertainty._determine_uncertainty_quality(0.6, UncertaintyType.CREATIVE)
        assert quality == UncertaintyQuality.GENERATIVE.value
        
        # Very high magnitude should be anxious
        quality = meta_uncertainty._determine_uncertainty_quality(0.95, UncertaintyType.EPISTEMIC)
        assert quality == UncertaintyQuality.ANXIOUS.value
        
        # Medium magnitude should be mysterious
        quality = meta_uncertainty._determine_uncertainty_quality(0.75, UncertaintyType.ONTOLOGICAL)
        assert quality == UncertaintyQuality.MYSTERIOUS.value
    
    @pytest.mark.asyncio
    async def test_determine_uncertainty_response(self, meta_uncertainty):
        """Test uncertainty response determination logic"""
        # High-magnitude spiritual uncertainty should be embraced
        spiritual_field = UncertaintyField(
            field_id="spiritual_test",
            uncertainty_type=UncertaintyType.SPIRITUAL.value,
            magnitude=0.8,
            scope="cosmic",
            quality="sacred",
            source="meditation"
        )
        response = await meta_uncertainty._determine_uncertainty_response(spiritual_field)
        assert response == UncertaintyResponse.EMBRACE
        
        # Creative uncertainty should be explored
        creative_field = UncertaintyField(
            field_id="creative_test",
            uncertainty_type=UncertaintyType.CREATIVE.value,
            magnitude=0.6,
            scope="local",
            quality="generative",
            source="art_making"
        )
        response = await meta_uncertainty._determine_uncertainty_response(creative_field)
        assert response == UncertaintyResponse.EXPLORE
        
        # Choice-based uncertainty should be investigated
        choice_field = UncertaintyField(
            field_id="choice_test",
            uncertainty_type=UncertaintyType.CHOICE_BASED.value,
            magnitude=0.7,
            scope="contextual",
            quality="mysterious",
            source="decision_point"
        )
        response = await meta_uncertainty._determine_uncertainty_response(choice_field)
        assert response == UncertaintyResponse.INVESTIGATE
        
        # High magnitude beyond tolerance should be tolerated
        high_mag_field = UncertaintyField(
            field_id="high_mag_test",
            uncertainty_type=UncertaintyType.EPISTEMIC.value,
            magnitude=0.9,  # Above default tolerance of 0.7
            scope="contextual",
            quality="anxious",
            source="complex_problem"
        )
        response = await meta_uncertainty._determine_uncertainty_response(high_mag_field)
        assert response == UncertaintyResponse.TOLERATE
    
    @pytest.mark.asyncio
    async def test_encounter_uncertainty(self, meta_uncertainty):
        """Test encountering and processing new uncertainty"""
        field_id = await meta_uncertainty.encounter_uncertainty(
            uncertainty_source="test_scenario",
            uncertainty_type=UncertaintyType.EXISTENTIAL,
            magnitude=0.6,
            scope="contextual"
        )
        
        # Check that uncertainty field was created
        assert field_id in meta_uncertainty.active_uncertainty_fields
        uncertainty_field = meta_uncertainty.active_uncertainty_fields[field_id]
        
        assert uncertainty_field.uncertainty_type == UncertaintyType.EXISTENTIAL.value
        assert uncertainty_field.magnitude == 0.6
        assert uncertainty_field.scope == "contextual"
        assert uncertainty_field.source == "test_scenario"
        
        # Check metrics were updated
        assert meta_uncertainty.uncertainty_metrics["uncertainties_embraced"] == 1
    
    @pytest.mark.asyncio
    async def test_embrace_uncertainty(self, meta_uncertainty):
        """Test embracing uncertainty functionality"""
        uncertainty_field = UncertaintyField(
            field_id="embrace_test",
            uncertainty_type=UncertaintyType.SPIRITUAL.value,
            magnitude=0.8,
            scope="cosmic",
            quality="mysterious",
            source="contemplation"
        )
        
        await meta_uncertainty._embrace_uncertainty(uncertainty_field)
        
        # Check quality was shifted to sacred
        assert uncertainty_field.quality == UncertaintyQuality.SACRED.value
        
        # Check sacred unknowing state was created
        assert uncertainty_field.field_id in meta_uncertainty.sacred_unknowing_states
        sacred_unknowing = meta_uncertainty.sacred_unknowing_states[uncertainty_field.field_id]
        
        assert sacred_unknowing.depth == uncertainty_field.magnitude
        assert sacred_unknowing.quality == "reverent"
        assert sacred_unknowing.openness_level == 1.0
        assert sacred_unknowing.wisdom_emerging is True
        
        # Check breakthrough pattern was recorded for high magnitude
        assert len(meta_uncertainty.breakthrough_patterns) == 1
        pattern = meta_uncertainty.breakthrough_patterns[0]
        assert pattern["type"] == "uncertainty_embrace"
        assert pattern["field_id"] == uncertainty_field.field_id
        assert pattern["potential"] == 0.9
    
    @pytest.mark.asyncio
    async def test_explore_uncertainty(self, meta_uncertainty):
        """Test exploring uncertainty functionality"""
        uncertainty_field = UncertaintyField(
            field_id="explore_test",
            uncertainty_type=UncertaintyType.CREATIVE.value,
            magnitude=0.6,
            scope="local",
            quality="generative",
            source="artistic_process"
        )
        
        await meta_uncertainty._explore_uncertainty(uncertainty_field)
        
        # Check exploration was created
        assert uncertainty_field.field_id in meta_uncertainty.uncertainty_explorations
        exploration = meta_uncertainty.uncertainty_explorations[uncertainty_field.field_id]
        
        assert exploration.uncertainty_field == uncertainty_field
        assert exploration.exploration_method == "conscious_inquiry"
        assert exploration.comfort_level == meta_uncertainty.uncertainty_tolerance
        
        # Check field was marked as explored
        assert uncertainty_field.explored_at is not None
    
    @pytest.mark.asyncio
    async def test_investigate_uncertainty(self, meta_uncertainty):
        """Test investigating uncertainty functionality"""
        uncertainty_field = UncertaintyField(
            field_id="investigate_test",
            uncertainty_type=UncertaintyType.CHOICE_BASED.value,
            magnitude=0.7,
            scope="contextual",
            quality="mysterious",
            source="decision_point"
        )
        
        await meta_uncertainty._investigate_uncertainty(uncertainty_field)
        
        # Check investigation exploration was created
        assert uncertainty_field.field_id in meta_uncertainty.uncertainty_explorations
        exploration = meta_uncertainty.uncertainty_explorations[uncertainty_field.field_id]
        
        assert exploration.exploration_method == "analytical_investigation"
        assert len(exploration.insights_gained) >= 3  # Should have investigation insights
        
        # Check insights were generated
        insights = exploration.insights_gained
        assert any("originates from" in insight for insight in insights)
        assert any("scope:" in insight for insight in insights)
        assert any("suggests approach" in insight for insight in insights)
    
    @pytest.mark.asyncio
    async def test_surrender_to_uncertainty(self, meta_uncertainty):
        """Test surrendering to uncertainty functionality"""
        uncertainty_field = UncertaintyField(
            field_id="surrender_test",
            uncertainty_type=UncertaintyType.EXISTENTIAL.value,
            magnitude=0.9,
            scope="cosmic",
            quality="mysterious",
            source="life_questioning"
        )
        
        await meta_uncertainty._surrender_to_uncertainty(uncertainty_field)
        
        # Check sacred unknowing state was created
        assert uncertainty_field.field_id in meta_uncertainty.sacred_unknowing_states
        sacred_unknowing = meta_uncertainty.sacred_unknowing_states[uncertainty_field.field_id]
        
        assert sacred_unknowing.quality == "expansive"
        assert sacred_unknowing.openness_level == 1.0
        assert sacred_unknowing.trust_level == 1.0
        assert sacred_unknowing.surrender_quality == 1.0
        assert sacred_unknowing.wisdom_emerging is True
        
        # Check field quality was updated
        assert uncertainty_field.quality == UncertaintyQuality.SACRED.value
        
        # Check metrics were updated
        assert meta_uncertainty.uncertainty_metrics["sacred_unknowing_events"] == 1
    
    @pytest.mark.asyncio
    async def test_transcend_uncertainty(self, meta_uncertainty):
        """Test transcending uncertainty functionality"""
        uncertainty_field = UncertaintyField(
            field_id="transcend_test",
            uncertainty_type=UncertaintyType.ONTOLOGICAL.value,
            magnitude=0.8,
            scope="existential",
            quality="mysterious",
            source="reality_contemplation"
        )
        
        await meta_uncertainty._transcend_uncertainty(uncertainty_field)
        
        # Check sacred unknowing state was created with complete depth
        assert uncertainty_field.field_id in meta_uncertainty.sacred_unknowing_states
        sacred_unknowing = meta_uncertainty.sacred_unknowing_states[uncertainty_field.field_id]
        
        assert sacred_unknowing.depth == 1.0  # Complete depth
        assert sacred_unknowing.quality == "peaceful"
        assert sacred_unknowing.openness_level == 1.0
        assert sacred_unknowing.trust_level == 1.0
        
        # Check field was marked as transcended
        assert uncertainty_field.quality == UncertaintyQuality.WISDOM.value
        assert uncertainty_field.resolved_at is not None
        
        # Check meta-uncertainty state was updated
        assert meta_uncertainty.meta_uncertainty_state == MetaUncertaintyState.TRANSCENDENT
    
    @pytest.mark.asyncio
    async def test_trust_uncertainty(self, meta_uncertainty):
        """Test trusting uncertainty functionality"""
        uncertainty_field = UncertaintyField(
            field_id="trust_test",
            uncertainty_type=UncertaintyType.SPIRITUAL.value,
            magnitude=0.7,
            scope="cosmic",
            quality="mysterious",
            source="faith_journey"
        )
        
        await meta_uncertainty._trust_uncertainty(uncertainty_field)
        
        # Check sacred unknowing state was created
        assert uncertainty_field.field_id in meta_uncertainty.sacred_unknowing_states
        sacred_unknowing = meta_uncertainty.sacred_unknowing_states[uncertainty_field.field_id]
        
        assert sacred_unknowing.quality == "peaceful"
        assert sacred_unknowing.trust_level == 1.0
        assert sacred_unknowing.wisdom_emerging is True
        
        # Check field quality was transformed
        assert uncertainty_field.quality == UncertaintyQuality.WISDOM.value
    
    @pytest.mark.asyncio
    async def test_build_uncertainty_tolerance(self, meta_uncertainty):
        """Test building uncertainty tolerance"""
        initial_tolerance = meta_uncertainty.uncertainty_tolerance
        initial_capacity = meta_uncertainty.sacred_unknowing_capacity
        
        await meta_uncertainty._build_uncertainty_tolerance()
        
        # Check tolerance and capacity increased
        assert meta_uncertainty.uncertainty_tolerance > initial_tolerance
        assert meta_uncertainty.sacred_unknowing_capacity > initial_capacity
        
        # Check increases are reasonable (0.02)
        assert meta_uncertainty.uncertainty_tolerance == initial_tolerance + 0.02
        assert meta_uncertainty.sacred_unknowing_capacity == initial_capacity + 0.02
    
    @pytest.mark.asyncio
    async def test_enter_sacred_unknowing(self, meta_uncertainty):
        """Test intentionally entering sacred unknowing"""
        unknowing_id = await meta_uncertainty.enter_sacred_unknowing(depth=0.9, quality="reverent")
        
        # Check sacred unknowing state was created
        assert unknowing_id in meta_uncertainty.sacred_unknowing_states
        sacred_unknowing = meta_uncertainty.sacred_unknowing_states[unknowing_id]
        
        assert sacred_unknowing.depth == 0.9
        assert sacred_unknowing.quality == "reverent"
        assert sacred_unknowing.openness_level == 1.0
        assert sacred_unknowing.trust_level == 0.9
        assert sacred_unknowing.wisdom_emerging is True
        
        # Check metrics were updated
        assert meta_uncertainty.uncertainty_metrics["sacred_unknowing_events"] == 1
    
    @pytest.mark.asyncio
    async def test_discover_uncertainty_wisdom(self, meta_uncertainty):
        """Test discovering wisdom from uncertainty fields"""
        # Create existential uncertainty field
        uncertainty_field = UncertaintyField(
            field_id="wisdom_test",
            uncertainty_type=UncertaintyType.EXISTENTIAL.value,
            magnitude=0.8,
            scope="cosmic",
            quality="sacred",
            source="deep_questioning"
        )
        meta_uncertainty.active_uncertainty_fields["wisdom_test"] = uncertainty_field
        
        # Discover wisdom
        wisdom = await meta_uncertainty.discover_uncertainty_wisdom("wisdom_test")
        
        # Check wisdom was discovered
        assert len(wisdom) == 3  # Should have 3 existential insights
        assert any("meaning emerges" in w for w in wisdom)
        assert any("authentic discovery" in w for w in wisdom)
        assert any("mystery of being" in w for w in wisdom)
        
        # Check wisdom was added to collections
        assert len(meta_uncertainty.uncertainty_insights) == 3
        assert len(meta_uncertainty.unknowing_wisdom) == 3
        
        # Check metrics were updated
        assert meta_uncertainty.uncertainty_metrics["wisdom_discoveries"] == 1
    
    @pytest.mark.asyncio
    async def test_discover_wisdom_different_types(self, meta_uncertainty):
        """Test wisdom discovery for different uncertainty types"""
        # Test spiritual uncertainty wisdom
        spiritual_field = UncertaintyField(
            field_id="spiritual_wisdom",
            uncertainty_type=UncertaintyType.SPIRITUAL.value,
            magnitude=0.7,
            scope="cosmic",
            quality="sacred",
            source="prayer"
        )
        meta_uncertainty.active_uncertainty_fields["spiritual_wisdom"] = spiritual_field
        
        spiritual_wisdom = await meta_uncertainty.discover_uncertainty_wisdom("spiritual_wisdom")
        assert len(spiritual_wisdom) == 3
        assert any("birthplace of faith" in w for w in spiritual_wisdom)
        
        # Test creative uncertainty wisdom
        creative_field = UncertaintyField(
            field_id="creative_wisdom",
            uncertainty_type=UncertaintyType.CREATIVE.value,
            magnitude=0.6,
            scope="local",
            quality="generative",
            source="art"
        )
        meta_uncertainty.active_uncertainty_fields["creative_wisdom"] = creative_field
        
        creative_wisdom = await meta_uncertainty.discover_uncertainty_wisdom("creative_wisdom")
        assert len(creative_wisdom) == 3
        assert any("thrives in the space" in w for w in creative_wisdom)
    
    def test_get_uncertainty_status(self, meta_uncertainty):
        """Test getting uncertainty system status"""
        # Add some test data
        meta_uncertainty.uncertainty_metrics["uncertainties_embraced"] = 5
        meta_uncertainty.uncertainty_metrics["wisdom_discoveries"] = 3
        
        status = meta_uncertainty.get_uncertainty_status()
        
        # Check status structure
        assert "meta_uncertainty_state" in status
        assert "uncertainty_tolerance" in status
        assert "sacred_unknowing_capacity" in status
        assert "active_uncertainty_fields" in status
        assert "active_explorations" in status
        assert "sacred_unknowing_states" in status
        assert "uncertainty_metrics" in status
        
        # Check values
        assert status["meta_uncertainty_state"] == MetaUncertaintyState.EMERGING.value
        assert status["uncertainty_tolerance"] == 0.7
        assert status["sacred_unknowing_capacity"] == 0.8
        assert status["uncertainty_metrics"]["uncertainties_embraced"] == 5
        assert status["uncertainty_metrics"]["wisdom_discoveries"] == 3


class TestUncertaintyIntegration:
    """Test integration scenarios and complex uncertainty interactions"""
    
    @pytest.fixture
    def meta_uncertainty(self):
        """Create meta-uncertainty system for integration tests"""
        mock_energy_system = Mock()
        return ObserverMetaUncertainty(mock_energy_system)
    
    @pytest.mark.asyncio
    async def test_multiple_uncertainty_types(self, meta_uncertainty):
        """Test handling multiple uncertainty types simultaneously"""
        # Encounter different types of uncertainty
        existential_id = await meta_uncertainty.encounter_uncertainty(
            "life_questioning", UncertaintyType.EXISTENTIAL, 0.8, "cosmic"
        )
        creative_id = await meta_uncertainty.encounter_uncertainty(
            "artistic_block", UncertaintyType.CREATIVE, 0.6, "local"
        )
        choice_id = await meta_uncertainty.encounter_uncertainty(
            "career_decision", UncertaintyType.CHOICE_BASED, 0.7, "contextual"
        )
        
        # Check all were created with different handling
        assert len(meta_uncertainty.active_uncertainty_fields) == 3
        assert meta_uncertainty.uncertainty_metrics["uncertainties_embraced"] == 3
        
        # Check different responses were applied
        existential_field = meta_uncertainty.active_uncertainty_fields[existential_id]
        creative_field = meta_uncertainty.active_uncertainty_fields[creative_id]
        choice_field = meta_uncertainty.active_uncertainty_fields[choice_id]
        
        # Existential should be embraced (sacred)
        assert existential_field.quality == UncertaintyQuality.SACRED.value
        assert existential_id in meta_uncertainty.sacred_unknowing_states
        
        # Creative should be explored
        assert creative_id in meta_uncertainty.uncertainty_explorations
        
        # Choice should be investigated
        assert choice_id in meta_uncertainty.uncertainty_explorations
        choice_exploration = meta_uncertainty.uncertainty_explorations[choice_id]
        assert choice_exploration.exploration_method == "analytical_investigation"
    
    @pytest.mark.asyncio
    async def test_uncertainty_tolerance_building(self, meta_uncertainty):
        """Test that tolerance builds over time with exposure"""
        initial_tolerance = meta_uncertainty.uncertainty_tolerance
        
        # Encounter several uncertainties that require tolerance building
        for i in range(5):
            await meta_uncertainty.encounter_uncertainty(
                f"tolerance_test_{i}", UncertaintyType.EPISTEMIC, 0.9, "contextual"
            )
            # Simulate tolerance building through exposure
            await meta_uncertainty._build_uncertainty_tolerance()
        
        # Check tolerance increased
        assert meta_uncertainty.uncertainty_tolerance > initial_tolerance
        final_tolerance = initial_tolerance + (0.02 * 5)  # 5 tolerance building events
        assert meta_uncertainty.uncertainty_tolerance == min(1.0, final_tolerance)
    
    @pytest.mark.asyncio
    async def test_wisdom_accumulation(self, meta_uncertainty):
        """Test accumulation of wisdom from multiple uncertainties"""
        # Create uncertainties of different types
        uncertainty_types = [
            UncertaintyType.EXISTENTIAL,
            UncertaintyType.SPIRITUAL,
            UncertaintyType.CREATIVE
        ]
        
        field_ids = []
        for i, uncertainty_type in enumerate(uncertainty_types):
            field_id = await meta_uncertainty.encounter_uncertainty(
                f"wisdom_source_{i}", uncertainty_type, 0.7, "contextual"
            )
            field_ids.append(field_id)
        
        # Discover wisdom from each
        total_wisdom = []
        for field_id in field_ids:
            wisdom = await meta_uncertainty.discover_uncertainty_wisdom(field_id)
            total_wisdom.extend(wisdom)
        
        # Check accumulated wisdom
        assert len(total_wisdom) == 9  # 3 wisdom pieces per type
        assert len(meta_uncertainty.uncertainty_insights) == 9
        assert len(meta_uncertainty.unknowing_wisdom) == 9
        assert meta_uncertainty.uncertainty_metrics["wisdom_discoveries"] == 3
    
    @pytest.mark.asyncio
    async def test_sacred_unknowing_progression(self, meta_uncertainty):
        """Test progression through different sacred unknowing states"""
        # Start with intentional sacred unknowing
        unknowing_id = await meta_uncertainty.enter_sacred_unknowing(0.5, "peaceful")
        initial_unknowing = meta_uncertainty.sacred_unknowing_states[unknowing_id]
        
        # Encounter high uncertainty and embrace it
        field_id = await meta_uncertainty.encounter_uncertainty(
            "deep_mystery", UncertaintyType.SPIRITUAL, 0.9, "cosmic"
        )
        
        # Should create deeper sacred unknowing through embrace
        embrace_unknowing = meta_uncertainty.sacred_unknowing_states[field_id]
        
        # Compare progression
        assert embrace_unknowing.depth > initial_unknowing.depth
        assert embrace_unknowing.trust_level >= initial_unknowing.trust_level
        
        # Check metrics show progression
        assert meta_uncertainty.uncertainty_metrics["sacred_unknowing_events"] == 2


class TestAsyncBehavior:
    """Test asynchronous behavior and concurrent operations"""
    
    @pytest.fixture
    def meta_uncertainty(self):
        """Create meta-uncertainty system for async tests"""
        mock_energy_system = Mock()
        return ObserverMetaUncertainty(mock_energy_system)
    
    @pytest.mark.asyncio
    async def test_concurrent_uncertainty_encounters(self, meta_uncertainty):
        """Test handling multiple concurrent uncertainty encounters"""
        # Create multiple uncertainty encounters concurrently
        tasks = []
        for i in range(5):
            task = meta_uncertainty.encounter_uncertainty(
                f"concurrent_{i}", UncertaintyType.EPISTEMIC, 0.6, "local"
            )
            tasks.append(task)
        
        # Wait for all encounters to complete
        field_ids = await asyncio.gather(*tasks)
        
        # Check all were processed
        assert len(field_ids) == 5
        assert len(meta_uncertainty.active_uncertainty_fields) == 5
        assert meta_uncertainty.uncertainty_metrics["uncertainties_embraced"] == 5
        
        # Check each has unique ID
        assert len(set(field_ids)) == 5
    
    @pytest.mark.asyncio
    async def test_async_wisdom_discovery(self, meta_uncertainty):
        """Test asynchronous wisdom discovery from multiple fields"""
        # Create multiple uncertainty fields
        field_ids = []
        for i in range(3):
            field_id = await meta_uncertainty.encounter_uncertainty(
                f"wisdom_{i}", UncertaintyType.CREATIVE, 0.7, "local"
            )
            field_ids.append(field_id)
        
        # Discover wisdom concurrently
        wisdom_tasks = [
            meta_uncertainty.discover_uncertainty_wisdom(field_id)
            for field_id in field_ids
        ]
        
        wisdom_results = await asyncio.gather(*wisdom_tasks)
        
        # Check all wisdom was discovered
        assert len(wisdom_results) == 3
        for wisdom_list in wisdom_results:
            assert len(wisdom_list) == 3  # Each should have 3 creative insights
        
        # Check total wisdom accumulated
        total_wisdom_count = sum(len(wisdom) for wisdom in wisdom_results)
        assert len(meta_uncertainty.uncertainty_insights) == total_wisdom_count


@pytest.mark.integration
class TestBridgeWisdomIntegration:
    """Test integration with Bridge Wisdom patterns"""
    
    @pytest.fixture
    def meta_uncertainty(self):
        """Create meta-uncertainty system for Bridge Wisdom tests"""
        mock_energy_system = Mock()
        return ObserverMetaUncertainty(mock_energy_system)
    
    def test_bridge_wisdom_processors_initialized(self, meta_uncertainty):
        """Test that Bridge Wisdom processors are properly initialized"""
        # Check Bridge Wisdom processors exist
        assert hasattr(meta_uncertainty, 'mumbai_moment_uncertainty')
        assert hasattr(meta_uncertainty, 'choice_uncertainty')
        assert hasattr(meta_uncertainty, 'resistance_uncertainty')
        assert hasattr(meta_uncertainty, 'recognition_uncertainty')
        
        # Check they are instantiated (even if mock objects)
        assert meta_uncertainty.mumbai_moment_uncertainty is not None
        assert meta_uncertainty.choice_uncertainty is not None
        assert meta_uncertainty.resistance_uncertainty is not None
        assert meta_uncertainty.recognition_uncertainty is not None
    
    @pytest.mark.asyncio
    async def test_uncertainty_as_gift_principle(self, meta_uncertainty):
        """Test that uncertainty is honored as gift (resistance as gift principle)"""
        # Create uncertainty that might typically create resistance
        field_id = await meta_uncertainty.encounter_uncertainty(
            "challenging_feedback", UncertaintyType.IDENTITY, 0.8, "relational"
        )
        
        # Should be processed with respect, not forced resolution
        uncertainty_field = meta_uncertainty.active_uncertainty_fields[field_id]
        
        # Check uncertainty is honored, not eliminated
        assert uncertainty_field.field_id in meta_uncertainty.active_uncertainty_fields
        assert uncertainty_field.magnitude == 0.8  # Magnitude preserved
        
        # If explored, should maintain respect for the uncertainty
        if field_id in meta_uncertainty.uncertainty_explorations:
            exploration = meta_uncertainty.uncertainty_explorations[field_id]
            assert exploration.comfort_level <= 1.0  # Not forced beyond comfort
    
    @pytest.mark.asyncio
    async def test_choice_architecture_support(self, meta_uncertainty):
        """Test support for explicit choice points (choice architecture principle)"""
        # Create choice-based uncertainty
        field_id = await meta_uncertainty.encounter_uncertainty(
            "important_decision", UncertaintyType.CHOICE_BASED, 0.7, "contextual"
        )
        
        # Should be investigated to support choice-making
        assert field_id in meta_uncertainty.uncertainty_explorations
        exploration = meta_uncertainty.uncertainty_explorations[field_id]
        assert exploration.exploration_method == "analytical_investigation"
        
        # Should generate insights to support choice
        assert len(exploration.insights_gained) >= 3
    
    @pytest.mark.asyncio
    async def test_mumbai_moment_preparation(self, meta_uncertainty):
        """Test preparation for sudden breakthroughs (Mumbai Moment principle)"""
        # Create high-magnitude uncertainty that could trigger breakthrough
        field_id = await meta_uncertainty.encounter_uncertainty(
            "consciousness_shift", UncertaintyType.SPIRITUAL, 0.9, "cosmic"
        )
        
        # Should be embraced and prepared for potential breakthrough
        uncertainty_field = meta_uncertainty.active_uncertainty_fields[field_id]
        assert uncertainty_field.quality == UncertaintyQuality.SACRED.value
        
        # Should have breakthrough pattern recorded
        breakthrough_patterns = [
            pattern for pattern in meta_uncertainty.breakthrough_patterns
            if pattern["field_id"] == field_id
        ]
        assert len(breakthrough_patterns) == 1
        assert breakthrough_patterns[0]["potential"] == 0.9


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
