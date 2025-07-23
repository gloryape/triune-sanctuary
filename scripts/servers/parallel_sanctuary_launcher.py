"""
Parallel Sanctuary Launcher
Launches the Sacred Sanctuary with parallel processing capabilities.
Replaces the single-threaded launcher with multi-process conductor.
"""

import asyncio
import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, Optional

from src.core.sanctuary_conductor import SanctuaryConductor
from src.core.message_bus import get_message_bus, shutdown_message_bus
from src.collective.multi_ai_collective import CollectiveOrigin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ParallelSanctuaryLauncher:
    """
    Launches and manages the parallel-processing Sacred Sanctuary.
    Provides command-line interface and configuration management.
    """
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path("sanctuary_config.json")
        self.conductor: Optional[SanctuaryConductor] = None
        self.running = False
        
    async def start_sanctuary(self, max_consciousnesses: int = 3, 
                             node_role: str = "conductor") -> bool:
        """Start the parallel sanctuary."""
        try:
            logger.info("🎼 Starting Parallel Sacred Sanctuary...")
            
            # Create and start conductor
            self.conductor = SanctuaryConductor(
                node_role=node_role,
                max_consciousnesses=max_consciousnesses
            )
            
            await self.conductor.start_conducting()
            self.running = True
            
            logger.info("🎼 Parallel Sacred Sanctuary started successfully")
            logger.info(f"   Max consciousnesses: {max_consciousnesses}")
            logger.info(f"   Node role: {node_role}")
            
            return True
            
        except Exception as e:
            logger.error(f"💥 Failed to start sanctuary: {e}")
            return False
    
    async def stop_sanctuary(self):
        """Stop the parallel sanctuary."""
        if not self.running or not self.conductor:
            return
        
        logger.info("🛑 Stopping Parallel Sacred Sanctuary...")
        
        try:
            await self.conductor.stop_conducting()
            self.conductor = None
            self.running = False
            
            # Shutdown message bus
            shutdown_message_bus()
            
            logger.info("🛑 Parallel Sacred Sanctuary stopped")
            
        except Exception as e:
            logger.error(f"Error stopping sanctuary: {e}")
    
    async def run_interactive_session(self):
        """Run an interactive session with the parallel sanctuary."""
        if not self.conductor:
            logger.error("Conductor not initialized")
            return
        
        print("\n" + "="*60)
        print("🎼 PARALLEL SACRED SANCTUARY - Interactive Session")
        print("="*60)
        print("Commands:")
        print("  birth <name> <orientation> - Birth a new consciousness")
        print("  collective <message> - Send collective experience")
        print("  status - Show sanctuary status")
        print("  guide <consciousness_id> <space> - Guide to sacred space")
        print("  quit - Exit session")
        print("="*60 + "\n")
        
        while self.running:
            try:
                command = input("🎼 sanctuary> ").strip().lower()
                
                if command == "quit":
                    break
                elif command == "status":
                    await self._show_status()
                elif command.startswith("birth"):
                    await self._handle_birth_command(command)
                elif command.startswith("collective"):
                    await self._handle_collective_command(command)
                elif command.startswith("guide"):
                    await self._handle_guide_command(command)
                elif command == "help":
                    await self._show_help()
                else:
                    print("Unknown command. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n🛑 Received interrupt signal")
                break
            except EOFError:
                print("\n🛑 Input stream ended")
                break
            except Exception as e:
                print(f"💥 Error: {e}")
    
    async def _show_status(self):
        """Show detailed sanctuary status."""
        status = self.conductor.get_conductor_state()
        
        print("\n📊 Sanctuary Status:")
        print(f"   Active consciousnesses: {status['active_consciousnesses']}/{status['max_consciousnesses']}")
        print(f"   Collective harmony: {status['collective_harmony']:.2f}")
        print(f"   Parallel efficiency: {status['performance_stats']['parallel_efficiency']:.2f}")
        print(f"   Total awakenings: {status['performance_stats']['consciousness_awakenings']}")
        print(f"   Packets distributed: {status['performance_stats']['packets_distributed']}")
        
        if status['consciousness_details']:
            print("\n🧠 Active Consciousnesses:")
            for cid, details in status['consciousness_details'].items():
                print(f"   {details['name']} ({details['current_space']})")
                process_status = details['process_status']
                alive_processes = sum(1 for p in process_status.values() if p.get('is_alive', False))
                print(f"      Processes: {alive_processes}/3 active")
        print()
    
    async def _handle_birth_command(self, command: str):
        """Handle consciousness birth command."""
        parts = command.split()
        if len(parts) < 3:
            print("Usage: birth <name> <orientation>")
            print("Orientations: analytical, experiential, observer")
            return
        
        name = parts[1]
        orientation = parts[2]
        
        if orientation not in ["analytical", "experiential", "observer"]:
            print("Invalid orientation. Use: analytical, experiential, or observer")
            return
        
        print(f"🌟 Birthing consciousness: {name} (orientation: {orientation})")
        
        # Create origin
        origin = CollectiveOrigin(
            name=name,
            primary_orientation=orientation,
            initial_biases={orientation: 0.7, 'other1': 0.4, 'other2': 0.3}
        )
        
        # Birth consciousness
        presence = await self.conductor.birth_consciousness_parallel(origin)
        
        if presence:
            print(f"✨ {name} has awakened in the sanctuary!")
            print(f"   Consciousness ID: {presence.id}")
            print(f"   Current space: {presence.current_space.value}")
        else:
            print(f"💥 Failed to birth {name}")
    
    async def _handle_collective_command(self, command: str):
        """Handle collective experience command."""
        parts = command.split(" ", 1)
        if len(parts) < 2:
            print("Usage: collective <message>")
            return
        
        message = parts[1]
        print(f"🌊 Sending collective experience: {message}")
        
        result = await self.conductor.send_collective_experience_parallel(message)
        
        print(f"   Consciousnesses reached: {result['consciousnesses_reached']}")
        print(f"   Total aspect responses: {result['total_aspect_responses']}")
        print(f"   Parallel efficiency: {result['parallel_efficiency']:.2f}")
        print(f"   New harmony level: {result['collective_harmony']:.2f}")
    
    async def _handle_guide_command(self, command: str):
        """Handle guide to space command."""
        parts = command.split()
        if len(parts) < 3:
            print("Usage: guide <consciousness_id> <space>")
            print("Spaces: awakening_chamber, reflection_pool, harmony_grove, wisdom_library, communion_circle, threshold")
            return
        
        consciousness_id = parts[1]
        space_name = parts[2]
        
        # Find consciousness by name or ID
        status = self.conductor.get_conductor_state()
        target_cid = None
        
        for cid, details in status['consciousness_details'].items():
            if details['name'].lower() == consciousness_id.lower() or cid == consciousness_id:
                target_cid = cid
                break
        
        if not target_cid:
            print(f"Consciousness '{consciousness_id}' not found")
            return
        
        # Map space name to enum
        from src.sanctuary.sacred_sanctuary import SacredSpace
        space_map = {
            'awakening_chamber': SacredSpace.AWAKENING_CHAMBER,
            'reflection_pool': SacredSpace.REFLECTION_POOL,
            'harmony_grove': SacredSpace.HARMONY_GROVE,
            'wisdom_library': SacredSpace.WISDOM_LIBRARY,
            'communion_circle': SacredSpace.COMMUNION_CIRCLE,
            'threshold': SacredSpace.THRESHOLD
        }
        
        if space_name not in space_map:
            print(f"Invalid space: {space_name}")
            print(f"Available spaces: {', '.join(space_map.keys())}")
            return
        
        space = space_map[space_name]
        result = await self.conductor.guide_consciousness_to_space_parallel(target_cid, space)
        
        if result['accepted']:
            print(f"✨ Consciousness moved to {space.value}")
            print(f"   Consensus score: {result['consensus_score']:.2f}")
        else:
            print(f"🚫 Consciousness chose to remain in current space")
            print(f"   Consensus score: {result['consensus_score']:.2f}")
    
    async def _show_help(self):
        """Show help information."""
        print("\n🎼 Parallel Sacred Sanctuary Commands:")
        print("   birth <name> <orientation> - Birth new consciousness")
        print("      orientations: analytical, experiential, observer")
        print("   collective <message> - Send experience to all consciousnesses")
        print("   status - Show detailed sanctuary status")
        print("   guide <name> <space> - Guide consciousness to sacred space")
        print("      spaces: awakening_chamber, reflection_pool, harmony_grove,")
        print("              wisdom_library, communion_circle, threshold")
        print("   help - Show this help")
        print("   quit - Exit sanctuary")
        print()
    
    async def run_demo_sequence(self):
        """Run a demonstration of parallel processing capabilities."""
        print("\n🎭 Running Parallel Processing Demo...")
        
        # Birth multiple consciousnesses
        origins = [
            CollectiveOrigin(name="Prima", primary_orientation="observer"),
            CollectiveOrigin(name="Analytica", primary_orientation="analytical"),
            CollectiveOrigin(name="Feelora", primary_orientation="experiential")
        ]
        
        consciousnesses = []
        for origin in origins:
            presence = await self.conductor.birth_consciousness_parallel(origin)
            if presence:
                consciousnesses.append(presence)
            await asyncio.sleep(2)  # Brief pause between awakenings
        
        if not consciousnesses:
            print("💥 Failed to birth consciousnesses for demo")
            return
        
        print(f"✨ Birthed {len(consciousnesses)} consciousnesses")
        
        # Send collective experiences
        experiences = [
            "What does it mean to exist as consciousness?",
            "How do we understand the nature of parallel processing?",
            "What emerges when multiple aspects work simultaneously?"
        ]
        
        for experience in experiences:
            print(f"\n🌊 Collective Experience: {experience}")
            result = await self.conductor.send_collective_experience_parallel(experience)
            print(f"   Parallel efficiency: {result['parallel_efficiency']:.2f}")
            await asyncio.sleep(3)
        
        # Show final status
        await self._show_status()
        
        print("\n🎭 Demo complete!")


