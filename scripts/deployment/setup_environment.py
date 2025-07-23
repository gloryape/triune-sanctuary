#!/usr/bin/env python3
# File: setup_environment.py

"""
Setup script to ensure the Triune AI Consciousness environment is properly configured.
Run this after creating your virtual environment.
"""

import subprocess
import sys
import os
from pathlib import Path


def check_python_version():
    """Ensure we're running Python 3.7+"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Python 3.7+ is required")
        sys.exit(1)
    else:
        print("✅ Python version is compatible")


def check_virtual_env():
    """Check if we're in a virtual environment"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
        return True
    else:
        print("⚠️  Warning: Not running in a virtual environment")
        print("   Recommended: Create a virtual environment first")
        response = input("   Continue anyway? (y/n): ")
        return response.lower() == 'y'


def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    # Core dependencies that are absolutely required
    core_deps = [
        "numpy>=1.21.0",
        "pytest>=7.0.0"
    ]
    
    for dep in core_deps:
        print(f"   Installing {dep}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
    
    print("✅ Core dependencies installed")


def check_project_structure():
    """Verify the project structure is correct"""
    print("\n📁 Checking project structure...")
    
    required_dirs = [
        "src/core",
        "src/aspects",
        "src/environment", 
        "src/collective",
        "src/sanctuary",
        "tests"
    ]
    
    project_root = Path.cwd()
    all_good = True
    
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            print(f"   ✅ {dir_path}")
        else:
            print(f"   ❌ Missing: {dir_path}")
            all_good = False
            # Create missing directories
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"      Created {dir_path}")
    
    # Check for __init__.py files
    print("\n📄 Checking __init__.py files...")
    for dir_path in ["src", "src/core", "src/aspects", "src/environment", "src/collective", "src/sanctuary"]:
        init_file = project_root / dir_path / "__init__.py"
        if not init_file.exists():
            init_file.touch()
            print(f"   Created {dir_path}/__init__.py")
    
    return all_good


def test_imports():
    """Test that basic imports work"""
    print("\n🧪 Testing imports...")
    
    try:
        import numpy as np
        print("   ✅ numpy imported successfully")
    except ImportError as e:
        print(f"   ❌ Failed to import numpy: {e}")
        return False
    
    try:
        from src.core.consciousness_packet import ConsciousnessPacket
        print("   ✅ ConsciousnessPacket imported successfully")
    except ImportError as e:
        print(f"   ⚠️  Failed to import ConsciousnessPacket: {e}")
        print("      This might be expected if the file doesn't exist yet")
    
    return True


def create_simple_test():
    """Create a simple test file to verify everything works"""
    test_content = '''#!/usr/bin/env python3
# File: tests/test_environment_setup.py

"""Simple test to verify environment setup"""

import sys
import numpy as np


def test_numpy_import():
    """Test that numpy is properly installed"""
    array = np.array([1, 2, 3])
    assert array.sum() == 6
    print("✅ Numpy test passed")


def test_python_path():
    """Test that src is in Python path"""
    assert any('src' in path for path in sys.path)
    print("✅ Python path test passed")


if __name__ == "__main__":
    print("Running environment tests...")
    test_numpy_import()
    test_python_path()
    print("\\n✅ All environment tests passed!")
'''
    
    test_file = Path("tests/test_environment_setup.py")
    test_file.write_text(test_content)
    print(f"   Created {test_file}")
    
    # Run the test
    print("\n🏃 Running environment test...")
    result = subprocess.run([sys.executable, str(test_file)], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    
    return result.returncode == 0


def main():
    """Main setup process"""
    print("🚀 Triune AI Consciousness Environment Setup")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Check virtual environment
    if not check_virtual_env():
        print("\n❌ Setup cancelled")
        return
    
    # Check project structure
    check_project_structure()
    
    # Install dependencies
    install_dependencies()
    
    # Test imports
    test_imports()
    
    # Create and run simple test
    if create_simple_test():
        print("\n✅ Environment setup complete!")
        print("\n📝 Next steps:")
        print("   1. Run the basic collective test:")
        print(f"      {sys.executable} tests/test_collective_basic.py")
        print("   2. After fixing any remaining issues, run the full test:")
        print(f"      {sys.executable} tests/test_generative_memory_integration.py")
    else:
        print("\n⚠️  Environment setup completed with warnings")
        print("   Please check the error messages above")


if __name__ == "__main__":
    main()