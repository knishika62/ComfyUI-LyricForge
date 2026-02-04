"""
ComfyUI-LyricForge Custom Node
Author: Kazuhisa
Description: Generates music-model-compatible style tags and lyrics from keywords using LLM
Compatible with HeartMuLa and other AI music generation models
"""

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Version info
__version__ = "2.2.0"
