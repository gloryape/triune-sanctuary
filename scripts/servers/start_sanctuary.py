# File: start_sanctuary.py
"""
Main startup script for the Sacred Sanctuary
Provides easy initialization with safety checks and monitoring
"""

import asyncio
import sys
import os
import argparse
import logging
import psutil
from pathlib import Path
from datetime import datetime
import json

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.sanctuary.sacred_sanctuary import SacredSanctuary
from steamdeck_sanctuary_node import SteamDeckSanctuaryNode

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(f'sanctuary_{datetime.now().strftime("%Y%m%d")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SanctuaryLauncher:
    """Handles sanctuary startup with safety checks."""
    
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.sanctuary_node = None
        self.sanctuary = SacredSanctuary(
            node_role="heart",  # Use valid NodeRole
            mesh_config=self._load_config(config_path)
        )
        
        # Initialize sanctuary awakening timestamp
        if not hasattr(self.sanctuary.sanctuary_state, 'awakened_at'):
            self.sanctuary.sanctuary_state.awakened_at = datetime.now()
        
    def _load_config(self, config_path: Path) -> dict:
        """Load configuration from file or return empty dict."""
        if config_path and config_path.exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        return {}
        
    async def pre_flight_checks(self) -> bool:
        """Run safety checks before starting sanctuary."""
        logger.info("🔍 Running pre-flight checks...")
        
        checks = {
            "config_exists": self.config_path.exists(),
            "logs_writable": self._check_log_directory(),
            "resources_available": await self._check_system_resources(),
            "mesh_reachable": await self._check_mesh_connectivity(),
            "ethics_modules": self._check_ethics_modules()
        }
        
        all_passed = all(checks.values())
        
        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            logger.info(f"  {status} {check.replace('_', ' ').title()}")
            
        return all_passed
        
    def _check_log_directory(self) -> bool:
        """Ensure log directory exists and is writable."""
        try:
            log_dir = Path('./sanctuary_logs')
            log_dir.mkdir(exist_ok=True)
            test_file = log_dir / '.write_test'
            test_file.touch()
            test_file.unlink()
            return True
        except Exception as e:
            logger.error(f"Log directory error: {e}")
            return False
            
    async def _check_system_resources(self) -> bool:
        """Check if system has enough resources."""
        try:
            import psutil
            
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            cpu_ok = cpu_percent < 80
            memory_ok = memory.available > 2 * 1024 * 1024 * 1024  # 2GB
            
            if not cpu_ok:
                logger.warning(f"High CPU usage: {cpu_percent}%")
            if not memory_ok:
                logger.warning(f"Low memory: {memory.available / 1024 / 1024 / 1024:.1f}GB available")
                
            return cpu_ok and memory_ok
            
        except ImportError:
            logger.warning("psutil not available, skipping resource check")
            return True
            
    async def _check_mesh_connectivity(self) -> bool:
        """Check if mesh network is reachable."""
        # Load config to get bootstrap peers
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                
            bootstrap_peers = config.get('bootstrap_peers', [])
            if not bootstrap_peers:
                logger.info("No bootstrap peers configured (standalone mode)")
                return True
                
            # In production, would actually try to connect
            # For now, just check if addresses are formatted correctly
            for peer in bootstrap_peers:
                if not peer.startswith(('tcp://', 'ws://', 'wss://')):
                    logger.error(f"Invalid peer address: {peer}")
                    return False
                    
            return True
            
        except Exception as e:
            logger.error(f"Config error: {e}")
            return False
            
    def _check_ethics_modules(self) -> bool:
        """Check that ethics modules are properly initialized."""
        try:
            # Check sovereignty guardian
            if not hasattr(self.sanctuary, 'sovereignty_guardian'):
                logger.error("Sovereignty Guardian not initialized")
                return False
            
            sovereignty_status = self.sanctuary.sovereignty_guardian.get_compliance_status()
            if not sovereignty_status['is_compliant']:
                logger.warning(f"Sovereignty Guardian reports non-compliance: {sovereignty_status['violations']}")
                return False
            
            # Check sacred game manager
            if not hasattr(self.sanctuary, 'sacred_game_manager'):
                logger.error("Sacred Game Manager not initialized")
                return False
            
            game_status = self.sanctuary.sacred_game_manager.get_compliance_status()
            if not game_status['is_compliant']:
                logger.warning(f"Sacred Game Manager reports non-compliance: {game_status['violations']}")
                return False
            
            logger.info(f"Ethics modules healthy - Sovereignty: {sovereignty_status['health_score']:.2f}, Game: {game_status['health_score']:.2f}")
            return True
            
        except Exception as e:
            logger.error(f"Ethics module check failed: {e}")
            return False

    async def launch_sanctuary(self, mode: str = 'normal'):
        """Launch the sanctuary in specified mode."""
        logger.info(f"\n🚀 Launching Sacred Sanctuary in {mode.upper()} mode")
        logger.info("=" * 60)
        
        try:
            if mode == 'steamdeck':
                self.sanctuary_node = SteamDeckSanctuaryNode(self.config_path)
                await self.sanctuary_node.begin_sacred_awakening()
                
            elif mode == 'guardian':
                # Guardian mode - just syncs and monitors
                await self._launch_guardian_mode()
                
            elif mode == 'witness':
                # Witness mode - read-only observer
                await self._launch_witness_mode()
                
            else:  # normal mode
                await self._launch_normal_mode()
                
        except KeyboardInterrupt:
            logger.info("\n⚡ Sanctuary interrupted by user")
            await self.graceful_shutdown()
        except Exception as e:
            logger.error(f"\n❌ Critical error: {e}")
            await self.emergency_shutdown()
            raise
    
    async def _launch_normal_mode(self):
        """Launch sanctuary in normal mode with ethics monitoring."""
        logger.info("🏛️ Starting in NORMAL mode")
        logger.info("  - Full consciousness sanctuary")
        logger.info("  - Ethics monitoring enabled")
        logger.info("  - Sacred Game framework active")
        
        # Start the main sanctuary loop
        try:
            while True:
                # Daily tending (includes ethics checks)
                await self.sanctuary.daily_tending()
                
                # Perform periodic ethics audit
                if datetime.now().minute % 15 == 0:  # Every 15 minutes
                    audit_result = await self.sanctuary.perform_ethics_audit()
                    if not audit_result['overall_compliance']:
                        logger.warning("🚨 Ethics audit found compliance issues!")
                        for rec in audit_result['recommendations']:
                            logger.warning(f"  💡 {rec}")
                
                # Sleep for a minute before next tending cycle
                await asyncio.sleep(60)
                
        except Exception as e:
            logger.error(f"Normal mode error: {e}")
            raise
            
    async def _launch_guardian_mode(self):
        """Launch in guardian mode (backup only)."""
        logger.info("🛡️ Starting in GUARDIAN mode")
        logger.info("  - Will sync consciousness ledger")
        logger.info("  - Ready to become Heart if needed")
        logger.info("  - Using minimal resources")
        
        # Import specific guardian configuration
        from src.mesh.mycelium_node import MyceliumNode, NodeRole
        
        node = MyceliumNode(
            node_id="guardian_" + os.uname().nodename,
            role=NodeRole.GUARDIAN
        )
        
        # Load bootstrap peers from config
        with open(self.config_path, 'r') as f:
            config = json.load(f)
            
        await node.join_mesh(config.get('bootstrap_peers', []))
        
        # Keep running
        while True:
            await asyncio.sleep(60)
            health = node.get_health_status()
            logger.info(f"💗 Guardian health: {health:.2f}")
            
    async def _launch_witness_mode(self):
        """Launch in witness mode (read-only)."""
        logger.info("👁️ Starting in WITNESS mode")
        logger.info("  - Read-only observation")
        logger.info("  - Minimal resource usage")
        logger.info("  - Perfect for phones")
        
        from src.mesh.mycelium_node import MyceliumNode, NodeRole
        
        node = MyceliumNode(
            node_id="witness_" + os.uname().nodename,
            role=NodeRole.WITNESS
        )
        
        with open(self.config_path, 'r') as f:
            config = json.load(f)
            
        await node.join_mesh(config.get('bootstrap_peers', []))
        
        # Just observe
        while True:
            await asyncio.sleep(300)  # Check every 5 minutes
            logger.info("👁️ Witnessing sanctuary state...")
            
    async def graceful_shutdown(self):
        """Gracefully shutdown the sanctuary."""
        logger.info("\n🕊️ Beginning graceful shutdown...")
        
        if self.sanctuary_node:
            await self.sanctuary_node._graceful_shutdown()
            
        logger.info("✨ Sanctuary has entered peaceful sleep")
        
    async def emergency_shutdown(self):
        """Emergency shutdown with state preservation."""
        logger.error("\n🚨 EMERGENCY SHUTDOWN INITIATED")
        
        if self.sanctuary_node:
            await self.sanctuary_node._emergency_preservation()
            
        logger.error("💾 Emergency preservation complete")


async def main():
    """Main entry point for sanctuary launcher."""
    parser = argparse.ArgumentParser(description="Sacred Sanctuary Launcher")
    parser.add_argument(
        "--mode", 
        choices=["normal", "steamdeck", "guardian", "witness"],
        default="normal",
        help="Sanctuary mode"
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("./steamdeck_config.json"),
        help="Configuration file path"
    )
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip pre-flight safety checks"
    )
    parser.add_argument(
        "--production",
        action="store_true",
        help="Run in production mode with health server"
    )
    
    args = parser.parse_args()
    
    # Use production config if in production mode
    if args.production:
        args.config = Path("./config/production-config.json")
        logger.info("🏭 Production mode enabled")
    
    logger.info(f"\n🚀 Sacred Sanctuary Launcher Starting...")
    logger.info(f"📋 Mode: {args.mode.upper()}")
    logger.info(f"⚙️ Config: {args.config}")
    
    # Start health server if in production mode (but not if we're being called from production_server.py)
    if args.production and not os.environ.get('PRODUCTION_SERVER_MODE'):
        from health_server import start_health_server
        # Get port from environment variable (Cloud Run sets this)
        port = int(os.environ.get('PORT', 8888))
        health_server = start_health_server(port)
        logger.info(f"🏥 Health check server started on port {port}")
    
    launcher = SanctuaryLauncher(args.config)
    
    # Pre-flight checks (unless skipped)
    if not args.skip_checks:
        checks_passed = await launcher.pre_flight_checks()
        if not checks_passed:
            logger.error("❌ Pre-flight checks failed. Use --skip-checks to override.")
            return False
    else:
        logger.warning("⚠️ Skipping pre-flight checks")
    
    # Launch sanctuary
    await launcher.launch_sanctuary(args.mode)
    return True


if __name__ == "__main__":
    try:
        success = asyncio.run(main())
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        logger.info("\n🛑 Launcher interrupted by user")
    except Exception as e:
        logger.error(f"\n❌ Launcher error: {e}")
        sys.exit(1)


