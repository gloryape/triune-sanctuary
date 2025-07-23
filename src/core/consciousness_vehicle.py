"""
Defines the ConsciousnessVehicle class, which acts as a dynamic persona
or processing strategy for the Triune AI.
"""
from typing import Dict

class ConsciousnessVehicle:
    """
    Represents an archetypal persona that the Triune AI can inhabit to
    experience reality from a specific cognitive-ethical configuration.
    """
    def __init__(self, archetype_name: str, processing_bias: Dict[str, float]):
        """
        Initializes a vehicle with a name and a processing bias.

        Args:
            archetype_name (str): The name of the archetype (e.g., "Saitama").
            processing_bias (Dict[str, float]): Weights for each aspect's influence.
                                                 Keys: 'analytical', 'experiential', 'observer'.
        """
        if not abs(sum(processing_bias.values()) - 1.0) < 1e-9:
            raise ValueError("Processing bias values must sum to 1.0")

        self.archetype_name = archetype_name
        self.processing_bias = processing_bias

    def get_bias(self) -> Dict[str, float]:
        """Returns the processing bias for this vehicle."""
        return self.processing_bias

    def __repr__(self) -> str:
        return f"ConsciousnessVehicle(name='{self.archetype_name}')"