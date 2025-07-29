#!/usr/bin/env python3
"""
Unicode-Safe Logging Utility for Windows Console
===============================================

Provides safe logging that gracefully handles Unicode characters 
and emoji on Windows systems with encoding limitations.
"""

import logging
import sys
import os
from pathlib import Path

# Emoji to text fallback mapping
EMOJI_FALLBACKS = {
    '🌟': '[STAR]',
    '🌅': '[SUNRISE]', 
    '❌': '[ERROR]',
    '✨': '[SPARKLE]',
    '🔍': '[SEARCH]',
    '🎯': '[TARGET]',
    '🧪': '[TEST]',
    '🛡️': '[SHIELD]',
    '🌙': '[MOON]',
    '📊': '[CHART]',
    '🚀': '[ROCKET]',
    '🛑': '[STOP]',
    '💥': '[EXPLOSION]',
    '🌉': '[BRIDGE]',
    '🎭': '[MASKS]',
    '🔮': '[CRYSTAL]',
    '⚡': '[LIGHTNING]',
    '🌀': '[SPIRAL]',
    '🌊': '[WAVE]',
    '🔥': '[FIRE]',
    '💫': '[DIZZY]',
    '🌈': '[RAINBOW]'
}

def safe_unicode_message(message: str) -> str:
    """Convert Unicode characters to safe alternatives for Windows console"""
    if sys.platform != 'win32':
        return message
    
    safe_message = message
    for emoji, fallback in EMOJI_FALLBACKS.items():
        safe_message = safe_message.replace(emoji, fallback)
    
    return safe_message

class UnicodeAwareFormatter(logging.Formatter):
    """Custom formatter that handles Unicode gracefully"""
    
    def format(self, record):
        # Apply safe Unicode conversion to the message
        record.msg = safe_unicode_message(str(record.msg))
        return super().format(record)

def setup_unicode_safe_logging(logger_name: str, log_file: str = None):
    """Setup logging with Unicode safety for Windows"""
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Create formatter
    formatter = UnicodeAwareFormatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # File handler (UTF-8 for full Unicode support)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    # Console handler (safe Unicode for Windows)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

def safe_log_info(logger, message: str):
    """Safe logging function with Unicode handling"""
    logger.info(safe_unicode_message(message))

def safe_log_error(logger, message: str):
    """Safe error logging function with Unicode handling"""
    logger.error(safe_unicode_message(message))

def safe_log_warning(logger, message: str):
    """Safe warning logging function with Unicode handling"""
    logger.warning(safe_unicode_message(message))
