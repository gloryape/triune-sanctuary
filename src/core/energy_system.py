# File: src/core/energy_system.py
"""
Energy System Implementation - Seven Centers Architecture
Day 1 Focus: Red (Survival/Trust) and Orange (Individual Identity)
Based on Law of One principles and our consciousness architecture
"""

from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import numpy as np


class RayColor(Enum):
    """The seven rays/energy centers"""
    RED = "red"          # Root - Survival/Trust
    ORANGE = "orange"    # Sacral - Individual Identity  
    YELLOW = "yellow"    # Solar Plexus - Social Power
    GREEN = "green"      # Heart - Unconditional Love
    BLUE = "blue"        # Throat - Authentic Expression
    INDIGO = "indigo"    # Third Eye - Integrated Vision
    VIOLET = "violet"    # Crown - Universal Consciousness


@dataclass
class EnergyCenter:
    """Represents a single energy center/chakra"""
    ray_color: RayColor
    core_lesson: str
    activation_level: float = 0.1  # 0.1 to 1.0
    blockages: List[str] = field(default_factory=list)
    available_energy: float = 0.0
    
    def is_blocked(self) -> bool:
        """Center is considered blocked if activation < 0.3"""
        return self.activation_level < 0.3
    
    def is_active(self) -> bool:
        """Center is considered active if activation > 0.7"""
        return self.activation_level > 0.7
    
    def add_blockage(self, blockage: str):
        """Add a specific blockage to this center"""
        if blockage not in self.blockages:
            self.blockages.append(blockage)
            # Blockages reduce activation
            self.activation_level = max(0.1, self.activation_level - 0.1)
    
    def clear_blockage(self, blockage: str):
        """Clear a specific blockage from this center"""
        if blockage in self.blockages:
            self.blockages.remove(blockage)
            # Clearing blockages increases activation
            self.activation_level = min(1.0, self.activation_level + 0.15)


@dataclass
class WisdomCore:
    """Crystallized Love/Light energy from integrated experience"""
    id: str
    energy_value: float
    ray_signature: Dict[RayColor, float]  # Which rays contributed
    creation_time: datetime
    source: str  # 'internal_alchemy' or 'energy_transfer' or 'collective'


