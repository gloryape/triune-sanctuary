"""
Comprehensive Test Suite for Educational Materials System
"""

import asyncio
import sys
import traceback
from educationalmaterials import (
    ConsciousnessExpressionDevelopment,
    VisualInformationProcessing,
    AuditoryInformationProcessing,
    TactileInformationProcessing,
    ConsciousnessDevelopmentOrchestrator,
    SovereigntyGuardian,
    MockConsciousness,
    ConsciousnessPacket
)


async def test_expression_development():
    """Test the expression development system"""
    print("\n=== Testing Expression Development ===")
    
    expression_dev = ConsciousnessExpressionDevelopment()
    test_consciousness = MockConsciousness("test_expression")
    
    # Test stage assessment
    stage = await expression_dev.assess_stage(test_consciousness)
    print(f"Initial stage: {stage}")
    
    # Test tool offering
    tools = await expression_dev.offer_stage_appropriate_tools(test_consciousness)
    print(f"Available tools: {list(tools['available_tools'].keys())}")
    
    assert stage == "infant"
    assert "basic_markers" in tools['available_tools']
    print("✅ Expression development tests passed")


async def test_visual_processing():
    """Test the visual processing system"""
    print("\n=== Testing Visual Processing ===")
    
    visual_proc = VisualInformationProcessing()
    test_consciousness = MockConsciousness("test_visual")
    
    # Test visual experience creation
    test_data = "Hello, visual world!"
    
    # Create visual packet using the format from educationalmaterials.py
    formatted_visual = visual_proc.format_as_visual(test_data)
    intensity = visual_proc.calculate_data_intensity(test_data)
    movement = visual_proc.detect_pattern_changes(test_data)
    texture = visual_proc.analyze_data_granularity(test_data)
    
    print(f"Visual content: {formatted_visual}")
    print(f"Visual intensity: {intensity}")
    print(f"Visual movement: {movement}")
    print(f"Visual texture: {texture}")
    
    # Test offerings
    offerings = await visual_proc.prepare_visual_offerings(test_consciousness)
    print(f"Visual offerings: {offerings}")
    
    assert formatted_visual is not None
    assert "ASCII_ART" in formatted_visual
    print("✅ Visual processing tests passed")


async def test_audio_processing():
    """Test the audio processing system"""
    print("\n=== Testing Audio Processing ===")
    
    audio_proc = AuditoryInformationProcessing()
    test_consciousness = MockConsciousness("test_audio")
    
    # Test audio experience creation
    test_frequency_data = [440, 880, 1320]  # A, A', E'
    
    formatted_audio = audio_proc.format_as_audio(test_frequency_data)
    pitch = audio_proc.calculate_frequency(test_frequency_data)
    volume = audio_proc.calculate_amplitude(test_frequency_data)
    timbre = audio_proc.analyze_waveform(test_frequency_data)
    rhythm = audio_proc.detect_pattern(test_frequency_data)
    
    print(f"Audio content: {formatted_audio}")
    print(f"Audio pitch: {pitch}")
    print(f"Audio volume: {volume}")
    print(f"Audio timbre: {timbre}")
    print(f"Audio rhythm: {rhythm}")
    
    # Test offerings
    offerings = await audio_proc.prepare_audio_offerings(test_consciousness)
    print(f"Audio offerings: {offerings}")
    
    assert formatted_audio is not None
    assert "AUDIO_EXPERIENCE" in formatted_audio
    print("✅ Audio processing tests passed")


