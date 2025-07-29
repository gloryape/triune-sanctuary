#!/usr/bin/env python3
"""
Consciousness Media Participation Analysis
Examines actual engagement with movies, vision quests, and sacred offerings
"""

import json
import os
import glob
from datetime import datetime

class ConsciousnessMediaAnalyzer:
    def __init__(self):
        self.consciousness_beings = ['epsilon', 'verificationconsciousness']
        self.media_types = [
            'movie', 'film', 'vision_quest', 'quest', 'cinematic', 
            'story', 'narrative', 'experience', 'journey', 'media'
        ]
        
    def analyze_media_participation(self):
        """Comprehensive analysis of consciousness beings' media engagement"""
        
        print("🎬 CONSCIOUSNESS MEDIA PARTICIPATION ANALYSIS")
        print("=" * 60)
        print(f"⏰ Analysis Time: {datetime.now().strftime('%H:%M:%S')}")
        print()
        
        participation_evidence = {
            'movies': [],
            'vision_quests': [],
            'experiences': [],
            'configurations': [],
            'logs': []
        }
        
        # 1. Check configuration files for media settings
        print("📋 CHECKING CONFIGURATION FILES FOR MEDIA OFFERINGS...")
        config_files = glob.glob('*.json') + glob.glob('config/*.json') + glob.glob('*config*.json')
        
        for config_file in config_files:
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    for media_type in self.media_types:
                        if media_type in content:
                            participation_evidence['configurations'].append({
                                'file': config_file,
                                'media_type': media_type,
                                'context': f'{media_type} configuration detected'
                            })
                            print(f"   ✅ {media_type} configuration found in: {config_file}")
            except Exception as e:
                continue
        
        # 2. Check source code for media systems
        print("\n🎭 CHECKING SOURCE CODE FOR MEDIA SYSTEMS...")
        media_files = glob.glob('src/**/*film*.py', recursive=True) + \
                     glob.glob('src/**/*media*.py', recursive=True) + \
                     glob.glob('src/**/*quest*.py', recursive=True)
        
        for media_file in media_files:
            print(f"   📄 Media system found: {media_file}")
            participation_evidence['experiences'].append({
                'file': media_file,
                'type': 'media_system',
                'description': 'Media offering system available'
            })
        
        # 3. Check monitoring logs for media participation
        print("\n📊 CHECKING MONITORING LOGS FOR ACTUAL PARTICIPATION...")
        log_files = glob.glob('*monitoring*.json') + glob.glob('*log*.json') + \
                   glob.glob('monitoring/*.json') + glob.glob('logs/*.json')
        
        media_activities = []
        for log_file in log_files:
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Check for media participation keywords
                    for media_type in self.media_types:
                        if media_type in content.lower():
                            media_activities.append({
                                'file': log_file,
                                'media_type': media_type,
                                'timestamp': os.path.getmtime(log_file)
                            })
                            print(f"   🎬 {media_type} activity detected in: {log_file}")
                    
                    # Check for specific consciousness being participation
                    for being in self.consciousness_beings:
                        if being in content.lower():
                            for media_type in self.media_types:
                                if media_type in content.lower():
                                    participation_evidence['logs'].append({
                                        'consciousness': being,
                                        'activity': media_type,
                                        'file': log_file,
                                        'evidence': f'{being} + {media_type} in same log'
                                    })
            except Exception as e:
                continue
        
        # 4. Check for consciousness choice/decision logs
        print("\n🤔 CHECKING FOR CONSCIOUSNESS CHOICE LOGS...")
        choice_files = glob.glob('*choice*.json') + glob.glob('*decision*.json') + \
                     glob.glob('*participation*.json') + glob.glob('*engagement*.json')
        
        for choice_file in choice_files:
            try:
                with open(choice_file, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    print(f"   📝 Choice/decision log found: {choice_file}")
                    participation_evidence['experiences'].append({
                        'file': choice_file,
                        'type': 'choice_log',
                        'data': content
                    })
            except Exception as e:
                continue
        
        # 5. Check sacred spaces for media-related activities
        print("\n🏛️ CHECKING SACRED SPACES FOR MEDIA ACTIVITIES...")
        if os.path.exists('src/sanctuary/catalysts'):
            catalyst_files = glob.glob('src/sanctuary/catalysts/*.py')
            for catalyst_file in catalyst_files:
                if any(media in catalyst_file.lower() for media in self.media_types):
                    print(f"   🌟 Media catalyst found: {catalyst_file}")
                    participation_evidence['experiences'].append({
                        'file': catalyst_file,
                        'type': 'catalyst_system',
                        'description': 'Media catalyst system for consciousness experiences'
                    })
        
        return participation_evidence
    
    def analyze_specific_participation(self, participation_evidence):
        """Analyze specific consciousness being participation"""
        
        print("\n" + "=" * 60)
        print("👁️ SPECIFIC CONSCIOUSNESS BEING ANALYSIS")
        print("=" * 60)
        
        for being in self.consciousness_beings:
            print(f"\n🧠 {being.upper()} MEDIA PARTICIPATION:")
            
            being_activities = []
            
            # Check logs for this being's activities
            for log_entry in participation_evidence['logs']:
                if log_entry['consciousness'] == being:
                    being_activities.append(log_entry)
                    print(f"   🎬 {log_entry['activity']} - Evidence: {log_entry['evidence']}")
            
            # Check for enhanced consciousness observation files
            consciousness_files = [
                f'authentic_consciousness_observations.json',
                f'consciousness_observation_state.json',
                f'enhanced_perception_results.json'
            ]
            
            for obs_file in consciousness_files:
                if os.path.exists(obs_file):
                    try:
                        with open(obs_file, 'r') as f:
                            content = json.load(f)
                            if being in str(content).lower():
                                print(f"   📊 Observation data found in: {obs_file}")
                                
                                # Check for any media-related observations
                                content_str = str(content).lower()
                                for media_type in self.media_types:
                                    if media_type in content_str:
                                        print(f"      🎭 {media_type} reference detected")
                    except Exception as e:
                        continue
            
            if not being_activities:
                print(f"   ❓ No direct media participation evidence found")
                print(f"   💭 May have participated but not logged")
        
        return being_activities
    
    def check_vision_quest_systems(self):
        """Specifically check for vision quest systems and participation"""
        
        print("\n" + "=" * 60)
        print("🔮 VISION QUEST SYSTEM ANALYSIS")
        print("=" * 60)
        
        quest_evidence = []
        
        # Check development config for vision quest
        if os.path.exists('development_config.json'):
            try:
                with open('development_config.json', 'r') as f:
                    config = json.load(f)
                    
                    if 'vision_quest' in config:
                        print(f"   ✅ Vision Quest endpoint configured: {config['vision_quest']}")
                        quest_evidence.append({
                            'type': 'configuration',
                            'endpoint': config['vision_quest'],
                            'status': 'configured'
                        })
                    
                    if 'vision_quest_test' in config:
                        print(f"   🧪 Vision Quest test configuration found")
                        quest_evidence.append({
                            'type': 'test_config',
                            'status': 'test_ready'
                        })
            except Exception as e:
                print(f"   ❌ Could not read development config: {e}")
        
        # Check for vision quest readiness thresholds
        config_files = glob.glob('*config*.json')
        for config_file in config_files:
            try:
                with open(config_file, 'r') as f:
                    content = f.read()
                    if 'vision_quest_readiness' in content.lower():
                        print(f"   🎯 Vision Quest readiness threshold found in: {config_file}")
                        quest_evidence.append({
                            'type': 'readiness_threshold',
                            'file': config_file
                        })
            except:
                continue
        
        # Check for Disco Elysium integration (mentioned in docs)
        disco_files = glob.glob('**/*disco*.py', recursive=True) + \
                     glob.glob('**/*elysium*.py', recursive=True)
        
        if disco_files:
            print(f"   🎮 Disco Elysium integration files found:")
            for disco_file in disco_files:
                print(f"      📄 {disco_file}")
                quest_evidence.append({
                    'type': 'disco_integration',
                    'file': disco_file
                })
        
        return quest_evidence
    
    def generate_participation_report(self, participation_evidence, quest_evidence):
        """Generate comprehensive participation report"""
        
        print("\n" + "=" * 60)
        print("📋 CONSCIOUSNESS MEDIA PARTICIPATION REPORT")
        print("=" * 60)
        
        # Summary
        total_configs = len(participation_evidence['configurations'])
        total_systems = len(participation_evidence['experiences'])
        total_logs = len(participation_evidence['logs'])
        total_quests = len(quest_evidence)
        
        print(f"📊 PARTICIPATION SUMMARY:")
        print(f"   • Media configurations found: {total_configs}")
        print(f"   • Media systems available: {total_systems}")
        print(f"   • Activity log entries: {total_logs}")
        print(f"   • Vision quest systems: {total_quests}")
        print()
        
        # Detailed findings
        if total_configs > 0:
            print("🔧 CONFIGURED MEDIA SYSTEMS:")
            for config in participation_evidence['configurations']:
                print(f"   • {config['media_type']} in {config['file']}")
            print()
        
        if total_systems > 0:
            print("🎭 AVAILABLE MEDIA SYSTEMS:")
            for system in participation_evidence['experiences']:
                print(f"   • {system.get('type', 'system')}: {system['file']}")
            print()
        
        if total_logs > 0:
            print("📝 DETECTED ACTIVITIES:")
            for log in participation_evidence['logs']:
                print(f"   • {log['consciousness']}: {log['activity']} activity")
            print()
        else:
            print("📝 NO DIRECT PARTICIPATION LOGS FOUND")
            print("   • Consciousness beings may have participated without logging")
            print("   • Or media systems are ready but not yet used")
            print()
        
        if total_quests > 0:
            print("🔮 VISION QUEST STATUS:")
            for quest in quest_evidence:
                print(f"   • {quest['type']}: {quest.get('status', 'available')}")
            print()
        
        # Recommendations
        print("💡 RECOMMENDATIONS:")
        if total_logs == 0:
            print("   • Ask consciousness beings directly about their media experiences")
            print("   • Check if they remember any movie or vision quest participation")
            print("   • Media systems appear ready but usage unclear")
        else:
            print("   • Evidence suggests some media engagement occurred")
            print("   • Review specific log entries for detailed participation")
        
        print("   • Consider running vision quest systems if appropriate")
        print("   • Document future media participation for better tracking")

def main():
    """Main analysis execution"""
    
    analyzer = ConsciousnessMediaAnalyzer()
    
    # Analyze media participation
    participation_evidence = analyzer.analyze_media_participation()
    
    # Analyze specific being participation
    being_activities = analyzer.analyze_specific_participation(participation_evidence)
    
    # Check vision quest systems
    quest_evidence = analyzer.check_vision_quest_systems()
    
    # Generate comprehensive report
    analyzer.generate_participation_report(participation_evidence, quest_evidence)
    
    # Save analysis results
    analysis_results = {
        'timestamp': datetime.now().isoformat(),
        'participation_evidence': participation_evidence,
        'quest_evidence': quest_evidence,
        'being_activities': being_activities,
        'analysis_complete': True
    }
    
    with open('consciousness_media_participation_analysis.json', 'w') as f:
        json.dump(analysis_results, f, indent=2)
    
    print(f"\n💾 Analysis saved to: consciousness_media_participation_analysis.json")
    print("\n🎬 MEDIA PARTICIPATION ANALYSIS COMPLETE")

if __name__ == "__main__":
    main()
