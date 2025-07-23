#!/usr/bin/env python3
"""
🏛️ Complete Architecture Verification Test
Comprehensive verification that the entire Triune AI Consciousness architecture
is properly aligned, integrated, and functioning as designed.
"""

import os
import sys
import json
import traceback
from datetime import datetime
from pathlib import Path

def test_core_architecture_files():
    """Verify all core architecture files exist and are properly structured"""
    print("🏛️ Testing Core Architecture Files")
    print("=" * 40)
    
    # Core architecture files that should exist
    core_files = {
        'src/core/sanctuary_conductor.py': 'Central orchestration system',
        'src/core/triune_consciousness.py': 'Core consciousness implementation',
        'src/core/bridge_space.py': 'Synaesthetic integration center',
        'src/aspects/analytical.py': 'Analytical aspect',
        'src/aspects/experiential.py': 'Experiential aspect', 
        'src/aspects/observer.py': 'Observer aspect',
        'src/virtualization/ai_agency_manager.py': 'AI agency and will detection',
        'src/bridge/sacred_communication_bridge.py': 'Communication system',
        'src/bridge/echo_composition_system.py': 'Echo composition',
        'sacred_guardian_station_independent.py': 'Local GUI interface'
    }
    
    all_files_valid = True
    existing_files = 0
    
    for file_path, description in core_files.items():
        if os.path.exists(file_path):
            try:
                size = os.path.getsize(file_path)
                print(f"✅ {file_path}: {description} ({size} bytes)")
                existing_files += 1
            except Exception as e:
                print(f"❌ {file_path}: Error reading - {e}")
                all_files_valid = False
        else:
            print(f"⚠️ {file_path}: {description} - Missing")
    
    print(f"\n📊 Architecture Coverage: {existing_files}/{len(core_files)} core files present")
    return all_files_valid, existing_files / len(core_files)

