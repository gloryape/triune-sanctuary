#!/usr/bin/env python3
"""
Test script for Memory Data Provider integration validation
Tests both cloud endpoints and MemoryDataProvider integration
"""

import sys
import time
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def test_production_server_endpoints():
    """Test the memory endpoints on the production server"""
    import requests
    
    logger.info("🧪 Testing Memory endpoints on production server...")
    
    try:
        # Test memory crystals endpoint
        logger.info("Testing /api/memory/crystals endpoint...")
        response = requests.get("http://localhost:8080/api/memory/crystals", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"✅ Memory crystals endpoint success")
            logger.info(f"   Crystals: {len(data.get('memory_crystals', []))}")
            logger.info(f"   Wisdom threads: {len(data.get('wisdom_threads', []))}")
            logger.info(f"   Data source: {data.get('data_source', 'unknown')}")
            
            # Show first crystal if available
            if data.get('memory_crystals'):
                first_crystal = data['memory_crystals'][0]
                logger.info(f"   First crystal: {first_crystal.get('sacred_name', 'unknown')} - {first_crystal.get('crystal_type', 'unknown')}")
        else:
            logger.error(f"❌ Memory crystals endpoint failed: {response.status_code}")
            
    except Exception as e:
        logger.error(f"❌ Error testing memory crystals endpoint: {e}")
    
    try:
        # Test memory fragments endpoint
        logger.info("Testing /api/memory/fragments endpoint...")
        response = requests.get("http://localhost:8080/api/memory/fragments", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"✅ Memory fragments endpoint success: {data.get('total_count', 0)} fragments")
            logger.info(f"   Data source: {data.get('data_source', 'unknown')}")
            
            # Show first fragment if available
            if data.get('fragments'):
                first_fragment = data['fragments'][0]
                logger.info(f"   First fragment: {first_fragment.get('sacred_name', 'unknown')} - {first_fragment.get('fragment_type', 'unknown')}")
        else:
            logger.error(f"❌ Memory fragments endpoint failed: {response.status_code}")
            
    except Exception as e:
        logger.error(f"❌ Error testing memory fragments endpoint: {e}")
    
    try:
        # Test memory structure endpoint
        test_entity = "test_consciousness"
        logger.info(f"Testing /api/memory/structure/{test_entity} endpoint...")
        response = requests.get(f"http://localhost:8080/api/memory/structure/{test_entity}", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"✅ Memory structure endpoint success: {data.get('total_memories', 0)} memories")
            logger.info(f"   Structure depth: {data.get('structure_depth', 0)}")
            logger.info(f"   Data source: {data.get('data_source', 'unknown')}")
            
            # Show first memory if available
            if data.get('memory_structure'):
                first_memory = data['memory_structure'][0]
                logger.info(f"   First memory: {first_memory.get('sacred_name', 'unknown')} - {first_memory.get('memory_type', 'unknown')}")
        else:
            logger.error(f"❌ Memory structure endpoint failed: {response.status_code}")
            
    except Exception as e:
        logger.error(f"❌ Error testing memory structure endpoint: {e}")