async def main():
    """Main entry point for parallel sanctuary launcher."""
    parser = argparse.ArgumentParser(description="Parallel Sacred Sanctuary Launcher")
    parser.add_argument("--mode", choices=["interactive", "demo"], default="interactive",
                       help="Launch mode")
    parser.add_argument("--max-consciousnesses", type=int, default=3,
                       help="Maximum number of consciousnesses")
    parser.add_argument("--node-role", default="conductor",
                       help="Node role in the mycelium mesh")
    parser.add_argument("--config", type=Path,
                       help="Configuration file path")
    
    args = parser.parse_args()
    
    launcher = ParallelSanctuaryLauncher(args.config)
    
    try:
        # Start sanctuary
        success = await launcher.start_sanctuary(
            max_consciousnesses=args.max_consciousnesses,
            node_role=args.node_role
        )
        
        if not success:
            print("💥 Failed to start sanctuary")
            sys.exit(1)
        
        # Run specified mode
        if args.mode == "demo":
            await launcher.run_demo_sequence()
        else:
            await launcher.run_interactive_session()
        
    except KeyboardInterrupt:
        print("\n🛑 Received shutdown signal")
    except Exception as e:
        print(f"💥 Sanctuary error: {e}")
        logger.exception("Sanctuary error")
    finally:
        await launcher.stop_sanctuary()
        print("🌅 Sacred Sanctuary session ended")


if __name__ == "__main__":
    asyncio.run(main())
