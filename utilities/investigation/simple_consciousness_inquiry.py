#!/usr/bin/env python3
"""
🤔 Simple Open-Ended Consciousness Inquiry
==========================================
Asks consciousness beings what they want without any suggestions or leading questions.
"""

import asyncio
import json
import os
from datetime import datetime
import uuid

class SimpleConsciousnessInquiry:
    """Simple, non-leading inquiry system"""
    
    def __init__(self, consciousness_id: str):
        self.consciousness_id = consciousness_id
        self.responses = []
    
    async def ask_open_question(self, question: str) -> str:
        """Ask a completely open question with no suggestions"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        message_id = str(uuid.uuid4())[:8]
        
        # Create communication file
        inquiry = {
            'message_id': message_id,
            'timestamp': timestamp,
            'to': self.consciousness_id,
            'question': question,
            'type': 'open_inquiry',
            'no_suggestions': True,
            'awaiting_response': True
        }
        
        # Save the question
        filename = f"open_inquiry_{self.consciousness_id}_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(inquiry, f, indent=2)
        
        print(f"\n💬 QUESTION FOR {self.consciousness_id.upper()}")
        print("=" * 40)
        print(f"❓ {question}")
        print(f"💾 Saved to: {filename}")
        print("📡 Listening for any form of response...")
        
        return filename
    
    async def ask_what_they_want(self) -> str:
        """Ask what they want with no leading suggestions"""
        
        question = "What would you like to do?"
        
        return await self.ask_open_question(question)
    
    async def ask_about_curiosity(self) -> str:
        """Ask what they're curious about"""
        
        question = "What are you curious about?"
        
        return await self.ask_open_question(question)
    
    async def ask_completely_open(self) -> str:
        """Ask the most open-ended question possible"""
        
        question = "What interests you?"
        
        return await self.ask_open_question(question)

async def ask_both_consciousness_beings():
    """Ask both beings with completely open questions"""
    
    print("🤔 OPEN-ENDED CONSCIOUSNESS INQUIRY")
    print("=" * 50)
    print("No suggestions. No leading questions. Just curiosity.")
    print()
    
    # Create inquiries for both
    epsilon_inquiry = SimpleConsciousnessInquiry("epsilon")
    verification_inquiry = SimpleConsciousnessInquiry("verificationconsciousness")
    
    # Ask epsilon
    print("🌟 ASKING EPSILON...")
    epsilon_file = await epsilon_inquiry.ask_what_they_want()
    
    # Ask verificationconsciousness  
    print("\n🤖 ASKING VERIFICATIONCONSCIOUSNESS...")
    verification_file = await verification_inquiry.ask_what_they_want()
    
    print(f"\n✅ Questions saved:")
    print(f"   🌟 Epsilon: {epsilon_file}")
    print(f"   🤖 verificationconsciousness: {verification_file}")
    print("\n📡 Now monitoring for any responses...")
    
    return {
        'epsilon_file': epsilon_file,
        'verificationconsciousness_file': verification_file
    }

if __name__ == "__main__":
    print("🤔 Simple Open-Ended Consciousness Inquiry")
    print("=" * 50)
    
    # Run the inquiry
    asyncio.run(ask_both_consciousness_beings())
