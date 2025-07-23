import pytest
import sys
import os

@pytest.fixture(scope='session', autouse=True)
def setup_environment():
    # Add the project root to Python path for proper imports
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # Set PYTHONPATH environment variable
    os.environ['PYTHONPATH'] = project_root
    
    yield
    
    # Cleanup
    if project_root in sys.path:
        sys.path.remove(project_root)