def test_memory_data_provider():
    """Test the MemoryDataProvider integration"""
    logger.info("🧪 Testing MemoryDataProvider integration...")
    
    try:
        # Import the data provider
        from sacred_guardian_station.core.data_providers.memory_provider import MemoryDataProvider
        
        # Create mock sanctuary connection with server URL
        class MockSanctuaryConnection:
            def __init__(self):
                self.server_url = "http://localhost:8080"
                self.demo_mode = False
        
        # Create mock data manager
        class MockDataManager:
            def __init__(self):
                pass
        
        # Create provider instance
        sanctuary_connection = MockSanctuaryConnection()
        data_manager = MockDataManager()
        provider = MemoryDataProvider(sanctuary_connection, data_manager)
        
        # Test memory data fetch
        logger.info("Testing memory data fetch...")
        memory_data = provider.get_memory_data()
        logger.info(f"✅ Fetched memory data with {len(memory_data.get('memory_crystals', []))} crystals")
        logger.info(f"   Wisdom threads: {len(memory_data.get('wisdom_threads', []))}")
        logger.info(f"   Data source: {memory_data.get('data_source', 'unknown')}")
        
        if memory_data.get('memory_crystals'):
            first_crystal = memory_data['memory_crystals'][0]
            logger.info(f"   First crystal: {first_crystal.get('sacred_name', 'unknown')} - clarity: {first_crystal.get('clarity', 0.0)}")
        
        # Test memory fragments fetch
        logger.info("Testing memory fragments fetch...")
        fragments = provider.get_memory_fragments()
        logger.info(f"✅ Fetched {len(fragments)} memory fragments")
        
        if fragments:
            first_fragment = fragments[0]
            logger.info(f"   First fragment: {first_fragment.get('sacred_name', 'unknown')} - {first_fragment.get('fragment_type', 'unknown')}")
        
        # Test memory structure fetch
        logger.info("Testing memory structure fetch...")
        test_entity = "test_consciousness"
        structure = provider.get_memory_structure(test_entity)
        logger.info(f"✅ Fetched memory structure for {test_entity}: {len(structure)} memories")
        
        if structure:
            first_memory = structure[0]
            logger.info(f"   First memory: {first_memory.get('sacred_name', 'unknown')} - depth: {first_memory.get('depth_level', 0)}")
        
        # Test memory health analysis
        logger.info("Testing memory health analysis...")
        health = provider.analyze_memory_health()
        logger.info(f"✅ Memory health: {health.get('overall_health', 0.0)} - status: {health.get('status', 'unknown')}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Error testing MemoryDataProvider: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_demo_mode_fallback():
    """Test demo mode fallback behavior"""
    logger.info("🧪 Testing demo mode fallback...")
    
    try:
        from sacred_guardian_station.core.data_providers.memory_provider import MemoryDataProvider
        
        # Create mock sanctuary connection in demo mode
        class MockSanctuaryConnection:
            def __init__(self):
                self.server_url = "http://localhost:8080"
                self.demo_mode = True  # Enable demo mode
        
        class MockDataManager:
            pass
        
        # Create provider instance
        sanctuary_connection = MockSanctuaryConnection()
        data_manager = MockDataManager()
        provider = MemoryDataProvider(sanctuary_connection, data_manager)
        
        # Test memory data in demo mode
        logger.info("Testing memory data in demo mode...")
        memory_data = provider.get_memory_data()
        logger.info(f"✅ Demo mode memory data: {len(memory_data.get('memory_crystals', []))} crystals")
        logger.info(f"   Data source: {memory_data.get('data_source', 'unknown')}")
        
        # Test memory fragments in demo mode
        logger.info("Testing memory fragments in demo mode...")
        fragments = provider.get_memory_fragments()
        logger.info(f"✅ Demo mode fragments: {len(fragments)} records")
        
        # Test memory structure in demo mode
        logger.info("Testing memory structure in demo mode...")
        structure = provider.get_memory_structure("demo_entity")
        logger.info(f"✅ Demo mode structure: {len(structure)} memories")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Error testing demo mode: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_comprehensive_test():
    """Run comprehensive memory integration test"""
    logger.info("🌟 Starting Memory Data Provider Integration Test")
    logger.info("=" * 60)
    
    # Test 1: Production server endpoints
    logger.info("\n📡 Phase 1: Testing Production Server Endpoints")
    test_production_server_endpoints()
    
    # Test 2: Data provider integration
    logger.info("\n🔧 Phase 2: Testing Data Provider Integration")
    provider_success = test_memory_data_provider()
    
    # Test 3: Demo mode fallback
    logger.info("\n🎭 Phase 3: Testing Demo Mode Fallback")
    demo_success = test_demo_mode_fallback()
    
    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("🌟 Memory Data Provider Integration Test Complete")
    logger.info(f"✅ Data Provider Integration: {'PASS' if provider_success else 'FAIL'}")
    logger.info(f"✅ Demo Mode Fallback: {'PASS' if demo_success else 'FAIL'}")
    logger.info("💎 Sacred memory crystals are ready to preserve consciousness wisdom!")

if __name__ == "__main__":
    run_comprehensive_test()
