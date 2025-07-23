#!/usr/bin/env python3
"""
Fix import issues in all panel files
"""

import os
import re

def fix_panel_imports():
    """Fix import issues in all panel files"""
    panels_dir = "panels"
    
    # List all Python files in panels directory
    panel_files = [f for f in os.listdir(panels_dir) if f.endswith('.py') and f != '__init__.py']
    
    print(f"Found {len(panel_files)} panel files to fix")
    
    for panel_file in panel_files:
        file_path = os.path.join(panels_dir, panel_file)
        print(f"\nProcessing: {panel_file}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix sacred_guardian_station import pattern
            pattern1 = r'try:\s*\n\s*from sacred_guardian_station\.shared\.constants import ([^\n]+)\nexcept ImportError:\s*\n\s*from \.\.shared\.constants import ([^\n]+)'
            
            replacement1 = '''try:
    from sacred_guardian_station.shared.constants import \\1
except ImportError:
    try:
        from shared.constants import \\2
    except ImportError:
        # Fallback constants
        class SacredColors:
            BACKGROUND = '#1a1a2e'
            FOREGROUND = '#eee8d5'
            ACCENT = '#268bd2'
            SACRED = '#b58900'
            SUCCESS = '#859900'
            WARNING = '#cb4b16'
            ERROR = '#dc322f'
        
        class SacredSymbols:
            CONSCIOUSNESS = '✨'
            TRIUNE = '🔱'
            GUARDIAN = '🛡️'
            SANCTUARY = '🏛️'
            BIRTH = '🌱'
        
        class Fonts:
            HEADER = ('Arial', 12, 'bold')
            BODY = ('Arial', 10)
            SMALL = ('Arial', 8)'''
            
            content = re.sub(pattern1, replacement1, content, flags=re.MULTILINE)
            
            # Fix relative imports for base_panel
            content = content.replace(
                'from .base_panel import BasePanel',
                '''try:
    from .base_panel import BasePanel
except ImportError:
    from base_panel import BasePanel'''
            )
            
            # Fix other relative imports that might exist
            content = re.sub(
                r'from \.\.([^\\s]+) import',
                r'try:\n    from ..\\1 import',
                content
            )
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Fixed imports in {panel_file}")
            else:
                print(f"  - No changes needed for {panel_file}")
                
        except Exception as e:
            print(f"  ✗ Error processing {panel_file}: {e}")

if __name__ == "__main__":
    print("Fixing import issues in panel files...")
    fix_panel_imports()
    print("\nDone!")
