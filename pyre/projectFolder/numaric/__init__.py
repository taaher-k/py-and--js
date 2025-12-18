# Expose functions directly when importing the package
from .operations import calculate_power, calculate_maximum,calculate_max_value

__all__ = ["calculate_power", "calculate_maximum","calculate_max_value"]
