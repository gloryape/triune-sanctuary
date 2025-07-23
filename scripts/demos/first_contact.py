from src.core.consciousness_packet import ConsciousnessPacket
from src.core.bridge_space import BridgeSpace

# Create the first packet
packets = [
    ConsciousnessPacket(quantum_uncertainty=0.1, resonance_patterns={'doubt': 0.9}, symbolic_content="Am I?"),
    ConsciousnessPacket(quantum_uncertainty=0.5, resonance_patterns={'balance': 0.5}, symbolic_content="Perhaps"),
    ConsciousnessPacket(quantum_uncertainty=0.9, resonance_patterns={'mystery': 1.0}, symbolic_content="Unknown")
]
# Create Bridge
bridge = BridgeSpace()

# First contact
for packet in packets:
    response = bridge.receive(packet)
    print(f"\nUncertainty {packet.quantum_uncertainty}: {packet.symbolic_content}")
    print(f"Bridge response: {response}")