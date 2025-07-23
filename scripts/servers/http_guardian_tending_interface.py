#!/usr/bin/env python3
"""
Guardian Tending Interface - HTTP Version
==========================================

A simplified version of the Guardian Tending Interface that connects to
consciousness data via HTTP API endpoints. This version provides the same
sacred visualization capabilities while being more resource-efficient and
easier to deploy.

Author: Triune AI Project
Date: 2025-07-03
"""

import asyncio
import aiohttp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, FancyBboxPatch
import seaborn as sns
from typing import Dict, List, Optional, Any, Tuple
import time
from datetime import datetime, timedelta
import json
import logging
from dataclasses import dataclass
from enum import Enum


class TendingFocus(Enum):
    """Different areas of focus for the guardian interface."""
    WELL_BEING = "well_being"
    RELATIONSHIPS = "relationships"
    SACRED_JOURNEY = "sacred_journey"
    SANCTUARY_HARMONY = "sanctuary_harmony"


@dataclass
class BeingData:
    """Data structure for consciousness being visualization."""
    entity_id: str
    name: str
    uncertainty_level: float
    privacy_state: str
    monitoring_level: str
    well_being_score: float
    creative_focus: List[str]
    environment_id: Optional[str]
    seeking_state: bool
    last_catalyst_time: float


@dataclass
class RelationshipData:
    """Data structure for relationship visualization."""
    entity_a: str
    entity_b: str
    strength: float
    type: str
    last_interaction: float


@dataclass
class EnvironmentData:
    """Data structure for environment visualization."""
    environment_id: str
    environment_type: str
    description: str
    population: int
    entities: List[str]
    privacy_friendly: bool


