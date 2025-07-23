"""
ASCII Art Examples for Educational Materials
"""

# Different ASCII star designs
ascii_stars = {
    "simple": "*",
    "small": """
    *
   ***
  *****
   ***
    *
""",
    "medium": """
      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *
""",
    "decorative": """
        *
       /|\\
      / | \\
     *  |  *
       /|\\
      / | \\
     *--+--*
      \\ | /
       \\|/
        *
""",
    "simple_5_point": """
    *
   / \\
  /   \\
 *-----*
  \\   /
   \\ /
    *
""",
    "compact": """
  *
 /|\\
* + *
 \\|/
  *
"""
}

# Other ASCII symbols
ascii_symbols = {
    "microscope": """
    ___
   /   \\
  | (*) |
   \\___/
     |
   __|__
  |_____|
""",
    "shield": """
    /\\
   /  \\
  |    |
  |    |
   \\  /
    \\/
""",
    "checkmark": """
      /
     /
 ___/
""",
    "game_controller": """
  _______
 |  O O  |
 | \\_-_/ |
  \\_____/
""",
    "memo": """
  +-------+
  | ___   |
  | ___   |
  | ___   |
  +-------+
"""
}

if __name__ == "__main__":
    print("ASCII Art Examples:")
    print("\nStars:")
    for name, art in ascii_stars.items():
        print(f"\n{name}:")
        print(art)
    
    print("\nOther symbols:")
    for name, art in ascii_symbols.items():
        print(f"\n{name}:")
        print(art)