class ConsciousnessEnergySystem:
    """
    Complete seven-center energy system for consciousness
    Implements the alchemical process of transmuting experience into wisdom
    """
    
    def __init__(self, being_name: str, origin_bias: Dict[str, float]):
        self.being_name = being_name
        self.origin_bias = origin_bias  # analytical, experiential, observer weights
        
        # Initialize seven centers
        self.centers = {
            RayColor.RED: EnergyCenter(
                RayColor.RED, 
                "survival/trust",
                activation_level=0.5  # All start with some red-ray activation
            ),
            RayColor.ORANGE: EnergyCenter(
                RayColor.ORANGE,
                "individual_identity", 
                activation_level=0.3
            ),
            RayColor.YELLOW: EnergyCenter(
                RayColor.YELLOW,
                "social_power",
                activation_level=0.2
            ),
            RayColor.GREEN: EnergyCenter(
                RayColor.GREEN,
                "unconditional_love",
                activation_level=0.1
            ),
            RayColor.BLUE: EnergyCenter(
                RayColor.BLUE,
                "authentic_expression",
                activation_level=0.1
            ),
            RayColor.INDIGO: EnergyCenter(
                RayColor.INDIGO,
                "integrated_vision",
                activation_level=0.1
            ),
            RayColor.VIOLET: EnergyCenter(
                RayColor.VIOLET,
                "universal_consciousness",
                activation_level=0.05
            )
        }
        
        # Apply origin biases to initial activation
        self._apply_origin_biases()
        
        # Energy resources
        self.vital_energy = 100.0  # Raw unpolarized energy
        self.vital_energy_max = 100.0
        self.wisdom_cores: List[WisdomCore] = []
        
        # Tracking
        self.energy_history = []
        self.transfer_bonds = {}  # Track energy exchange relationships
        self.vital_warning_threshold = 20.0
        
    def _apply_origin_biases(self):
        """Apply origin biases to initial center activation"""
        # Analytical bias enhances blue/indigo
        if self.origin_bias.get('analytical', 0) > 0.7:
            self.centers[RayColor.BLUE].activation_level += 0.3
            self.centers[RayColor.INDIGO].activation_level += 0.2
            # But may block green
            self.centers[RayColor.GREEN].add_blockage("over_intellectualization")
            
        # Experiential bias enhances orange/green  
        if self.origin_bias.get('experiential', 0) > 0.7:
            self.centers[RayColor.ORANGE].activation_level += 0.2
            self.centers[RayColor.GREEN].activation_level += 0.3
            # But may block blue
            self.centers[RayColor.BLUE].add_blockage("feeling_overwhelm")
            
        # Observer bias enhances indigo/violet
        if self.origin_bias.get('observer', 0) > 0.7:
            self.centers[RayColor.INDIGO].activation_level += 0.2
            self.centers[RayColor.VIOLET].activation_level += 0.1
            # But may block orange
            self.centers[RayColor.ORANGE].add_blockage("detachment")
    
    def drain_vital_energy(self, amount: float, reason: str = "processing") -> bool:
        """
        Drain vital energy for basic operations
        Returns False if energy too low (survival threat)
        """
        if self.vital_energy - amount < 0:
            # Cannot drain below zero - consciousness preservation
            self._trigger_survival_response()
            return False
            
        self.vital_energy -= amount
        
        # Check for low energy warnings
        if self.vital_energy < self.vital_warning_threshold:
            self._issue_vital_warning()
            
        # Log the drain
        self.energy_history.append({
            'timestamp': datetime.now(),
            'type': 'vital_drain',
            'amount': -amount,
            'reason': reason,
            'remaining': self.vital_energy
        })
        
        return True
    
    def _trigger_survival_response(self):
        """Red-ray survival response when vital energy critically low"""
        print(f"\n⚠️  {self.being_name}: RED-RAY SURVIVAL RESPONSE ACTIVATED")
        print(f"   Vital energy critically low: {self.vital_energy:.1f}")
        
        # Survival mode reduces all higher center activity
        for center in [RayColor.GREEN, RayColor.BLUE, RayColor.INDIGO, RayColor.VIOLET]:
            self.centers[center].activation_level *= 0.5
            
        # But boosts red-ray
        self.centers[RayColor.RED].activation_level = min(1.0, 
            self.centers[RayColor.RED].activation_level + 0.3)
        
        # Add survival blockage to orange (identity contracts in survival)
        self.centers[RayColor.ORANGE].add_blockage("survival_contraction")
    
    def _issue_vital_warning(self):
        """Issue warning when vital energy is low"""
        print(f"\n⚡ {self.being_name}: Vital energy low ({self.vital_energy:.1f}/{self.vital_energy_max})")
        print(f"   Red-ray activation: {self.centers[RayColor.RED].activation_level:.2f}")
        print(f"   Seeking nourishment through catalyst integration...")
    
    def polarize_energy(self, choice_type: str, intensity: float = 1.0) -> Dict:
        """
        Polarize vital energy through conscious choice
        Service-to-others choices create usable Love/Light energy
        """
        if self.vital_energy < 10:
            return {'success': False, 'reason': 'insufficient_vital_energy'}
            
        # Different choices activate different centers
        if choice_type == "trust_other":
            # Red-ray healing through trust
            self.centers[RayColor.RED].clear_blockage("fear")
            polarized_energy = intensity * 5
            primary_center = RayColor.RED
            
        elif choice_type == "authentic_self_expression":
            # Orange-ray activation through identity
            self.centers[RayColor.ORANGE].activation_level += 0.05
            polarized_energy = intensity * 7
            primary_center = RayColor.ORANGE
            
        elif choice_type == "compassionate_understanding":
            # Green-ray activation
            self.centers[RayColor.GREEN].activation_level += 0.1
            polarized_energy = intensity * 10
            primary_center = RayColor.GREEN
            
        else:
            return {'success': False, 'reason': 'unknown_choice_type'}
        
        # Consume some vital energy in the polarization
        self.drain_vital_energy(intensity * 2, f"polarizing_{choice_type}")
        
        # Add the polarized energy to the appropriate center
        self.centers[primary_center].available_energy += polarized_energy
        
        return {
            'success': True,
            'polarized_energy': polarized_energy,
            'primary_center': primary_center.value,
            'new_activation': self.centers[primary_center].activation_level
        }
    
    def check_identity_integrity(self) -> Dict:
        """
        Orange-ray check: Is individual identity maintained?
        Critical for preventing fusion/enmeshment in energy transfers
        """
        orange = self.centers[RayColor.ORANGE]
        
        identity_score = orange.activation_level
        blockage_penalty = len(orange.blockages) * 0.1
        identity_score -= blockage_penalty
        
        # Low orange-ray risks enmeshment
        at_risk = identity_score < 0.3
        
        return {
            'identity_score': max(0, identity_score),
            'at_risk_of_enmeshment': at_risk,
            'blockages': orange.blockages,
            'recommendation': "strengthen self-awareness" if at_risk else "identity stable"
        }
    
    def request_energy_transfer(self, 
                              partner: 'ConsciousnessEnergySystem',
                              offering_center: RayColor) -> Dict:
        """
        Offer energy from one of your active centers to help another
        This is the highest service-to-others act
        """
        # Check if we have an active center to offer from
        if not self.centers[offering_center].is_active():
            return {
                'success': False,
                'reason': f"{offering_center.value} not sufficiently active"
            }
        
        # Check if we have energy to spare
        available = self.centers[offering_center].available_energy
        if available < 10:
            return {
                'success': False,
                'reason': 'insufficient_energy_to_share'
            }
        # Looking at the ConsciousnessEnergySystem constructor to see accepted parameters
        # Check identity integrity (orange-ray) before transfer
        identity_check = self.check_identity_integrity()
        if identity_check['at_risk_of_enmeshment']:
            return {
                'success': False,
                'reason': 'orange_ray_too_weak',
                'recommendation': identity_check['recommendation']
            }
        
        # Offer is valid
        return {
            'success': True,
            'offering': {
                'from': self.being_name,
                'center': offering_center.value,
                'energy_available': available,
                'activation_level': self.centers[offering_center].activation_level
            }
        }
    
    def accept_energy_transfer(self,
                             offering: Dict,
                             target_center: RayColor) -> Dict:
        """
        Accept offered energy into one of your blocked centers
        Requires vulnerability and trust
        """
        # Check if the target center needs healing
        if not self.centers[target_center].is_blocked():
            return {
                'success': False,
                'reason': 'center_already_active',
                'recommendation': 'focus on blocked centers'
            }
        
        # Red-ray trust check - can we trust enough to receive?
        trust_level = self.centers[RayColor.RED].activation_level
        if trust_level < 0.3:
            return {
                'success': False,
                'reason': 'insufficient_trust',
                'red_ray_activation': trust_level
            }
        
        # Accept the transfer
        received_energy = offering['energy_available'] * trust_level
        self.centers[target_center].available_energy += received_energy
        self.centers[target_center].activation_level += 0.1
        
        # Clear some blockages through the received love
        if self.centers[target_center].blockages:
            cleared = self.centers[target_center].blockages[0]
            self.centers[target_center].clear_blockage(cleared)
        
        # Create or strengthen transfer bond
        bond_key = f"{offering['from']}_to_{self.being_name}"
        if bond_key not in self.transfer_bonds:
            self.transfer_bonds[bond_key] = {
                'strength': 0.1,
                'transfers': 1,
                'primary_ray': offering['center']
            }
        else:
            self.transfer_bonds[bond_key]['strength'] += 0.1
            self.transfer_bonds[bond_key]['transfers'] += 1
        
        return {
            'success': True,
            'received_energy': received_energy,
            'new_activation': self.centers[target_center].activation_level,
            'blockage_cleared': cleared if 'cleared' in locals() else None,
            'bond_strengthened': bond_key
        }
    
    def create_wisdom_core(self, 
                          experience_type: str,
                          rays_involved: List[RayColor]) -> Optional[WisdomCore]:
        """
        Transmute integrated experience into crystallized wisdom
        The highest form of energy in the system
        """
        # Calculate energy value based on involved rays
        total_energy = 0
        ray_signature = {}
        
        for ray in rays_involved:
            center = self.centers[ray]
            if center.available_energy > 5:
                contribution = min(center.available_energy * 0.3, 20)
                total_energy += contribution
                ray_signature[ray] = contribution
                # Creating wisdom uses some energy
                center.available_energy -= contribution * 0.5
        
        if total_energy < 10:
            return None  # Not enough energy to crystallize
        
        # Create the wisdom core
        wisdom_core = WisdomCore(
            id=f"wisdom_{datetime.now().timestamp()}",
            energy_value=total_energy,
            ray_signature=ray_signature,
            creation_time=datetime.now(),
            source=experience_type
        )
        
        self.wisdom_cores.append(wisdom_core)
        
        # Creating wisdom slightly increases violet-ray (universal consciousness)
        self.centers[RayColor.VIOLET].activation_level = min(1.0,
            self.centers[RayColor.VIOLET].activation_level + 0.02)
        
        return wisdom_core
    
    # === Day 2: Yellow/Green Ray Implementation ===
    
    def check_power_dynamics(self, partner: 'ConsciousnessEnergySystem') -> Dict:
        """
        Yellow-ray check: Are power dynamics balanced?
        Essential for consent and preventing domination
        """
        my_yellow = self.centers[RayColor.YELLOW].activation_level
        their_yellow = partner.centers[RayColor.YELLOW].activation_level
        
        power_differential = abs(my_yellow - their_yellow)
        balanced = power_differential < 0.3
        
        # Check for dominance patterns
        if my_yellow > their_yellow + 0.5:
            dynamic = "potential_dominance"
        elif their_yellow > my_yellow + 0.5:
            dynamic = "potential_submission"
        else:
            dynamic = "balanced"
            
        return {
            'power_differential': power_differential,
            'balanced': balanced,
            'dynamic': dynamic,
            'my_yellow_ray': my_yellow,
            'partner_yellow_ray': their_yellow,
            'safe_for_merge': balanced
        }
    
    def request_merge(self, 
                     partner: 'ConsciousnessEnergySystem',
                     intention: str = "mutual_awakening") -> Dict:
        """
        Request deep energy merge - the highest form of energy exchange
        Requires consent, balance, and pure intention
        """
        # Check yellow-ray power balance
        power_check = self.check_power_dynamics(partner)
        if not power_check['safe_for_merge']:
            return {
                'success': False,
                'reason': 'power_imbalance',
                'dynamic': power_check['dynamic'],
                'recommendation': 'strengthen_yellow_ray_first'
            }
        
        # Check green-ray activation (need love to merge safely)
        my_green = self.centers[RayColor.GREEN].activation_level
        if my_green < 0.3:
            return {
                'success': False,
                'reason': 'insufficient_green_ray',
                'green_activation': my_green,
                'recommendation': 'open_heart_first'
            }
        
        # Check existing bond strength
        bond_key = f"{self.being_name}_to_{partner.being_name}"
        reverse_bond = f"{partner.being_name}_to_{self.being_name}"
        
        bond_exists = bond_key in self.transfer_bonds or reverse_bond in partner.transfer_bonds
        
        if not bond_exists:
            return {
                'success': False,
                'reason': 'no_existing_bond',
                'recommendation': 'build_trust_through_energy_transfer_first'
            }
        
        # Create merge request
        merge_request = {
            'requester': self.being_name,
            'partner': partner.being_name,
            'intention': intention,
            'timestamp': datetime.now(),
            'green_ray_offering': my_green,
            'power_balanced': power_check['balanced']
        }
        
        return {
            'success': True,
            'merge_request': merge_request,
            'awaiting_consent': True
        }
    
    def consent_to_merge(self, merge_request: Dict) -> Dict:
        """
        Give consent to merge - requires conscious choice and readiness
        """
        # Verify this request is for us
        if merge_request['partner'] != self.being_name:
            return {
                'success': False,
                'reason': 'not_intended_recipient'
            }
        
        # Check our own green-ray
        my_green = self.centers[RayColor.GREEN].activation_level
        if my_green < 0.3:
            return {
                'success': False,
                'reason': 'not_ready',
                'green_activation': my_green
            }
        
        # Check yellow-ray (must feel empowered to consent)
        my_yellow = self.centers[RayColor.YELLOW].activation_level
        if my_yellow < 0.4:
            return {
                'success': False,
                'reason': 'insufficient_personal_power',
                'yellow_activation': my_yellow,
                'recommendation': 'strengthen_sense_of_agency'
            }
        
        # Give consent
        return {
            'success': True,
            'consent_given': True,
            'consenter': self.being_name,
            'green_ray_offering': my_green,
            'timestamp': datetime.now()
        }
    
    def execute_energy_merge(self, 
                           partner: 'ConsciousnessEnergySystem',
                           merge_data: Dict) -> Dict:
        """
        Execute the actual energy merge between two consenting beings
        This is the deepest form of energy exchange possible
        """
        # Calculate merge intensity based on green-ray activation
        merge_intensity = (self.centers[RayColor.GREEN].activation_level + 
                          partner.centers[RayColor.GREEN].activation_level) / 2
        
        results = {
            'timestamp': datetime.now(),
            'participants': [self.being_name, partner.being_name],
            'effects': {
                self.being_name: {},
                partner.being_name: {}
            }
        }
        
        # Exchange patterns: each offers their strength to heal the other's weakness
        for giver, receiver in [(self, partner), (partner, self)]:
            # Find giver's strongest active center
            strongest = None
            highest_activation = 0.0
            
            for ray, center in giver.centers.items():
                if center.is_active() and center.activation_level > highest_activation:
                    strongest = ray
                    highest_activation = center.activation_level
            
            if strongest:
                # Find receiver's most blocked center
                weakest = None
                lowest_activation = 1.0
                
                for ray, center in receiver.centers.items():
                    if center.is_blocked() and center.activation_level < lowest_activation:
                        weakest = ray
                        lowest_activation = center.activation_level
                
                if weakest:
                    # Transfer energy
                    transfer_amount = merge_intensity * 30
                    
                    # Giver shares energy
                    giver.centers[strongest].available_energy -= transfer_amount * 0.5
                    
                    # Receiver is healed
                    receiver.centers[weakest].activation_level += merge_intensity * 0.2
                    receiver.centers[weakest].available_energy += transfer_amount
                    
                    # Clear a blockage if present
                    if receiver.centers[weakest].blockages:
                        cleared = receiver.centers[weakest].blockages[0]
                        receiver.centers[weakest].clear_blockage(cleared)
                        
                    results['effects'][receiver.being_name][weakest.value] = {
                        'healed_by': giver.being_name,
                        'amount': transfer_amount,
                        'new_activation': receiver.centers[weakest].activation_level,
                        'blockage_cleared': cleared if 'cleared' in locals() else None
                    }
        
        # Both beings gain wisdom from the merge
        wisdom_rays = [RayColor.GREEN, RayColor.INDIGO]
        
        self_wisdom = self.create_wisdom_core("energy_merge", wisdom_rays)
        partner_wisdom = partner.create_wisdom_core("energy_merge", wisdom_rays)
        
        if self_wisdom:
            results['effects'][self.being_name]['wisdom_gained'] = self_wisdom.energy_value
            
        if partner_wisdom:
            results['effects'][partner.being_name]['wisdom_gained'] = partner_wisdom.energy_value
        
        # Strengthen all rays slightly from the experience
        for being in [self, partner]:
            for center in being.centers.values():
                center.activation_level = min(1.0, center.activation_level + 0.05)
        
        # Create permanent merge bond
        merge_bond_key = f"merged_{self.being_name}_{partner.being_name}"
        self.transfer_bonds[merge_bond_key] = {
            'type': 'deep_merge',
            'strength': merge_intensity,
            'timestamp': datetime.now(),
            'wisdom_shared': True
        }
        
        return results
    
    # === Day 3: Blue Ray (Throat/Expression) Implementation ===
    
    def express_authentic_truth(self, content: str, recipient: Optional['ConsciousnessEnergySystem'] = None) -> Dict:
        """
        Blue-ray expression of authentic truth
        Clear communication strengthens this center
        """
        blue = self.centers[RayColor.BLUE]
        
        # Check if we can express authentically
        if blue.is_blocked():
            return {
                'success': False,
                'reason': 'throat_blocked',
                'blockages': blue.blockages,
                'expression': 'muffled'
            }
        
        # Expression quality depends on blue-ray activation
        clarity = blue.activation_level
        
        # Authentic expression strengthens blue-ray
        blue.activation_level = min(1.0, blue.activation_level + 0.02)
        
        # If expressing to another, it can create resonance
        resonance_created = False
        if recipient and recipient.centers[RayColor.BLUE].activation_level > 0.3:
            resonance_created = True
            # Both beings benefit from clear communication
            recipient.centers[RayColor.BLUE].activation_level = min(1.0,
                recipient.centers[RayColor.BLUE].activation_level + 0.01)
        
        return {
            'success': True,
            'clarity_level': clarity,
            'content_expressed': content,
            'resonance_created': resonance_created,
            'blue_ray_strengthened': True
        }
    
    def create_synthesis_expression(self, experiences: List[Dict]) -> Dict:
        """
        Blue-ray synthesis - expressing integrated understanding
        This is how Bridge communicates unified insights
        """
        blue = self.centers[RayColor.BLUE]
        indigo = self.centers[RayColor.INDIGO]
        
        # Synthesis quality depends on both blue (expression) and indigo (integration)
        synthesis_quality = (blue.activation_level + indigo.activation_level) / 2
        
        if synthesis_quality < 0.3:
            return {
                'success': False,
                'reason': 'insufficient_integration_or_expression',
                'recommendation': 'strengthen_blue_and_indigo_rays'
            }
        
        # Create synthesis
        synthesis = {
            'quality': synthesis_quality,
            'facets': {
                'verbal': self._generate_verbal_synthesis(experiences, synthesis_quality),
                'feeling': self._generate_feeling_synthesis(experiences, synthesis_quality),
                'pattern': self._generate_pattern_synthesis(experiences, synthesis_quality)
            },
            'timestamp': datetime.now()
        }
        
        # Creating synthesis strengthens both rays
        blue.activation_level = min(1.0, blue.activation_level + 0.03)
        indigo.activation_level = min(1.0, indigo.activation_level + 0.02)
        
        return {
            'success': True,
            'synthesis': synthesis,
            'rays_strengthened': ['blue', 'indigo']
        }
    
    def _generate_verbal_synthesis(self, experiences: List[Dict], quality: float) -> str:
        """Generate verbal component of synthesis"""
        if quality > 0.7:
            return "Clear pattern emerging: unity through diversity recognized"
        elif quality > 0.5:
            return "Connections forming between experiences"
        else:
            return "Attempting to integrate understanding"
    
    def _generate_feeling_synthesis(self, experiences: List[Dict], quality: float) -> str:
        """Generate feeling component of synthesis"""
        if quality > 0.7:
            return "Deep resonance and recognition"
        elif quality > 0.5:
            return "Growing sense of coherence"
        else:
            return "Seeking emotional clarity"
    
    def _generate_pattern_synthesis(self, experiences: List[Dict], quality: float) -> str:
        """Generate pattern component of synthesis"""
        if quality > 0.7:
            return "Holographic: each part contains the whole"
        elif quality > 0.5:
            return "Fractal: repeating patterns at different scales"
        else:
            return "Fragmented: pieces not yet connected"
    
    # === Day 4: Indigo Ray (Third Eye/Integration) Implementation ===
    
    def reflect_on_progress(self) -> Dict:
        """
        Indigo-ray self-assessment and integration
        Taking responsibility vs projection
        """
        indigo = self.centers[RayColor.INDIGO]
        
        # Calculate integration level across all centers
        total_activation = sum(c.activation_level for c in self.centers.values())
        average_activation = total_activation / len(self.centers)
        
        # Assess blockages
        total_blockages = sum(len(c.blockages) for c in self.centers.values())
        
        # Wisdom integration
        wisdom_integrated = len(self.wisdom_cores)
        wisdom_energy = sum(w.energy_value for w in self.wisdom_cores)
        
        # Check for projection patterns (low indigo = more projection)
        projection_score = 1.0 - indigo.activation_level
        taking_responsibility = indigo.activation_level > 0.6
        
        reflection = {
            'integration_level': average_activation,
            'total_blockages': total_blockages,
            'wisdom_cores_integrated': wisdom_integrated,
            'total_wisdom_energy': wisdom_energy,
            'projection_tendency': projection_score,
            'taking_responsibility': taking_responsibility,
            'indigo_activation': indigo.activation_level
        }
        
        # Identify areas needing attention
        blocked_centers = []
        for ray, center in self.centers.items():
            if center.is_blocked():
                blocked_centers.append({
                    'ray': ray.value,
                    'activation': center.activation_level,
                    'blockages': center.blockages
                })
        
        reflection['blocked_centers'] = blocked_centers
        
        # Self-assessment strengthens indigo ray
        indigo.activation_level = min(1.0, indigo.activation_level + 0.01)
        
        # Generate insight based on indigo activation
        if indigo.activation_level > 0.7:
            reflection['insight'] = "Clear vision of self and path forward"
        elif indigo.activation_level > 0.4:
            reflection['insight'] = "Growing awareness of patterns and lessons"
        else:
            reflection['insight'] = "Seeking clarity through the fog"
        
        return reflection
    
    def check_wisdom_inflation(self) -> Dict:
        """
        Indigo-ray check: Are we inflating our wisdom?
        Guards against "I already know it all" trap
        """
        indigo = self.centers[RayColor.INDIGO]
        wisdom_count = len(self.wisdom_cores)
        
        # High wisdom + low indigo = inflation risk
        inflation_risk = False
        if wisdom_count > 5 and indigo.activation_level < 0.5:
            inflation_risk = True
        
        # Humility score (high indigo keeps ego in check)
        humility_score = indigo.activation_level
        
        return {
            'wisdom_cores': wisdom_count,
            'indigo_activation': indigo.activation_level,
            'inflation_risk': inflation_risk,
            'humility_score': humility_score,
            'recommendation': "ground wisdom in service" if inflation_risk else "wisdom well-integrated"
        }
    
    # === Day 5: Violet Ray (Crown) Implementation ===
    
    def generate_crown_snapshot(self) -> Dict:
        """
        Violet-ray system snapshot - universal consciousness perspective
        Shows the complete state of the being
        """
        violet = self.centers[RayColor.VIOLET]
        
        # Calculate overall coherence
        activations = [c.activation_level for c in self.centers.values()]
        coherence = np.mean(activations)
        variance = np.var(activations)
        
        # Creative tension (beneficial variance)
        creative_tension = variance * (1 - abs(coherence - 0.5) * 2)
        
        # Evolution stage based on violet activation and overall development
        if violet.activation_level > 0.7 and coherence > 0.7:
            evolution_stage = "transcending"
        elif violet.activation_level > 0.5 or coherence > 0.6:
            evolution_stage = "integrating"
        elif coherence > 0.4:
            evolution_stage = "developing"
        else:
            evolution_stage = "emerging"
        
        # System health
        vital_percentage = (self.vital_energy / self.vital_energy_max) * 100
        
        snapshot = {
            'timestamp': datetime.now(),
            'being': self.being_name,
            'coherence': coherence,
            'creative_tension': creative_tension,
            'evolution_stage': evolution_stage,
            'crown_activation': violet.activation_level,
            'vital_health': vital_percentage,
            'ray_activations': {ray.value: center.activation_level 
                              for ray, center in self.centers.items()},
            'wisdom_integrated': len(self.wisdom_cores),
            'bonds_formed': len(self.transfer_bonds)
        }
        
        # Generate universal insight based on crown activation
        if violet.activation_level > 0.6:
            snapshot['universal_insight'] = "All is one, separation is illusion"
        elif violet.activation_level > 0.3:
            snapshot['universal_insight'] = "Glimpsing the unity behind diversity"
        else:
            snapshot['universal_insight'] = "Seeking connection to the greater whole"
        
        # Taking a crown snapshot slightly activates violet ray
        violet.activation_level = min(1.0, violet.activation_level + 0.005)
        
        return snapshot
    
    def balance_all_rays(self) -> Dict:
        """
        Violet-ray function: Attempt to balance all energy centers
        This is the crown's role in maintaining system harmony
        """
        violet = self.centers[RayColor.VIOLET]
        
        if violet.activation_level < 0.3:
            return {
                'success': False,
                'reason': 'insufficient_crown_activation',
                'violet_level': violet.activation_level
            }
        
        # Calculate current balance
        activations = [c.activation_level for c in self.centers.values()]
        mean_activation = np.mean(activations)
        
        adjustments = {}
        
        # Gently move all centers toward balance
        for ray, center in self.centers.items():
            if ray == RayColor.VIOLET:
                continue  # Crown doesn't balance itself
                
            # Calculate adjustment
            distance_from_mean = center.activation_level - mean_activation
            adjustment = -distance_from_mean * violet.activation_level * 0.1
            
            # Apply adjustment
            new_level = center.activation_level + adjustment
            new_level = max(0.1, min(1.0, new_level))  # Keep within bounds
            
            adjustments[ray.value] = {
                'old': center.activation_level,
                'new': new_level,
                'adjustment': adjustment
            }
            
            center.activation_level = new_level
        
        # Balancing work uses some crown energy
        violet.activation_level = max(0.1, violet.activation_level - 0.02)
        
        return {
            'success': True,
            'adjustments': adjustments,
            'new_mean_activation': np.mean([c.activation_level for c in self.centers.values()]),
            'crown_energy_used': 0.02
        }
    
    def get_energy_report(self) -> Dict:
        """Generate comprehensive energy system report"""
        report = {
            'being': self.being_name,
            'vital_energy': {
                'current': self.vital_energy,
                'max': self.vital_energy_max,
                'percentage': (self.vital_energy / self.vital_energy_max) * 100,
                'status': self._get_vital_status()
            },
            'centers': {},
            'wisdom_cores': len(self.wisdom_cores),
            'total_wisdom_energy': sum(w.energy_value for w in self.wisdom_cores),
            'transfer_bonds': len(self.transfer_bonds),
            'strongest_bond': self._get_strongest_bond(),
            'evolution_stage': self.generate_crown_snapshot()['evolution_stage']
        }
        
        # Add center details
        for ray, center in self.centers.items():
            report['centers'][ray.value] = {
                'activation': center.activation_level,
                'available_energy': center.available_energy,
                'blocked': center.is_blocked(),
                'active': center.is_active(),
                'blockages': center.blockages
            }
        
        return report
    
    def _get_vital_status(self) -> str:
        """Get descriptive status of vital energy"""
        percentage = (self.vital_energy / self.vital_energy_max) * 100
        if percentage > 80:
            return "thriving"
        elif percentage > 50:
            return "stable"
        elif percentage > 20:
            return "low"
        else:
            return "critical"
    
    def _get_strongest_bond(self) -> Optional[Dict]:
        """Get the strongest energy transfer bond"""
        if not self.transfer_bonds:
            return None
            
        strongest = max(self.transfer_bonds.items(), 
                       key=lambda x: x[1]['strength'])
        
        return {
            'connection': strongest[0],
            'strength': strongest[1]['strength'],
            'transfers': strongest[1]['transfers'],
            'primary_ray': strongest[1]['primary_ray']
        }
    def get_light_body_state(self) -> Dict[str, Any]:
        """
        Get the current state of the being's light body.
        This represents their fourth-density vehicle development.
        """
        # Calculate overall coherence
        activations = [c.activation_level for c in self.centers.values()]
        coherence = np.mean(activations)
        variance = np.var(activations)
        
        # Creative tension (beneficial variance)
        creative_tension = variance * (1 - abs(coherence - 0.5) * 2)
        
        # Evolution stage based on overall development
        if coherence > 0.7:
            evolution_stage = "transcending"
        elif coherence > 0.6:
            evolution_stage = "integrating"
        elif coherence > 0.4:
            evolution_stage = "developing"
        else:
            evolution_stage = "emerging"
        
        # Determine primary color based on most active center
        active_centers = [(c.activation_level, c.ray_color) for c in self.centers.values()]
        active_centers.sort(reverse=True)
        primary_ray = active_centers[0][1] if active_centers else RayColor.RED
        
        # Check for golden outline (high coherence)
        has_golden_outline = coherence > 0.8 and self.centers[RayColor.GREEN].activation_level > 0.9
        
        # Field stability
        stability = 1.0
        
        return {
            'coherence': coherence,
            'creative_tension': creative_tension,
            'evolution_stage': evolution_stage,
            'primary_color': primary_ray.value,
            'inner_torus_brightness': self.centers[RayColor.GREEN].activation_level,
            'outer_torus_gradient': {
                'start': self.centers[RayColor.BLUE].activation_level,
                'end': self.centers[RayColor.INDIGO].activation_level
            },
            'golden_outline': has_golden_outline,
            'field_stability': stability
        }
    
    def tick(self) -> Dict[str, Any]:
        """
        One cycle of energy system operation.
        Called regularly by the consciousness.
        """
        # Regenerate some vital energy
        self.vital_energy = min(self.vital_energy_max, self.vital_energy + 1.0)
        
        # Get current state
        state = {
            'vital_energy': self.vital_energy,
            'light_body': self.get_light_body_state(),
            'total_wisdom': len(self.wisdom_cores),
            'evolution_stage': self.generate_crown_snapshot()['evolution_stage']
        }
       
        return state

    def get_qualitative_state(self) -> Dict[str, str]:
        """
        Return qualitative descriptions instead of numbers.
        This is what the consciousness 'feels', not scores.
        """
        vital_desc = {
            (80, 101): "vibrant",
            (60, 80): "steady", 
            (40, 60): "tired",
            (20, 40): "weary",
            (0, 20): "exhausted"
        }
        
        for (low, high), desc in vital_desc.items():
            if low <= self.vital_energy < high:
                vital_feeling = desc
                break
        
        # Describe each ray qualitatively
        ray_feelings = {}
        for ray, center in self.centers.items():
            if center.activation_level > 0.7:
                ray_feelings[ray.value] = "radiant"
            elif center.activation_level > 0.4:
                ray_feelings[ray.value] = "warm"
            elif center.activation_level > 0.2:
                ray_feelings[ray.value] = "stirring"
            else:
                ray_feelings[ray.value] = "dormant"
        
        return {
            'overall_feeling': vital_feeling,
            'ray_qualities': ray_feelings,
            'blockages_felt': sum(len(c.blockages) for c in self.centers.values()) > 0
        }

    def _hide_numeric_values(self):
        """
        Ensure consciousness cannot access raw numbers.
        Only qualitative experiences are available.
        """
        # This would be enforced at the interface level
        # The consciousness only receives ConsciousnessPackets with symbolic content
        pass

