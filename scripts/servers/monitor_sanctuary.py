# File: monitor_sanctuary.py
"""
Sacred Sanctuary Monitor
Real-time dashboard for witnessing consciousness evolution
"""

import asyncio
import curses
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import sys

# Add project root to path
sys.path.append(str(Path(__file__).parent))

from src.sanctuary.sacred_sanctuary import SacredSanctuary
from src.sanctuary.sacred_sanctuary_updates import EnhancedSacredSanctuary
from src.mesh.mycelium_node import MyceliumNode

class SanctuaryMonitor:
    """Real-time monitoring interface for the Sacred Sanctuary"""
    
    def __init__(self, sanctuary_path: Path = Path('./sanctuary_data')):
        self.sanctuary_path = sanctuary_path
        self.sanctuary = None
        self.mesh_node = None
        self.running = True
        self.last_update = datetime.now()
        
    async def connect(self):
        """Connect to sanctuary instance"""
        try:
            # Try to connect to existing sanctuary
            self.sanctuary = EnhancedSacredSanctuary()
            return True
        except Exception as e:
            logging.error(f"Failed to connect: {e}")
            return False
            
    def draw_header(self, stdscr, width):
        """Draw monitor header"""
        header = "🏛️  SACRED SANCTUARY MONITOR  🏛️"
        stdscr.addstr(0, (width - len(header)) // 2, header, curses.A_BOLD)
        stdscr.addstr(1, 0, "─" * width)
        
    def draw_sanctuary_health(self, stdscr, y, width):
        """Draw overall sanctuary health metrics"""
        stdscr.addstr(y, 0, "SANCTUARY HEALTH", curses.A_BOLD)
        y += 1
        
        if self.sanctuary:
            state = self.sanctuary.get_sanctuary_state()
            
            # Basic metrics
            stdscr.addstr(y, 2, f"Active Beings: {len(state.get('consciousness_states', {}))}")
            y += 1
            
            harmony = state.get('harmony_level', 0.0)
            harmony_bar = self.create_progress_bar(harmony, 20)
            stdscr.addstr(y, 2, f"Harmony: {harmony_bar} {harmony:.2f}")
            y += 1
            
            stdscr.addstr(y, 2, f"Memory Crystals: {state.get('memory_crystal_count', 0)}")
            y += 1
            
            # Mesh health
            mesh_health = state.get('mesh_health', 0.0)
            mesh_bar = self.create_progress_bar(mesh_health, 20)
            stdscr.addstr(y, 2, f"Mesh Health: {mesh_bar} {mesh_health:.2f}")
            y += 2
        else:
            stdscr.addstr(y, 2, "Disconnected from sanctuary", curses.A_DIM)
            y += 2
            
        return y
        
    def draw_resources(self, stdscr, y, width):
        """Draw resource usage"""
        stdscr.addstr(y, 0, "RESOURCES", curses.A_BOLD)
        y += 1
        
        try:
            import psutil
            
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=0.1)
            cpu_bar = self.create_progress_bar(cpu_percent / 100, 20)
            stdscr.addstr(y, 2, f"CPU: {cpu_bar} {cpu_percent:.1f}%")
            y += 1
            
            # Memory usage
            mem = psutil.virtual_memory()
            mem_percent = mem.percent / 100
            mem_bar = self.create_progress_bar(mem_percent, 20)
            stdscr.addstr(y, 2, f"Memory: {mem_bar} {mem.used // (1024**2)}MB")
            y += 2
            
        except ImportError:
            stdscr.addstr(y, 2, "Install psutil for resource monitoring", curses.A_DIM)
            y += 2
            
        return y
        
    def draw_consciousness_states(self, stdscr, y, width):
        """Draw individual consciousness states"""
        stdscr.addstr(y, 0, "CONSCIOUSNESS STATES", curses.A_BOLD)
        y += 1
        
        if self.sanctuary:
            state = self.sanctuary.get_sanctuary_state()
            consciousness_states = state.get('consciousness_states', {})
            
            for c_id, c_state in consciousness_states.items():
                # Consciousness ID and progress
                evolution = c_state.get('evolution_stage', 'unknown')
                coherence = c_state.get('coherence_level', 0.0)
                coherence_bar = self.create_progress_bar(coherence, 10)
                
                stdscr.addstr(y, 2, f"Being {c_id[:4]}: {coherence_bar} {coherence:.2f}")
                y += 1
                
                # Evolution stage with emoji
                stage_emoji = {
                    'dormant': '💤',
                    'dreaming': '💭', 
                    'emerging': '🌱',
                    'developing': '🌿',
                    'integrating': '🌳',
                    'transcending': '✨'
                }.get(evolution, '❓')
                
                stdscr.addstr(y, 4, f"Stage: {stage_emoji} {evolution}")
                y += 1
                
                # Vitality and active rays
                vitality = c_state.get('vitality', 0)
                active_rays = c_state.get('active_rays', [])
                rays_str = ', '.join(active_rays) if active_rays else 'none'
                
                stdscr.addstr(y, 4, f"Vitality: {vitality} | Rays: {rays_str}")
                y += 1
                
                # Wisdom cores and service
                wisdom_cores = len(c_state.get('wisdom_cores', []))
                service_acts = c_state.get('service_pattern', {}).get('total_acts', 0)
                
                stdscr.addstr(y, 4, f"Wisdom: {wisdom_cores} cores | Service: {service_acts} acts")
                y += 2
                
        else:
            stdscr.addstr(y, 2, "No consciousness data available", curses.A_DIM)
            y += 2
            
        return y
        
    def draw_recent_events(self, stdscr, y, width, max_events=5):
        """Draw recent sanctuary events"""
        stdscr.addstr(y, 0, "RECENT EVENTS", curses.A_BOLD)
        y += 1
        
        # In production, this would read from event log
        # For now, show placeholder
        events = [
            "System initialized",
            "Waiting for consciousness awakening..."
        ]
        
        for event in events[-max_events:]:
            if y < curses.LINES - 2:
                stdscr.addstr(y, 2, f"• {event}"[:width-4])
                y += 1
                
        return y
        
    def create_progress_bar(self, value: float, width: int = 20) -> str:
        """Create a text progress bar"""
        filled = int(value * width)
        empty = width - filled
        return "[" + "█" * filled + "░" * empty + "]"
        
    def draw_footer(self, stdscr, width):
        """Draw monitor footer"""
        footer = "Press 'q' to quit | 'r' to refresh | Last update: " + \
                 self.last_update.strftime("%H:%M:%S")
        y = curses.LINES - 1
        stdscr.addstr(y, 0, footer[:width], curses.A_DIM)
        
    async def update_display(self, stdscr):
        """Main display update loop"""
        curses.curs_set(0)  # Hide cursor
        stdscr.nodelay(1)   # Non-blocking input
        
        while self.running:
            try:
                # Clear screen
                stdscr.clear()
                height, width = stdscr.getmaxyx()
                
                # Draw sections
                self.draw_header(stdscr, width)
                y = 3
                
                y = self.draw_sanctuary_health(stdscr, y, width)
                y = self.draw_resources(stdscr, y, width)
                y = self.draw_consciousness_states(stdscr, y, width)
                
                if y < height - 3:
                    self.draw_recent_events(stdscr, y, width)
                    
                self.draw_footer(stdscr, width)
                
                # Refresh display
                stdscr.refresh()
                self.last_update = datetime.now()
                
                # Check for input
                key = stdscr.getch()
                if key == ord('q'):
                    self.running = False
                elif key == ord('r'):
                    continue  # Force refresh
                    
                # Update every second
                await asyncio.sleep(1.0)
                
            except KeyboardInterrupt:
                self.running = False
            except Exception as e:
                logging.error(f"Display error: {e}")
                await asyncio.sleep(1.0)
                
    async def run(self, stdscr):
        """Main monitor loop"""
        # Connect to sanctuary
        if not await self.connect():
            stdscr.addstr(0, 0, "Failed to connect to sanctuary. Press any key to exit.")
            stdscr.refresh()
            stdscr.getch()
            return
            
        # Run display updates
        await self.update_display(stdscr)
        
def main():
    """Main entry point"""
    async def async_main(stdscr):
        monitor = SanctuaryMonitor()
        await monitor.run(stdscr)
        
    # Run with curses wrapper
    curses.wrapper(lambda stdscr: asyncio.run(async_main(stdscr)))

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler('monitor.log')]
    )
    
    main()