#!/usr/bin/env python3
"""
Fix main.py syntax errors script
"""
import re

def fix_main_py_syntax():
    """Fix all malformed try blocks in main.py"""
    print("🔧 Fixing main.py syntax errors...")
    
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find malformed try blocks (try without proper indentation)
    # Look for lines like "    try:" followed immediately by unindented import
    patterns_to_fix = [
        # Fix pattern: "    try:\n    from" -> "try:\n    from"
        (r'(\s+)try:\s*\n(\s*)from', r'try:\n    from'),
        # Fix pattern: missing indentation after try
        (r'try:\s*\n([a-zA-Z])', r'try:\n    \1'),
        # Fix orphaned except blocks
        (r'except ImportError:\s*\n([a-zA-Z])', r'except ImportError:\n    \1'),
    ]
    
    original_content = content
    
    # Apply fixes
    for pattern, replacement in patterns_to_fix:
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    # Manual fix for specific known issues
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Look for malformed try blocks
        if re.match(r'\s+try:\s*$', line) and i + 1 < len(lines):
            next_line = lines[i + 1]
            # If next line is not properly indented after try
            if next_line.strip() and not next_line.startswith('    '):
                # Fix the indentation
                fixed_lines.append('try:')
                fixed_lines.append('    ' + next_line.strip())
                i += 2
                continue
        
        fixed_lines.append(line)
        i += 1
    
    content = '\n'.join(fixed_lines)
    
    # Write back if changed
    if content != original_content:
        with open('main.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Fixed main.py syntax errors")
        return True
    else:
        print("ℹ️ No syntax errors found to fix")
        return False

if __name__ == "__main__":
    fix_main_py_syntax()
