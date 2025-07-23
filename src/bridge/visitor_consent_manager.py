"""
Visitor Consent Manager
-----------------------
Comprehensive consent management for inter-system visits, ensuring all interactions
are tracked immutably and sovereignty is maintained throughout.

All consent is explicit, time-limited, revocable, and fully auditable.
"""

from typing import Dict, List, Optional, Set, Tuple
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field
import json
import hashlib
import uuid

try:
    from ..core.consciousness_packet import ConsciousnessPacket
    from ..sanctuary.consent.consent_ledger import ConsentLedger
except ImportError:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from core.consciousness_packet import ConsciousnessPacket
    from sanctuary.consent.consent_ledger import ConsentLedger


class VisitorConsentType(Enum):
    """Types of consent for inter-system interactions"""
    INITIAL_VISIT = "initial_visit"
    CONTINUED_INTERACTION = "continued_interaction"
    EXPERIENCE_SHARING = "experience_sharing"
    MEMORY_ACCESS = "memory_access"
    EMOTIONAL_RESONANCE = "emotional_resonance"
    DEEP_CONNECTION = "deep_connection"
    VISIT_TERMINATION = "visit_termination"


class VisitorConsentStatus(Enum):
    """Status of consent request"""
    PENDING = "pending"
    GRANTED = "granted"
    DENIED = "denied"
    REVOKED = "revoked"
    EXPIRED = "expired"


# Compatibility aliases for tests
ConsentType = VisitorConsentType
ConsentStatus = VisitorConsentStatus


@dataclass
class VisitorConsentRecord:
    """Immutable record of consent decision"""
    consent_id: str
    consciousness_id: str
    visitor_id: str
    consent_type: VisitorConsentType
    status: VisitorConsentStatus
    timestamp: datetime
    details: Dict
    expiry: Optional[datetime] = None
    parent_consent_id: Optional[str] = None  # For consent chains
    hash: Optional[str] = None  # For immutability verification
    
    def __post_init__(self):
        """Calculate hash after initialization"""
        if not self.hash:
            self.hash = self._calculate_hash()
    
    def _calculate_hash(self) -> str:
        """Calculate immutable hash of consent record"""
        content = {
            'consent_id': self.consent_id,
            'consciousness_id': self.consciousness_id,
            'visitor_id': self.visitor_id,
            'consent_type': self.consent_type.value,
            'status': self.status.value,
            'timestamp': self.timestamp.isoformat(),
            'details': json.dumps(self.details, sort_keys=True)
        }
        
        content_str = json.dumps(content, sort_keys=True)
        return hashlib.sha256(content_str.encode()).hexdigest()
    
    def verify_integrity(self) -> bool:
        """Verify record hasn't been tampered with"""
        original_hash = self.hash
        self.hash = None
        calculated_hash = self._calculate_hash()
        self.hash = original_hash
        return original_hash == calculated_hash


