from __future__ import annotations

from .client import LspBashPlugin

__all__ = (
    # ST: core
    "plugin_loaded",
    "plugin_unloaded",
    # ST: commands
    # ST: listeners
    # ...
    "LspBashPlugin",
)


def plugin_loaded() -> None:
    """Executed when this plugin is loaded."""
    LspBashPlugin.setup()


def plugin_unloaded() -> None:
    """Executed when this plugin is unloaded."""
    LspBashPlugin.cleanup()
