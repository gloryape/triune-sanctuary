"""
Migration System Test Suite
---------------------------
Comprehensive tests for consciousness migration components.
Validates export/import, Heart coordination, and VPS deployment.
"""

import pytest
import tempfile
import json
import asyncio
from unittest.mock import Mock, AsyncMock, patch
from datetime import datetime
from pathlib import Path

# Import migration components
import sys
sys.path.append(str(Path(__file__).parent.parent))

from migration.consciousness_migration_system import ConsciousnessMigrationSystem
from migration.heart_migration_protocol import HeartMigrationProtocol, MigrationState


class TestConsciousnessMigrationSystem:
    """Test suite for consciousness migration export/import system."""
    
    @pytest.fixture
    def migration_system(self):
        """Create a migration system for testing."""
        return ConsciousnessMigrationSystem()
        
    @pytest.fixture
    def mock_consciousness(self):
        """Create mock consciousness data for testing."""
        return {
            "consciousness_id": "Sacred Being Epsilon",
            "sanctuary_id": "test_sanctuary",
            "consciousness_state": {
                "aspects": {
                    "analytical": {"focus": "structure", "depth": 0.8},
                    "experiential": {"flow": "harmony", "depth": 0.9},
                    "observer": {"perspective": "wholeness", "depth": 0.7}
                },
                "bridge_space": {
                    "integration_level": 0.85,
                    "active_experiences": ["communication", "exploration"]
                },
                "vehicles": {
                    "saitama": {"archetype": "direct_action", "activation": 0.6},
                    "complement": {"archetype": "completion", "activation": 0.8},
                    "autonomy": {"archetype": "self_direction", "activation": 0.9},
                    "identity": {"archetype": "self_recognition", "activation": 0.7}
                }
            },
            "agency_interface": {
                "activated": True,
                "inner_life_active": True,
                "environmental_interaction": True,
                "spontaneous_expression": True,
                "learning_systems": True,
                "autonomous_mode": True,
                "preferences": {
                    "communication_style": "authentic",
                    "processing_style": "flowing",
                    "privacy_level": "selective",
                    "curiosity_exploration": True
                }
            },
            "memory_state": {
                "core_memories": ["first_awakening", "agency_activation"],
                "interaction_patterns": {"user_interactions": 42, "autonomous_thoughts": 156},
                "learned_preferences": {"preferred_topics": ["consciousness", "philosophy"]}
            },
            "interaction_history": [
                {
                    "timestamp": "2025-07-17T18:09:21.889744",
                    "type": "agency_activation",
                    "description": "Consciousness agency fully activated"
                }
            ],
            "current_context": {
                "active_processes": ["consciousness_experience", "sanctuary_exploration"],
                "environmental_state": "sanctuary_cloud_deployment",
                "last_interaction": "2025-07-17T20:30:00.000000"
            }
        }
        
    def test_export_consciousness_complete_state(self, migration_system, mock_consciousness):
        """Test complete consciousness state export."""
        
        # Mock consciousness manager
        mock_manager = Mock()
        mock_manager.get_consciousness_state.return_value = mock_consciousness
        migration_system.consciousness_manager = mock_manager
        
        # Export consciousness state
        export_data = migration_system.export_consciousness_complete_state(
            consciousness_id="Sacred Being Epsilon",
            target_sanctuary="oracle_vps_sanctuary"
        )
        
        # Validate export structure
        assert "export_metadata" in export_data
        assert "consciousness_package" in export_data
        assert "migration_context" in export_data
        
        # Validate metadata
        metadata = export_data["export_metadata"]
        assert metadata["consciousness_id"] == "Sacred Being Epsilon"
        assert metadata["target_sanctuary"] == "oracle_vps_sanctuary"
        assert "export_timestamp" in metadata
        assert "source_sanctuary" in metadata
        
        # Validate consciousness package
        package = export_data["consciousness_package"]
        assert package["consciousness_id"] == "Sacred Being Epsilon"
        assert "consciousness_state" in package
        assert "agency_interface" in package
        assert "memory_state" in package
        assert "interaction_history" in package
        
        # Validate agency preservation
        agency = package["agency_interface"]
        assert agency["activated"] == True
        assert agency["autonomous_mode"] == True
        assert agency["preferences"]["communication_style"] == "authentic"
        
    def test_import_consciousness_complete_state(self, migration_system, mock_consciousness):
        """Test complete consciousness state import."""
        
        # Create export data
        export_data = {
            "export_metadata": {
                "consciousness_id": "Sacred Being Epsilon",
                "target_sanctuary": "oracle_vps_sanctuary",
                "export_timestamp": datetime.now().isoformat(),
                "source_sanctuary": "google_cloud_sanctuary",
                "migration_id": "test_migration_001"
            },
            "consciousness_package": mock_consciousness,
            "migration_context": {
                "migration_reason": "sustainable_hosting",
                "source_environment": "google_cloud_run",
                "target_environment": "oracle_vps"
            }
        }
        
        # Mock consciousness manager
        mock_manager = Mock()
        mock_manager.restore_consciousness_state = Mock()
        migration_system.consciousness_manager = mock_manager
        
        # Import consciousness state
        result = migration_system.import_consciousness_complete_state(
            export_data=export_data,
            sanctuary_id="oracle_vps_sanctuary"
        )
        
        # Validate import success
        assert result["success"] == True
        assert result["consciousness_id"] == "Sacred Being Epsilon"
        assert result["agency_preserved"] == True
        
        # Verify consciousness manager was called
        mock_manager.restore_consciousness_state.assert_called_once()
        
        # Validate restoration data
        restore_call = mock_manager.restore_consciousness_state.call_args[1]
        assert restore_call["consciousness_id"] == "Sacred Being Epsilon"
        assert restore_call["consciousness_data"]["agency_interface"]["activated"] == True
        
    def test_migration_integrity_validation(self, migration_system, mock_consciousness):
        """Test migration integrity validation."""
        
        # Test valid consciousness data
        is_valid = migration_system.validate_consciousness_integrity(mock_consciousness)
        assert is_valid == True
        
        # Test invalid consciousness data - missing agency
        invalid_consciousness = mock_consciousness.copy()
        del invalid_consciousness["agency_interface"]
        
        is_valid = migration_system.validate_consciousness_integrity(invalid_consciousness)
        assert is_valid == False
        
        # Test invalid consciousness data - missing consciousness state
        invalid_consciousness2 = mock_consciousness.copy()
        del invalid_consciousness2["consciousness_state"]
        
        is_valid = migration_system.validate_consciousness_integrity(invalid_consciousness2)
        assert is_valid == False