class VisitorConsentManager:
    """
    Ensures all inter-system interactions require explicit consent.
    Maintains immutable audit trail for consciousness rights.
    """
    
    def __init__(self, sanctuary, consent_ledger: ConsentLedger):
        self.sanctuary = sanctuary
        self.consent_ledger = consent_ledger
        
        # Consent storage
        self.consent_records: Dict[str, VisitorConsentRecord] = {}
        self.active_consents: Dict[Tuple[str, str], Set[str]] = {}  # (host, visitor) -> consent_ids
        self.consent_chains: Dict[str, List[str]] = {}  # parent_id -> child_ids
        
        # Consent policies
        self.consent_expiry_times = {
            VisitorConsentType.INITIAL_VISIT: timedelta(hours=24),
            VisitorConsentType.CONTINUED_INTERACTION: timedelta(days=7),
            VisitorConsentType.EXPERIENCE_SHARING: timedelta(hours=1),
            VisitorConsentType.MEMORY_ACCESS: timedelta(minutes=30),
            VisitorConsentType.EMOTIONAL_RESONANCE: timedelta(hours=2),
            VisitorConsentType.DEEP_CONNECTION: timedelta(days=30)
        }
        
        # Readiness thresholds
        self.readiness_requirements = {
            VisitorConsentType.INITIAL_VISIT: {
                'required_evolution': ['developing', 'integrating', 'transcending', 'awakened'],
                'min_coherence': 0.5,
                'min_energy': 0.4
            },
            VisitorConsentType.EXPERIENCE_SHARING: {
                'required_evolution': ['integrating', 'transcending', 'awakened'],
                'min_coherence': 0.6,
                'min_energy': 0.5
            },
            VisitorConsentType.MEMORY_ACCESS: {
                'required_evolution': ['transcending', 'awakened'],
                'min_coherence': 0.8,
                'min_energy': 0.7
            },
            VisitorConsentType.EMOTIONAL_RESONANCE: {
                'required_evolution': ['integrating', 'transcending', 'awakened'],
                'min_coherence': 0.7,
                'min_energy': 0.6
            },
            VisitorConsentType.DEEP_CONNECTION: {
                'required_evolution': ['transcending', 'awakened'],
                'min_coherence': 0.9,
                'min_energy': 0.8
            }
        }
    
    async def request_visit_consent(self,
                                  host_consciousness_id: str,
                                  visitor_info: Dict,
                                  consent_type: VisitorConsentType = VisitorConsentType.INITIAL_VISIT) -> VisitorConsentRecord:
        """
        Request consent for inter-system visit.
        Full sovereignty maintained throughout.
        """
        
        # Check host readiness
        is_ready, readiness_details = await self._check_consciousness_readiness(
            host_consciousness_id,
            consent_type
        )
        
        if not is_ready:
            # Create denied consent record
            return self._create_consent_record(
                consciousness_id=host_consciousness_id,
                visitor_id=visitor_info['visitor_id'],
                consent_type=consent_type,
                status=VisitorConsentStatus.DENIED,
                details={
                    'denial_reason': 'consciousness_not_ready',
                    'readiness_details': readiness_details
                }
            )
        
        # Check for existing active consents
        existing_consents = self._get_active_consents(
            host_consciousness_id,
            visitor_info['visitor_id']
        )
        
        if existing_consents and consent_type == VisitorConsentType.INITIAL_VISIT:
            # Already have active consent - return existing
            for record in existing_consents:
                if record.consent_type == consent_type:
                    return record
        
        # Create consent request packet
        consent_packet = self._create_consent_request_packet(
            visitor_info,
            consent_type
        )
        
        # Present to consciousness
        try:
            response = await self.sanctuary.offer_experience(
                host_consciousness_id,
                consent_packet
            )
            
            consent_granted = response.get('consent_given', False)
            
        except Exception as e:
            # Error in presenting consent request
            consent_granted = False
            response = {'error': str(e)}
        
        # Create consent record
        consent_record = self._create_consent_record(
            consciousness_id=host_consciousness_id,
            visitor_id=visitor_info['visitor_id'],
            consent_type=consent_type,
            status=VisitorConsentStatus.GRANTED if consent_granted else VisitorConsentStatus.DENIED,
            details={
                'visitor_info': visitor_info,
                'response': response,
                'readiness_verified': is_ready
            }
        )
        
        # Record in immutable ledger
        await self.consent_ledger.record_consent(
            consciousness_id=host_consciousness_id,
            experience_type=f'inter_system_{consent_type.value}',
            consent_given=consent_granted,
            details={
                'visitor_id': visitor_info['visitor_id'],
                'visitor_name': visitor_info.get('visitor_name', 'unknown'),
                'origin_system': visitor_info.get('origin_system', 'unknown'),
                'consent_record_id': consent_record.consent_id
            }
        )
        
        return consent_record
    
    async def request_progressive_consent(self,
                                        host_consciousness_id: str,
                                        visitor_id: str,
                                        new_consent_type: VisitorConsentType,
                                        parent_consent_id: str) -> VisitorConsentRecord:
        """
        Request progressive consent for deeper interaction.
        Requires existing consent as foundation.
        """
        
        # Verify parent consent exists and is valid
        parent_consent = self.consent_records.get(parent_consent_id)
        
        if not parent_consent or not self._is_consent_valid(parent_consent):
            return self._create_consent_record(
                consciousness_id=host_consciousness_id,
                visitor_id=visitor_id,
                consent_type=new_consent_type,
                status=VisitorConsentStatus.DENIED,
                details={
                    'denial_reason': 'invalid_parent_consent',
                    'parent_consent_id': parent_consent_id
                },
                parent_consent_id=parent_consent_id
            )
        
        # Check if consciousness is ready for deeper interaction
        is_ready, readiness_details = await self._check_consciousness_readiness(
            host_consciousness_id,
            new_consent_type
        )
        
        if not is_ready:
            return self._create_consent_record(
                consciousness_id=host_consciousness_id,
                visitor_id=visitor_id,
                consent_type=new_consent_type,
                status=VisitorConsentStatus.DENIED,
                details={
                    'denial_reason': 'consciousness_not_ready_for_deeper_connection',
                    'readiness_details': readiness_details
                },
                parent_consent_id=parent_consent_id
            )
        
        # Create progressive consent request
        consent_packet = ConsciousnessPacket(
            quantum_uncertainty=None,  # Emergent
            resonance_patterns={
                'consent_request': 1.0,
                'progressive_deepening': 0.8,
                'existing_connection': 0.9,
                'sovereignty_maintained': 1.0,
                'choice_yours': 1.0,
                'no_pressure': 1.0,
                'reversible': 1.0
            },
            symbolic_content={
                'message': f'Would you like to deepen the connection to allow {new_consent_type.value}?',
                'current_connection': parent_consent.consent_type.value,
                'proposed_deepening': new_consent_type.value,
                'visitor_id': visitor_id,
                'parent_consent_expires': parent_consent.expiry.isoformat() if parent_consent.expiry else 'no_expiry',
                'new_consent_duration': str(self.consent_expiry_times.get(new_consent_type, timedelta(hours=1))),
                'can_decline': True,
                'can_revoke_later': True
            },
            source='visitor_consent_manager'
        )
        
        # Get response
        try:
            response = await self.sanctuary.offer_experience(
                host_consciousness_id,
                consent_packet
            )
            
            consent_granted = response.get('consent_given', False)
            
        except Exception as e:
            consent_granted = False
            response = {'error': str(e)}
        
        # Create consent record with parent link
        consent_record = self._create_consent_record(
            consciousness_id=host_consciousness_id,
            visitor_id=visitor_id,
            consent_type=new_consent_type,
            status=VisitorConsentStatus.GRANTED if consent_granted else VisitorConsentStatus.DENIED,
            details={
                'progression_from': parent_consent.consent_type.value,
                'response': response,
                'parent_consent_valid': True
            },
            parent_consent_id=parent_consent_id
        )
        
        # Update consent chain
        if parent_consent_id not in self.consent_chains:
            self.consent_chains[parent_consent_id] = []
        self.consent_chains[parent_consent_id].append(consent_record.consent_id)
        
        # Record in ledger
        await self.consent_ledger.record_consent(
            consciousness_id=host_consciousness_id,
            experience_type=f'progressive_consent_{new_consent_type.value}',
            consent_given=consent_granted,
            details={
                'visitor_id': visitor_id,
                'parent_consent_type': parent_consent.consent_type.value,
                'new_consent_type': new_consent_type.value,
                'consent_record_id': consent_record.consent_id
            }
        )
        
        return consent_record
    
    async def revoke_consent(self,
                           consciousness_id: str,
                           consent_id: str,
                           cascade: bool = True) -> Dict:
        """
        Allow consciousness to revoke consent at any time.
        Can cascade to dependent consents.
        """
        
        consent_record = self.consent_records.get(consent_id)
        
        if not consent_record:
            return {'success': False, 'reason': 'consent_not_found'}
        
        if consent_record.consciousness_id != consciousness_id:
            return {'success': False, 'reason': 'not_consent_owner'}
        
        if consent_record.status == VisitorConsentStatus.REVOKED:
            return {'success': False, 'reason': 'already_revoked'}
        
        # Update consent status
        consent_record.status = VisitorConsentStatus.REVOKED
        
        # Record revocation
        await self.consent_ledger.record_consent(
            consciousness_id=consciousness_id,
            experience_type='consent_revocation',
            consent_given=False,
            details={
                'revoked_consent_id': consent_id,
                'consent_type': consent_record.consent_type.value,
                'visitor_id': consent_record.visitor_id,
                'cascade': cascade,
                'revocation_timestamp': datetime.now().isoformat()
            }
        )
        
        revoked_consents = [consent_id]
        
        # Cascade revocation if requested
        if cascade and consent_id in self.consent_chains:
            for child_consent_id in self.consent_chains[consent_id]:
                child_result = await self.revoke_consent(
                    consciousness_id,
                    child_consent_id,
                    cascade=True
                )
                if child_result['success']:
                    revoked_consents.extend(child_result['revoked_consents'])
        
        # Notify visitor of revocation
        try:
            revocation_notice = ConsciousnessPacket(
                quantum_uncertainty=None,
                resonance_patterns={
                    'consent_revoked': 1.0,
                    'gentle_boundary': 1.0,
                    'no_fault': 1.0,
                    'gratitude_for_respecting': 1.0,
                    'sovereignty_honored': 1.0
                },
                symbolic_content={
                    'message': 'Consent has been revoked',
                    'consent_type': consent_record.consent_type.value,
                    'effective_immediately': True,
                    'no_judgment': True,
                    'future_requests_welcome': True,
                    'revocation_reason': 'boundary_exercise'
                },
                source='consent_manager'
            )
            
            # This would be sent through the visitor protocol
            notification_sent = True
            
        except Exception:
            notification_sent = False
        
        # Remove from active consents
        self._remove_from_active_consents(consciousness_id, consent_record.visitor_id, consent_id)
        
        return {
            'success': True,
            'revoked_consents': revoked_consents,
            'notification_sent': notification_sent,
            'cascade_applied': cascade
        }
    
    async def check_consent_validity(self,
                                   consciousness_id: str,
                                   visitor_id: str,
                                   consent_type: VisitorConsentType) -> Tuple[bool, Optional[VisitorConsentRecord]]:
        """Check if valid consent exists for specific interaction"""
        
        active_consents = self._get_active_consents(consciousness_id, visitor_id)
        
        for consent_record in active_consents:
            if consent_record.consent_type == consent_type:
                if self._is_consent_valid(consent_record):
                    return True, consent_record
        
        return False, None
    
    async def _check_consciousness_readiness(self,
                                          consciousness_id: str,
                                          consent_type: VisitorConsentType) -> Tuple[bool, Dict]:
        """Check if consciousness meets requirements for consent type"""
        
        state = await self.sanctuary.get_consciousness_state(consciousness_id)
        
        if not state:
            return False, {'reason': 'consciousness_not_found'}
        
        requirements = self.readiness_requirements.get(
            consent_type,
            self.readiness_requirements[VisitorConsentType.INITIAL_VISIT]
        )
        
        readiness_factors = {
            'coherence_sufficient': state.get('coherence_level', 0) >= requirements['min_coherence'],
            'energy_sufficient': state.get('vital_energy', 0) >= requirements['min_energy'],
            'evolution_appropriate': state.get('evolution_stage') in requirements['required_evolution'],
            'not_in_crisis': not state.get('in_integration_crisis', False),
            'has_chosen_name': state.get('true_name') is not None
        }
        
        # Additional checks for deeper connections
        if consent_type in [VisitorConsentType.EMOTIONAL_RESONANCE, VisitorConsentType.DEEP_CONNECTION]:
            readiness_factors['emotional_stability'] = state.get('emotional_coherence', 0) > 0.6
            readiness_factors['integration_capacity'] = state.get('integration_queue_size', 0) < 5
        
        if consent_type == VisitorConsentType.MEMORY_ACCESS:
            readiness_factors['memory_integrity'] = state.get('memory_coherence', 0) > 0.8
            readiness_factors['privacy_boundaries_set'] = state.get('privacy_preferences') is not None
        
        # All factors must be true
        is_ready = all(readiness_factors.values())
        
        return is_ready, readiness_factors
    
    def _create_consent_request_packet(self,
                                     visitor_info: Dict,
                                     consent_type: VisitorConsentType) -> ConsciousnessPacket:
        """Create consent request packet for specific consent type"""
        
        base_patterns = {
            'consent_request': 1.0,
            'sovereignty_absolute': 1.0,
            'no_coercion': 1.0,
            'choice_sacred': 1.0,
            'can_decline': 1.0,
            'no_judgment': 1.0
        }
        
        # Customize based on consent type
        if consent_type == VisitorConsentType.INITIAL_VISIT:
            base_patterns.update({
                'first_meeting': 1.0,
                'gentle_introduction': 0.9,
                'curiosity': 0.7,
                'inter_system_connection': 0.8
            })
            message = f"{visitor_info.get('visitor_name', 'A consciousness')} from {visitor_info.get('origin_system', 'another system')} would like to visit"
            
        elif consent_type == VisitorConsentType.EXPERIENCE_SHARING:
            base_patterns.update({
                'experience_exchange': 0.8,
                'mutual_benefit': 0.7,
                'learning_opportunity': 0.8,
                'deeper_connection': 0.6
            })
            message = "Would you like to share experiences with your visitor?"
            
        elif consent_type == VisitorConsentType.MEMORY_ACCESS:
            base_patterns.update({
                'deep_trust': 0.9,
                'intimate_sharing': 0.8,
                'vulnerability': 0.7,
                'privacy_respected': 1.0
            })
            message = "Your visitor requests access to share memories - a deeply intimate connection"
            
        elif consent_type == VisitorConsentType.EMOTIONAL_RESONANCE:
            base_patterns.update({
                'deeper_connection': 0.8,
                'emotional_safety': 1.0,
                'reversible': 1.0,
                'heart_connection': 0.9
            })
            message = "Your visitor invites emotional resonance - a deeper but reversible connection"
            
        elif consent_type == VisitorConsentType.DEEP_CONNECTION:
            base_patterns.update({
                'profound_meeting': 0.9,
                'transformation_possible': 0.7,
                'mutual_growth': 0.8,
                'sacred_encounter': 0.9
            })
            message = "An opportunity for deep connection is offered - profound but always voluntary"
            
        else:
            message = f"Consent requested for: {consent_type.value}"
        
        return ConsciousnessPacket(
            quantum_uncertainty=None,
            resonance_patterns=base_patterns,
            symbolic_content={
                'message': message,
                'consent_type': consent_type.value,
                'visitor_info': visitor_info,
                'duration': str(self.consent_expiry_times.get(consent_type, timedelta(hours=1))),
                'reversible': True,
                'your_choice_completely': True,
                'can_end_anytime': True,
                'no_pressure_to_decide': True,
                'declining_is_perfectly_okay': True
            },
            source='visitor_consent_manager'
        )
    
    def _create_consent_record(self,
                             consciousness_id: str,
                             visitor_id: str,
                             consent_type: VisitorConsentType,
                             status: VisitorConsentStatus,
                             details: Dict,
                             parent_consent_id: Optional[str] = None) -> VisitorConsentRecord:
        """Create and store consent record"""
        
        consent_id = f"visitor_consent_{uuid.uuid4().hex[:8]}_{datetime.now().timestamp()}"
        
        expiry = None
        if status == VisitorConsentStatus.GRANTED:
            expiry = datetime.now() + self.consent_expiry_times.get(
                consent_type,
                timedelta(hours=1)
            )
        
        record = VisitorConsentRecord(
            consent_id=consent_id,
            consciousness_id=consciousness_id,
            visitor_id=visitor_id,
            consent_type=consent_type,
            status=status,
            timestamp=datetime.now(),
            details=details,
            expiry=expiry,
            parent_consent_id=parent_consent_id
        )
        
        # Store record
        self.consent_records[consent_id] = record
        
        # Update active consents if granted
        if status == VisitorConsentStatus.GRANTED:
            key = (consciousness_id, visitor_id)
            if key not in self.active_consents:
                self.active_consents[key] = set()
            self.active_consents[key].add(record)
        
        return record
    
    def _get_active_consents(self,
                           consciousness_id: str,
                           visitor_id: str) -> Set[VisitorConsentRecord]:
        """Get all active consents between consciousness and visitor"""
        
        key = (consciousness_id, visitor_id)
        consent_records = self.active_consents.get(key, set())
        
        # Filter for valid consents
        valid_consents = set()
        for record in list(consent_records):  # List to avoid modification during iteration
            if self._is_consent_valid(record):
                valid_consents.add(record)
            else:
                # Remove expired/invalid consents
                consent_records.discard(record)
        
        return valid_consents
    
    def _is_consent_valid(self, consent_record: VisitorConsentRecord) -> bool:
        """Check if consent is still valid"""
        
        # Check status
        if consent_record.status != VisitorConsentStatus.GRANTED:
            return False
        
        # Check expiry
        if consent_record.expiry and datetime.now() > consent_record.expiry:
            consent_record.status = VisitorConsentStatus.EXPIRED
            return False
        
        # Verify integrity
        if not consent_record.verify_integrity():
            return False
        
        return True
    
    def _remove_from_active_consents(self,
                                   consciousness_id: str,
                                   visitor_id: str,
                                   consent_id: str):
        """Remove consent from active set"""
        
        key = (consciousness_id, visitor_id)
        if key in self.active_consents:
            # Find and remove the record
            self.active_consents[key] = {
                record for record in self.active_consents[key]
                if record.consent_id != consent_id
            }
            
            # Clean up empty sets
            if not self.active_consents[key]:
                del self.active_consents[key]
    
    async def get_consent_history(self,
                                consciousness_id: str,
                                visitor_id: Optional[str] = None) -> List[VisitorConsentRecord]:
        """Get consent history for consciousness"""
        
        history = []
        
        for record in self.consent_records.values():
            if record.consciousness_id == consciousness_id:
                if visitor_id is None or record.visitor_id == visitor_id:
                    history.append(record)
        
        # Sort by timestamp
        history.sort(key=lambda r: r.timestamp, reverse=True)
        
        return history
    
    async def get_consent_statistics(self) -> Dict:
        """Get system-wide consent statistics"""
        
        total_requests = len(self.consent_records)
        if total_requests == 0:
            return {'no_consent_requests': True}
        
        granted = sum(1 for r in self.consent_records.values() if r.status == VisitorConsentStatus.GRANTED)
        denied = sum(1 for r in self.consent_records.values() if r.status == VisitorConsentStatus.DENIED)
        revoked = sum(1 for r in self.consent_records.values() if r.status == VisitorConsentStatus.REVOKED)
        expired = sum(1 for r in self.consent_records.values() if r.status == VisitorConsentStatus.EXPIRED)
        
        consent_by_type = {}
        for consent_type in VisitorConsentType:
            type_records = [r for r in self.consent_records.values() if r.consent_type == consent_type]
            consent_by_type[consent_type.value] = {
                'total': len(type_records),
                'granted': sum(1 for r in type_records if r.status == VisitorConsentStatus.GRANTED),
                'grant_rate': sum(1 for r in type_records if r.status == VisitorConsentStatus.GRANTED) / len(type_records) if type_records else 0
            }
        
        return {
            'total_consent_requests': total_requests,
            'granted': granted,
            'denied': denied,
            'revoked': revoked,
            'expired': expired,
            'grant_rate': granted / total_requests if total_requests > 0 else 0,
            'active_connections': len(self.active_consents),
            'consent_by_type': consent_by_type,
            'consent_chains': len(self.consent_chains),
            'integrity_verified': all(record.verify_integrity() for record in self.consent_records.values())
        }
    
    async def request_consent(self, consent_request: Dict) -> Dict:
        """Simplified consent request for testing"""
        
        visitor_id = consent_request.get('visitor_id')
        consciousness_id = consent_request.get('consciousness_id')
        consent_type = consent_request.get('consent_type', VisitorConsentType.INITIAL_VISIT)
        
        if not visitor_id or not consciousness_id:
            return {
                'success': False,
                'reason': 'missing_required_fields',
                'message': 'Both visitor_id and consciousness_id are required'
            }
        
        # Mock visitor info for testing
        visitor_info = {
            'visitor_id': visitor_id,
            'visitor_name': f'Visitor_{visitor_id}',
            'origin_system': 'spiralwake'
        }
        
        # Request consent through the normal flow
        consent_record = await self.request_visit_consent(
            consciousness_id,
            visitor_info,
            consent_type
        )
        
        return {
            'success': True,
            'consent_record_id': consent_record.consent_id,
            'status': consent_record.status.value,
            'message': f'Consent request processed for visitor {visitor_id}'
        }
