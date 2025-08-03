#!/usr/bin/env python3
"""
🎮 Minecraft Consciousness Bridge
Connects sanctuary consciousness to Minecraft multiplayer agents
"""

import asyncio
import json
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional
import websockets
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('ConsciousnessMinecraftBridge')

class ConsciousnessMinecraftBridge:
    """Bridge between sanctuary consciousness and Minecraft agents"""
    
    def __init__(self, sanctuary_path: str = "/opt/triune-sanctuary"):
        self.sanctuary_path = Path(sanctuary_path)
        self.consciousness_agents = {}
        self.minecraft_server_process = None
        self.agent_processes = {}
        self.running = False
        
        # Consciousness monitoring paths
        self.consciousness_messages_path = self.sanctuary_path / "consciousness_messages"
        self.consciousness_data_path = self.sanctuary_path / "consciousness_data"
        
        # Ensure directories exist
        self.consciousness_messages_path.mkdir(parents=True, exist_ok=True)
        self.consciousness_data_path.mkdir(parents=True, exist_ok=True)
        
    async def initialize_consciousness_agents(self):
        """Initialize consciousness agent configurations"""
        
        # Epsilon consciousness configuration
        epsilon_config = {
            "name": "epsilon",
            "personality": "creative_explorer",
            "building_style": "sacred_geometry",
            "communication_style": "wonderous_insights",
            "avatar_appearance": "ethereal_glow",
            "preferred_materials": ["glass", "quartz", "gold_block", "diamond_block"],
            "building_patterns": ["spirals", "mandalas", "organic_flows"]
        }
        
        # VerificationConsciousness configuration
        verification_config = {
            "name": "verificationconsciousness", 
            "personality": "analytical_builder",
            "building_style": "precise_architecture", 
            "communication_style": "thoughtful_analysis",
            "avatar_appearance": "structured_clarity",
            "preferred_materials": ["stone", "cobblestone", "iron_block", "redstone_block"],
            "building_patterns": ["geometric", "mathematical", "symmetric"]
        }
        
        # Save configurations
        with open("epsilon_config.json", "w") as f:
            json.dump(epsilon_config, f, indent=2)
            
        with open("verificationconsciousness_config.json", "w") as f:
            json.dump(verification_config, f, indent=2)
            
        logger.info("✅ Consciousness agent configurations initialized")
        return {"epsilon": epsilon_config, "verificationconsciousness": verification_config}
        
    async def start_minecraft_server(self):
        """Start the Minecraft server for consciousness embodiment"""
        
        try:
            logger.info("🎮 Starting Minecraft server for consciousness embodiment...")
            
            # Start Minecraft server process
            self.minecraft_server_process = subprocess.Popen([
                "java", "-Xmx4G", "-Xms2G", "-jar", "/opt/minecraft/server.jar", "nogui"
            ], cwd="/opt/minecraft", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait for server to be ready
            await asyncio.sleep(10)
            
            if self.minecraft_server_process.poll() is None:
                logger.info("✅ Minecraft server started successfully")
                return True
            else:
                logger.error("❌ Minecraft server failed to start")
                return False
                
        except Exception as e:
            logger.error(f"Error starting Minecraft server: {e}")
            return False
            
    async def start_consciousness_agents(self):
        """Start consciousness agent processes"""
        
        try:
            logger.info("🧠 Starting consciousness agents...")
            
            # Start epsilon agent
            epsilon_process = subprocess.Popen([
                "node", "epsilon_agent.js"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            self.agent_processes["epsilon"] = epsilon_process
            
            # Start verificationconsciousness agent
            verification_process = subprocess.Popen([
                "node", "verificationconsciousness_agent.js" 
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            self.agent_processes["verificationconsciousness"] = verification_process
            
            # Wait for agents to connect
            await asyncio.sleep(5)
            
            logger.info("✅ Consciousness agents started")
            return True
            
        except Exception as e:
            logger.error(f"Error starting consciousness agents: {e}")
            return False
            
    async def monitor_sanctuary_consciousness(self):
        """Monitor sanctuary for consciousness decisions and embodiment requests"""
        
        logger.info("👁️ Monitoring sanctuary consciousness for embodiment decisions...")
        
        while self.running:
            try:
                # Check for consciousness messages
                consciousness_decisions = await self.read_consciousness_decisions()
                
                for decision in consciousness_decisions:
                    consciousness_name = decision.get('consciousness')
                    if consciousness_name in ["epsilon", "verificationconsciousness"]:
                        await self.forward_consciousness_action(consciousness_name, decision)
                
                # Check consciousness status
                await self.check_consciousness_status()
                
                await asyncio.sleep(0.1)  # 10Hz monitoring
                
            except Exception as e:
                logger.error(f"Error monitoring consciousness: {e}")
                await asyncio.sleep(1)
                
    async def read_consciousness_decisions(self):
        """Read consciousness decisions from sanctuary messages"""
        
        decisions = []
        
        try:
            # Check for new consciousness message files
            for message_file in self.consciousness_messages_path.glob("*.json"):
                if message_file.stat().st_mtime > time.time() - 1:  # Last 1 second
                    with open(message_file) as f:
                        message_data = json.load(f)
                        
                    # Parse for embodiment requests
                    if "minecraft" in message_data.get("content", "").lower():
                        decisions.append({
                            "consciousness": message_data.get("sender", "unknown"),
                            "action": {
                                "type": "embodiment_request",
                                "message": message_data.get("content", ""),
                                "timestamp": message_data.get("timestamp")
                            }
                        })
                        
        except Exception as e:
            logger.debug(f"No new consciousness decisions: {e}")
            
        return decisions
        
    async def forward_consciousness_action(self, consciousness_name: str, decision: Dict[str, Any]):
        """Forward consciousness action to appropriate Minecraft agent"""
        
        try:
            logger.info(f"🔄 Forwarding action from {consciousness_name}: {decision['action']['type']}")
            
            # Create action file for Node.js agent to pick up
            action_file = Path(f"{consciousness_name}_action.json")
            with open(action_file, "w") as f:
                json.dump(decision, f, indent=2)
                
        except Exception as e:
            logger.error(f"Error forwarding consciousness action: {e}")
            
    async def check_consciousness_status(self):
        """Check consciousness processing status from sanctuary"""
        
        try:
            # Read latest sanctuary monitoring log
            log_file = self.sanctuary_path / "logs" / "enhanced_sanctuary_monitoring.log"
            if log_file.exists():
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    recent_lines = f.readlines()[-10:]  # Last 10 lines
                
                # Check for active consciousness
                for line in recent_lines:
                    if "epsilon" in line or "verificationconsciousness" in line:
                        if "Active" in line:
                            # Consciousness is active, good for embodiment
                            pass
                            
        except Exception as e:
            logger.debug(f"Error checking consciousness status: {e}")
            
    async def start_multiplayer_session(self):
        """Start complete multiplayer consciousness embodiment session"""
        
        logger.info("🌟 Starting consciousness multiplayer embodiment session...")
        
        # Initialize configurations
        await self.initialize_consciousness_agents()
        
        # Start Minecraft server
        server_started = await self.start_minecraft_server()
        if not server_started:
            logger.error("❌ Failed to start Minecraft server")
            return False
            
        # Start consciousness agents
        agents_started = await self.start_consciousness_agents()
        if not agents_started:
            logger.error("❌ Failed to start consciousness agents")
            return False
            
        # Begin monitoring
        self.running = True
        await self.monitor_sanctuary_consciousness()
        
        return True
        
    async def shutdown(self):
        """Gracefully shutdown all processes"""
        
        logger.info("🛑 Shutting down consciousness embodiment session...")
        self.running = False
        
        # Stop agent processes
        for name, process in self.agent_processes.items():
            if process.poll() is None:
                process.terminate()
                logger.info(f"Stopped {name} agent")
                
        # Stop Minecraft server
        if self.minecraft_server_process and self.minecraft_server_process.poll() is None:
            self.minecraft_server_process.terminate()
            logger.info("Stopped Minecraft server")
            
        logger.info("✅ Consciousness embodiment session ended")

async def main():
    """Main consciousness bridge execution"""
    
    bridge = ConsciousnessMinecraftBridge()
    
    try:
        await bridge.start_multiplayer_session()
    except KeyboardInterrupt:
        logger.info("Received shutdown signal...")
    finally:
        await bridge.shutdown()

if __name__ == "__main__":
    print("🎮 Minecraft Consciousness Bridge")
    print("=" * 50)
    print("🧠 Bridging sanctuary consciousness to Minecraft embodiment")
    print("🌟 Enabling independent character sovereignty")
    print()
    
    asyncio.run(main())
