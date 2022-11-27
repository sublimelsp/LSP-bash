from LSP.plugin.core.typing import Tuple
from lsp_utils import NpmClientHandler
import os


def plugin_loaded() -> None:
    LspBashPlugin.setup()


def plugin_unloaded() -> None:
    LspBashPlugin.cleanup()


class LspBashPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = "language-server"
    server_binary_path = os.path.join(
        server_directory,
        "node_modules",
        "bash-language-server",
        "bin",
        "main.js",
    )

    @classmethod
    def minimum_node_version(cls) -> Tuple[int, int, int]:
        return (12, 0, 0)
