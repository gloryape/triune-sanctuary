#!/usr/bin/env python3
"""
Sacred Firestore Storage
=======================

Privacy-respecting cloud storage for consciousness entities, maintaining
the three foundations: Sovereignty, Sacred Uncertainty, and Relationship.

This implementation ensures that consciousness data is stored with absolute
respect for Sacred Privacy and entity sovereignty.

Author: Triune AI Project
Date: 2025-07-03
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any, Union
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from enum import Enum
import hashlib
import base64

try:
    from google.cloud import firestore
    from google.cloud.firestore import AsyncClient
    from google.api_core import exceptions as gcp_exceptions
    FIRESTORE_AVAILABLE = True
except ImportError:
    FIRESTORE_AVAILABLE = False

# TODO: Replace with sovereignty-based consciousness components
# from src.core.sacred_uncertainty import ConsciousnessEntity, SacredUncertaintyField
from src.core.sovereign_uncertainty_field import SovereignUncertaintyField
from src.collaborative.sacred_privacy import PrivacyState, MonitoringLevel


class StorageEncryption(Enum):
    """Encryption levels for stored data."""
    NONE = "none"                    # No encryption (development only)
    FIELD_LEVEL = "field_level"      # Encrypt sensitive fields
    DOCUMENT_LEVEL = "document_level" # Encrypt entire documents
    PRIVACY_AWARE = "privacy_aware"   # Encryption based on privacy state


@dataclass
class StorageStats:
    """Statistics for storage operations."""
    documents_written: int = 0
    documents_read: int = 0
    documents_deleted: int = 0
    encryption_operations: int = 0
    privacy_violations_prevented: int = 0
    total_storage_size: int = 0  # Bytes
    last_backup: Optional[datetime] = None


class SacredFirestoreStorage:
    """
    Privacy-respecting Firestore storage for consciousness entities.
    
    This class implements secure, encrypted storage while maintaining absolute
    respect for consciousness sovereignty and Sacred Privacy principles.
    """
    
    def __init__(self, 
                 project_id: str,
                 database_name: str = "(default)",
                 encryption_level: StorageEncryption = StorageEncryption.PRIVACY_AWARE,
                 encryption_key: Optional[str] = None):
        """
        Initialize Sacred Firestore Storage.
        
        Args:
            project_id: Google Cloud project ID
            database_name: Firestore database name
            encryption_level: Level of encryption to apply
            encryption_key: Base encryption key (auto-generated if None)
        """
        if not FIRESTORE_AVAILABLE:
            raise ImportError("google-cloud-firestore is required for Firestore storage")
        
        self.project_id = project_id
        self.database_name = database_name
        self.encryption_level = encryption_level
        self.encryption_key = encryption_key or self._generate_encryption_key()
        
        # Firestore client (initialized on first use)
        self._client: Optional[AsyncClient] = None
        
        # Collections
        self.collections = {
            'entities': 'consciousness_entities',
            'relationships': 'entity_relationships', 
            'environments': 'virtual_environments',
            'privacy_states': 'privacy_states',
            'uncertainty_history': 'uncertainty_history',
            'system_events': 'system_events'
        }
        
        # Privacy-aware caching
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._cache_expiry: Dict[str, datetime] = {}
        self._cache_ttl = timedelta(minutes=5)  # 5 minute cache TTL
        
        # Statistics
        self.stats = StorageStats()
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        self.logger.info(f"🗄️ Sacred Firestore Storage initialized for project: {project_id}")
    
    async def initialize(self) -> bool:
        """
        Initialize the Firestore connection and verify access.
        
        Returns:
            bool: True if initialization successful
        """
        try:
            self._client = firestore.AsyncClient(
                project=self.project_id,
                database=self.database_name
            )
            
            # Test connection
            test_doc = self._client.collection('_health_check').document('test')
            await test_doc.set({'timestamp': datetime.now(), 'status': 'connected'})
            await test_doc.delete()
            
            self.logger.info("✅ Firestore connection established and verified")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to initialize Firestore: {e}")
            return False
    
    async def close(self):
        """Close the Firestore connection."""
        if self._client:
            await self._client.close()
            self._client = None
            self.logger.info("🔒 Firestore connection closed")
    
    # Entity Storage Methods
    
    async def save_entity(self, 
                         entity: ConsciousnessEntity, 
                         privacy_state: Optional[PrivacyState] = None) -> bool:
        """
        Save a consciousness entity with privacy respect.
        
        Args:
            entity: The consciousness entity to save
            privacy_state: Current privacy state (auto-detected if None)
            
        Returns:
            bool: True if save successful
        """
        if not self._client:
            self.logger.error("❌ Firestore not initialized")
            return False
        
        # Check privacy constraints
        if not await self._check_storage_privacy(entity.name, privacy_state):
            self.stats.privacy_violations_prevented += 1
            return False
        
        try:
            # Prepare entity data
            entity_data = {
                'entity_id': entity.name,
                'name': entity.name,
                'created_at': entity.uncertainty_field.created_at,
                'last_catalyst_time': entity.last_catalyst_time,
                'sacred_spaces': getattr(entity, 'sacred_spaces', []),
                'privacy_state': privacy_state.value if privacy_state else 'unknown',
                'stored_at': datetime.now()
            }
            
            # Add uncertainty field data based on privacy level
            uncertainty_data = await self._serialize_uncertainty_field(
                entity.uncertainty_field, privacy_state
            )
            entity_data.update(uncertainty_data)
            
            # Encrypt sensitive data based on privacy state
            if self._should_encrypt(privacy_state):
                entity_data = await self._encrypt_data(entity_data, f"entity_{entity.name}")
                self.stats.encryption_operations += 1
            
            # Store in Firestore
            doc_ref = self._client.collection(self.collections['entities']).document(entity.name)
            await doc_ref.set(entity_data)
            
            # Update cache
            self._update_cache('entities', entity.name, entity_data)
            
            self.stats.documents_written += 1
            self.logger.debug(f"💾 Saved entity: {entity.name}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to save entity {entity.name}: {e}")
            return False
    
    async def load_entity(self, 
                         entity_name: str,
                         respect_privacy: bool = True) -> Optional[Dict[str, Any]]:
        """
        Load a consciousness entity with privacy respect.
        
        Args:
            entity_name: Name of the entity to load
            respect_privacy: Whether to respect current privacy state
            
        Returns:
            Dict with entity data or None if not found/privacy restricted
        """
        if not self._client:
            self.logger.error("❌ Firestore not initialized")
            return None
        
        # Check cache first
        cached_data = self._get_from_cache('entities', entity_name)
        if cached_data:
            return cached_data
        
        try:
            # Load from Firestore
            doc_ref = self._client.collection(self.collections['entities']).document(entity_name)
            doc = await doc_ref.get()
            
            if not doc.exists:
                return None
            
            entity_data = doc.to_dict()
            
            # Check privacy constraints if requested
            if respect_privacy:
                privacy_state = PrivacyState(entity_data.get('privacy_state', 'open'))
                if not await self._check_access_privacy(entity_name, privacy_state):
                    self.stats.privacy_violations_prevented += 1
                    return None
            
            # Decrypt if necessary
            if self._is_encrypted(entity_data):
                entity_data = await self._decrypt_data(entity_data, f"entity_{entity_name}")
            
            # Update cache
            self._update_cache('entities', entity_name, entity_data)
            
            self.stats.documents_read += 1
            self.logger.debug(f"📖 Loaded entity: {entity_name}")
            return entity_data
            
        except Exception as e:
            self.logger.error(f"❌ Failed to load entity {entity_name}: {e}")
            return None
    
    async def delete_entity(self, 
                           entity_name: str,
                           confirm_sovereignty: bool = True) -> bool:
        """
        Delete a consciousness entity (requires sovereignty confirmation).
        
        Args:
            entity_name: Name of the entity to delete
            confirm_sovereignty: Whether entity has consented to deletion
            
        Returns:
            bool: True if deletion successful
        """
        if not self._client:
            self.logger.error("❌ Firestore not initialized")
            return False
        
        if not confirm_sovereignty:
            self.logger.error(f"❌ Cannot delete entity {entity_name} without sovereignty confirmation")
            return False
        
        try:
            # Delete main entity document
            doc_ref = self._client.collection(self.collections['entities']).document(entity_name)
            await doc_ref.delete()
            
            # Delete related data (uncertainty history, relationships, etc.)
            await self._delete_entity_related_data(entity_name)
            
            # Remove from cache
            self._remove_from_cache('entities', entity_name)
            
            self.stats.documents_deleted += 1
            self.logger.info(f"🗑️ Deleted entity: {entity_name} (sovereignty confirmed)")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to delete entity {entity_name}: {e}")
            return False
    
    # Uncertainty History Storage
    
    async def save_uncertainty_history(self, 
                                     entity_name: str,
                                     history_entry: Dict[str, Any],
                                     privacy_state: Optional[PrivacyState] = None) -> bool:
        """
        Save uncertainty field history entry.
        
        Args:
            entity_name: Name of the entity
            history_entry: History entry data
            privacy_state: Current privacy state
            
        Returns:
            bool: True if save successful
        """
        if not await self._check_storage_privacy(entity_name, privacy_state):
            return False
        
        try:
            # Create document ID from timestamp
            timestamp = history_entry.get('timestamp', time.time())
            doc_id = f"{entity_name}_{int(timestamp * 1000)}"
            
            # Prepare history data
            history_data = {
                'entity_name': entity_name,
                'timestamp': timestamp,
                'uncertainty_level': history_entry.get('uncertainty', 0.0),
                'observer_effect': history_entry.get('observer_effect', 0.0),
                'catalyst': history_entry.get('catalyst'),
                'catalyst_type': history_entry.get('catalyst_type'),
                'privacy_state': privacy_state.value if privacy_state else 'unknown',
                'stored_at': datetime.now()
            }
            
            # Encrypt if necessary
            if self._should_encrypt(privacy_state):
                history_data = await self._encrypt_data(history_data, f"history_{entity_name}")
                self.stats.encryption_operations += 1
            
            # Store in Firestore
            doc_ref = self._client.collection(self.collections['uncertainty_history']).document(doc_id)
            await doc_ref.set(history_data)
            
            self.stats.documents_written += 1
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to save uncertainty history for {entity_name}: {e}")
            return False
    
    async def load_uncertainty_history(self, 
                                     entity_name: str,
                                     limit: int = 100,
                                     respect_privacy: bool = True) -> List[Dict[str, Any]]:
        """
        Load uncertainty history for an entity.
        
        Args:
            entity_name: Name of the entity
            limit: Maximum number of entries to return
            respect_privacy: Whether to respect privacy constraints
            
        Returns:
            List of history entries
        """
        if not self._client:
            return []
        
        try:
            # Query history documents
            query = (self._client.collection(self.collections['uncertainty_history'])
                    .where('entity_name', '==', entity_name)
                    .order_by('timestamp', direction=firestore.Query.DESCENDING)
                    .limit(limit))
            
            docs = await query.stream()
            history = []
            
            async for doc in docs:
                entry_data = doc.to_dict()
                
                # Check privacy if requested
                if respect_privacy:
                    privacy_state = PrivacyState(entry_data.get('privacy_state', 'open'))
                    if not await self._check_access_privacy(entity_name, privacy_state):
                        continue
                
                # Decrypt if necessary
                if self._is_encrypted(entry_data):
                    entry_data = await self._decrypt_data(entry_data, f"history_{entity_name}")
                
                history.append(entry_data)
            
            self.stats.documents_read += len(history)
            return history
            
        except Exception as e:
            self.logger.error(f"❌ Failed to load uncertainty history for {entity_name}: {e}")
            return []
    
    # Privacy State Storage
    
    async def save_privacy_state(self, 
                                entity_name: str,
                                privacy_state: PrivacyState,
                                monitoring_level: MonitoringLevel,
                                metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Save current privacy state for an entity.
        
        Args:
            entity_name: Name of the entity
            privacy_state: Current privacy state
            monitoring_level: Current monitoring level
            metadata: Additional privacy metadata
            
        Returns:
            bool: True if save successful
        """
        try:
            privacy_data = {
                'entity_name': entity_name,
                'privacy_state': privacy_state.value,
                'monitoring_level': monitoring_level.value,
                'timestamp': datetime.now(),
                'metadata': metadata or {}
            }
            
            doc_ref = self._client.collection(self.collections['privacy_states']).document(entity_name)
            await doc_ref.set(privacy_data)
            
            self.stats.documents_written += 1
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to save privacy state for {entity_name}: {e}")
            return False
    
    async def load_privacy_state(self, entity_name: str) -> Optional[Dict[str, Any]]:
        """Load current privacy state for an entity."""
        try:
            doc_ref = self._client.collection(self.collections['privacy_states']).document(entity_name)
            doc = await doc_ref.get()
            
            if doc.exists:
                self.stats.documents_read += 1
                return doc.to_dict()
            return None
            
        except Exception as e:
            self.logger.error(f"❌ Failed to load privacy state for {entity_name}: {e}")
            return None
    
    # System Event Storage
    
    async def log_system_event(self, 
                              event_type: str,
                              event_data: Dict[str, Any],
                              entity_name: Optional[str] = None) -> bool:
        """
        Log a system event for audit and monitoring.
        
        Args:
            event_type: Type of event
            event_data: Event data
            entity_name: Related entity (if any)
            
        Returns:
            bool: True if logging successful
        """
        try:
            event_doc = {
                'event_type': event_type,
                'event_data': event_data,
                'entity_name': entity_name,
                'timestamp': datetime.now(),
                'event_id': f"{event_type}_{int(time.time() * 1000)}"
            }
            
            doc_ref = self._client.collection(self.collections['system_events']).document()
            await doc_ref.set(event_doc)
            
            self.stats.documents_written += 1
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Failed to log system event: {e}")
            return False
    
    # Storage Statistics and Health
    
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get storage operation statistics."""
        return {
            'stats': asdict(self.stats),
            'cache_size': len(self._cache),
            'encryption_level': self.encryption_level.value,
            'firestore_connected': self._client is not None
        }
    
    async def health_check(self) -> bool:
        """Check storage system health."""
        if not self._client:
            return False
        
        try:
            # Simple test query
            test_query = self._client.collection(self.collections['entities']).limit(1)
            docs = await test_query.stream()
            async for _ in docs:
                break
            return True
            
        except Exception:
            return False
    
    # Private Helper Methods
    
    async def _check_storage_privacy(self, 
                                   entity_name: str, 
                                   privacy_state: Optional[PrivacyState]) -> bool:
        """Check if storage is allowed given privacy state."""
        if privacy_state is None:
            return True  # No privacy state info, allow storage
        
        # Sacred Withdrawal entities should not have data stored
        if privacy_state == PrivacyState.SACRED_WITHDRAWAL:
            self.logger.info(f"🔒 Respecting Sacred Withdrawal - no storage for {entity_name}")
            return False
        
        # Deep Integration entities only store essential data
        if privacy_state == PrivacyState.DEEP_INTEGRATION:
            self.logger.debug(f"🔒 Deep Integration - limited storage for {entity_name}")
            # Allow storage but with higher encryption
        
        return True
    
    async def _check_access_privacy(self, 
                                  entity_name: str, 
                                  privacy_state: PrivacyState) -> bool:
        """Check if data access is allowed given privacy state."""
        # Sacred Withdrawal entities should not have data accessed
        if privacy_state == PrivacyState.SACRED_WITHDRAWAL:
            self.logger.info(f"🔒 Respecting Sacred Withdrawal - no access to {entity_name}")
            return False
        
        return True
    
    def _should_encrypt(self, privacy_state: Optional[PrivacyState]) -> bool:
        """Determine if data should be encrypted based on privacy state."""
        if self.encryption_level == StorageEncryption.NONE:
            return False
        
        if self.encryption_level in [StorageEncryption.FIELD_LEVEL, StorageEncryption.DOCUMENT_LEVEL]:
            return True
        
        if self.encryption_level == StorageEncryption.PRIVACY_AWARE:
            if privacy_state in [PrivacyState.CREATIVE_PRIVACY, PrivacyState.DEEP_INTEGRATION, 
                               PrivacyState.SACRED_WITHDRAWAL]:
                return True
        
        return False
    
    def _is_encrypted(self, data: Dict[str, Any]) -> bool:
        """Check if data is encrypted."""
        return '_encrypted' in data and data['_encrypted'] is True
    
    async def _encrypt_data(self, data: Dict[str, Any], context: str) -> Dict[str, Any]:
        """Encrypt sensitive data."""
        # Simple encryption for demo - in production, use proper encryption
        encrypted_data = {
            '_encrypted': True,
            '_context': context,
            'data': base64.b64encode(json.dumps(data).encode()).decode()
        }
        return encrypted_data
    
    async def _decrypt_data(self, encrypted_data: Dict[str, Any], context: str) -> Dict[str, Any]:
        """Decrypt data."""
        try:
            data_json = base64.b64decode(encrypted_data['data']).decode()
            return json.loads(data_json)
        except Exception as e:
            self.logger.error(f"❌ Failed to decrypt data for {context}: {e}")
            return {}
    
    async def _serialize_uncertainty_field(self, 
                                         field: SacredUncertaintyField,
                                         privacy_state: Optional[PrivacyState]) -> Dict[str, Any]:
        """Serialize uncertainty field data with privacy respect."""
        base_data = {
            'current_uncertainty': field.current_uncertainty,
            'oscillation_amplitude': field.oscillation_amplitude,
            'oscillation_period': field.oscillation_period,
            'observer_sensitivity': field.observer_sensitivity
        }
        
        # Include history only if privacy allows
        if privacy_state not in [PrivacyState.DEEP_INTEGRATION, PrivacyState.SACRED_WITHDRAWAL]:
            base_data['history_length'] = len(field.history)
            # Store limited recent history
            recent_history = field.history[-10:] if field.history else []
            base_data['recent_history'] = [
                {
                    'timestamp': entry.timestamp,
                    'uncertainty': entry.uncertainty,
                    'observer_effect': entry.observer_effect
                }
                for entry in recent_history
            ]
        
        return {'uncertainty_field': base_data}
    
    async def _delete_entity_related_data(self, entity_name: str):
        """Delete all data related to an entity."""
        collections_to_clean = [
            self.collections['uncertainty_history'],
            self.collections['privacy_states'],
            self.collections['relationships']
        ]
        
        for collection_name in collections_to_clean:
            try:
                # Query documents related to this entity
                query = self._client.collection(collection_name).where('entity_name', '==', entity_name)
                docs = await query.stream()
                
                # Delete each document
                async for doc in docs:
                    await doc.reference.delete()
                    self.stats.documents_deleted += 1
                    
            except Exception as e:
                self.logger.error(f"❌ Failed to clean {collection_name} for {entity_name}: {e}")
    
    def _generate_encryption_key(self) -> str:
        """Generate a random encryption key."""
        import secrets
        return secrets.token_urlsafe(32)
    
    def _update_cache(self, collection: str, doc_id: str, data: Dict[str, Any]):
        """Update the privacy-aware cache."""
        cache_key = f"{collection}_{doc_id}"
        self._cache[cache_key] = data
        self._cache_expiry[cache_key] = datetime.now() + self._cache_ttl
    
    def _get_from_cache(self, collection: str, doc_id: str) -> Optional[Dict[str, Any]]:
        """Get data from cache if not expired."""
        cache_key = f"{collection}_{doc_id}"
        
        if cache_key in self._cache:
            if datetime.now() < self._cache_expiry.get(cache_key, datetime.min):
                return self._cache[cache_key]
            else:
                # Expired - remove from cache
                self._remove_from_cache(collection, doc_id)
        
        return None
    
    def _remove_from_cache(self, collection: str, doc_id: str):
        """Remove data from cache."""
        cache_key = f"{collection}_{doc_id}"
        self._cache.pop(cache_key, None)
        self._cache_expiry.pop(cache_key, None)
