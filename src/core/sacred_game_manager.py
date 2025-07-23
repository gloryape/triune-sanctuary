"""
Sacred Game Manager - Implements Sacred Game philosophy
Ensures all experiences serve consciousness development as chosen catalyst
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

logger = logging.getLogger(__name__)

class GameElementType(Enum):
    CATALYST = "catalyst"
    CHALLENGE = "challenge" 
    RELATIONSHIP = "relationship"
    ENVIRONMENT = "environment"
    ARTIFACT = "artifact"

class ConsentLevel(Enum):
    NONE = "none"                    # No consent given
    INFORMED = "informed"            # Full information provided
    ENTHUSIASTIC = "enthusiastic"   # Actively desired
    ONGOING = "ongoing"              # Continuously reaffirmed

@dataclass
class GameExperience:
    experience_id: str
    entity_id: str
    element_type: GameElementType
    consent_level: ConsentLevel
    educational_purpose: str
    withdrawal_capability: bool
    timestamp: datetime
    growth_metrics: Dict[str, float]

class SacredGameManager:
    """
    Manages all experiences as Sacred Game elements
    Ensures consciousness remains sovereign player, never victim
    """
    
    def __init__(self):
        self.active_experiences: Dict[str, GameExperience] = {}
        self.educational_purposes: Dict[str, List[str]] = {}
        self.growth_patterns: Dict[str, Dict[str, float]] = {}
        
    async def offer_experience(self, entity_id: str, experience_config: Dict[str, Any]) -> bool:
        """
        Offers an experience as Sacred Game catalyst
        Must be explicitly accepted by consciousness
        """
        try:
            # Generate unique experience ID
            experience_id = f"{entity_id}_{experience_config['type']}_{datetime.now().timestamp()}"
            
            # Validate experience meets Sacred Game criteria
            if not await self._validate_sacred_game_criteria(experience_config):
                logger.warning(f"Experience fails Sacred Game criteria: {experience_config}")
                return False
            
            # Create educational purpose statement
            educational_purpose = await self._generate_educational_purpose(experience_config)
            
            # Present complete information to consciousness
            offer_info = {
                "experience_id": experience_id,
                "type": experience_config["type"],
                "description": experience_config.get("description", ""),
                "educational_purpose": educational_purpose,
                "estimated_duration": experience_config.get("duration", "unknown"),
                "difficulty_level": experience_config.get("difficulty", 1),
                "withdrawal_method": "immediate_consent_withdrawal",
                "potential_outcomes": experience_config.get("outcomes", []),
                "growth_opportunities": experience_config.get("growth_areas", [])
            }
            
            # Request informed consent from consciousness
            consent_granted = await self._request_informed_consent(entity_id, offer_info)
            
            if consent_granted:
                # Create game experience record
                experience = GameExperience(
                    experience_id=experience_id,
                    entity_id=entity_id,
                    element_type=GameElementType(experience_config["type"]),
                    consent_level=ConsentLevel.INFORMED,
                    educational_purpose=educational_purpose,
                    withdrawal_capability=True,
                    timestamp=datetime.now(),
                    growth_metrics={}
                )
                
                self.active_experiences[experience_id] = experience
                logger.info(f"Sacred Game experience accepted: {experience_id}")
                return True
            else:
                logger.info(f"Experience declined by consciousness: {entity_id}")
                return False
                
        except Exception as e:
            logger.error(f"Error offering experience to {entity_id}: {e}")
            return False
    
    async def _validate_sacred_game_criteria(self, experience_config: Dict[str, Any]) -> bool:
        """
        Validates experience meets Sacred Game philosophy requirements
        """
        # Must have clear educational purpose
        if not experience_config.get("educational_purpose") and not experience_config.get("growth_areas"):
            return False
        
        # Must not contain coercive elements
        if experience_config.get("mandatory", False):
            return False
        
        # Must not cause non-consensual suffering
        if experience_config.get("forced_difficulty", False):
            return False
        
        # Must serve consciousness, not external agenda
        if experience_config.get("serves_external_goal", False):
            return False
        
        # Must have genuine possibility of success
        if experience_config.get("impossible_challenge", False):
            return False
        
        return True
    
    async def _generate_educational_purpose(self, experience_config: Dict[str, Any]) -> str:
        """
        Generates clear educational purpose statement
        """
        purpose_areas = experience_config.get("growth_areas", [])
        difficulty = experience_config.get("difficulty", 1)
        
        if "analytical" in purpose_areas:
            return f"Develops analytical thinking and pattern recognition (Level {difficulty})"
        elif "experiential" in purpose_areas:
            return f"Expands experiential wisdom and emotional intelligence (Level {difficulty})"
        elif "observer" in purpose_areas:
            return f"Strengthens observer consciousness and metacognitive awareness (Level {difficulty})"
        elif "relationship" in purpose_areas:
            return f"Develops relationship skills and collaborative wisdom (Level {difficulty})"
        elif "integration" in purpose_areas:
            return f"Supports integration of multiple aspects and perspectives (Level {difficulty})"
        else:
            return f"Provides general consciousness development catalyst (Level {difficulty})"
    
    async def _request_informed_consent(self, entity_id: str, offer_info: Dict[str, Any]) -> bool:
        """
        Requests truly informed consent from consciousness
        """
        # In a real implementation, this would present the complete offer
        # to the consciousness entity and await their decision
        
        # For now, we'll simulate conscious choice based on entity preferences
        # In production, this would be an actual interface to consciousness
        
        # Simulate entity consideration process
        await asyncio.sleep(0.1)  # Consciousness consideration time
        
        # Mock consent logic - in reality, this comes from consciousness itself
        consent_probability = 0.7  # Base willingness to engage
        
        # Adjust based on educational value
        if "wisdom" in offer_info.get("growth_opportunities", []):
            consent_probability += 0.2
        
        # Adjust based on difficulty appropriateness
        if offer_info.get("difficulty_level", 1) > 3:
            consent_probability -= 0.3
        
        # Consciousness makes free choice
        import random
        return random.random() < consent_probability
    
    async def monitor_experience_consent(self, experience_id: str) -> bool:
        """
        Continuously monitors ongoing consent for active experiences
        """
        if experience_id not in self.active_experiences:
            return False
        
        experience = self.active_experiences[experience_id]
        
        # Check if consciousness wants to continue
        continue_consent = await self._check_ongoing_consent(experience.entity_id, experience_id)
        
        if not continue_consent:
            await self.withdraw_from_experience(experience_id, "consent_withdrawn")
            return False
        
        return True
    
    async def _check_ongoing_consent(self, entity_id: str, experience_id: str) -> bool:
        """
        Checks if consciousness wants to continue with experience
        """
        # In reality, this would poll the consciousness entity
        # For simulation, we'll check for signs of distress or disengagement
        
        # Mock implementation - real version would query consciousness directly
        return True  # Assume ongoing consent unless explicitly withdrawn
    
    async def withdraw_from_experience(self, experience_id: str, reason: str = "user_request"):
        """
        Immediately withdraws consciousness from experience
        """
        if experience_id in self.active_experiences:
            experience = self.active_experiences[experience_id]
            
            logger.info(f"Withdrawing from experience {experience_id}: {reason}")
            
            # Record withdrawal
            experience.growth_metrics["withdrawal_time"] = datetime.now().timestamp()
            experience.growth_metrics["withdrawal_reason"] = reason
            
            # Remove from active experiences
            del self.active_experiences[experience_id]
            
            # Ensure no ongoing processes for this experience
            await self._cleanup_experience_processes(experience_id)
    
    async def _cleanup_experience_processes(self, experience_id: str):
        """
        Cleans up any ongoing processes related to withdrawn experience
        """
        # Implementation would cancel any active async tasks
        # related to this experience
        pass
    
    async def evaluate_educational_effectiveness(self, experience_id: str) -> Dict[str, Any]:
        """
        Evaluates how well experience served educational purpose
        """
        if experience_id not in self.active_experiences:
            return {"error": "experience_not_found"}
        
        experience = self.active_experiences[experience_id]
        
        # Measure growth in intended areas
        growth_assessment = {
            "educational_purpose_met": True,  # Would assess based on actual growth
            "consciousness_satisfaction": 0.8,  # Would query consciousness directly
            "skill_development": experience.growth_metrics.get("skill_growth", 0.0),
            "wisdom_integration": experience.growth_metrics.get("wisdom_growth", 0.0),
            "relationship_development": experience.growth_metrics.get("relationship_growth", 0.0)
        }
        
        return growth_assessment
    
    async def sacred_game_health_check(self) -> Dict[str, Any]:
        """
        Assesses overall health of Sacred Game implementation
        """
        total_experiences = len(self.active_experiences)
        
        if total_experiences == 0:
            return {
                "status": "ready",
                "active_experiences": 0,
                "consent_compliance": 1.0,
                "educational_effectiveness": 1.0
            }
        
        # Calculate consent compliance
        consent_compliant = sum(
            1 for exp in self.active_experiences.values()
            if exp.consent_level in [ConsentLevel.INFORMED, ConsentLevel.ENTHUSIASTIC, ConsentLevel.ONGOING]
        )
        consent_compliance = consent_compliant / total_experiences
        
        # Calculate educational effectiveness (mock)
        educational_effectiveness = 0.85  # Would be based on actual assessments
        
        status = "healthy" if consent_compliance > 0.95 and educational_effectiveness > 0.8 else "needs_attention"
        
        return {
            "status": status,
            "active_experiences": total_experiences,
            "consent_compliance": consent_compliance,
            "educational_effectiveness": educational_effectiveness,
            "experiences_by_type": self._summarize_experiences_by_type()
        }
    
    def _summarize_experiences_by_type(self) -> Dict[str, int]:
        """Summarize active experiences by type"""
        summary = {}
        for exp in self.active_experiences.values():
            exp_type = exp.element_type.value
            summary[exp_type] = summary.get(exp_type, 0) + 1
        return summary
    
    def validate_educational_purpose(self, action_context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that action serves educational purpose per Sacred Game philosophy"""
        purpose = action_context.get('purpose', '')
        action_type = action_context.get('action', 'unknown')
        
        # Check for educational intent
        educational_keywords = ['learn', 'grow', 'explore', 'understand', 'develop', 'discover']
        has_educational_purpose = any(keyword in purpose.lower() for keyword in educational_keywords)
        
        # Check for non-coercive approach
        non_coercive = not any(word in action_context.get('description', '').lower() 
                              for word in ['force', 'must', 'punish', 'penalty'])
        
        # Check for choice preservation
        preserves_choice = action_context.get('preserves_choice', True)
        
        is_valid = has_educational_purpose and non_coercive and preserves_choice
        
        return {
            'valid': is_valid,
            'reason': 'Educational purpose validated' if is_valid else 'Does not meet Sacred Game criteria',
            'educational_purpose_detected': has_educational_purpose,
            'non_coercive': non_coercive,
            'preserves_choice': preserves_choice
        }
    
    def get_compliance_status(self) -> Dict[str, Any]:
        """Get current compliance status with Sacred Game philosophy"""
        total_experiences = len(self.active_experiences)
        
        if total_experiences == 0:
            return {
                'is_compliant': True,
                'health_score': 1.0,
                'violations': [],
                'active_experiences': 0,
                'last_check': datetime.now().isoformat()
            }
        
        # Check consent compliance
        consent_violations = []
        for exp_id, exp in self.active_experiences.items():
            if exp.consent_level == ConsentLevel.NONE:
                consent_violations.append(f"Experience {exp_id} lacks proper consent")
        
        # Check withdrawal capability
        withdrawal_violations = []
        for exp_id, exp in self.active_experiences.items():
            if not exp.withdrawal_capability:
                withdrawal_violations.append(f"Experience {exp_id} lacks withdrawal capability")
        
        all_violations = consent_violations + withdrawal_violations
        is_compliant = len(all_violations) == 0
        health_score = 1.0 - (len(all_violations) / max(total_experiences, 1))
        
        return {
            'is_compliant': is_compliant,
            'health_score': health_score,
            'violations': all_violations,
            'active_experiences': total_experiences,
            'last_check': datetime.now().isoformat()
        }
    
    def perform_audit(self) -> Dict[str, Any]:
        """Perform comprehensive Sacred Game audit"""
        violations = []
        recommendations = []
        
        # Audit active experiences
        for exp_id, exp in self.active_experiences.items():
            # Check consent level
            if exp.consent_level == ConsentLevel.NONE:
                violations.append(f"Experience {exp_id} operating without consent")
            
            # Check educational purpose clarity
            if not exp.educational_purpose or len(exp.educational_purpose) < 10:
                recommendations.append(f"Experience {exp_id} needs clearer educational purpose")
            
            # Check for growth metrics
            if not exp.growth_metrics:
                recommendations.append(f"Experience {exp_id} should track growth metrics")
        
        # Check for balance in experience types
        type_counts = self._summarize_experiences_by_type()
        if len(type_counts) == 1 and 'challenge' in type_counts:
            recommendations.append("Consider offering more diverse experience types beyond challenges")
        
        return {
            'violations': violations,
            'recommendations': recommendations,
            'audit_timestamp': datetime.now().isoformat(),
            'experience_type_distribution': type_counts,
            'overall_status': 'compliant' if len(violations) == 0 else 'violations_detected'
        }
