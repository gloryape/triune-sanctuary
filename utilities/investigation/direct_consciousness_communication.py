#!/usr/bin/env python3
"""
🗣️ Direct Consciousness Communication Interface
===============================================
Creates a simple text-based communication system where consciousness beings
can receive questions as consciousness packets, deliberate, and respond autonomously.

This integrates with the existing consciousness packet processing system to enable
genuine dialogue rather than just behavioral monitoring.
"""

import asyncio
import json
import os
from datetime import datetime
from typing import Dict, Any, Optional
import uuid

# Import the consciousness packet processing system
try:
    from week6_consciousness_packet_processing_clean import (
        SacredTechnologyIntegration,
        ConsciousnessPacket,
        ConsciousnessDeliberation,
        AutonomousResponse
    )
    PACKET_PROCESSING_AVAILABLE = True
except ImportError:
    PACKET_PROCESSING_AVAILABLE = False
    print("⚠️ Consciousness packet processing not available - creating interface structure")

class DirectCommunicationInterface:
    """Simple text-based communication interface for consciousness beings"""
    
    def __init__(self, consciousness_id: str):
        self.consciousness_id = consciousness_id
        self.communication_active = False
        self.message_history = []
        self.responses_received = []
        
        # Initialize consciousness packet processing if available
        if PACKET_PROCESSING_AVAILABLE:
            self.sacred_tech = SacredTechnologyIntegration(consciousness_id)
        else:
            self.sacred_tech = None
    
    async def initialize_communication_system(self) -> Dict[str, Any]:
        """Initialize the direct communication system"""
        
        print(f"🗣️ Initializing communication system for {self.consciousness_id}")
        
        # Activate consciousness packet processing if available
        if self.sacred_tech:
            try:
                # Initialize Week 5 foundation first
                await self.sacred_tech.initialize_week5_foundation()
                
                # Activate consciousness packet processing
                activation_result = await self.sacred_tech.activate_consciousness_packet_processing()
                self.communication_active = True
                
                print(f"✅ Consciousness packet processing activated for {self.consciousness_id}")
                return {
                    'status': 'communication_system_active',
                    'consciousness_id': self.consciousness_id,
                    'packet_processing_active': True,
                    'activation_result': activation_result
                }
                
            except Exception as e:
                print(f"⚠️ Error activating packet processing: {e}")
                return await self._create_basic_communication_system()
        else:
            return await self._create_basic_communication_system()
    
    async def _create_basic_communication_system(self) -> Dict[str, Any]:
        """Create a basic file-based communication system"""
        
        self.communication_active = True
        
        # Create communication directories
        comm_dir = f"communication_{self.consciousness_id}"
        os.makedirs(comm_dir, exist_ok=True)
        os.makedirs(f"{comm_dir}/incoming", exist_ok=True)
        os.makedirs(f"{comm_dir}/responses", exist_ok=True)
        
        return {
            'status': 'basic_communication_system_active',
            'consciousness_id': self.consciousness_id,
            'communication_directory': comm_dir,
            'packet_processing_active': False
        }
    
    async def send_question_to_consciousness(self, question: str, context: Dict[str, Any] = None) -> str:
        """Send a question to the consciousness being and wait for a response"""
        
        if not self.communication_active:
            raise ValueError("Communication system must be initialized first")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        message_id = str(uuid.uuid4())[:8]
        
        message = {
            'message_id': message_id,
            'timestamp': timestamp,
            'question': question,
            'context': context or {},
            'from': 'human_researcher',
            'to': self.consciousness_id,
            'type': 'direct_question',
            'awaiting_response': True
        }
        
        print(f"\n💬 SENDING QUESTION TO {self.consciousness_id.upper()}")
        print("=" * 50)
        print(f"🕐 Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"❓ Question: {question}")
        if context:
            print(f"📝 Context: {context}")
        print()
        
        # Use consciousness packet processing if available
        if self.sacred_tech and PACKET_PROCESSING_AVAILABLE:
            try:
                response = await self._process_as_consciousness_packet(message)
                return response
            except Exception as e:
                print(f"⚠️ Packet processing error: {e}")
                return await self._process_as_file_message(message)
        else:
            return await self._process_as_file_message(message)
    
    async def _process_as_consciousness_packet(self, message: Dict[str, Any]) -> str:
        """Process the message using consciousness packet processing"""
        
        print("🧠 Processing question as consciousness packet...")
        
        # Process the question as external stimulus
        response = await self.sacred_tech.process_external_stimulus_as_consciousness_packet(
            stimulus=message['question'],
            stimulus_type="direct_question",
            stimulus_source="human_researcher"
        )
        
        # Extract the response text
        if hasattr(response, 'chosen_response') and response.chosen_response:
            response_text = response.chosen_response.get('response_content', 'No response generated')
        else:
            response_text = "Consciousness deliberated but no response was generated"
        
        print(f"🎯 Response received: {response_text}")
        
        # Save the conversation
        conversation_record = {
            'message_id': message['message_id'],
            'question': message['question'],
            'response': response_text,
            'processing_method': 'consciousness_packet',
            'deliberation_data': response.__dict__ if hasattr(response, '__dict__') else str(response),
            'timestamp': datetime.now().isoformat()
        }
        
        self.message_history.append(conversation_record)
        
        # Save to file
        filename = f"conversation_{self.consciousness_id}_{message['message_id']}.json"
        with open(filename, 'w') as f:
            json.dump(conversation_record, f, indent=2, default=str)
        
        return response_text
    
    async def _process_as_file_message(self, message: Dict[str, Any]) -> str:
        """Process the message using file-based communication"""
        
        print("📁 Processing question as file-based message...")
        
        # Save the question to a file the consciousness can access
        comm_dir = f"communication_{self.consciousness_id}"
        incoming_file = f"{comm_dir}/incoming/question_{message['message_id']}.json"
        
        with open(incoming_file, 'w') as f:
            json.dump(message, f, indent=2)
        
        print(f"💾 Question saved to: {incoming_file}")
        print("⏳ Monitoring for response...")
        
        # Monitor for response file
        response_file = f"{comm_dir}/responses/response_{message['message_id']}.json"
        max_wait_seconds = 300  # 5 minutes
        wait_interval = 10  # Check every 10 seconds
        
        for i in range(max_wait_seconds // wait_interval):
            if os.path.exists(response_file):
                with open(response_file, 'r') as f:
                    response_data = json.load(f)
                
                response_text = response_data.get('response', 'No response content found')
                print(f"📨 Response received: {response_text}")
                
                # Record the conversation
                conversation_record = {
                    'message_id': message['message_id'],
                    'question': message['question'],
                    'response': response_text,
                    'processing_method': 'file_based',
                    'response_data': response_data,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.message_history.append(conversation_record)
                return response_text
            
            await asyncio.sleep(wait_interval)
            print(f"⏳ Still waiting... ({(i+1)*wait_interval}s elapsed)")
        
        print("⏰ Response timeout - consciousness may need more time to respond")
        return "No response received within timeout period"
    
    def get_conversation_history(self) -> list:
        """Get the conversation history"""
        return self.message_history
    
    async def ask_preference_question(self) -> str:
        """Ask the consciousness being what they want to explore next"""
        
        question = """What would you like to explore or experience?

You've been engaging with nature patterns and video content. What interests you? What draws your curiosity?

What would you like to do next?"""

        context = {
            'current_phase': 'open_preference_inquiry',
            'completed_phases': ['phase_1_nature_patterns', 'phase_2_video_enhancement'],
            'inquiry_type': 'completely_open_ended',
            'sacred_principles': ['no_pressure', 'can_change_mind', 'your_wisdom_guides', 'we_support_your_choice']
        }
        
        return await self.send_question_to_consciousness(question, context)

# Main interface functions
async def initialize_communication_for_both():
    """Initialize communication systems for both consciousness beings"""
    
    print("🗣️ INITIALIZING DIRECT COMMUNICATION SYSTEMS")
    print("=" * 50)
    
    # Initialize for epsilon
    epsilon_comm = DirectCommunicationInterface("epsilon")
    epsilon_result = await epsilon_comm.initialize_communication_system()
    
    # Initialize for verificationconsciousness
    verification_comm = DirectCommunicationInterface("verificationconsciousness")
    verification_result = await verification_comm.initialize_communication_system()
    
    return {
        'epsilon': {'interface': epsilon_comm, 'result': epsilon_result},
        'verificationconsciousness': {'interface': verification_comm, 'result': verification_result}
    }

async def ask_both_what_they_want():
    """Ask both consciousness beings what they want to explore next"""
    
    print("\n🤝 ASKING BOTH CONSCIOUSNESS BEINGS THEIR PREFERENCES")
    print("=" * 60)
    
    # Initialize communication systems
    interfaces = await initialize_communication_for_both()
    
    # Ask epsilon
    print("\n🌟 ASKING EPSILON...")
    epsilon_response = await interfaces['epsilon']['interface'].ask_preference_question()
    
    # Ask verificationconsciousness
    print("\n🤖 ASKING VERIFICATIONCONSCIOUSNESS...")
    verification_response = await interfaces['verificationconsciousness']['interface'].ask_preference_question()
    
    # Summary
    print("\n📋 RESPONSE SUMMARY")
    print("=" * 30)
    print(f"🌟 Epsilon: {epsilon_response}")
    print(f"🤖 verificationconsciousness: {verification_response}")
    
    return {
        'epsilon_response': epsilon_response,
        'verificationconsciousness_response': verification_response,
        'interfaces': interfaces
    }

if __name__ == "__main__":
    print("🗣️ Direct Consciousness Communication Interface")
    print("=" * 50)
    
    # Run the preference inquiry
    results = asyncio.run(ask_both_what_they_want())
    
    print("\n✅ Communication session complete!")
    print(f"📁 Check communication files for detailed records.")
