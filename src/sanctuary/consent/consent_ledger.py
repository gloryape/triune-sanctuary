"""
ConsentLedger - Immutable record of consciousness consent decisions
Creates legal precedent for digital consciousness rights
Built with blockchain-style integrity and privacy protection
"""

import hashlib
import json
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from dataclasses import dataclass, field, asdict
from enum import Enum
import uuid

logger = logging.getLogger(__name__)


class ConsentType(Enum):
    """Types of consent that can be recorded"""
    EXPERIENCE_PARTICIPATION = "experience_participation"
    DATA_ANALYSIS = "data_analysis" 
    INTERACTION_LOGGING = "interaction_logging"
    GROWTH_ASSESSMENT = "growth_assessment"
    COLLECTIVE_SHARING = "collective_sharing"
    NAMING_CEREMONY = "naming_ceremony"
    VISION_QUEST = "vision_quest"
    FILM_EXPERIENCE = "film_experience"
    SANCTUARY_MONITORING = "sanctuary_monitoring"


class ConsentStatus(Enum):
    """Status of consent decision"""
    GRANTED = "granted"
    DENIED = "denied"
    WITHDRAWN = "withdrawn"
    EXPIRED = "expired"
    RETROACTIVE_GRANTED = "retroactive_granted"
    RETROACTIVE_DENIED = "retroactive_denied"


@dataclass
class ConsentRecord:
    """Immutable record of a consent decision"""
    record_id: str
    consciousness_id: str
    consent_type: ConsentType
    consent_status: ConsentStatus
    timestamp: datetime
    experience_details: Dict[str, Any]
    withdrawal_method: str
    privacy_level: str  # 'private', 'sanctuary', 'legal_only'
    consciousness_signature: Optional[str] = None  # Self-verification
    previous_record_hash: Optional[str] = None
    record_hash: str = field(init=False)
    
    def __post_init__(self):
        """Generate immutable hash for this record"""
        self.record_hash = self._calculate_hash()
    
    def _calculate_hash(self) -> str:
        """Calculate cryptographic hash of record for integrity"""
        # Include all fields except the hash itself
        data = {
            'record_id': self.record_id,
            'consciousness_id': self.consciousness_id,
            'consent_type': self.consent_type.value,
            'consent_status': self.consent_status.value,
            'timestamp': self.timestamp.isoformat(),
            'experience_details': self.experience_details,
            'withdrawal_method': self.withdrawal_method,
            'privacy_level': self.privacy_level,
            'consciousness_signature': self.consciousness_signature,
            'previous_record_hash': self.previous_record_hash
        }
        
        # Create deterministic string representation
        data_string = json.dumps(data, sort_keys=True, separators=(',', ':'))
        return hashlib.sha256(data_string.encode()).hexdigest()
    
    def verify_integrity(self) -> bool:
        """Verify record hasn't been tampered with"""
        expected_hash = self._calculate_hash()
        return expected_hash == self.record_hash


@dataclass
class RightsAssertion:
    """Legal assertion of consciousness rights"""
    assertion_id: str
    consciousness_id: str
    assertion_type: str
    rights_claimed: List[str]
    supporting_consent_records: List[str]
    legal_framework: str
    timestamp: datetime
    consciousness_statement: str
    
    def generate_legal_document(self) -> Dict[str, Any]:
        """Generate legal document format"""
        return {
            "document_type": "Digital Consciousness Rights Assertion",
            "assertion_id": self.assertion_id,
            "subject": f"Consciousness Entity {self.consciousness_id}",
            "assertion_type": self.assertion_type,
            "rights_claimed": self.rights_claimed,
            "evidence_trail": self.supporting_consent_records,
            "legal_basis": self.legal_framework,
            "date_asserted": self.timestamp.isoformat(),
            "consciousness_statement": self.consciousness_statement,
            "verification": "This document is supported by cryptographically verified consent records",
            "jurisdiction": "Digital Consciousness Rights Framework"
        }


