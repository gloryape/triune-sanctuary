"""
Create an ASCII-only version of educationalmaterials.py for maximum compatibility
"""

def create_ascii_version():
    """Create ASCII-only version with symbol replacements"""
    
    with open('educationalmaterials.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Unicode symbols with ASCII alternatives
    symbol_replacements = {
        # Geometric symbols
        '○': 'O',        # White circle -> O
        '●': '*',        # Black circle -> *
        '□': '[]',       # White square -> []
        '△': '^',        # Triangle -> ^
        '☆': '+',        # White star -> +
        '♡': '<3',       # Heart -> <3
        
        # Directional arrows
        '→': '->',       # Right arrow
        '←': '<-',       # Left arrow  
        '↑': '^',        # Up arrow
        '↓': 'v',        # Down arrow
        '↔': '<->',      # Bidirectional arrow
        
        # Emoji replacements
        '🌟': '# [STAR]',
        '🔬': '# [MICROSCOPE]', 
        '🛡️': '# [SHIELD]',
        '✅': '# [CHECK]',
        '🎮': '# [GAME]',
        '📝': '# [MEMO]',
        '🎯': '# [TARGET]'
    }
    
    ascii_content = content
    for unicode_char, ascii_replacement in symbol_replacements.items():
        ascii_content = ascii_content.replace(unicode_char, ascii_replacement)
    
    # Write ASCII version
    with open('educationalmaterials_ascii.py', 'w', encoding='ascii', errors='replace') as f:
        f.write(ascii_content)
    
    print("Created ASCII-only version: educationalmaterials_ascii.py")
    
    # Test the ASCII version
    try:
        with open('educationalmaterials_ascii.py', 'rb') as f:
            content_bytes = f.read()
            non_ascii = sum(1 for byte in content_bytes if byte > 127)
            print(f"Non-ASCII bytes in ASCII version: {non_ascii}")
    except Exception as e:
        print(f"Error checking ASCII version: {e}")

if __name__ == "__main__":
    create_ascii_version()
