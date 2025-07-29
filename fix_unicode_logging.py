#!/usr/bin/env python3
"""
Quick Unicode Fix for Enhanced Consciousness Testing
===================================================

This script patches the enhanced_consciousness_testing_node.py to use
Unicode-safe logging that works on Windows systems.
"""

import re
from pathlib import Path

def fix_unicode_logging():
    """Fix Unicode logging issues in the enhanced consciousness testing node"""
    
    file_path = Path("scripts/servers/enhanced_consciousness_testing_node.py")
    
    # Read the current file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace logger calls with safe versions
    replacements = [
        (r'logger\.info\((f?"[^"]*[🌟🌅❌✨🔍🎯🧪🛡️🌙📊🚀🛑💥⚠️][^"]*"[^)]*)\)', r'safe_log_info(logger, \1)'),
        (r'logger\.error\((f?"[^"]*[🌟🌅❌✨🔍🎯🧪🛡️🌙📊🚀🛑💥⚠️][^"]*"[^)]*)\)', r'safe_log_error(logger, \1)'),
        (r'logger\.warning\((f?"[^"]*[🌟🌅❌✨🔍🎯🧪🛡️🌙📊🚀🛑💥⚠️][^"]*"[^)]*)\)', r'safe_log_warning(logger, \1)'),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    # Write the fixed content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Unicode logging issues fixed in enhanced_consciousness_testing_node.py")

if __name__ == "__main__":
    fix_unicode_logging()