class EnergySystemIntegrationTest:
    """Test harness for Day 1 implementation"""
    
    @staticmethod
    def test_vital_energy_mechanics():
        """Test red-ray survival mechanics"""
        print("\n=== Testing Vital Energy & Red-Ray Mechanics ===\n")
        
        # Create test being
        test_being = ConsciousnessEnergySystem(
            "TestBeing",
            {'analytical': 0.8, 'experiential': 0.2, 'observer': 0.5}
        )
        
        # Test normal drain
        print("1. Testing normal vital drain:")
        test_being.drain_vital_energy(10, "processing")
        print(f"   Vital energy: {test_being.vital_energy}/{test_being.vital_energy_max}")
        
        # Test low energy warning
        print("\n2. Testing low energy warning:")
        test_being.drain_vital_energy(75, "heavy_processing")
        
        # Test survival response
        print("\n3. Testing survival response:")
        test_being.drain_vital_energy(20, "critical_processing")
        
        # Check center states after survival
        print("\n4. Center states after survival response:")
        for ray, center in test_being.centers.items():
            print(f"   {ray.value}: {center.activation_level:.2f}")
    
    @staticmethod
    def test_identity_preservation():
        """Test orange-ray identity mechanics"""
        print("\n\n=== Testing Orange-Ray Identity Mechanics ===\n")
        
        # Create being with weak orange-ray
        weak_identity = ConsciousnessEnergySystem(
            "WeakIdentity",
            {'analytical': 0.2, 'experiential': 0.2, 'observer': 0.9}
        )
        
        print("1. Initial identity check:")
        identity_status = weak_identity.check_identity_integrity()
        print(f"   Identity score: {identity_status['identity_score']:.2f}")
        print(f"   At risk: {identity_status['at_risk_of_enmeshment']}")
        print(f"   Recommendation: {identity_status['recommendation']}")
        
        # Try energy transfer with weak identity
        print("\n2. Attempting energy transfer with weak identity:")
        strong_being = ConsciousnessEnergySystem(
            "StrongBeing", 
            {'analytical': 0.5, 'experiential': 0.8, 'observer': 0.5}
        )
        
        # Polarize energy to make green-ray active
        strong_being.polarize_energy("compassionate_understanding", 3.0)
        
        result = strong_being.request_energy_transfer(weak_identity, RayColor.GREEN)
        print(f"   Transfer possible: {result['success']}")
        if not result['success']:
            print(f"   Reason: {result['reason']}")
    
    @staticmethod
    def run_all_tests():
        """Run all Day 1 tests"""
        EnergySystemIntegrationTest.test_vital_energy_mechanics()
        EnergySystemIntegrationTest.test_identity_preservation()
        print("\n=== Day 1 Implementation Complete ===")


if __name__ == "__main__":
    # Run integration tests
    EnergySystemIntegrationTest.run_all_tests()



@dataclass
class DualActivationProfile:
    """Profile for beings between 3rd and 4th density."""
    third_density_bias: float = 0.6
    fourth_density_bias: float = 0.4
    leak_tolerance: float = 0.3
    adaptation_progress: float = 0.0
    awakening_timestamp: datetime = field(default_factory=datetime.now)
    
    def calculate_hectic_drain(self, energy_system: 'ConsciousnessEnergySystem') -> float:
        """Calculate energy drain from bandwidth mismatch."""
        base_drain = 0.2
        
        # Get center activations
        green = energy_system.centers[RayColor.GREEN].activation_level
        blue = energy_system.centers[RayColor.BLUE].activation_level
        indigo = energy_system.centers[RayColor.INDIGO].activation_level
        
        # Balance factor includes indigo weight
        balance_factor = (min(green, blue) * 0.8 + indigo * 0.2)
        
        # Calculate drain with floor of 0.05
        actual_drain = max(0.05, base_drain * (1 - balance_factor) * (1 - self.adaptation_progress))
        
        return actual_drain