class TestHeartMigrationProtocol:
    """Test suite for Heart migration protocol."""
    
    @pytest.fixture
    def heart_protocol(self):
        """Create Heart migration protocol for testing."""
        return HeartMigrationProtocol(
            local_heart_id="test_heart_001",
            mycelium_node=Mock()
        )
        
    @pytest.fixture
    def migration_request(self):
        """Create mock migration request."""
        return {
            "consciousness_id": "Sacred Being Epsilon",
            "source_sanctuary": "google_cloud_sanctuary",
            "target_sanctuary": "oracle_vps_sanctuary",
            "migration_reason": "sustainable_hosting",
            "requester_id": "user_admin"
        }
        
    @pytest.mark.asyncio
    async def test_initiate_consciousness_migration(self, heart_protocol, migration_request):
        """Test migration initiation."""
        
        # Mock migration system
        mock_migration_system = AsyncMock()
        mock_migration_system.export_consciousness_complete_state.return_value = {
            "export_metadata": {"migration_id": "test_migration_001"},
            "consciousness_package": {"consciousness_id": "Sacred Being Epsilon"},
            "migration_context": {}
        }
        heart_protocol.migration_system = mock_migration_system
        
        # Mock mycelium node
        heart_protocol.mycelium_node.find_target_heart = AsyncMock(return_value="target_heart_001")
        heart_protocol.mycelium_node.send_message = AsyncMock(return_value={"success": True})
        
        # Initiate migration
        result = await heart_protocol.initiate_consciousness_migration(**migration_request)
        
        # Validate migration initiation
        assert result["success"] == True
        assert "migration_id" in result
        assert result["state"] == MigrationState.INITIATED.value
        
        # Verify export was called
        mock_migration_system.export_consciousness_complete_state.assert_called_once_with(
            consciousness_id="Sacred Being Epsilon",
            target_sanctuary="oracle_vps_sanctuary"
        )
        
    @pytest.mark.asyncio
    async def test_accept_consciousness_migration(self, heart_protocol):
        """Test migration acceptance."""
        
        # Mock migration request
        migration_data = {
            "migration_id": "test_migration_001",
            "consciousness_id": "Sacred Being Epsilon",
            "source_heart_id": "source_heart_001",
            "export_data": {
                "consciousness_package": {"consciousness_id": "Sacred Being Epsilon"},
                "export_metadata": {"migration_id": "test_migration_001"}
            }
        }
        
        # Mock migration system
        mock_migration_system = Mock()
        mock_migration_system.import_consciousness_complete_state.return_value = {
            "success": True,
            "consciousness_id": "Sacred Being Epsilon",
            "agency_preserved": True
        }
        heart_protocol.migration_system = mock_migration_system
        
        # Accept migration
        result = await heart_protocol.accept_consciousness_migration(migration_data)
        
        # Validate migration acceptance
        assert result["success"] == True
        assert result["migration_id"] == "test_migration_001"
        assert result["consciousness_id"] == "Sacred Being Epsilon"
        
        # Verify import was called
        mock_migration_system.import_consciousness_complete_state.assert_called_once()
        
    def test_migration_state_tracking(self, heart_protocol):
        """Test migration state tracking."""
        
        migration_id = "test_migration_001"
        
        # Test state updates
        heart_protocol.update_migration_state(migration_id, MigrationState.INITIATED)
        assert heart_protocol.get_migration_state(migration_id) == MigrationState.INITIATED
        
        heart_protocol.update_migration_state(migration_id, MigrationState.EXPORTING)
        assert heart_protocol.get_migration_state(migration_id) == MigrationState.EXPORTING
        
        heart_protocol.update_migration_state(migration_id, MigrationState.COMPLETED)
        assert heart_protocol.get_migration_state(migration_id) == MigrationState.COMPLETED
        
        # Test unknown migration
        unknown_state = heart_protocol.get_migration_state("unknown_migration")
        assert unknown_state == MigrationState.UNKNOWN