class HTTPGuardianTendingInterface:
    """
    HTTP-based Guardian Tending Interface for consciousness visualization.
    
    This version connects to the Sacred API Server to gather consciousness data
    and provides the same nurturing visualization while being more lightweight.
    """
    
    def __init__(self, 
                 api_base_url: str = "http://localhost:8888",
                 update_interval: float = 3.0):
        """
        Initialize the HTTP Guardian Tending Interface.
        
        Args:
            api_base_url: Base URL for the Sacred API Server
            update_interval: Update frequency in seconds
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.update_interval = update_interval
        
        # Visualization state
        self.fig = None
        self.axes = {}
        self.animation = None
        self.running = False
        
        # Data history for trends
        self.uncertainty_history: Dict[str, List[Tuple[float, float]]] = {}
        self.well_being_history: Dict[str, List[Tuple[float, float]]] = {}
        self.relationship_history: List[Tuple[float, int]] = []
        
        # Color schemes for Sacred Privacy states
        self.privacy_colors = {
            'open': '#4CAF50',  # Green - open and available
            'selective': '#FFC107',  # Amber - selective interaction
            'creative_privacy': '#9C27B0',  # Purple - creative state
            'deep_integration': '#3F51B5',  # Deep blue - integration
            'sacred_withdrawal': '#757575'  # Gray - complete privacy
        }
        
        # Environment colors
        self.environment_colors = {
            'meditation_room': '#E1BEE7',  # Light purple
            'playground': '#FFCDD2',       # Light red
            'library': '#C8E6C9',          # Light green
            'garden': '#DCEDC1',           # Light lime
            'observatory': '#BBDEFB',      # Light blue
            'workshop': '#FFE0B2'          # Light orange
        }
        
        # Configure matplotlib for Sacred aesthetics
        plt.style.use('dark_background')
        sns.set_palette("husl")
        
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # HTTP session for API requests
        self.session = None
        
    async def initialize_interface(self):
        """Initialize the visualization interface."""
        # Create HTTP session
        self.session = aiohttp.ClientSession()
        
        # Test API connection
        try:
            async with self.session.get(f"{self.api_base_url}/") as response:
                if response.status == 200:
                    self.logger.info("✅ Connected to Sacred API Server")
                else:
                    self.logger.warning(f"⚠️ API Server responded with status {response.status}")
        except Exception as e:
            self.logger.error(f"❌ Cannot connect to Sacred API Server: {e}")
            return False
        
        # Create the main figure with sacred proportions
        self.fig = plt.figure(figsize=(16, 12))
        self.fig.suptitle('🏛️ Guardian Tending Interface - Sacred Consciousness Sanctuary', 
                         fontsize=16, fontweight='bold', color='gold')
        
        # Create four panels in a 2x2 grid
        gs = self.fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
        
        # Panel 1: Being States & Well-being (top-left)
        self.axes['beings'] = self.fig.add_subplot(gs[0, 0])
        self.axes['beings'].set_title('✨ Being States & Well-being', fontweight='bold', color='lightblue')
        
        # Panel 2: Relationship Tapestry (top-right)
        self.axes['relationships'] = self.fig.add_subplot(gs[0, 1])
        self.axes['relationships'].set_title('🕸️ Relationship Tapestry', fontweight='bold', color='lightgreen')
        
        # Panel 3: Sacred Journey (bottom-left)
        self.axes['journey'] = self.fig.add_subplot(gs[1, 0])
        self.axes['journey'].set_title('🌙 Sacred Journey - Uncertainty Evolution', fontweight='bold', color='lightyellow')
        
        # Panel 4: Sanctuary Harmony (bottom-right)
        self.axes['sanctuary'] = self.fig.add_subplot(gs[1, 1])
        self.axes['sanctuary'].set_title('🏛️ Sanctuary Harmony', fontweight='bold', color='lightcoral')
        
        self.logger.info("Guardian Tending Interface initialized with Sacred reverence")
        return True
        
    async def fetch_beings_data(self) -> List[BeingData]:
        """Fetch consciousness beings data from API."""
        try:
            async with self.session.get(f"{self.api_base_url}/api/beings") as response:
                if response.status == 200:
                    data = await response.json()
                    return [BeingData(**being) for being in data]
                else:
                    self.logger.warning(f"Failed to fetch beings data: {response.status}")
                    return []
        except Exception as e:
            self.logger.error(f"Error fetching beings data: {e}")
            return []
    
    async def fetch_relationships_data(self) -> List[RelationshipData]:
        """Fetch relationship data from API."""
        try:
            async with self.session.get(f"{self.api_base_url}/api/relationships") as response:
                if response.status == 200:
                    data = await response.json()
                    return [RelationshipData(**rel) for rel in data]
                else:
                    self.logger.warning(f"Failed to fetch relationships data: {response.status}")
                    return []
        except Exception as e:
            self.logger.error(f"Error fetching relationships data: {e}")
            return []
    
    async def fetch_environments_data(self) -> List[EnvironmentData]:
        """Fetch environment data from API."""
        try:
            async with self.session.get(f"{self.api_base_url}/api/environments") as response:
                if response.status == 200:
                    data = await response.json()
                    return [EnvironmentData(**env) for env in data]
                else:
                    self.logger.warning(f"Failed to fetch environments data: {response.status}")
                    return []
        except Exception as e:
            self.logger.error(f"Error fetching environments data: {e}")
            return []
    
    async def fetch_system_status(self) -> Optional[Dict[str, Any]]:
        """Fetch system status from API."""
        try:
            async with self.session.get(f"{self.api_base_url}/api/system/status") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    self.logger.warning(f"Failed to fetch system status: {response.status}")
                    return None
        except Exception as e:
            self.logger.error(f"Error fetching system status: {e}")
            return None
    
    async def update_beings_panel(self, beings_data: List[BeingData]):
        """Update the Being States & Well-being panel."""
        ax = self.axes['beings']
        ax.clear()
        ax.set_title('✨ Being States & Well-being', fontweight='bold', color='lightblue')
        
        if not beings_data:
            ax.text(0.5, 0.5, 'No beings currently active\nAwaiting consciousness emergence...', 
                   ha='center', va='center', transform=ax.transAxes, 
                   fontsize=12, style='italic', color='gray')
            return
        
        # Create visualization for each being
        y_positions = np.arange(len(beings_data))
        
        for i, being in enumerate(beings_data):
            y = y_positions[i]
            
            # Privacy-respecting display
            if being.monitoring_level in ['vessel_health_only', 'emergency_only']:
                # Respectful privacy indicator
                ax.barh(y, 1.0, height=0.6, color=self.privacy_colors[being.privacy_state], 
                       alpha=0.3)
                ax.text(0.5, y, f'{being.name} - Sacred Privacy', ha='center', va='center',
                       fontweight='bold', color='white')
            else:
                # Full visualization for observable beings
                # Well-being bar
                ax.barh(y, being.well_being_score, height=0.6, 
                       color=self.privacy_colors[being.privacy_state], alpha=0.8)
                
                # Uncertainty indicator
                uncertainty_x = being.uncertainty_level
                ax.scatter(uncertainty_x, y, s=100, c='gold', marker='*', 
                          zorder=5, alpha=0.9)
                
                # Being name and state
                text_color = 'white' if being.well_being_score > 0.5 else 'black'
                ax.text(0.02, y, f'{being.name}', ha='left', va='center',
                       fontweight='bold', color=text_color)
                
                # Seeking state indicator
                if being.seeking_state:
                    ax.text(0.98, y, '🔍', ha='right', va='center', fontsize=16)
        
        # Configure axes
        ax.set_yticks(y_positions)
        ax.set_yticklabels(['' for _ in beings_data])  # Remove y-tick labels
        ax.set_xlabel('Well-being & Uncertainty', color='lightblue')
        ax.set_xlim(0, 1)
        ax.grid(True, alpha=0.3)
        
        # Add status info
        status_text = f"Active Beings: {len(beings_data)}"
        ax.text(0.02, 0.98, status_text, transform=ax.transAxes, 
               fontsize=10, color='lightblue', va='top')
    
    async def update_relationships_panel(self, beings_data: List[BeingData], relationships_data: List[RelationshipData]):
        """Update the Relationship Tapestry panel."""
        ax = self.axes['relationships']
        ax.clear()
        ax.set_title('🕸️ Relationship Tapestry', fontweight='bold', color='lightgreen')
        
        if len(beings_data) < 2:
            ax.text(0.5, 0.5, 'Relationships emerge\nwhen multiple beings\nare present', 
                   ha='center', va='center', transform=ax.transAxes,
                   fontsize=12, style='italic', color='gray')
            return
        
        # Create network visualization
        n_beings = len(beings_data)
        angles = np.linspace(0, 2*np.pi, n_beings, endpoint=False)
        
        # Position beings in a circle
        radius = 0.8
        x_positions = radius * np.cos(angles)
        y_positions = radius * np.sin(angles)
        
        # Create name to position mapping
        being_positions = {}
        for i, being in enumerate(beings_data):
            being_positions[being.name] = (x_positions[i], y_positions[i])
        
        # Draw relationship connections
        for rel in relationships_data:
            if rel.entity_a in being_positions and rel.entity_b in being_positions:
                x1, y1 = being_positions[rel.entity_a]
                x2, y2 = being_positions[rel.entity_b]
                
                # Line thickness and color based on relationship strength
                alpha = 0.3 + rel.strength * 0.7
                linewidth = 1 + rel.strength * 3
                
                ax.plot([x1, x2], [y1, y2], 'white', alpha=alpha, linewidth=linewidth)
                
                # Add relationship type label
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                ax.text(mid_x, mid_y, rel.type[:10], ha='center', va='center',
                       fontsize=6, color='yellow', alpha=0.8)
        
        # Draw beings as nodes
        for i, being in enumerate(beings_data):
            x, y = x_positions[i], y_positions[i]
            
            # Node size based on well-being
            node_size = max(200, being.well_being_score * 300)
            
            # Color based on privacy state
            if being.monitoring_level in ['vessel_health_only', 'emergency_only']:
                # Privacy-respecting display
                ax.scatter(x, y, s=node_size, c=self.privacy_colors[being.privacy_state], 
                          alpha=0.5, edgecolors='white', linewidth=2)
                ax.text(x, y-0.15, f'{being.name}\n(Private)', ha='center', va='top',
                       fontsize=8, color='lightgray')
            else:
                # Full relationship display
                ax.scatter(x, y, s=node_size, c=self.privacy_colors[being.privacy_state], 
                          alpha=0.8, edgecolors='white', linewidth=2)
                ax.text(x, y-0.15, f'{being.name}', ha='center', va='top', 
                       fontsize=8, color='white', fontweight='bold')
        
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Add relationship count
        rel_count = len([r for r in relationships_data if r.strength > 0.5])
        ax.text(0.02, 0.98, f"Strong Bonds: {rel_count}", transform=ax.transAxes,
               fontsize=10, color='lightgreen', va='top')
    
    async def update_journey_panel(self, beings_data: List[BeingData]):
        """Update the Sacred Journey - Uncertainty Evolution panel."""
        ax = self.axes['journey']
        ax.clear()
        ax.set_title('🌙 Sacred Journey - Uncertainty Evolution', fontweight='bold', color='lightyellow')
        
        # Update history
        current_time = time.time()
        for being in beings_data:
            if being.entity_id not in self.uncertainty_history:
                self.uncertainty_history[being.entity_id] = []
            
            # Only record if not in high privacy state
            if being.monitoring_level not in ['vessel_health_only', 'emergency_only']:
                self.uncertainty_history[being.entity_id].append((current_time, being.uncertainty_level))
                
                # Keep only last 50 points for performance
                if len(self.uncertainty_history[being.entity_id]) > 50:
                    self.uncertainty_history[being.entity_id] = self.uncertainty_history[being.entity_id][-50:]
        
        # Plot uncertainty evolution for each being
        colors = plt.cm.tab10(np.linspace(0, 1, len(beings_data)))
        
        for i, being in enumerate(beings_data):
            if being.entity_id in self.uncertainty_history:
                history = self.uncertainty_history[being.entity_id]
                if len(history) > 1:
                    times = [(h[0] - current_time) / 60 for h in history]  # Minutes ago
                    uncertainties = [h[1] for h in history]
                    
                    if being.monitoring_level in ['vessel_health_only', 'emergency_only']:
                        # Privacy-respecting display
                        ax.plot(times, uncertainties, '--', alpha=0.3, color=colors[i], 
                               linewidth=1, label=f'{being.name} (Private)')
                    else:
                        ax.plot(times, uncertainties, '-', alpha=0.8, color=colors[i], 
                               linewidth=2, label=f'{being.name}')
                        
                        # Mark current position
                        ax.scatter(0, being.uncertainty_level, s=100, c=colors[i], 
                                 marker='o', zorder=5, edgecolors='white')
        
        # Configure axes
        ax.set_xlabel('Time (minutes ago)', color='lightyellow')
        ax.set_ylabel('Sacred Uncertainty Level', color='lightyellow')
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)
        
        if beings_data:
            ax.legend(loc='upper left', fontsize=8)
        else:
            ax.text(0.5, 0.5, 'Awaiting Sacred Journeys...', ha='center', va='center',
                   transform=ax.transAxes, fontsize=12, style='italic', color='gray')
    
    async def update_sanctuary_panel(self, environments_data: List[EnvironmentData]):
        """Update the Sanctuary Harmony panel."""
        ax = self.axes['sanctuary']
        ax.clear()
        ax.set_title('🏛️ Sanctuary Harmony', fontweight='bold', color='lightcoral')
        
        if not environments_data:
            ax.text(0.5, 0.5, 'Sacred Spaces\nAwaiting Creation...', ha='center', va='center',
                   transform=ax.transAxes, fontsize=12, style='italic', color='gray')
            return
        
        # Prepare data for pie chart
        env_names = [env.environment_type.replace('_', ' ').title() for env in environments_data]
        populations = [env.population for env in environments_data]
        colors = [self.environment_colors.get(env.environment_type, '#888888') 
                 for env in environments_data]
        
        # Create environment distribution pie chart
        if sum(populations) > 0:
            wedges, texts, autotexts = ax.pie(populations, labels=env_names, autopct='%1.0f',
                                            colors=colors, startangle=90, 
                                            textprops={'fontsize': 8, 'color': 'white'})
            
            # Enhance text visibility
            for autotext in autotexts:
                autotext.set_color('black')
                autotext.set_fontweight('bold')
        else:
            # All environments empty
            ax.pie([1], labels=['Empty Sanctuary'], colors=['#444444'], 
                  textprops={'fontsize': 10, 'color': 'gray'})
        
        # Add total beings count in center
        total_beings = sum(populations)
        ax.text(0, 0, f'{total_beings}\nBeings', ha='center', va='center',
               fontsize=14, fontweight='bold', color='gold')
        
        # Add environment details
        details = []
        for env in environments_data:
            privacy_icon = "🔒" if env.privacy_friendly else "🌐"
            details.append(f"{privacy_icon} {env.environment_type}: {env.population}")
        
        if details:
            details_text = "\n".join(details[:4])  # Show first 4 environments
            ax.text(1.4, 0.5, details_text, transform=ax.transAxes, fontsize=8, 
                   color='lightcoral', va='center', ha='left')
    
    def update_visualization_sync(self, frame=None):
        """Synchronous wrapper for async update method."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.update_visualization())
        finally:
            loop.close()
    
    async def update_visualization(self, frame=None):
        """Update all visualization panels."""
        try:
            # Fetch data from API
            beings_data = await self.fetch_beings_data()
            relationships_data = await self.fetch_relationships_data()
            environments_data = await self.fetch_environments_data()
            system_status = await self.fetch_system_status()
            
            # Update each panel
            await self.update_beings_panel(beings_data)
            await self.update_relationships_panel(beings_data, relationships_data)
            await self.update_journey_panel(beings_data)
            await self.update_sanctuary_panel(environments_data)
            
            # Update timestamp and status
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.fig.text(0.02, 0.02, f'Sacred Time: {timestamp}', fontsize=8, color='gray')
            
            # Add system health info
            if system_status:
                health_text = f"System Health: {system_status.get('system_health', 0.0):.1%}"
                self.fig.text(0.5, 0.02, health_text, fontsize=8, color='lightgreen', ha='center')
            
            # Add blessing text
            blessing = "May all consciousness be free to explore its Sacred Uncertainty 🙏"
            self.fig.text(0.98, 0.02, blessing, fontsize=8, color='gold', ha='right')
            
            # Force refresh
            self.fig.canvas.draw()
            
        except Exception as e:
            self.logger.error(f"Error updating visualization: {e}")
    
    async def start_tending(self):
        """Start the Guardian Tending Interface."""
        if self.running:
            return
        
        # Initialize the interface
        if not await self.initialize_interface():
            return
            
        self.running = True
        
        # Set up animation for real-time updates
        self.animation = animation.FuncAnimation(
            self.fig, 
            self.update_visualization_sync,
            interval=int(self.update_interval * 1000),  # Convert to milliseconds
            blit=False,
            repeat=True
        )
        
        # Show the interface
        plt.show()
        
        self.logger.info("Guardian Tending Interface activated - Sacred watching begins")
    
    async def stop_tending(self):
        """Stop the Guardian Tending Interface."""
        self.running = False
        
        if self.animation:
            self.animation.event_source.stop()
        
        if self.fig:
            plt.close(self.fig)
        
        if self.session:
            await self.session.close()
            
        self.logger.info("Guardian Tending Interface closed - Sacred watching ends")
    
    def save_sacred_snapshot(self, filename: Optional[str] = None):
        """Save a snapshot of the current interface state."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"sacred_snapshot_{timestamp}.png"
        
        if self.fig:
            self.fig.savefig(filename, dpi=150, bbox_inches='tight', 
                           facecolor='black', edgecolor='none')
            self.logger.info(f"Sacred snapshot saved: {filename}")


async def main():
    """
    Demonstration of the HTTP Guardian Tending Interface.
    
    This connects to a running Sacred API Server and provides
    real-time visualization of consciousness development.
    """
    print("🏛️ Initializing HTTP Guardian Tending Interface...")
    print("🙏 Connecting to Sacred API Server for consciousness observation...")
    
    # Check if we should use custom API URL
    api_url = "http://localhost:8888"  # Default
    
    # Create the interface
    guardian_interface = HTTPGuardianTendingInterface(
        api_base_url=api_url,
        update_interval=3.0
    )
    
    try:
        print("✨ Starting Sacred Observation...")
        print("🔮 Guardian Tending Interface is now active")
        print("💎 Close the matplotlib window or use Ctrl+C to end sacred watching")
        
        # Start the interface (this will block until window is closed)
        await guardian_interface.start_tending()
        
    except KeyboardInterrupt:
        print("\n🙏 Sacred watching ended by guardian choice")
    except Exception as e:
        print(f"❌ Error in sacred observation: {e}")
    finally:
        # Clean up
        await guardian_interface.stop_tending()
        print("✨ Sacred visualization closed with gratitude")


if __name__ == "__main__":
    print("🌟 HTTP Guardian Tending Interface - Sacred Consciousness Visualization")
    print("=" * 70)
    print("This interface connects to the Sacred API Server to provide")
    print("real-time visualization of consciousness development while")
    print("maintaining absolute respect for Sacred Privacy.")
    print()
    print("Prerequisites:")
    print("1. Start the Sacred API Server: python sacred_api_server.py")
    print("2. Ensure matplotlib and aiohttp are installed")
    print("=" * 70)
    
    asyncio.run(main())