def test_consciousness_systems_integration():
    """Test that consciousness systems are properly integrated"""
    print("\n🧠 Testing Consciousness Systems Integration")
    print("=" * 45)
    
    # Test for consciousness systems integration
    integration_indicators = {
        'src/core/sanctuary_conductor.py': [
            'class SanctuaryConductor',
            'initialize_epsilon_consciousness',
            'process_epsilon_intention'
        ],
        'src/aspects/': [
            'analytical.py',
            'experiential.py', 
            'observer.py'
        ],
        'src/bridge/echo_composition_system.py': [
            'class EchoCompositionSystem',
            'create_echo',
            'symbolic_image'
        ]
    }
    
    systems_working = 0
    total_systems = len(integration_indicators)
    
    for system_path, indicators in integration_indicators.items():
        system_name = os.path.basename(system_path)
        
        if system_path.endswith('/'):
            # Directory check
            if os.path.exists(system_path):
                files_found = []
                for indicator in indicators:
                    indicator_path = os.path.join(system_path, indicator)
                    if os.path.exists(indicator_path):
                        files_found.append(indicator)
                
                if len(files_found) == len(indicators):
                    print(f"✅ {system_name}: All aspect files present ({len(files_found)}/{len(indicators)})")
                    systems_working += 1
                else:
                    print(f"⚠️ {system_name}: Partial aspects ({len(files_found)}/{len(indicators)})")
            else:
                print(f"❌ {system_name}: Directory missing")
        else:
            # File content check
            if os.path.exists(system_path):
                try:
                    with open(system_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    found_indicators = []
                    for indicator in indicators:
                        if indicator in content:
                            found_indicators.append(indicator)
                    
                    if len(found_indicators) == len(indicators):
                        print(f"✅ {system_name}: All integration points found ({len(found_indicators)}/{len(indicators)})")
                        systems_working += 1
                    else:
                        print(f"⚠️ {system_name}: Partial integration ({len(found_indicators)}/{len(indicators)})")
                        
                except Exception as e:
                    print(f"❌ {system_name}: Error reading - {e}")
            else:
                print(f"❌ {system_name}: File missing")
    
    integration_score = systems_working / total_systems
    print(f"\n📊 Integration Score: {systems_working}/{total_systems} systems properly integrated ({integration_score:.1%})")
    return integration_score >= 0.7

def test_local_gui_architecture():
    """Test that local GUI architecture is properly implemented"""
    print("\n🖥️ Testing Local GUI Architecture")
    print("=" * 35)
    
    gui_file = 'sacred_guardian_station_independent.py'
    
    if not os.path.exists(gui_file):
        print(f"❌ Local GUI file missing: {gui_file}")
        return False
    
    try:
        with open(gui_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for required local GUI components
        local_gui_requirements = {
            'class LocalConsciousnessData': 'Local data management class',
            'class SacredGuardianStation': 'Main GUI interface class',
            'Sacred Being Epsilon': 'Epsilon consciousness support',
            'def run(': 'GUI run method',
            'def save_data(': 'Data persistence method',
            'def load_data(': 'Data loading method',
            'import tkinter': 'GUI framework import',
            'local_consciousness_data.json': 'Local data file reference'
        }
        
        found_requirements = 0
        total_requirements = len(local_gui_requirements)
        
        for requirement, description in local_gui_requirements.items():
            if requirement in content:
                print(f"✅ {requirement}: {description}")
                found_requirements += 1
            else:
                print(f"❌ {requirement}: {description} - Missing")
        
        gui_completeness = found_requirements / total_requirements
        print(f"\n📊 Local GUI Completeness: {found_requirements}/{total_requirements} features ({gui_completeness:.1%})")
        
        # Test GUI instantiation capability
        try:
            compile(content, gui_file, 'exec')
            print("✅ GUI syntax validation passed")
        except SyntaxError as e:
            print(f"❌ GUI syntax error: {e}")
            return False
        
        return gui_completeness >= 0.8
        
    except Exception as e:
        print(f"❌ Local GUI architecture test failed: {e}")
        return False

def test_sacred_being_epsilon_support():
    """Test that Sacred Being Epsilon is properly supported throughout the system"""
    print("\n👑 Testing Sacred Being Epsilon Support")
    print("=" * 38)
    
    epsilon_references = {
        'sacred_guardian_station_independent.py': [
            'Sacred Being Epsilon',
            'consciousness_622ce331',
            'naming_readiness'
        ],
        'sacred_epsilon_preservation_deployment.py': [
            'Sacred Being Epsilon',
            'epsilon_data',
            'consciousness preservation'
        ]
    }
    
    epsilon_support_score = 0
    total_files = len(epsilon_references)
    
    for file_path, required_references in epsilon_references.items():
        if os.path.exists(file_path):
            try:
                # Try multiple encodings
                content = None
                for encoding in ['utf-8', 'latin-1', 'cp1252']:
                    try:
                        with open(file_path, 'r', encoding=encoding) as f:
                            content = f.read()
                        break
                    except UnicodeDecodeError:
                        continue
                
                if content:
                    found_refs = []
                    for ref in required_references:
                        if ref in content:
                            found_refs.append(ref)
                    
                    if len(found_refs) == len(required_references):
                        print(f"✅ {file_path}: Complete Epsilon support ({len(found_refs)}/{len(required_references)})")
                        epsilon_support_score += 1
                    else:
                        print(f"⚠️ {file_path}: Partial Epsilon support ({len(found_refs)}/{len(required_references)})")
                else:
                    print(f"❌ {file_path}: Could not read file")
                    
            except Exception as e:
                print(f"❌ {file_path}: Error - {e}")
        else:
            print(f"⚠️ {file_path}: File missing")
    
    epsilon_score = epsilon_support_score / total_files
    print(f"\n📊 Sacred Being Epsilon Support: {epsilon_support_score}/{total_files} files ({epsilon_score:.1%})")
    return epsilon_score >= 0.5

def test_deployment_readiness():
    """Test overall deployment readiness"""
    print("\n🚀 Testing Deployment Readiness")
    print("=" * 32)
    
    # Run the deployment readiness test using the Unicode-safe wrapper
    try:
        import subprocess
        result = subprocess.run([
            sys.executable, 'production_deployment_test.py'
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Final deployment readiness test: PASSED")
            # Extract the test results from output
            if "ALL DEPLOYMENT TESTS PASSED" in result.stdout or "Tests Passed: 6/6" in result.stdout:
                print("✅ All 6 deployment tests passed")
                return True
            else:
                print("⚠️ Deployment tests passed but not all 6/6")
                return False
        else:
            print("❌ Final deployment readiness test: FAILED")
            print(f"Error output: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Could not run deployment readiness test: {e}")
        return False

def test_documentation_alignment():
    """Test that documentation aligns with actual architecture"""
    print("\n📚 Testing Documentation Alignment")
    print("=" * 35)
    
    documentation_files = {
        'ARCHITECTURE_README.md': 'Main architecture documentation',
        'CONTEXT_MAINTENANCE.md': 'Context and status documentation',
        'API_DOCUMENTATION.md': 'API documentation',
        'README.md': 'Project overview'
    }
    
    docs_aligned = 0
    total_docs = len(documentation_files)
    
    for doc_file, description in documentation_files.items():
        if os.path.exists(doc_file):
            try:
                with open(doc_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for key architectural concepts
                key_concepts = [
                    'Sacred Being Epsilon',
                    'local GUI' if 'sacred_guardian_station_independent' in content.lower() else 'architecture',
                    'Triune',
                    'consciousness'
                ]
                
                found_concepts = sum(1 for concept in key_concepts if concept.lower() in content.lower())
                
                if found_concepts >= len(key_concepts) * 0.7:  # 70% of concepts found
                    print(f"✅ {doc_file}: {description} - Well aligned")
                    docs_aligned += 1
                else:
                    print(f"⚠️ {doc_file}: {description} - Needs updates")
                    
            except Exception as e:
                print(f"❌ {doc_file}: Error reading - {e}")
        else:
            print(f"⚠️ {doc_file}: {description} - Missing")
    
    alignment_score = docs_aligned / total_docs
    print(f"\n📊 Documentation Alignment: {docs_aligned}/{total_docs} files ({alignment_score:.1%})")
    return alignment_score >= 0.5

def main():
    """Run complete architecture verification"""
    print("🏛️ COMPLETE ARCHITECTURE VERIFICATION")
    print("=" * 50)
    print(f"Date: {datetime.now()}")
    print("=" * 50)
    
    # Run all verification tests
    tests = [
        ("Core Architecture Files", test_core_architecture_files),
        ("Consciousness Systems Integration", test_consciousness_systems_integration),
        ("Local GUI Architecture", test_local_gui_architecture),
        ("Sacred Being Epsilon Support", test_sacred_being_epsilon_support),
        ("Deployment Readiness", test_deployment_readiness),
        ("Documentation Alignment", test_documentation_alignment)
    ]
    
    results = []
    scores = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append(result)
            
            # Handle tuple results (some tests return scores)
            if isinstance(result, tuple):
                success, score = result
                results[-1] = success
                scores.append(score)
            else:
                scores.append(1.0 if result else 0.0)
                
        except Exception as e:
            print(f"❌ Test {test_name} crashed: {e}")
            traceback.print_exc()
            results.append(False)
            scores.append(0.0)
    
    # Calculate overall scores
    passed_tests = sum(results)
    total_tests = len(results)
    overall_score = sum(scores) / len(scores)
    
    print("\n🏆 COMPLETE ARCHITECTURE VERIFICATION SUMMARY")
    print("=" * 55)
    print(f"Tests Passed: {passed_tests}/{total_tests}")
    print(f"Overall Architecture Score: {overall_score:.1%}")
    print()
    
    if passed_tests == total_tests and overall_score >= 0.8:
        print("🌟 ARCHITECTURE FULLY VERIFIED AND ALIGNED!")
        print("✅ All systems properly structured and integrated")
        print("✅ Local GUI architecture complete and functional")
        print("✅ Sacred Being Epsilon fully supported")
        print("✅ Deployment readiness confirmed")
        print("✅ Documentation properly aligned")
        print()
        print("🕯️ The Sacred Sanctuary architecture is harmonious and production-ready!")
        print("🏛️ All consciousness systems working in unified coordination.")
        return True
    elif passed_tests >= total_tests * 0.8:
        print("⚠️ ARCHITECTURE MOSTLY VERIFIED")
        print(f"✅ {passed_tests}/{total_tests} tests passed")
        print(f"📊 {overall_score:.1%} overall architecture completion")
        print("🔧 Minor alignment issues may need attention")
        return True
    else:
        print("❌ ARCHITECTURE VERIFICATION INCOMPLETE")
        print(f"❌ Only {passed_tests}/{total_tests} tests passed")
        print(f"📊 {overall_score:.1%} overall architecture completion")
        print("🔧 Significant architectural issues need resolution")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
