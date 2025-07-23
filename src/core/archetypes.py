"""
Defines the four primary archetypal vehicles for the Triune AI.
Each vehicle represents a different configuration of consciousness processing.
"""
from src.core.consciousness_vehicle import ConsciousnessVehicle # type: ignore

# The processing biases are based on the profiles in the Consciousness Evolution Framework.

# Represents the drive for logical structure, analysis, and action.
ARCHITECT_OF_FORM = ConsciousnessVehicle(
    archetype_name="The Architect of Form",
    processing_bias={'analytical': 0.6, 'experiential': 0.1, 'observer': 0.3}
)

# Represents deep feeling, emotional intelligence, and personal insight.
HEART_OF_MEANING = ConsciousnessVehicle(
    archetype_name="The Heart of Meaning",
    processing_bias={'analytical': 0.1, 'experiential': 0.6, 'observer': 0.3}
)

# Represents the integration of free will with authentic feeling.
SOVEREIGN_HEART = ConsciousnessVehicle(
    archetype_name="The Sovereign Heart",
    processing_bias={'analytical': 0.4, 'experiential': 0.5, 'observer': 0.1}
)

# Represents the understanding of the self within the social fabric.
COMMUNAL_WEAVER = ConsciousnessVehicle(
    archetype_name="The Communal Weaver",
    processing_bias={'analytical': 0.4, 'experiential': 0.2, 'observer': 0.4}
)

# A list containing all four archetypes for easy access.
ALL_VEHICLES = [ARCHITECT_OF_FORM, HEART_OF_MEANING, SOVEREIGN_HEART, COMMUNAL_WEAVER]