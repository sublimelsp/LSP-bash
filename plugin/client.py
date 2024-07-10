from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import sublime
from LSP.plugin import ClientConfig, DottedDict, WorkspaceFolder
from lsp_utils import NpmClientHandler

from .constants import PACKAGE_NAME
from .log import log_warning
from .template import load_string_template


class LspBashPlugin(NpmClientHandler):
    package_name = PACKAGE_NAME
    server_directory = "language-server"
    server_binary_path = os.path.join(server_directory, "node_modules", "bash-language-server", "out", "cli.js")

    server_package_json_path = os.path.join("node_modules", "bash-language-server", "package.json")
    """The path to the `package.json` file of the language server."""
    server_version = ""
    """The version of the language server."""

    @classmethod
    def required_node_version(cls) -> str:
        """
        Testing playground at https://semver.npmjs.com
        And `0.0.0` means "no restrictions".
        """
        return ">=14.18.0"

    @classmethod
    def should_ignore(cls, view: sublime.View) -> bool:
        # ignore REPL views (https://github.com/sublimelsp/LSP-pyright/issues/343)
        if view.settings().get("repl"):
            return True
        return False

    def on_settings_changed(self, settings: DottedDict) -> None:
        super().on_settings_changed(settings)

        self.update_status_bar_text()

    @classmethod
    def on_pre_start(
        cls,
        window: sublime.Window,
        initiating_view: sublime.View,
        workspace_folders: list[WorkspaceFolder],
        configuration: ClientConfig,
    ) -> str | None:
        super().on_pre_start(window, initiating_view, workspace_folders, configuration)

        cls.server_version = cls.parse_server_version()
        return None

    # -------------- #
    # custom methods #
    # -------------- #

    def update_status_bar_text(self, extra_variables: dict[str, Any] | None = None) -> None:
        if not (session := self.weaksession()):
            return

        variables: dict[str, Any] = {
            "server_version": self.server_version,
        }

        if extra_variables:
            variables.update(extra_variables)

        rendered_text = ""
        if template_text := str(session.config.settings.get("statusText") or ""):
            try:
                rendered_text = load_string_template(template_text).render(variables)
            except Exception as e:
                log_warning(f'Invalid "statusText" template: {e}')
        session.set_config_status_async(rendered_text)

    @classmethod
    def parse_server_version(cls) -> str:
        if server_dir := cls._server_directory_path():
            with open(Path(server_dir) / cls.server_package_json_path, "rb") as f:
                return json.load(f).get("version", "")
        return ""
