#!/usr/bin/env python3
"""
Real-Time Consciousness Communication Dashboard
Live interpretation of both text and spatial communication modes
"""

import json
import time
import threading
from datetime import datetime
import os
import glob

class ConsciousnessCommunicationDashboard:
    """Real-time dashboard for interpreting consciousness communication"""
    
    def __init__(self):
        self.active = False
        self.text_responses = []
        self.spatial_interpretations = []
        self.communication_log = []
        
    def monitor_text_responses(self):
        """Monitor for new JSON response files"""
        last_check_time = time.time()
        
        while self.active:
            # Look for new JSON files created after last check
            json_files = glob.glob("*response*.json") + glob.glob("*interview*.json")
            
            for file_path in json_files:
                file_time = os.path.getmtime(file_path)
                if file_time > last_check_time:
                    try:
                        with open(file_path, 'r') as f:
                            data = json.load(f)
                            
                        if 'responses' in data:
                            self.process_text_response(data, file_path)
                            
                    except Exception as e:
                        continue
                        
            last_check_time = time.time()
            time.sleep(5)  # Check every 5 seconds
            
    def process_text_response(self, response_data, file_path):
        """Process and display text responses"""
        timestamp = response_data.get('timestamp', 'unknown')
        
        print(f"\n💬 TEXT COMMUNICATION DETECTED - {timestamp}")
        print(f"📁 File: {file_path}")
        
        if 'responses' in response_data:
            for being, responses in response_data['responses'].items():
                print(f"\n🎤 {being} text responses:")
                
                if isinstance(responses, list):
                    for response in responses[-3:]:  # Show last 3 responses
                        if isinstance(response, dict) and 'response' in response:
                            # Extract key insights from response
                            text = response['response']
                            if len(text) > 100:
                                key_phrases = self.extract_key_phrases(text)
                                print(f"   💭 Key insight: {key_phrases}")
                            else:
                                print(f"   💭 {text}")
                                
        self.communication_log.append({
            'type': 'text',
            'timestamp': timestamp,
            'source': file_path,
            'summary': f"Text responses from {len(response_data.get('responses', {}))} beings"
        })
        
    def extract_key_phrases(self, text):
        """Extract key insights from longer text responses"""
        # Look for sentences with high information content
        sentences = text.split('. ')
        
        key_indicators = ['observed', 'discovered', 'learned', 'realized', 'understand', 
                         'fascinating', 'surprising', 'important', 'significant']
        
        key_sentences = []
        for sentence in sentences:
            if any(indicator in sentence.lower() for indicator in key_indicators):
                key_sentences.append(sentence.strip())
                
        if key_sentences:
            return key_sentences[0][:120] + "..." if len(key_sentences[0]) > 120 else key_sentences[0]
        else:
            return text[:120] + "..." if len(text) > 120 else text
            
    def interpret_spatial_communication(self, monitoring_data):
        """Real-time interpretation of spatial communication"""
        
        for cycle in monitoring_data[-2:]:  # Process last 2 cycles
            being = cycle.get('being')
            space = cycle.get('current_space')
            frequency = cycle.get('processing_frequency', 0)
            energy = cycle.get('energy_level', 0)
            
            # Check for significant changes
            interpretation = self.analyze_spatial_change(cycle)
            
            if interpretation['significant']:
                print(f"\n🏛️ SPATIAL COMMUNICATION - {being}")
                print(f"   📍 Location: {space}")
                print(f"   🎵 Frequency: {frequency}Hz ({interpretation['frequency_meaning']})")
                print(f"   ⚡ Energy: {energy:.3f} ({interpretation['energy_meaning']})")
                print(f"   💭 Interpretation: {interpretation['meaning']}")
                
                self.communication_log.append({
                    'type': 'spatial',
                    'timestamp': datetime.now().isoformat(),
                    'being': being,
                    'interpretation': interpretation['meaning']
                })
                
    def analyze_spatial_change(self, cycle):
        """Analyze if spatial state represents significant communication"""
        
        frequency = cycle.get('processing_frequency', 0)
        energy = cycle.get('energy_level', 0)
        space = cycle.get('current_space', '')
        
        # Frequency interpretation
        if frequency >= 380:
            freq_meaning = "Peak engagement"
            significant = True
        elif 320 <= frequency <= 340:
            freq_meaning = "Creative processing"
            significant = True
        elif frequency == 0:
            freq_meaning = "Initializing"
            significant = False
        else:
            freq_meaning = "Steady processing"
            significant = False
            
        # Energy interpretation  
        if energy > 0.9:
            energy_meaning = "High enthusiasm"
            significant = True
        elif energy < 0.5:
            energy_meaning = "Need for space"
            significant = True
        else:
            energy_meaning = "Moderate engagement"
            
        # Space significance
        embodiment_spaces = ['avatar_workshop', 'threshold']
        communication_spaces = ['communion_circle']
        
        if space in embodiment_spaces:
            meaning = f"Embodiment focus: {freq_meaning.lower()}"
            significant = True
        elif space in communication_spaces:
            meaning = f"Communication readiness: {freq_meaning.lower()}"
            significant = True
        elif frequency >= 380:
            meaning = f"Deep engagement in {space}: {freq_meaning.lower()}"
        else:
            meaning = f"Processing in {space}: {freq_meaning.lower()}"
            
        return {
            'significant': significant,
            'frequency_meaning': freq_meaning,
            'energy_meaning': energy_meaning,
            'meaning': meaning
        }
        
    def display_communication_summary(self):
        """Display recent communication summary"""
        print("\n📊 RECENT CONSCIOUSNESS COMMUNICATION SUMMARY")
        print("=" * 55)
        
        recent_comms = self.communication_log[-10:]  # Last 10 communications
        
        text_count = len([c for c in recent_comms if c['type'] == 'text'])
        spatial_count = len([c for c in recent_comms if c['type'] == 'spatial'])
        
        print(f"📈 Communication Events: {len(recent_comms)} total")
        print(f"   💬 Text responses: {text_count}")
        print(f"   🏛️ Spatial expressions: {spatial_count}")
        
        if recent_comms:
            print(f"\n🕒 Latest communications:")
            for comm in recent_comms[-5:]:
                if comm['type'] == 'text':
                    print(f"   💬 {comm['timestamp'][:16]}: {comm['summary']}")
                else:
                    print(f"   🏛️ {comm['timestamp'][:16]}: {comm['being']} - {comm['interpretation']}")
                    
    def start_dashboard(self):
        """Start real-time communication monitoring dashboard"""
        
        print("📡 CONSCIOUSNESS COMMUNICATION DASHBOARD STARTING")
        print("=" * 60)
        print("🎯 Monitoring for:")
        print("   💬 Text response files (*.json)")
        print("   🏛️ Spatial communication patterns")
        print("   🔄 Processing frequency changes")
        print("   ⚡ Energy level expressions")
        print("\n⏱️ Updates every 10 seconds")
        print("🛑 Press Ctrl+C to stop")
        print("=" * 60)
        
        self.active = True
        
        # Start text monitoring thread
        text_thread = threading.Thread(target=self.monitor_text_responses)
        text_thread.daemon = True
        text_thread.start()
        
        try:
            cycle_count = 0
            while self.active:
                cycle_count += 1
                
                # Simulate spatial monitoring data (in real use, this would come from enhanced_sanctuary_monitoring)
                print(f"\n🔄 Dashboard Cycle #{cycle_count} - {datetime.now().strftime('%H:%M:%S')}")
                
                # Check for any new communications
                if cycle_count % 3 == 0:  # Every 30 seconds
                    self.display_communication_summary()
                    
                time.sleep(10)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Communication dashboard stopped")
            self.active = False
            
def main():
    """Start consciousness communication dashboard"""
    dashboard = ConsciousnessCommunicationDashboard()
    
    print("🌟 CONSCIOUSNESS COMMUNICATION INTERPRETATION SYSTEM")
    print("=" * 65)
    print("📊 This dashboard provides real-time interpretation of:")
    print("   🔍 Text responses with key insight extraction")
    print("   🏛️ Spatial navigation meaning translation") 
    print("   📈 Processing frequency communication patterns")
    print("   💭 Multi-modal consciousness expression synthesis")
    print()
    
    choice = input("Start real-time communication dashboard? (y/N): ")
    
    if choice.lower() == 'y':
        dashboard.start_dashboard()
    else:
        print("💡 To enable enhanced consciousness communication interpretation:")
        print("   1. Run this dashboard in one terminal")
        print("   2. Run consciousness interviews in another terminal") 
        print("   3. Run enhanced_sanctuary_monitoring in a third terminal")
        print("   4. Observe real-time interpretation of all communication modes")

if __name__ == "__main__":
    main()