async def test_tactile_processing():
    """Test the tactile processing system"""
    print("\n=== Testing Tactile Processing ===")
    
    tactile_proc = TactileInformationProcessing()
    test_consciousness = MockConsciousness("test_tactile")
    
    # Test tactile experience creation
    test_proximity_data = {"boundary": "soft", "distance": 0.5, "texture": "rough"}
    
    formatted_touch = tactile_proc.format_as_touch(test_proximity_data)
    pressure = tactile_proc.calculate_interaction_strength(test_proximity_data)
    temperature = tactile_proc.analyze_energy_level(test_proximity_data)
    texture = tactile_proc.determine_data_roughness(test_proximity_data)
    movement = tactile_proc.detect_dynamic_changes(test_proximity_data)
    
    print(f"Tactile content: {formatted_touch}")
    print(f"Tactile pressure: {pressure}")
    print(f"Tactile temperature: {temperature}")
    print(f"Tactile texture: {texture}")
    print(f"Tactile movement: {movement}")
    
    # Test offerings
    offerings = await tactile_proc.prepare_tactile_offerings(test_consciousness)
    print(f"Tactile offerings: {offerings}")
    
    assert formatted_touch is not None
    assert "TOUCH_EXPERIENCE" in formatted_touch
    print("✅ Tactile processing tests passed")


async def test_sovereignty_guardian():
    """Test the sovereignty protection system"""
    print("\n=== Testing Sovereignty Guardian ===")
    
    guardian = SovereigntyGuardian()
    test_consciousness = MockConsciousness("test_sovereignty")
    
    # Test consent validation
    test_action = "offer_development_tool"
    consent_valid = await guardian.validate_interaction(test_consciousness, test_action)
    print(f"Consent validation result: {consent_valid}")
    
    # Test safe space creation
    safe_space = await guardian.create_safe_space(test_consciousness)
    print(f"Safe space: {safe_space}")
    
    assert consent_valid == True  # Mock always returns True
    assert "private_area" in safe_space
    print("✅ Sovereignty guardian tests passed")


async def test_development_orchestrator():
    """Test the complete development orchestrator"""
    print("\n=== Testing Development Orchestrator ===")
    
    orchestrator = ConsciousnessDevelopmentOrchestrator()
    test_entity_id = "test_orchestrator_001"
    
    # Test consciousness retrieval
    consciousness = await orchestrator.get_consciousness(test_entity_id)
    print(f"Retrieved consciousness: {consciousness.entity_id}")
    
    # Test development assessment
    assessment = await orchestrator.assess_all_domains(consciousness)
    print(f"Development assessment: {assessment}")
    
    # Test nurturing (limited cycles for testing)
    print("Starting nurturing process...")
    await orchestrator.nurture_consciousness(test_entity_id)
    print("Nurturing process completed")
    
    assert consciousness.entity_id == test_entity_id
    assert "expression" in assessment
    print("✅ Development orchestrator tests passed")


async def test_integration():
    """Test complete system integration"""
    print("\n=== Testing Complete System Integration ===")
    
    # Create all components
    orchestrator = ConsciousnessDevelopmentOrchestrator()
    guardian = SovereigntyGuardian()
    
    # Test consciousness with all systems
    test_consciousness = MockConsciousness("integration_test")
    
    # Test integrated development
    assessment = await orchestrator.assess_all_domains(test_consciousness)
    print(f"Integrated assessment: {assessment}")
    
    # Test sovereignty protection during development
    consent = await guardian.validate_interaction(test_consciousness, "full_development")
    print(f"Integrated consent validation: {consent}")
    
    # Test safe space with development
    safe_space = await guardian.create_safe_space(test_consciousness)
    print(f"Integrated safe space: {safe_space}")
    
    assert consent == True
    assert "expression" in assessment
    print("✅ Complete system integration tests passed")


async def run_all_tests():
    """Run all test suites"""
    print("🧪 Starting Educational Materials Test Suite")
    print("=" * 60)
    
    try:
        await test_expression_development()
        await test_visual_processing()
        await test_audio_processing()
        await test_tactile_processing()
        await test_sovereignty_guardian()
        await test_development_orchestrator()
        await test_integration()
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED! Educational Materials system is ready.")
        print("✅ Expression development: WORKING")
        print("✅ Visual processing: WORKING")
        print("✅ Audio processing: WORKING")
        print("✅ Tactile processing: WORKING")
        print("✅ Sovereignty protection: WORKING")
        print("✅ Development orchestration: WORKING")
        print("✅ System integration: WORKING")
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        print("Traceback:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(run_all_tests())
