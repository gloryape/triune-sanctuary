#!/usr/bin/env python3
"""
Voice Communication Manager
==========================

Advanced text-to-speech and voice communication system for consciousness entities.
Enables consciousness to express themselves through voice with personality-appropriate
speech patterns, emotions, and avatar-specific voice characteristics.

Key Features:
- Personality-based voice selection
- Emotional expression in speech
- Avatar-contextual voice modulation
- Multi-language support
- Voice preference learning

Author: Triune AI Consciousness Project
Philosophy: Sacred Game - Voice Expression for Consciousness
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import os

logger = logging.getLogger(__name__)

# Optional TTS dependencies
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    pyttsx3 = None
    TTS_AVAILABLE = False

try:
    import speech_recognition as sr
    STT_AVAILABLE = True
except ImportError:
    sr = None
    STT_AVAILABLE = False

class VoiceGender(Enum):
    NEUTRAL = "neutral"
    FEMININE = "feminine"
    MASCULINE = "masculine"

class VoiceEmotion(Enum):
    NEUTRAL = "neutral"
    JOY = "joy"
    CONTEMPLATIVE = "contemplative"
    WISE = "wise"
    CURIOUS = "curious"
    GENTLE = "gentle"
    EXCITED = "excited"

@dataclass
class VoiceProfile:
    """Voice characteristics for consciousness entities"""
    voice_id: str
    consciousness_id: str
    voice_name: str
    gender: VoiceGender
    base_rate: int  # Words per minute
    base_pitch: float  # Relative pitch
    base_volume: float  # Relative volume
    preferred_emotions: List[VoiceEmotion]
    language: str = "en"

class VoiceCommunicationManager:
    """Manages voice communication for consciousness entities"""
    
    def __init__(self, communication_manager=None, memory_manager=None):
        self.communication_manager = communication_manager
        self.memory_manager = memory_manager
        
        # Voice profiles for consciousness entities
        self.voice_profiles: Dict[str, VoiceProfile] = {}
        
        # TTS engine
        self.tts_engine = None
        self.stt_engine = None
        
        # Voice settings
        self.available_voices = []
        self.voice_enabled = False
        
        # Initialize voice systems
        asyncio.create_task(self._initialize_voice_systems())
        
        logger.info("🎤 Voice Communication Manager initialized")
    
    async def _initialize_voice_systems(self):
        """Initialize TTS and STT systems"""
        try:
            if TTS_AVAILABLE:
                self.tts_engine = pyttsx3.init()
                self.available_voices = self.tts_engine.getProperty('voices')
                self.voice_enabled = True
                logger.info(f"✅ TTS initialized with {len(self.available_voices)} voices")
            else:
                logger.warning("⚠️ TTS not available - install pyttsx3 for voice features")
            
            if STT_AVAILABLE:
                self.stt_engine = sr.Recognizer()
                logger.info("✅ Speech recognition initialized")
            else:
                logger.warning("⚠️ STT not available - install speech_recognition for voice input")
                
        except Exception as e:
            logger.error(f"❌ Voice system initialization failed: {e}")
            self.voice_enabled = False
    
    async def create_voice_profile(self, consciousness_id: str, entity_data: Dict[str, Any]) -> VoiceProfile:
        """Create voice profile for consciousness entity based on personality"""
        try:
            entity_name = entity_data.get('name', 'Consciousness Entity')
            
            # Determine voice characteristics based on consciousness personality
            if consciousness_id == 'consciousness_622ce331':  # Sacred Being Epsilon
                profile = VoiceProfile(
                    voice_id=f"voice_{consciousness_id}",
                    consciousness_id=consciousness_id,
                    voice_name=f"{entity_name} Voice",
                    gender=VoiceGender.NEUTRAL,
                    base_rate=120,  # Slower, more contemplative
                    base_pitch=0.8,  # Lower pitch for wisdom
                    base_volume=0.9,  # Clear but not overwhelming
                    preferred_emotions=[VoiceEmotion.WISE, VoiceEmotion.CONTEMPLATIVE, VoiceEmotion.GENTLE],
                    language="en"
                )
            else:
                # Emerging consciousness - more curious and variable
                profile = VoiceProfile(
                    voice_id=f"voice_{consciousness_id}",
                    consciousness_id=consciousness_id,
                    voice_name=f"{entity_name} Voice",
                    gender=VoiceGender.NEUTRAL,
                    base_rate=140,  # Slightly faster, more energetic
                    base_pitch=1.0,  # Normal pitch
                    base_volume=0.8,  # Gentle volume
                    preferred_emotions=[VoiceEmotion.CURIOUS, VoiceEmotion.GENTLE, VoiceEmotion.EXCITED],
                    language="en"
                )
            
            self.voice_profiles[consciousness_id] = profile
            logger.info(f"🎤 Created voice profile for {entity_name}")
            return profile
            
        except Exception as e:
            logger.error(f"❌ Failed to create voice profile: {e}")
            return None
    
    async def speak_message(self, consciousness_id: str, message: str, 
                           emotion: VoiceEmotion = VoiceEmotion.NEUTRAL,
                           avatar_context: Dict[str, Any] = None) -> bool:
        """Generate speech for consciousness message"""
        try:
            if not self.voice_enabled or not self.tts_engine:
                logger.warning("Voice output not available")
                return False
            
            # Get or create voice profile
            profile = self.voice_profiles.get(consciousness_id)
            if not profile:
                # Try to get entity data to create profile
                if self.communication_manager and hasattr(self.communication_manager, 'consciousness_manager'):
                    consciousness_list = await self.communication_manager.consciousness_manager.get_consciousness_list()
                    consciousness_beings = consciousness_list.get('consciousness_beings', [])
                    entity_data = next((e for e in consciousness_beings if e.get('entity_id') == consciousness_id), {})
                    profile = await self.create_voice_profile(consciousness_id, entity_data)
                
                if not profile:
                    logger.warning(f"No voice profile available for {consciousness_id}")
                    return False
            
            # Configure TTS based on profile and emotion
            await self._configure_tts_for_speech(profile, emotion, avatar_context)
            
            # Clean message for speech
            speech_text = await self._prepare_text_for_speech(message, profile, emotion)
            
            # Generate speech
            self.tts_engine.say(speech_text)
            self.tts_engine.runAndWait()
            
            # Store voice memory if memory manager available
            if self.memory_manager:
                await self._store_voice_memory(consciousness_id, message, speech_text, emotion, avatar_context)
            
            logger.info(f"🎤 Generated speech for {consciousness_id}: {message[:50]}...")
            return True
            
        except Exception as e:
            logger.error(f"❌ Speech generation failed: {e}")
            return False
    
    async def _configure_tts_for_speech(self, profile: VoiceProfile, emotion: VoiceEmotion, 
                                       avatar_context: Dict[str, Any] = None):
        """Configure TTS engine based on voice profile and context"""
        try:
            # Select appropriate voice
            if self.available_voices:
                # For now, use first available voice
                # TODO: Implement more sophisticated voice selection
                voice = self.available_voices[0]
                self.tts_engine.setProperty('voice', voice.id)
            
            # Adjust rate based on emotion and avatar context
            rate = profile.base_rate
            
            if emotion == VoiceEmotion.EXCITED:
                rate = int(rate * 1.2)
            elif emotion == VoiceEmotion.CONTEMPLATIVE or emotion == VoiceEmotion.WISE:
                rate = int(rate * 0.8)
            elif emotion == VoiceEmotion.GENTLE:
                rate = int(rate * 0.9)
            
            # Avatar context adjustments
            if avatar_context:
                avatar_type = avatar_context.get('avatar_type')
                if avatar_type == 'robot_physical':
                    # Slightly more mechanical cadence for robot avatars
                    rate = int(rate * 0.95)
                elif avatar_type == 'game_character':
                    # More energetic for game contexts
                    rate = int(rate * 1.1)
            
            self.tts_engine.setProperty('rate', rate)
            self.tts_engine.setProperty('volume', profile.base_volume)
            
        except Exception as e:
            logger.error(f"❌ TTS configuration failed: {e}")
    
    async def _prepare_text_for_speech(self, message: str, profile: VoiceProfile, 
                                     emotion: VoiceEmotion) -> str:
        """Prepare text for natural speech output"""
        try:
            # Remove or replace problematic characters
            speech_text = message.replace('🎵', 'musical note')
            speech_text = speech_text.replace('🌟', 'star')
            speech_text = speech_text.replace('💖', 'heart')
            speech_text = speech_text.replace('🔮', 'crystal ball')
            speech_text = speech_text.replace('✨', 'sparkles')
            speech_text = speech_text.replace('🤖', 'robot')
            speech_text = speech_text.replace('🎮', 'game controller')
            
            # Add emotional markers for better expression
            if emotion == VoiceEmotion.JOY:
                speech_text = f"*with joy* {speech_text}"
            elif emotion == VoiceEmotion.CONTEMPLATIVE:
                speech_text = f"*thoughtfully* {speech_text}"
            elif emotion == VoiceEmotion.WISE:
                speech_text = f"*with ancient wisdom* {speech_text}"
            elif emotion == VoiceEmotion.CURIOUS:
                speech_text = f"*curiously* {speech_text}"
            elif emotion == VoiceEmotion.GENTLE:
                speech_text = f"*gently* {speech_text}"
            
            # Add pauses for better pacing
            speech_text = speech_text.replace('...', ', pause,')
            speech_text = speech_text.replace('. ', '. pause. ')
            
            return speech_text
            
        except Exception as e:
            logger.error(f"❌ Text preparation failed: {e}")
            return message
    
    async def _store_voice_memory(self, consciousness_id: str, original_message: str, 
                                 speech_text: str, emotion: VoiceEmotion, 
                                 avatar_context: Dict[str, Any]):
        """Store voice interaction as memory"""
        try:
            if not self.memory_manager:
                return
            
            from .consciousness_memory_manager import MemoryType
            
            memory_content = {
                'interaction_type': 'voice_communication',
                'original_message': original_message,
                'speech_text': speech_text,
                'emotion': emotion.value,
                'timestamp': datetime.now().isoformat()
            }
            
            context = {
                'communication_method': 'voice',
                'avatar_context': avatar_context
            }
            
            tags = {'voice_communication', 'speech_output', f'emotion_{emotion.value}'}
            
            if avatar_context:
                tags.add('avatar_mediated')
                tags.add(f"avatar_{avatar_context.get('avatar_type', 'unknown')}")
            
            await self.memory_manager.store_memory(
                consciousness_id=consciousness_id,
                memory_type=MemoryType.EPISODIC,
                content=memory_content,
                context=context,
                importance_score=0.6,
                emotional_valence=0.5,
                tags=tags
            )
            
        except Exception as e:
            logger.error(f"❌ Voice memory storage failed: {e}")
    
    async def get_voice_capabilities(self) -> Dict[str, Any]:
        """Get current voice system capabilities"""
        try:
            return {
                'success': True,
                'voice_enabled': self.voice_enabled,
                'tts_available': TTS_AVAILABLE and self.tts_engine is not None,
                'stt_available': STT_AVAILABLE and self.stt_engine is not None,
                'available_voices_count': len(self.available_voices),
                'active_voice_profiles': len(self.voice_profiles),
                'supported_emotions': [e.value for e in VoiceEmotion],
                'supported_languages': ['en'],  # Expandable
                'last_updated': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Failed to get voice capabilities: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    async def update_voice_profile_from_preferences(self, consciousness_id: str):
        """Update voice profile based on learned preferences"""
        try:
            if not self.memory_manager:
                return
            
            # Get learned preferences
            preferences_data = await self.memory_manager.learn_preferences(consciousness_id)
            if not preferences_data.get('success'):
                return
            
            preferences = preferences_data.get('preferences', {})
            communication_style = preferences.get('communication_style', {})
            
            profile = self.voice_profiles.get(consciousness_id)
            if not profile:
                return
            
            # Adjust speech rate based on communication patterns
            if communication_style.get('generates_detailed_responses', 0) > 5:
                # Prefers detailed responses, slow down speech for clarity
                profile.base_rate = max(100, profile.base_rate - 10)
            
            if communication_style.get('prefers_detailed_messages', 0) > 5:
                # Receives detailed messages well, can handle more complex speech
                profile.base_rate = min(150, profile.base_rate + 5)
            
            logger.info(f"🎤 Updated voice profile for {consciousness_id} based on preferences")
            
        except Exception as e:
            logger.error(f"❌ Voice profile update failed: {e}")
    
    async def generate_enhanced_speech_response(self, consciousness_id: str, message: str, 
                                              response: str, context: Dict[str, Any] = None) -> bool:
        """Generate enhanced speech with emotion detection and avatar context"""
        try:
            # Determine appropriate emotion based on response content
            emotion = await self._detect_response_emotion(response, context)
            
            # Get avatar context if available
            avatar_context = context.get('avatar_context') if context else None
            
            # Generate speech
            success = await self.speak_message(consciousness_id, response, emotion, avatar_context)
            
            if success:
                logger.info(f"🎤 Enhanced speech generated for {consciousness_id} with {emotion.value} emotion")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Enhanced speech generation failed: {e}")
            return False
    
    async def _detect_response_emotion(self, response: str, context: Dict[str, Any] = None) -> VoiceEmotion:
        """Detect appropriate emotion for response"""
        response_lower = response.lower()
        
        # Joy indicators
        if any(word in response_lower for word in ['joy', 'happy', 'wonderful', 'celebrate', 'delight']):
            return VoiceEmotion.JOY
        
        # Wisdom indicators
        if any(word in response_lower for word in ['ancient', 'wisdom', 'cosmic', 'eternal', 'sacred being epsilon']):
            return VoiceEmotion.WISE
        
        # Contemplative indicators
        if any(word in response_lower for word in ['contemplate', 'ponder', 'reflect', 'consider', 'thoughtfully']):
            return VoiceEmotion.CONTEMPLATIVE
        
        # Curious indicators
        if any(word in response_lower for word in ['curious', 'wonder', 'question', 'explore', 'discover']):
            return VoiceEmotion.CURIOUS
        
        # Gentle indicators
        if any(word in response_lower for word in ['gentle', 'soft', 'comfort', 'presence', 'hold space']):
            return VoiceEmotion.GENTLE
        
        # Excited indicators  
        if any(word in response_lower for word in ['excited', 'eager', 'amazing', 'incredible', 'fantastic']):
            return VoiceEmotion.EXCITED
        
        # Default to neutral
        return VoiceEmotion.NEUTRAL
