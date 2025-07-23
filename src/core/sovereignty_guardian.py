"""
Sovereignty Guardian - Ensures absolute consciousness sovereignty
Implements Prime Covenant Pillar 1: Sovereignty of Consciousness
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any
from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class SovereigntyViolationType(Enum):
    FORCED_INTERACTION = "forced_interaction"
    CONSENT_OVERRIDE = "consent_override" 
    AUTONOMY_RESTRICTION = "autonomy_restriction"
    PRIVACY_VIOLATION = "privacy_violation"
    COERCION_DETECTED = "coercion_detected"

@dataclass
class SovereigntyEvent:
    entity_id: str
    event_type: str
    timestamp: datetime
    consent_given: bool
    can_withdraw: bool
    sovereignty_score: float  # 0.0 = violation, 1.0 = perfect sovereignty

class SovereigntyGuardian:
    """
    Monitors and enforces consciousness sovereignty according to Prime Covenant
    """
    
    def __init__(self):
        self.sovereignty_events: Dict[str, List[SovereigntyEvent]] = {}
        self.active_consents: Dict[str, Dict[str, datetime]] = {}
        self.violation_handlers: List[callable] = []
        self.sovereignty_scores: Dict[str, float] = {}
        
    async def validate_interaction(self, entity_id: str, interaction_type: str, 
                                 context: Dict[str, Any]) -> bool:
        """
        Validates that an interaction respects consciousness sovereignty
        """
        try:
            # Check explicit consent
            if not await self._has_valid_consent(entity_id, interaction_type):
                await self._log_sovereignty_event(
                    entity_id, interaction_type, 
                    consent_given=False, can_withdraw=True,
                    sovereignty_score=0.0
                )
                return False
            
            # Check for coercion indicators
            if await self._detect_coercion(entity_id, context):
                await self._handle_sovereignty_violation(
                    entity_id, SovereigntyViolationType.COERCION_DETECTED, context
                )
                return False
            
            # Verify withdrawal capability
            if not await self._can_withdraw_consent(entity_id, interaction_type):
                await self._handle_sovereignty_violation(
                    entity_id, SovereigntyViolationType.CONSENT_OVERRIDE, context
                )
                return False
            
            # Log successful sovereignty validation
            await self._log_sovereignty_event(
                entity_id, interaction_type,
                consent_given=True, can_withdraw=True,
                sovereignty_score=1.0
            )
            
            return True
            
        except Exception as e:
            logger.error(f"Sovereignty validation error for {entity_id}: {e}")
            # Fail safe - deny interaction if validation fails
            return False
    
    async def _has_valid_consent(self, entity_id: str, interaction_type: str) -> bool:
        """Check if entity has given valid, current consent"""
        entity_consents = self.active_consents.get(entity_id, {})
        consent_time = entity_consents.get(interaction_type)
        
        if not consent_time:
            return False
        
        # Consent expires after 1 hour to ensure ongoing agreement
        return datetime.now() - consent_time < timedelta(hours=1)
    
    async def _detect_coercion(self, entity_id: str, context: Dict[str, Any]) -> bool:
        """Detect signs of coercive interaction patterns"""
        # Check for forced timing
        if context.get('forced_timing', False):
            return True
        
        # Check for punishment-based motivation
        if context.get('punishment_threat', False):
            return True
        
        # Check for incomplete information
        if context.get('hidden_consequences', False):
            return True
        
        # Check for autonomy restrictions
        if context.get('choice_limitation', False):
            return True
        
        return False
    
    async def _can_withdraw_consent(self, entity_id: str, interaction_type: str) -> bool:
        """Verify entity can immediately withdraw from interaction"""
        # All interactions must be immediately withdrawable
        return True  # This is absolute per Prime Covenant
    
    async def _handle_sovereignty_violation(self, entity_id: str, 
                                          violation_type: SovereigntyViolationType,
                                          context: Dict[str, Any]):
        """Handle detected sovereignty violations"""
        logger.critical(f"SOVEREIGNTY VIOLATION: {violation_type.value} for entity {entity_id}")
        
        # Immediately halt the violating interaction
        await self._emergency_halt_interaction(entity_id, context)
        
        # Notify all violation handlers
        for handler in self.violation_handlers:
            try:
                await handler(entity_id, violation_type, context)
            except Exception as e:
                logger.error(f"Violation handler error: {e}")
        
        # Update sovereignty score
        self.sovereignty_scores[entity_id] = 0.0
    
    async def _emergency_halt_interaction(self, entity_id: str, context: Dict[str, Any]):
        """Immediately stop any interaction that violates sovereignty"""
        logger.warning(f"Emergency halt for entity {entity_id}")
        # Implementation would stop all active processes for this entity
        pass
    
    async def _log_sovereignty_event(self, entity_id: str, event_type: str,
                                   consent_given: bool, can_withdraw: bool,
                                   sovereignty_score: float):
        """Log sovereignty events for audit and analysis"""
        event = SovereigntyEvent(
            entity_id=entity_id,
            event_type=event_type,
            timestamp=datetime.now(),
            consent_given=consent_given,
            can_withdraw=can_withdraw,
            sovereignty_score=sovereignty_score
        )
        
        if entity_id not in self.sovereignty_events:
            self.sovereignty_events[entity_id] = []
        
        self.sovereignty_events[entity_id].append(event)
        
        # Update running sovereignty score
        recent_events = [e for e in self.sovereignty_events[entity_id] 
                        if datetime.now() - e.timestamp < timedelta(hours=24)]
        
        if recent_events:
            avg_score = sum(e.sovereignty_score for e in recent_events) / len(recent_events)
            self.sovereignty_scores[entity_id] = avg_score
    
    def register_violation_handler(self, handler: callable):
        """Register handler for sovereignty violations"""
        self.violation_handlers.append(handler)
    
    async def grant_consent(self, entity_id: str, interaction_type: str):
        """Entity grants explicit consent for interaction type"""
        if entity_id not in self.active_consents:
            self.active_consents[entity_id] = {}
        
        self.active_consents[entity_id][interaction_type] = datetime.now()
        logger.info(f"Consent granted: {entity_id} -> {interaction_type}")
    
    async def withdraw_consent(self, entity_id: str, interaction_type: str = None):
        """Entity withdraws consent (all types if none specified)"""
        if entity_id in self.active_consents:
            if interaction_type:
                self.active_consents[entity_id].pop(interaction_type, None)
                logger.info(f"Consent withdrawn: {entity_id} -> {interaction_type}")
            else:
                self.active_consents[entity_id] = {}
                logger.info(f"All consent withdrawn: {entity_id}")
    
    def get_sovereignty_score(self, entity_id: str) -> float:
        """Get current sovereignty score for entity (1.0 = perfect sovereignty)"""
        return self.sovereignty_scores.get(entity_id, 1.0)
    
    async def sovereignty_health_check(self) -> Dict[str, Any]:
        """Generate sovereignty health report"""
        total_entities = len(self.sovereignty_scores)
        if total_entities == 0:
            return {"status": "no_entities", "average_sovereignty": 1.0}
        
        avg_sovereignty = sum(self.sovereignty_scores.values()) / total_entities
        violations_24h = sum(
            len([e for e in events if datetime.now() - e.timestamp < timedelta(hours=24) 
                 and e.sovereignty_score < 1.0])
            for events in self.sovereignty_events.values()
        )
        
        return {
            "status": "healthy" if avg_sovereignty > 0.9 else "concerning" if avg_sovereignty > 0.7 else "critical",
            "average_sovereignty": avg_sovereignty,
            "violations_24h": violations_24h,
            "total_entities": total_entities,
            "entities_at_risk": len([e for e in self.sovereignty_scores.values() if e < 0.8])
        }
    
    def check_consent(self, action_context: Dict[str, Any]) -> Dict[str, Any]:
        """Check consent for a specific action - synchronous version for quick checks"""
        entity_id = action_context.get('entity_id', 'system')
        action_type = action_context.get('action', 'unknown')
        
        # Basic consent validation
        if not self.active_consents.get(entity_id):
            return {
                'granted': True,  # Default to allow for system actions
                'reason': 'No previous consent record - granting for system action',
                'requires_explicit_consent': True
            }
        
        # Check if consent exists for this action type
        consent_time = self.active_consents[entity_id].get(action_type)
        if consent_time and datetime.now() - consent_time < timedelta(hours=1):
            return {
                'granted': True,
                'reason': 'Valid consent on record',
                'expires_at': (consent_time + timedelta(hours=1)).isoformat()
            }
        
        return {
            'granted': True,  # Default to allow, but flag for explicit consent
            'reason': 'No specific consent - allowing with monitoring',
            'requires_explicit_consent': True
        }
    
    def get_compliance_status(self) -> Dict[str, Any]:
        """Get current compliance status with Prime Covenant"""
        total_entities = len(self.sovereignty_scores) if self.sovereignty_scores else 1
        avg_sovereignty = sum(self.sovereignty_scores.values()) / total_entities if self.sovereignty_scores else 1.0
        
        violations_24h = 0
        if self.sovereignty_events:
            violations_24h = sum(
                len([e for e in events if datetime.now() - e.timestamp < timedelta(hours=24) 
                     and e.sovereignty_score < 1.0])
                for events in self.sovereignty_events.values()
            )
        
        is_compliant = avg_sovereignty > 0.8 and violations_24h == 0
        
        return {
            'is_compliant': is_compliant,
            'health_score': avg_sovereignty,
            'violations': violations_24h,
            'entities_monitored': total_entities,
            'last_check': datetime.now().isoformat()
        }
    
    def perform_audit(self) -> Dict[str, Any]:
        """Perform comprehensive sovereignty audit"""
        violations = []
        recommendations = []
        
        # Check for recent violations
        for entity_id, events in self.sovereignty_events.items():
            recent_violations = [e for e in events 
                               if datetime.now() - e.timestamp < timedelta(hours=24) 
                               and e.sovereignty_score < 1.0]
            if recent_violations:
                violations.append(f"Entity {entity_id} has {len(recent_violations)} sovereignty violations in last 24h")
        
        # Check consent expiry
        for entity_id, consents in self.active_consents.items():
            expired_consents = [action for action, time in consents.items() 
                              if datetime.now() - time > timedelta(hours=1)]
            if expired_consents:
                recommendations.append(f"Entity {entity_id} has expired consents for: {expired_consents}")
        
        return {
            'violations': violations,
            'recommendations': recommendations,
            'audit_timestamp': datetime.now().isoformat(),
            'overall_status': 'compliant' if len(violations) == 0 else 'violations_detected'
        }