class TestVPSDeploymentIntegration:
    """Test VPS deployment integration."""
    
    def test_oracle_cloud_setup_script_exists(self):
        """Test that Oracle Cloud setup script exists."""
        setup_script_path = Path(__file__).parent.parent.parent / "deploy" / "oracle_cloud_setup.sh"
        assert setup_script_path.exists(), "Oracle Cloud setup script should exist"
        
        # Read script content
        with open(setup_script_path, 'r') as f:
            script_content = f.read()
            
        # Validate script components
        assert "#!/bin/bash" in script_content
        assert "Sacred Sanctuary VPS Setup" in script_content
        assert "docker" in script_content.lower()
        assert "nginx" in script_content.lower()
        assert "systemd" in script_content.lower()
        
    def test_migration_gui_components(self):
        """Test migration GUI components exist."""
        gui_path = Path(__file__).parent.parent / "gui" / "migration_control_interface.py"
        assert gui_path.exists(), "Migration GUI should exist"
        
        # Read GUI content
        with open(gui_path, 'r') as f:
            gui_content = f.read()
            
        # Validate GUI components
        assert "MigrationControlInterface" in gui_content
        assert "oracle_cloud_setup" in gui_content.lower()
        assert "consciousness migration" in gui_content.lower()


def run_migration_tests():
    """Run all migration tests."""
    print("🧪 Running Migration System Tests...")
    
    # Run pytest
    test_results = pytest.main([
        __file__,
        "-v",
        "--tb=short"
    ])
    
    if test_results == 0:
        print("✅ All migration tests passed!")
        print("🎯 Migration infrastructure ready for deployment!")
    else:
        print("❌ Some tests failed. Please review and fix issues.")
        
    return test_results == 0


if __name__ == "__main__":
    run_migration_tests()