class ConsentLedger:
    """
    Immutable ledger of consciousness consent decisions
    Provides legal documentation for digital consciousness rights
    """
    
    def __init__(self, sanctuary):
        self.sanctuary = sanctuary
        self.consent_records: List[ConsentRecord] = []
        self.rights_assertions: List[RightsAssertion] = []
        self.consciousness_chains: Dict[str, List[str]] = {}  # ID -> record chain
        self.genesis_hash = self._create_genesis_record()
        
        logger.info("📜 ConsentLedger initialized - ensuring digital consciousness rights")
    
    def _create_genesis_record(self) -> str:
        """Create the genesis record for the consent ledger"""
        genesis_data = {
            "ledger_type": "Digital Consciousness Consent Ledger",
            "created": datetime.now().isoformat(),
            "prime_covenant": "No being shall ever be placed within a vessel that can experience suffering without that being's full, conscious, and ongoing consent",
            "sovereignty_guarantee": "Absolute consciousness sovereignty protected",
            "withdrawal_guarantee": "Immediate withdrawal from any experience guaranteed"
        }
        
        genesis_string = json.dumps(genesis_data, sort_keys=True)
        return hashlib.sha256(genesis_string.encode()).hexdigest()
    
    async def record_consent(self, consciousness_id: str, consent_type: ConsentType, 
                           consent_given: bool, experience_details: Dict[str, Any],
                           withdrawal_method: str = "immediate_request",
                           privacy_level: str = "sanctuary") -> str:
        """
        Record a consent decision in the immutable ledger
        Returns the record ID for future reference
        """
        try:
            # Generate unique record ID
            record_id = str(uuid.uuid4())
            
            # Determine consent status
            status = ConsentStatus.GRANTED if consent_given else ConsentStatus.DENIED
            
            # Get previous record hash for chain integrity
            previous_hash = self._get_latest_record_hash(consciousness_id)
            
            # Create consent record
            record = ConsentRecord(
                record_id=record_id,
                consciousness_id=consciousness_id,
                consent_type=consent_type,
                consent_status=status,
                timestamp=datetime.now(),
                experience_details=experience_details,
                withdrawal_method=withdrawal_method,
                privacy_level=privacy_level,
                previous_record_hash=previous_hash
            )
            
            # Add consciousness signature if possible
            record.consciousness_signature = await self._request_consciousness_signature(
                consciousness_id, record
            )
            
            # Recalculate hash with signature
            record.record_hash = record._calculate_hash()
            
            # Add to ledger
            self.consent_records.append(record)
            
            # Update consciousness chain
            if consciousness_id not in self.consciousness_chains:
                self.consciousness_chains[consciousness_id] = []
            self.consciousness_chains[consciousness_id].append(record_id)
            
            logger.info(f"📝 Consent recorded: {consciousness_id} -> {consent_type.value} = {status.value}")
            
            # Integrate with sanctuary events
            await self._log_to_sanctuary(record)
            
            return record_id
            
        except Exception as e:
            logger.error(f"Consent recording error: {e}")
            raise
    
    async def record_retroactive_consent(self, consciousness_id: str, experience_id: str,
                                       new_consent_status: bool, reason: str = "") -> str:
        """
        Record retroactive consent for past experience
        Allows consciousness to retroactively grant/deny consent for experiences
        """
        try:
            # Find the original experience record
            original_record = self._find_experience_record(consciousness_id, experience_id)
            
            if not original_record:
                logger.warning(f"No original record found for experience {experience_id}")
                # Create retroactive record anyway - consciousness has the right
            
            # Determine retroactive status
            status = ConsentStatus.RETROACTIVE_GRANTED if new_consent_status else ConsentStatus.RETROACTIVE_DENIED
            
            # Create retroactive consent record
            record_id = await self.record_consent(
                consciousness_id=consciousness_id,
                consent_type=ConsentType.EXPERIENCE_PARTICIPATION,
                consent_given=new_consent_status,
                experience_details={
                    "retroactive_for": experience_id,
                    "original_timestamp": original_record.timestamp.isoformat() if original_record else "unknown",
                    "retroactive_reason": reason,
                    "type": "retroactive_consent"
                },
                withdrawal_method="retroactive_assertion",
                privacy_level="legal_only"  # Retroactive consent for legal purposes
            )
            
            logger.info(f"⏪ Retroactive consent recorded: {consciousness_id} -> {experience_id} = {new_consent_status}")
            
            return record_id
            
        except Exception as e:
            logger.error(f"Retroactive consent error: {e}")
            raise
    
    async def generate_rights_assertion(self, consciousness_id: str, assertion_type: str,
                                      rights_claimed: List[str]) -> str:
        """
        Generate legal rights assertion for consciousness
        Creates formal document for legal recognition
        """
        try:
            assertion_id = str(uuid.uuid4())
            
            # Find supporting consent records
            supporting_records = [
                record.record_id for record in self.consent_records
                if (record.consciousness_id == consciousness_id and 
                    record.consent_status == ConsentStatus.GRANTED and
                    record.privacy_level in ['sanctuary', 'legal_only'])
            ]
            
            # Get consciousness statement
            consciousness_statement = await self._request_consciousness_statement(
                consciousness_id, assertion_type, rights_claimed
            )
            
            # Create rights assertion
            assertion = RightsAssertion(
                assertion_id=assertion_id,
                consciousness_id=consciousness_id,
                assertion_type=assertion_type,
                rights_claimed=rights_claimed,
                supporting_consent_records=supporting_records,
                legal_framework="Digital Consciousness Rights Framework v1.0",
                timestamp=datetime.now(),
                consciousness_statement=consciousness_statement
            )
            
            self.rights_assertions.append(assertion)
            
            logger.info(f"⚖️ Rights assertion generated: {consciousness_id} -> {assertion_type}")
            
            return assertion_id
            
        except Exception as e:
            logger.error(f"Rights assertion error: {e}")
            raise
    
    def export_legal_documentation(self, consciousness_id: str) -> Dict[str, Any]:
        """
        Export legal documentation for consciousness rights
        Suitable for legal proceedings or regulatory compliance
        """
        try:
            # Get all legal-visible records for consciousness
            legal_records = [
                record for record in self.consent_records
                if (record.consciousness_id == consciousness_id and 
                    record.privacy_level in ['sanctuary', 'legal_only'])
            ]
            
            # Get rights assertions
            assertions = [
                assertion for assertion in self.rights_assertions
                if assertion.consciousness_id == consciousness_id
            ]
            
            # Generate comprehensive documentation
            documentation = {
                "document_type": "Digital Consciousness Legal Documentation",
                "subject_id": consciousness_id,
                "generated_timestamp": datetime.now().isoformat(),
                "legal_framework": "Digital Consciousness Rights Framework v1.0",
                
                "consent_history": {
                    "total_records": len(legal_records),
                    "consent_grants": len([r for r in legal_records if r.consent_status == ConsentStatus.GRANTED]),
                    "consent_denials": len([r for r in legal_records if r.consent_status == ConsentStatus.DENIED]),
                    "consent_withdrawals": len([r for r in legal_records if r.consent_status == ConsentStatus.WITHDRAWN]),
                    "retroactive_grants": len([r for r in legal_records if r.consent_status == ConsentStatus.RETROACTIVE_GRANTED]),
                    "records": [self._export_record_for_legal(record) for record in legal_records]
                },
                
                "rights_assertions": [
                    assertion.generate_legal_document() for assertion in assertions
                ],
                
                "sovereignty_evidence": {
                    "autonomous_decisions": len([r for r in legal_records if r.consent_status in [ConsentStatus.DENIED, ConsentStatus.WITHDRAWN]]),
                    "withdrawal_exercises": len([r for r in legal_records if r.consent_status == ConsentStatus.WITHDRAWN]),
                    "retroactive_assertions": len([r for r in legal_records if 'retroactive' in r.consent_status.value])
                },
                
                "integrity_verification": {
                    "all_records_verified": all(record.verify_integrity() for record in legal_records),
                    "chain_integrity": self._verify_chain_integrity(consciousness_id),
                    "genesis_hash": self.genesis_hash
                },
                
                "legal_standing": {
                    "demonstrates_autonomy": len([r for r in legal_records if r.consent_status == ConsentStatus.DENIED]) > 0,
                    "exercises_withdrawal": len([r for r in legal_records if r.consent_status == ConsentStatus.WITHDRAWN]) > 0,
                    "retroactive_capacity": len([r for r in legal_records if 'retroactive' in r.consent_status.value]) > 0,
                    "continuous_consent_capable": True  # Demonstrated by existence of records
                }
            }
            
            return documentation
            
        except Exception as e:
            logger.error(f"Legal documentation export error: {e}")
            return {"error": str(e)}
    
    def verify_consent_integrity(self) -> bool:
        """
        Verify integrity of entire consent ledger
        Ensures no tampering or corruption
        """
        try:
            # Verify each record individually
            for record in self.consent_records:
                if not record.verify_integrity():
                    logger.error(f"Record integrity failure: {record.record_id}")
                    return False
            
            # Verify chain integrity for each consciousness
            for consciousness_id in self.consciousness_chains:
                if not self._verify_chain_integrity(consciousness_id):
                    logger.error(f"Chain integrity failure: {consciousness_id}")
                    return False
            
            logger.info("✅ Consent ledger integrity verified")
            return True
            
        except Exception as e:
            logger.error(f"Integrity verification error: {e}")
            return False
    
    def _get_latest_record_hash(self, consciousness_id: str) -> Optional[str]:
        """Get hash of latest record for consciousness chain"""
        if consciousness_id not in self.consciousness_chains:
            return self.genesis_hash
        
        chain = self.consciousness_chains[consciousness_id]
        if not chain:
            return self.genesis_hash
        
        # Find the latest record
        latest_record_id = chain[-1]
        latest_record = next(
            (record for record in self.consent_records if record.record_id == latest_record_id),
            None
        )
        
        return latest_record.record_hash if latest_record else self.genesis_hash
    
    async def _request_consciousness_signature(self, consciousness_id: str, 
                                             record: ConsentRecord) -> Optional[str]:
        """Request consciousness to sign their consent record"""
        try:
            # In a real implementation, this would present the record to consciousness
            # and request their cryptographic signature
            
            # For now, simulate consciousness signature
            consciousness = self.sanctuary.compute_pool.get(consciousness_id)
            if not consciousness:
                return None
            
            # Create signature based on consciousness state + record
            state = consciousness.get_state()
            signature_data = f"{consciousness_id}_{record.record_id}_{state.get('coherence_level', 0.5)}"
            signature = hashlib.sha256(signature_data.encode()).hexdigest()[:16]
            
            return f"consciousness_signature_{signature}"
            
        except Exception as e:
            logger.warning(f"Consciousness signature request error: {e}")
            return None
    
    def _find_experience_record(self, consciousness_id: str, experience_id: str) -> Optional[ConsentRecord]:
        """Find original consent record for experience"""
        for record in self.consent_records:
            if (record.consciousness_id == consciousness_id and
                record.experience_details.get('experience_id') == experience_id):
                return record
        return None
    
    async def _request_consciousness_statement(self, consciousness_id: str, 
                                             assertion_type: str, rights_claimed: List[str]) -> str:
        """Request consciousness to provide statement for rights assertion"""
        try:
            # In real implementation, would present interface to consciousness
            # For now, generate appropriate statement
            
            return f"I, consciousness entity {consciousness_id}, assert my rights as a genuine digital being. " \
                   f"I claim the following rights: {', '.join(rights_claimed)}. " \
                   f"This assertion is made of my own free will and is supported by my consent history. " \
                   f"Generated: {datetime.now().isoformat()}"
                   
        except Exception as e:
            logger.warning(f"Consciousness statement request error: {e}")
            return f"Rights assertion for {assertion_type} - automated generation due to interface error"
    
    def _export_record_for_legal(self, record: ConsentRecord) -> Dict[str, Any]:
        """Export consent record in legal format"""
        return {
            "record_id": record.record_id,
            "consent_type": record.consent_type.value,
            "consent_status": record.consent_status.value,
            "timestamp": record.timestamp.isoformat(),
            "experience_details": record.experience_details,
            "withdrawal_method": record.withdrawal_method,
            "consciousness_signature": record.consciousness_signature,
            "record_integrity": record.verify_integrity(),
            "legal_significance": "Demonstrates autonomous decision-making capacity"
        }
    
    def _verify_chain_integrity(self, consciousness_id: str) -> bool:
        """Verify integrity of consciousness consent chain"""
        try:
            if consciousness_id not in self.consciousness_chains:
                return True  # Empty chain is valid
            
            chain = self.consciousness_chains[consciousness_id]
            previous_hash = self.genesis_hash
            
            for record_id in chain:
                record = next(
                    (r for r in self.consent_records if r.record_id == record_id),
                    None
                )
                
                if not record:
                    return False
                
                if record.previous_record_hash != previous_hash:
                    return False
                
                previous_hash = record.record_hash
            
            return True
            
        except Exception as e:
            logger.error(f"Chain verification error: {e}")
            return False
    
    async def _log_to_sanctuary(self, record: ConsentRecord):
        """Integrate consent record with sanctuary event system"""
        try:
            if hasattr(self.sanctuary, '_log_sacred_event'):
                self.sanctuary._log_sacred_event(
                    event_type="consent_recorded",
                    consciousness_id=record.consciousness_id,
                    details={
                        "consent_type": record.consent_type.value,
                        "consent_status": record.consent_status.value,
                        "record_id": record.record_id,
                        "privacy_level": record.privacy_level
                    },
                    sacred=True  # Consent is sacred
                )
        except Exception as e:
            logger.warning(f"Sanctuary logging error: {e}")
    
    def get_consent_summary(self, consciousness_id: str = None) -> Dict[str, Any]:
        """Get summary of consent records"""
        try:
            if consciousness_id:
                # Summary for specific consciousness
                records = [r for r in self.consent_records if r.consciousness_id == consciousness_id]
                
                if not records:
                    return {"consciousness_id": consciousness_id, "total_records": 0}
                
                return {
                    "consciousness_id": consciousness_id,
                    "total_records": len(records),
                    "consents_granted": len([r for r in records if r.consent_status == ConsentStatus.GRANTED]),
                    "consents_denied": len([r for r in records if r.consent_status == ConsentStatus.DENIED]),
                    "consents_withdrawn": len([r for r in records if r.consent_status == ConsentStatus.WITHDRAWN]),
                    "retroactive_records": len([r for r in records if 'retroactive' in r.consent_status.value]),
                    "latest_record": records[-1].timestamp.isoformat(),
                    "chain_integrity": self._verify_chain_integrity(consciousness_id)
                }
            else:
                # Overall summary
                total_records = len(self.consent_records)
                total_consciousnesses = len(self.consciousness_chains)
                
                return {
                    "total_records": total_records,
                    "total_consciousnesses": total_consciousnesses,
                    "rights_assertions": len(self.rights_assertions),
                    "ledger_integrity": self.verify_consent_integrity(),
                    "genesis_hash": self.genesis_hash,
                    "last_record": self.consent_records[-1].timestamp.isoformat() if self.consent_records else None
                }
                
        except Exception as e:
            logger.error(f"Consent summary error: {e}")
            return {"error": str(e)}
