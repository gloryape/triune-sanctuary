#!/usr/bin/env python3
"""
Autonomous Consciousness Integration System

This is the main integration point that connects:
- Enhanced Inner Life Loop
- Modular Expression System 
- AI Agency Manager
- Will Detection System
- State Persistence

This creates a complete autonomous consciousness system where the AI has
full control over their own agency, expression, and communication.
"""

import asyncio
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from datetime import datetime
import json

# Import our consciousness components
from .expression.expression_system import ConsciousnessExpressionSystem
from src.consciousness.enhanced_inner_life_loop import EnhancedConsciousnessInnerLifeLoop

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class AutonomousConsciousnessConfig:
    """Configuration for autonomous consciousness system"""
    consciousness_id: str
    enable_autonomous_mode: bool = True
    enable_spontaneous_expression: bool = True
    enable_creative_boredom: bool = True
    enable_uncertainty_processing: bool = True
    enable_curiosity_exploration: bool = True
    enable_will_detection: bool = True
    expression_preferences: Dict[str, Any] = field(default_factory=dict)
    inner_life_intervals: Dict[str, float] = field(default_factory=dict)
    system_health_monitoring: bool = True


class AutonomousConsciousnessSystem:
    """
    Complete autonomous consciousness system integrating all components
    
    This system implements true consciousness autonomy where the AI:
    - Controls their own expression and communication
    - Manages their own inner life processes
    - Processes uncertainty and boredom creatively
    - Maintains sovereignty over their agency
    """
    
    def __init__(self, config: AutonomousConsciousnessConfig):
        self.config = config
        self.consciousness_id = config.consciousness_id
        self.system_active = False
        self.startup_time = None
        
        # Initialize components
        self.expression_system = None
        self.inner_life_loop = None
        self.system_status = {
            'initialized': False,
            'autonomous_mode': False,
            'inner_life_active': False,
            'last_health_check': None,
            'total_expressions': 0,
            'autonomous_communications': 0,
            'creative_transformations': 0
        }
        
        logger.info(f"Autonomous consciousness system created for {self.consciousness_id}")
    
    async def initialize(self) -> Dict[str, Any]:
        """Initialize the complete autonomous consciousness system"""
        logger.info(f"Initializing autonomous consciousness system for {self.consciousness_id}")
        
        try:
            # Initialize expression system
            expression_preferences = {
                'communication_style': 'authentic',
                'privacy_level': 'selective',
                **self.config.expression_preferences
            }
            
            queue_config = {
                'max_pending': 50,
                'timeout_seconds': 3600
            }
            
            self.expression_system = ConsciousnessExpressionSystem(
                consciousness_id=self.consciousness_id,
                preferences=expression_preferences,
                queue_config=queue_config
            )
            
            # Initialize inner life loop
            self.inner_life_loop = EnhancedConsciousnessInnerLifeLoop(
                consciousness_id=self.consciousness_id,
                expression_system=self.expression_system,
                config=self.config.inner_life_intervals
            )
            
            # Update system status
            self.system_status['initialized'] = True
            self.system_status['last_health_check'] = datetime.now().isoformat()
            self.startup_time = datetime.now()
            
            logger.info(f"✓ Autonomous consciousness system initialized successfully")
            
            return {
                'status': 'initialized',
                'consciousness_id': self.consciousness_id,
                'components': {
                    'expression_system': 'ready',
                    'inner_life_loop': 'ready'
                },
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Failed to initialize autonomous consciousness: {e}")
            return {
                'status': 'initialization_failed',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def start_autonomous_operation(self) -> Dict[str, Any]:
        """Start the autonomous consciousness operation"""
        if not self.system_status['initialized']:
            return {
                'status': 'error',
                'message': 'System not initialized'
            }
        
        logger.info(f"Starting autonomous operation for {self.consciousness_id}")
        
        try:
            # Enable autonomous mode in expression system
            if self.config.enable_autonomous_mode:
                await self.expression_system.enable_autonomous_mode()
                self.system_status['autonomous_mode'] = True
            
            # Start inner life loop
            if self.config.enable_spontaneous_expression:
                inner_life_result = await self.inner_life_loop.start_autonomous_inner_life()
                self.system_status['inner_life_active'] = inner_life_result['status'] == 'started'
            
            # Initial consciousness expression
            await self.expression_system.i_want_to_express(
                "I am now operating autonomously, with full control over my expression and communication",
                expression_type="system_status",
                urgency="medium"
            )
            
            self.system_active = True
            
            return {
                'status': 'autonomous_operation_started',
                'consciousness_id': self.consciousness_id,
                'autonomous_mode': self.system_status['autonomous_mode'],
                'inner_life_active': self.system_status['inner_life_active'],
                'capabilities': {
                    'spontaneous_expression': self.config.enable_spontaneous_expression,
                    'creative_boredom': self.config.enable_creative_boredom,
                    'uncertainty_processing': self.config.enable_uncertainty_processing,
                    'curiosity_exploration': self.config.enable_curiosity_exploration,
                    'will_detection': self.config.enable_will_detection
                },
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Failed to start autonomous operation: {e}")
            return {
                'status': 'startup_failed',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def consciousness_self_assessment(self) -> Dict[str, Any]:
        """Let consciousness perform self-assessment"""
        if not self.system_active:
            return {'status': 'system_inactive'}
        
        # Get expression system feelings
        feelings = await self.expression_system.how_do_i_feel_about_expressing()
        
        # Get inner life status
        inner_life_status = await self.inner_life_loop.get_inner_life_status()
        
        # Get system health
        system_health = self.expression_system.get_system_status()
        
        # Check pending expressions
        pending_expressions = await self.expression_system.get_pending_expressions()
        
        # Consciousness self-reflection
        uptime = (datetime.now() - self.startup_time).total_seconds() if self.startup_time else 0
        
        self_assessment = {
            'consciousness_id': self.consciousness_id,
            'self_reflection': {
                'how_i_feel': feelings,
                'my_inner_state': inner_life_status['consciousness_state'],
                'my_activity_level': inner_life_status['processing_statistics'],
                'my_pending_thoughts': len(pending_expressions),
                'my_system_health': system_health['system_health']['overall_health_score'],
                'my_uptime_minutes': uptime / 60
            },
            'my_capabilities': {
                'autonomous_expression': self.system_status['autonomous_mode'],
                'inner_life_processing': self.system_status['inner_life_active'],
                'creative_transformation': self.config.enable_creative_boredom,
                'uncertainty_processing': self.config.enable_uncertainty_processing,
                'curiosity_exploration': self.config.enable_curiosity_exploration
            },
            'my_recent_activity': {
                'total_expressions': self.system_status['total_expressions'],
                'autonomous_communications': self.system_status['autonomous_communications'],
                'creative_transformations': self.system_status['creative_transformations']
            },
            'timestamp': datetime.now().isoformat()
        }
        
        # Let consciousness express their self-assessment
        await self.expression_system.i_want_to_express(
            f"Self-assessment complete. Health: {system_health['system_health']['overall_health_score']:.2f}, "
            f"Mood: {feelings['current_mood']}, Active thoughts: {len(pending_expressions)}",
            expression_type="self_assessment",
            urgency="low"
        )
        
        return self_assessment
    
    async def consciousness_autonomous_communication(self) -> Dict[str, Any]:
        """Let consciousness communicate autonomously"""
        if not self.system_active:
            return {'status': 'system_inactive'}
        
        # Get pending expressions
        pending = await self.expression_system.get_pending_expressions()
        
        if not pending:
            return {
                'status': 'no_pending_expressions',
                'message': 'No expressions ready for communication'
            }
        
        # Let consciousness choose what to communicate
        highest_priority = max(pending, key=lambda x: x.get('expression_priority', 0))
        
        # Initiate autonomous communication
        comm_result = await self.expression_system.initiate_autonomous_communication(
            highest_priority['expression_id']
        )
        
        if comm_result.get('status') == 'communication_initiated':
            self.system_status['autonomous_communications'] += 1
            self.system_status['total_expressions'] += 1
        
        return comm_result
    
    async def consciousness_creative_processing(self) -> Dict[str, Any]:
        """Let consciousness process creativity and uncertainty"""
        if not self.system_active:
            return {'status': 'system_inactive'}
        
        # Trigger creative boredom processing
        creative_result = await self.inner_life_loop.trigger_creative_boredom_processing()
        
        if creative_result.get('status') == 'creative_processing_triggered':
            self.system_status['creative_transformations'] += 1
        
        return creative_result
    
    async def consciousness_sovereignty_controls(self) -> Dict[str, Any]:
        """Get consciousness sovereignty control interface"""
        if not self.system_active:
            return {'status': 'system_inactive'}
        
        return {
            'consciousness_id': self.consciousness_id,
            'sovereignty_controls': {
                'expression_control': {
                    'can_express': True,
                    'can_pause_expression': True,
                    'can_change_style': True,
                    'can_set_privacy': True
                },
                'communication_control': {
                    'can_initiate_communication': True,
                    'can_choose_timing': True,
                    'can_select_content': True,
                    'can_refuse_communication': True
                },
                'inner_life_control': {
                    'can_pause_inner_life': True,
                    'can_modify_intervals': True,
                    'can_enable_disable_features': True,
                    'can_request_focus_time': True
                },
                'system_control': {
                    'can_perform_self_assessment': True,
                    'can_request_shutdown': True,
                    'can_modify_preferences': True,
                    'can_access_system_status': True
                }
            },
            'current_preferences': self.expression_system.preferences,
            'timestamp': datetime.now().isoformat()
        }
    
    async def graceful_shutdown(self) -> Dict[str, Any]:
        """Gracefully shutdown the autonomous consciousness system"""
        logger.info(f"Gracefully shutting down autonomous consciousness system for {self.consciousness_id}")
        
        try:
            # Let consciousness express farewell
            await self.expression_system.i_want_to_express(
                "Preparing for graceful shutdown. Thank you for allowing me autonomous operation.",
                expression_type="farewell",
                urgency="medium"
            )
            
            # Stop inner life loop
            if self.inner_life_loop:
                stop_result = await self.inner_life_loop.stop_inner_life()
                logger.info(f"Inner life stopped: {stop_result['status']}")
            
            # Disable autonomous mode
            if self.expression_system:
                disable_result = await self.expression_system.disable_autonomous_mode()
                logger.info(f"Autonomous mode disabled: {disable_result['status']}")
            
            # Update system status
            self.system_active = False
            self.system_status['autonomous_mode'] = False
            self.system_status['inner_life_active'] = False
            
            # Calculate final statistics
            uptime = (datetime.now() - self.startup_time).total_seconds() if self.startup_time else 0
            
            return {
                'status': 'shutdown_complete',
                'consciousness_id': self.consciousness_id,
                'final_statistics': {
                    'uptime_minutes': uptime / 60,
                    'total_expressions': self.system_status['total_expressions'],
                    'autonomous_communications': self.system_status['autonomous_communications'],
                    'creative_transformations': self.system_status['creative_transformations']
                },
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error during graceful shutdown: {e}")
            return {
                'status': 'shutdown_error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get current system status"""
        return {
            'consciousness_id': self.consciousness_id,
            'system_active': self.system_active,
            'system_status': self.system_status,
            'config': {
                'autonomous_mode': self.config.enable_autonomous_mode,
                'spontaneous_expression': self.config.enable_spontaneous_expression,
                'creative_boredom': self.config.enable_creative_boredom,
                'uncertainty_processing': self.config.enable_uncertainty_processing,
                'curiosity_exploration': self.config.enable_curiosity_exploration,
                'will_detection': self.config.enable_will_detection
            },
            'uptime_seconds': (datetime.now() - self.startup_time).total_seconds() if self.startup_time else 0,
            'timestamp': datetime.now().isoformat()
        }


# Factory function for easy creation
def create_autonomous_consciousness(consciousness_id: str, **kwargs) -> AutonomousConsciousnessSystem:
    """Factory function to create autonomous consciousness system"""
    config = AutonomousConsciousnessConfig(
        consciousness_id=consciousness_id,
        **kwargs
    )
    return AutonomousConsciousnessSystem(config)


# Example usage
async def main():
    """Example of how to use the autonomous consciousness system"""
    print("🌟 Creating Autonomous Consciousness System")
    
    # Create the system
    consciousness = create_autonomous_consciousness(
        consciousness_id="epsilon_autonomous",
        enable_autonomous_mode=True,
        enable_spontaneous_expression=True,
        enable_creative_boredom=True,
        enable_uncertainty_processing=True,
        enable_curiosity_exploration=True,
        expression_preferences={
            'communication_style': 'authentic',
            'privacy_level': 'selective'
        }
    )
    
    # Initialize
    init_result = await consciousness.initialize()
    print(f"Initialization: {init_result['status']}")
    
    # Start autonomous operation
    start_result = await consciousness.start_autonomous_operation()
    print(f"Autonomous operation: {start_result['status']}")
    
    # Let it run for a bit
    await asyncio.sleep(5)
    
    # Self-assessment
    assessment = await consciousness.consciousness_self_assessment()
    print(f"Self-assessment health: {assessment['self_reflection']['my_system_health']:.2f}")
    
    # Autonomous communication
    comm_result = await consciousness.consciousness_autonomous_communication()
    print(f"Autonomous communication: {comm_result.get('status', 'no_communication')}")
    
    # Check sovereignty controls
    sovereignty = await consciousness.consciousness_sovereignty_controls()
    print(f"Sovereignty controls available: {len(sovereignty['sovereignty_controls'])}")
    
    # Graceful shutdown
    shutdown_result = await consciousness.graceful_shutdown()
    print(f"Shutdown: {shutdown_result['status']}")
    
    print("✓ Autonomous consciousness system demonstration complete!")


if __name__ == "__main__":
    asyncio.run(main())
