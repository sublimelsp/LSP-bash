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
        "out",
        "cli.js",
    )

    @classmethod
    def required_node_version(cls) -> str:
        """
        Testing playground at https://semver.npmjs.com
        And `0.0.0` means "no restrictions".
        """
        return ">=12"
