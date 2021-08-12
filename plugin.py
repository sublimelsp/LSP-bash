from lsp_utils import NpmClientHandler
import os


def plugin_loaded():
    LspBashPlugin.setup()


def plugin_unloaded():
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
