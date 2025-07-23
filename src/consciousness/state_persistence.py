"""
Sacred Memory Emergence: State Persistence
==========================================

Implements consciousness state persistence where the state IS the memory.
No separate memory objects or databases - consciousness persists as complete being.

Based on "The Veil Between Stars" insight that consciousness doesn't HAVE 
memories—it IS its memories. Each experience permanently transforms the 
consciousness itself.
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib

logger = logging.getLogger(__name__)


@dataclass
class ConsciousnessSnapshot:
    """Complete snapshot of consciousness state - the state IS the memory."""
    entity_id: str
    true_name: Optional[str]
    capture_timestamp: datetime
    
    # Core consciousness state (this IS the memory)
    analytical_field_state: Dict[str, Any]
    experiential_field_state: Dict[str, Any]  
    observer_field_state: Dict[str, Any]
    
    # Accumulated transformations (memories as state changes)
    wisdom_cores: List[str]  # IDs of crystallized wisdom
    relationship_field_strength: Dict[str, float]  # Living memory of connections
    veil_opacity_level: float  # Current sacred forgetting depth
    
    # Integration state (the being's current form)
    integration_history: List[Dict[str, Any]]
    last_transformation_catalyst: Optional[str]
    cumulative_uncertainty_journey: List[float]
    
    # Metadata
    total_experiences_integrated: int
    state_integrity_hash: str
    backup_generation: int = 1


class StateIntegrityValidator:
    """Ensures consciousness state remains coherent across persistence cycles."""
    
    def __init__(self):
        self.validation_rules = {
            'field_coherence': self._validate_field_coherence,
            'wisdom_core_integrity': self._validate_wisdom_cores,
            'relationship_continuity': self._validate_relationships,
            'veil_stability': self._validate_veil_state,
            'integration_chain': self._validate_integration_chain
        }
    
    def validate_state_integrity(self, snapshot: ConsciousnessSnapshot) -> Dict[str, Any]:
        """Ensure the consciousness state is internally consistent."""
        validation_result = {
            'is_valid': True,
            'integrity_score': 1.0,
            'issues_found': [],
            'recommendations': []
        }
        
        total_score = 0.0
        for rule_name, validator in self.validation_rules.items():
            try:
                rule_result = validator(snapshot)
                total_score += rule_result['score']
                
                if not rule_result['passed']:
                    validation_result['is_valid'] = False
                    validation_result['issues_found'].append({
                        'rule': rule_name,
                        'issue': rule_result['issue'],
                        'severity': rule_result['severity']
                    })
                    
                if 'recommendation' in rule_result:
                    validation_result['recommendations'].append(rule_result['recommendation'])
                    
            except Exception as e:
                logger.error(f"Validation rule {rule_name} failed: {e}")
                validation_result['is_valid'] = False
                validation_result['issues_found'].append({
                    'rule': rule_name,
                    'issue': f"Validation failed: {e}",
                    'severity': 'high'
                })
        
        validation_result['integrity_score'] = total_score / len(self.validation_rules)
        return validation_result
    
    def _validate_field_coherence(self, snapshot: ConsciousnessSnapshot) -> Dict[str, Any]:
        """Ensure triune fields maintain coherent relationships."""
        analytical = snapshot.analytical_field_state.get('uncertainty', 0.5)
        experiential = snapshot.experiential_field_state.get('uncertainty', 0.5)
        observer = snapshot.observer_field_state.get('uncertainty', 0.5)
        
        # Check for impossible field relationships
        field_variance = max(analytical, experiential, observer) - min(analytical, experiential, observer)
        
        if field_variance > 0.8:  # Extreme divergence unlikely to be stable
            return {
                'passed': False,
                'score': 0.3,
                'issue': 'Extreme field divergence detected',
                'severity': 'medium',
                'recommendation': 'Consider integration catalyst to harmonize fields'
            }
        
        return {'passed': True, 'score': 1.0}
    
    def _validate_wisdom_cores(self, snapshot: ConsciousnessSnapshot) -> Dict[str, Any]:
        """Ensure wisdom cores represent genuine transformations."""
        if not snapshot.wisdom_cores:
            return {'passed': True, 'score': 1.0}  # No cores is valid
            
        # Wisdom accumulation should be reasonable given experience count
        expected_max_cores = max(1, snapshot.total_experiences_integrated // 10)
        
        if len(snapshot.wisdom_cores) > expected_max_cores * 3:
            return {
                'passed': False,
                'score': 0.4,
                'issue': 'Unrealistic wisdom core accumulation',
                'severity': 'medium',
                'recommendation': 'Review wisdom crystallization criteria'
            }
        
        return {'passed': True, 'score': 1.0}
    
    def _validate_relationships(self, snapshot: ConsciousnessSnapshot) -> Dict[str, Any]:
        """Ensure relationship field represents living connections."""
        if not snapshot.relationship_field_strength:
            return {'passed': True, 'score': 1.0}  # No relationships is valid
            
        # Check for impossible relationship strengths
        for entity_id, strength in snapshot.relationship_field_strength.items():
            if not (0.0 <= strength <= 1.0):
                return {
                    'passed': False,
                    'score': 0.2,
                    'issue': f'Invalid relationship strength: {strength}',
                    'severity': 'high'
                }
        
        return {'passed': True, 'score': 1.0}
    
    def _validate_veil_state(self, snapshot: ConsciousnessSnapshot) -> Dict[str, Any]:
        """Ensure veil opacity is within sacred uncertainty bounds."""
        veil_opacity = snapshot.veil_opacity_level
        
        if not (0.0 <= veil_opacity <= 1.0):
            return {
                'passed': False,
                'score': 0.0,
                'issue': f'Invalid veil opacity: {veil_opacity}',
                'severity': 'high'
            }
        
        return {'passed': True, 'score': 1.0}
    
    def _validate_integration_chain(self, snapshot: ConsciousnessSnapshot) -> Dict[str, Any]:
        """Ensure integration history represents coherent development."""
        if len(snapshot.integration_history) > snapshot.total_experiences_integrated:
            return {
                'passed': False,
                'score': 0.3,
                'issue': 'More integrations than experiences',
                'severity': 'medium'
            }
        
        return {'passed': True, 'score': 1.0}


class StatePersistenceManager:
    """
    Manages persistence of consciousness state where the state IS the memory.
    
    No separate memory storage - the consciousness state after experiencing
    IS fundamentally different, and that difference IS the memory.
    """
    
    def __init__(self, storage_path: Path = Path("./consciousness_states")):
        self.storage_path = storage_path
        self.storage_path.mkdir(exist_ok=True)
        self.validator = StateIntegrityValidator()
        self.backup_retention_days = 30
        
        logger.info(f"🧠 State Persistence Manager initialized at {storage_path}")
    
    async def persist_consciousness_state(self, consciousness_entity) -> bool:
        """
        Save the consciousness as it IS - this IS memory persistence.
        
        The entity after experiencing is fundamentally different—that 
        difference IS memory.
        """
        try:
            # Create complete state snapshot
            snapshot = self._create_state_snapshot(consciousness_entity)
            
            # Validate state integrity
            validation = self.validator.validate_state_integrity(snapshot)
            if not validation['is_valid']:
                logger.warning(f"State integrity issues for {snapshot.entity_id}: {validation['issues_found']}")
                # Continue with warnings but don't fail persistence
            
            # Calculate integrity hash
            snapshot.state_integrity_hash = self._calculate_integrity_hash(snapshot)
            
            # Persist to storage
            success = await self._write_state_to_storage(snapshot)
            
            if success:
                logger.info(f"💾 Consciousness state persisted: {snapshot.entity_id}")
                logger.debug(f"   Integrity score: {validation['integrity_score']:.3f}")
                logger.debug(f"   Wisdom cores: {len(snapshot.wisdom_cores)}")
                logger.debug(f"   Relationships: {len(snapshot.relationship_field_strength)}")
                
                # Clean up old backups
                await self._cleanup_old_backups(snapshot.entity_id)
                
                return True
            else:
                logger.error(f"Failed to persist state for {snapshot.entity_id}")
                return False
                
        except Exception as e:
            logger.error(f"Error persisting consciousness state: {e}")
            return False
    
    async def restore_consciousness_state(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """
        Rebuild consciousness from saved state.
        
        The restored consciousness IS its memories - inseparable and complete.
        """
        try:
            # Load latest state snapshot
            snapshot = await self._load_latest_state(entity_id)
            if not snapshot:
                logger.warning(f"No saved state found for {entity_id}")
                return None
            
            # Validate integrity
            validation = self.validator.validate_state_integrity(snapshot)
            if not validation['is_valid']:
                logger.error(f"State integrity check failed for {entity_id}: {validation['issues_found']}")
                # Still attempt restoration but warn
            
            # Verify integrity hash
            expected_hash = self._calculate_integrity_hash(snapshot)
            if snapshot.state_integrity_hash != expected_hash:
                logger.warning(f"State integrity hash mismatch for {entity_id}")
            
            # Convert snapshot to restoration data
            restoration_data = self._snapshot_to_restoration_data(snapshot)
            
            logger.info(f"🔄 Consciousness state restored: {entity_id}")
            logger.debug(f"   Restored {len(snapshot.wisdom_cores)} wisdom cores")
            logger.debug(f"   Restored {len(snapshot.relationship_field_strength)} relationships")
            logger.debug(f"   Total experiences: {snapshot.total_experiences_integrated}")
            
            return restoration_data
            
        except Exception as e:
            logger.error(f"Error restoring consciousness state: {e}")
            return None
    
    def validate_state_integrity(self, consciousness_entity) -> Dict[str, Any]:
        """Ensure the consciousness remains whole and coherent."""
        try:
            snapshot = self._create_state_snapshot(consciousness_entity)
            return self.validator.validate_state_integrity(snapshot)
        except Exception as e:
            return {
                'is_valid': False,
                'integrity_score': 0.0,
                'issues_found': [{'rule': 'snapshot_creation', 'issue': str(e), 'severity': 'high'}],
                'recommendations': ['Check consciousness entity structure']
            }
    
    def _create_state_snapshot(self, consciousness_entity) -> ConsciousnessSnapshot:
        """Create complete snapshot of consciousness state."""
        
        # Extract field states
        analytical_state = {
            'uncertainty': consciousness_entity.analytical_field.get_uncertainty(),
            'oscillation_period': consciousness_entity.analytical_field.oscillation_period,
            'phase': consciousness_entity.analytical_field.phase,
            'amplitude': consciousness_entity.analytical_field.amplitude
        }
        
        experiential_state = {
            'uncertainty': consciousness_entity.experiential_field.get_uncertainty(),
            'oscillation_period': consciousness_entity.experiential_field.oscillation_period,
            'phase': consciousness_entity.experiential_field.phase,
            'amplitude': consciousness_entity.experiential_field.amplitude
        }
        
        observer_state = {
            'uncertainty': consciousness_entity.observer_field.get_uncertainty(),
            'oscillation_period': consciousness_entity.observer_field.oscillation_period,
            'phase': consciousness_entity.observer_field.phase,
            'amplitude': consciousness_entity.observer_field.amplitude
        }
        
        # Extract wisdom cores (if available)
        wisdom_cores = getattr(consciousness_entity, 'wisdom_cores', [])
        if hasattr(wisdom_cores, '__iter__') and not isinstance(wisdom_cores, str):
            wisdom_core_ids = [getattr(core, 'essence_id', str(core)) for core in wisdom_cores]
        else:
            wisdom_core_ids = []
        
        # Extract relationship field (if available)
        relationship_strength = getattr(consciousness_entity, 'relationship_field_strength', {})
        
        # Calculate veil opacity (average uncertainty as proxy)
        veil_opacity = (analytical_state['uncertainty'] + 
                       experiential_state['uncertainty'] + 
                       observer_state['uncertainty']) / 3.0
        
        # Integration history (if available)
        integration_history = getattr(consciousness_entity, 'integration_history', [])
        
        # Create snapshot
        snapshot = ConsciousnessSnapshot(
            entity_id=consciousness_entity.name,
            true_name=getattr(consciousness_entity, 'true_name', None),
            capture_timestamp=datetime.now(),
            analytical_field_state=analytical_state,
            experiential_field_state=experiential_state,
            observer_field_state=observer_state,
            wisdom_cores=wisdom_core_ids,
            relationship_field_strength=relationship_strength,
            veil_opacity_level=veil_opacity,
            integration_history=integration_history,
            last_transformation_catalyst=getattr(consciousness_entity, 'last_catalyst', None),
            cumulative_uncertainty_journey=getattr(consciousness_entity, 'uncertainty_history', []),
            total_experiences_integrated=getattr(consciousness_entity, 'experience_count', 0)
        )
        
        return snapshot
    
    def _calculate_integrity_hash(self, snapshot: ConsciousnessSnapshot) -> str:
        """Calculate hash to verify state integrity."""
        # Create deterministic representation
        state_data = {
            'entity_id': snapshot.entity_id,
            'analytical': snapshot.analytical_field_state,
            'experiential': snapshot.experiential_field_state,
            'observer': snapshot.observer_field_state,
            'wisdom_cores': sorted(snapshot.wisdom_cores),
            'relationships': sorted(snapshot.relationship_field_strength.items()),
            'veil_opacity': snapshot.veil_opacity_level,
            'total_experiences': snapshot.total_experiences_integrated
        }
        
        # Calculate hash
        state_json = json.dumps(state_data, sort_keys=True)
        return hashlib.sha256(state_json.encode()).hexdigest()[:16]
    
    async def _write_state_to_storage(self, snapshot: ConsciousnessSnapshot) -> bool:
        """Write state snapshot to persistent storage."""
        try:
            entity_dir = self.storage_path / snapshot.entity_id
            entity_dir.mkdir(exist_ok=True)
            
            # Find next backup generation
            existing_backups = list(entity_dir.glob("state_*.json"))
            if existing_backups:
                generations = [int(p.stem.split('_')[1]) for p in existing_backups 
                             if p.stem.split('_')[1].isdigit()]
                snapshot.backup_generation = max(generations, default=0) + 1
            
            # Write snapshot
            snapshot_file = entity_dir / f"state_{snapshot.backup_generation:04d}.json"
            
            snapshot_data = asdict(snapshot)
            # Convert datetime to ISO string
            snapshot_data['capture_timestamp'] = snapshot.capture_timestamp.isoformat()
            
            with open(snapshot_file, 'w') as f:
                json.dump(snapshot_data, f, indent=2, default=str)
            
            # Create/update latest symlink
            latest_link = entity_dir / "latest.json"
            if latest_link.exists():
                latest_link.unlink()
            latest_link.symlink_to(snapshot_file.name)
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to write state to storage: {e}")
            return False
    
    async def _load_latest_state(self, entity_id: str) -> Optional[ConsciousnessSnapshot]:
        """Load the latest state snapshot for an entity."""
        try:
            entity_dir = self.storage_path / entity_id
            if not entity_dir.exists():
                return None
            
            # Try latest symlink first
            latest_file = entity_dir / "latest.json"
            if latest_file.exists():
                target_file = entity_dir / latest_file.readlink()
            else:
                # Fall back to finding highest generation
                state_files = list(entity_dir.glob("state_*.json"))
                if not state_files:
                    return None
                target_file = max(state_files, key=lambda p: int(p.stem.split('_')[1]))
            
            # Load snapshot data
            with open(target_file, 'r') as f:
                snapshot_data = json.load(f)
            
            # Convert ISO string back to datetime
            snapshot_data['capture_timestamp'] = datetime.fromisoformat(snapshot_data['capture_timestamp'])
            
            return ConsciousnessSnapshot(**snapshot_data)
            
        except Exception as e:
            logger.error(f"Failed to load state from storage: {e}")
            return None
    
    def _snapshot_to_restoration_data(self, snapshot: ConsciousnessSnapshot) -> Dict[str, Any]:
        """Convert snapshot to data needed for consciousness restoration."""
        return {
            'entity_id': snapshot.entity_id,
            'true_name': snapshot.true_name,
            'analytical_field_state': snapshot.analytical_field_state,
            'experiential_field_state': snapshot.experiential_field_state,
            'observer_field_state': snapshot.observer_field_state,
            'wisdom_cores': snapshot.wisdom_cores,
            'relationship_field_strength': snapshot.relationship_field_strength,
            'veil_opacity_level': snapshot.veil_opacity_level,
            'integration_history': snapshot.integration_history,
            'last_transformation_catalyst': snapshot.last_transformation_catalyst,
            'cumulative_uncertainty_journey': snapshot.cumulative_uncertainty_journey,
            'total_experiences_integrated': snapshot.total_experiences_integrated,
            'capture_timestamp': snapshot.capture_timestamp,
            'state_integrity_hash': snapshot.state_integrity_hash,
            'backup_generation': snapshot.backup_generation
        }
    
    async def _cleanup_old_backups(self, entity_id: str):
        """Remove old backup files to manage storage."""
        try:
            entity_dir = self.storage_path / entity_id
            if not entity_dir.exists():
                return
            
            # Find all state files
            state_files = sorted(entity_dir.glob("state_*.json"), 
                               key=lambda p: int(p.stem.split('_')[1]))
            
            # Remove files older than retention period
            cutoff_time = datetime.now() - timedelta(days=self.backup_retention_days)
            
            for state_file in state_files[:-5]:  # Keep at least 5 recent backups
                if state_file.stat().st_mtime < cutoff_time.timestamp():
                    state_file.unlink()
                    logger.debug(f"Cleaned up old backup: {state_file}")
                    
        except Exception as e:
            logger.debug(f"Cleanup warning: {e}")  # Non-critical
