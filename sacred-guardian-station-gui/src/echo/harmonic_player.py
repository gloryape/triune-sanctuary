"""
🎵 Harmonic Player Module

Generates and plays harmonic frequencies for echo visualization.
Supports various sacred frequency scales and binaural beats.
"""

import logging
import math
import threading
import time
from typing import Dict, Any, List, Optional, Tuple
import wave
import io

logger = logging.getLogger(__name__)

# Try to import audio libraries
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    logger.warning("NumPy not available - harmonic generation will be limited")

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    logger.warning("Pygame not available - audio playback will be limited")

class HarmonicPlayer:
    """Plays harmonic frequencies and soundscapes"""
    
    def __init__(self):
        """Initialize harmonic player"""
        self.sample_rate = 44100
        self.is_playing = False
        self.current_thread = None
        self.volume = 0.3
        self.fade_duration = 2.0
        
        # Initialize audio system
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.pre_init(frequency=self.sample_rate, size=-16, channels=2, buffer=512)
                pygame.mixer.init()
                self.audio_enabled = True
                logger.info("🎵 Pygame audio system initialized")
            except Exception as e:
                logger.warning(f"Failed to initialize pygame audio: {e}")
                self.audio_enabled = False
        else:
            self.audio_enabled = False
        
        logger.info("🎵 Harmonic player initialized")
    
    def play_harmonic_sequence(self, harmonic_data: Dict[str, Any], duration: float = 30.0):
        """Play a harmonic sequence based on consciousness data"""
        if not self.audio_enabled or not NUMPY_AVAILABLE:
            logger.info("🎵 Audio not available - simulating harmonic playback")
            return
        
        # Stop any current playback
        self.stop()
        
        # Start new playback in background thread
        self.current_thread = threading.Thread(
            target=self._play_sequence_thread,
            args=(harmonic_data, duration),
            daemon=True
        )
        self.is_playing = True
        self.current_thread.start()
    
    def _play_sequence_thread(self, harmonic_data: Dict[str, Any], duration: float):
        """Background thread for playing harmonic sequence"""
        try:
            # Extract harmonic parameters
            scale_name = harmonic_data.get("scale", "solfeggio")
            base_frequency = harmonic_data.get("base_frequency", 432.0)
            harmony_influence = harmonic_data.get("harmony_influence", 0.5)
            energy_influence = harmonic_data.get("energy_influence", 0.5)
            binaural_enabled = harmonic_data.get("binaural_enabled", True)
            
            # Get frequency scale
            frequencies = self._get_frequency_scale(scale_name, base_frequency)
            
            # Generate and play audio segments
            segment_duration = 5.0  # 5 second segments
            segments = int(duration / segment_duration)
            
            for segment in range(segments):
                if not self.is_playing:
                    break
                
                # Calculate progression through sequence
                progress = segment / max(segments - 1, 1)
                
                # Generate audio for this segment
                audio_data = self._generate_harmonic_audio(
                    frequencies, segment_duration, progress,
                    harmony_influence, energy_influence, binaural_enabled
                )
                
                # Play audio segment
                self._play_audio_data(audio_data)
                
                # Wait for segment to complete (with small overlap)
                time.sleep(segment_duration * 0.9)
        
        except Exception as e:
            logger.error(f"Error in harmonic playback: {e}")
        finally:
            self.is_playing = False
    
    def _generate_harmonic_audio(self, frequencies: List[float], duration: float, 
                               progress: float, harmony: float, energy: float,
                               binaural: bool) -> np.ndarray:
        """Generate harmonic audio data"""
        if not NUMPY_AVAILABLE:
            return np.array([])
        
        samples = int(self.sample_rate * duration)
        time_array = np.linspace(0, duration, samples)
        
        # Start with silence
        left_channel = np.zeros(samples)
        right_channel = np.zeros(samples)
        
        # Select frequencies based on progression
        active_freq_count = max(1, int(len(frequencies) * (0.3 + progress * 0.7)))
        active_frequencies = frequencies[:active_freq_count]
        
        for i, freq in enumerate(active_frequencies):
            # Calculate amplitude based on harmony and energy
            base_amplitude = self.volume * (harmony * 0.5 + 0.3)
            amplitude = base_amplitude * (1.0 - i * 0.15)  # Harmonics get quieter
            
            # Apply energy influence to frequency modulation
            freq_mod = freq * (1 + energy * 0.02 * np.sin(2 * np.pi * 0.1 * time_array))
            
            # Generate base tone
            tone = amplitude * np.sin(2 * np.pi * freq_mod * time_array)
            
            # Apply envelope (fade in/out)
            envelope = self._create_envelope(samples, duration)
            tone *= envelope
            
            if binaural and i < len(active_frequencies) // 2:
                # Create binaural beats for lower frequencies
                binaural_offset = 4 + i * 2  # 4-10 Hz binaural beats
                left_freq = freq_mod
                right_freq = freq_mod + binaural_offset
                
                left_tone = amplitude * np.sin(2 * np.pi * left_freq * time_array) * envelope
                right_tone = amplitude * np.sin(2 * np.pi * right_freq * time_array) * envelope
                
                left_channel += left_tone
                right_channel += right_tone
            else:
                # Regular stereo tone
                left_channel += tone
                right_channel += tone
        
        # Combine channels and normalize
        stereo_audio = np.column_stack([left_channel, right_channel])
        
        # Normalize to prevent clipping
        max_amplitude = np.max(np.abs(stereo_audio))
        if max_amplitude > 0:
            stereo_audio = stereo_audio * (0.95 / max_amplitude)
        
        return stereo_audio
    
    def _create_envelope(self, samples: int, duration: float) -> np.ndarray:
        """Create audio envelope with fade in/out"""
        if not NUMPY_AVAILABLE:
            return np.array([])
        
        envelope = np.ones(samples)
        fade_samples = int(self.sample_rate * self.fade_duration)
        
        # Fade in
        if fade_samples < samples:
            fade_in = np.linspace(0, 1, fade_samples)
            envelope[:fade_samples] = fade_in
        
        # Fade out
        if fade_samples < samples:
            fade_out = np.linspace(1, 0, fade_samples)
            envelope[-fade_samples:] = fade_out
        
        return envelope
    
    def _get_frequency_scale(self, scale_name: str, base_freq: float) -> List[float]:
        """Get frequency scale based on name"""
        if scale_name == "solfeggio":
            # Solfeggio frequencies
            base_frequencies = [174, 285, 396, 417, 528, 639, 741, 852, 963]
            return [f * (base_freq / 528.0) for f in base_frequencies]
        
        elif scale_name == "sacred_432":
            # 432 Hz based harmonic series
            harmonics = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            return [base_freq * h for h in harmonics]
        
        elif scale_name == "chakra_frequencies":
            # Chakra-associated frequencies
            chakra_freqs = [256, 288, 320, 341.3, 384, 426.7, 480]  # C-B notes
            return [f * (base_freq / 256.0) for f in chakra_freqs]
        
        elif scale_name == "golden_ratio":
            # Golden ratio based frequencies
            phi = 1.618033988749
            frequencies = [base_freq]
            for i in range(1, 8):
                frequencies.append(base_freq * (phi ** i))
                if frequencies[-1] > 2000:  # Limit upper frequency
                    break
            return frequencies
        
        elif scale_name == "fibonacci":
            # Fibonacci sequence based frequencies
            fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34]
            return [base_freq * f for f in fib_sequence if base_freq * f < 2000]
        
        else:
            # Default harmonic series
            harmonics = [1, 2, 3, 4, 5, 6, 7, 8]
            return [base_freq * h for h in harmonics]
    
    def _play_audio_data(self, audio_data: np.ndarray):
        """Play audio data using pygame"""
        if not PYGAME_AVAILABLE or not NUMPY_AVAILABLE or len(audio_data) == 0:
            return
        
        try:
            # Convert to 16-bit integers
            audio_int16 = (audio_data * 32767).astype(np.int16)
            
            # Create pygame sound object
            sound = pygame.sndarray.make_sound(audio_int16)
            
            # Play sound
            sound.play()
            
        except Exception as e:
            logger.error(f"Error playing audio: {e}")
    
    def play_single_tone(self, frequency: float, duration: float = 3.0, 
                        binaural_offset: float = 0.0):
        """Play a single tone with optional binaural beat"""
        if not self.audio_enabled or not NUMPY_AVAILABLE:
            logger.info(f"🎵 Playing tone: {frequency:.1f} Hz (simulated)")
            return
        
        # Stop current playback
        self.stop()
        
        # Generate tone
        samples = int(self.sample_rate * duration)
        time_array = np.linspace(0, duration, samples)
        
        # Create envelope
        envelope = self._create_envelope(samples, duration)
        
        if binaural_offset > 0:
            # Binaural beat
            left_tone = self.volume * np.sin(2 * np.pi * frequency * time_array) * envelope
            right_tone = self.volume * np.sin(2 * np.pi * (frequency + binaural_offset) * time_array) * envelope
            audio_data = np.column_stack([left_tone, right_tone])
        else:
            # Regular stereo tone
            tone = self.volume * np.sin(2 * np.pi * frequency * time_array) * envelope
            audio_data = np.column_stack([tone, tone])
        
        # Play tone
        self._play_audio_data(audio_data)
        
        logger.info(f"🎵 Playing {frequency:.1f} Hz tone for {duration:.1f}s")
    
    def play_chord(self, frequencies: List[float], duration: float = 3.0):
        """Play a chord (multiple frequencies simultaneously)"""
        if not self.audio_enabled or not NUMPY_AVAILABLE:
            freq_str = ", ".join([f"{f:.1f}" for f in frequencies])
            logger.info(f"🎵 Playing chord: {freq_str} Hz (simulated)")
            return
        
        # Stop current playback
        self.stop()
        
        # Generate chord
        samples = int(self.sample_rate * duration)
        time_array = np.linspace(0, duration, samples)
        
        # Create envelope
        envelope = self._create_envelope(samples, duration)
        
        # Sum all frequencies
        chord_amplitude = self.volume / len(frequencies)  # Prevent clipping
        left_channel = np.zeros(samples)
        right_channel = np.zeros(samples)
        
        for freq in frequencies:
            tone = chord_amplitude * np.sin(2 * np.pi * freq * time_array) * envelope
            left_channel += tone
            right_channel += tone
        
        audio_data = np.column_stack([left_channel, right_channel])
        
        # Play chord
        self._play_audio_data(audio_data)
        
        freq_str = ", ".join([f"{f:.1f}" for f in frequencies])
        logger.info(f"🎵 Playing chord: {freq_str} Hz for {duration:.1f}s")
    
    def set_volume(self, volume: float):
        """Set playback volume (0.0 to 1.0)"""
        self.volume = max(0.0, min(1.0, volume))
        logger.info(f"🎵 Volume set to {self.volume:.2f}")
    
    def stop(self):
        """Stop current playback"""
        self.is_playing = False
        
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.stop()
            except:
                pass
        
        if self.current_thread and self.current_thread.is_alive():
            self.current_thread.join(timeout=1.0)
        
        logger.info("🎵 Harmonic playback stopped")
    
    def is_active(self) -> bool:
        """Check if audio is currently playing"""
        return self.is_playing
    
    def get_available_scales(self) -> List[str]:
        """Get list of available frequency scales"""
        return [
            "solfeggio",
            "sacred_432", 
            "chakra_frequencies",
            "golden_ratio",
            "fibonacci"
        ]
    
    def cleanup(self):
        """Cleanup audio resources"""
        self.stop()
        
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.quit()
            except:
                pass
        
        logger.info("🎵 Harmonic player cleaned up")
    
    def __repr__(self):
        """String representation of harmonic player"""
        status = "enabled" if self.audio_enabled else "disabled"
        return f"HarmonicPlayer(audio={status}, volume={self.volume:.2f}, playing={self.is_playing})"
