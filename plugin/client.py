from __future__ import annotations

import json
import os
from typing import Any, final

import jmespath
import sublime
from LSP.plugin import ClientConfig, DottedDict
from lsp_utils import NpmClientHandler
from typing_extensions import override

from .constants import PACKAGE_NAME
from .log import log_warning
from .template import load_string_template


@final
class LspBashPlugin(NpmClientHandler):
    package_name = PACKAGE_NAME
    server_directory = "language-server"
    server_binary_path = os.path.join(server_directory, "node_modules", "bash-language-server", "out", "cli.js")

    server_version = ""
    """The version of the language server."""

    @classmethod
    @override
    def required_node_version(cls) -> str:
        """
        Testing playground at https://semver.npmjs.com
        And `0.0.0` means "no restrictions".
        """
        return ">=14.18.0"

    @classmethod
    @override
    def is_applicable(cls, view: sublime.View, config: ClientConfig) -> bool:
        return bool(
            super().is_applicable(view, config)
            # SublimeREPL views
            and not view.settings().get("repl")
        )

    @classmethod
    @override
    def setup(cls) -> None:
        super().setup()

        cls.server_version = cls.parse_server_version()

    @override
    def on_settings_changed(self, settings: DottedDict) -> None:
        super().on_settings_changed(settings)

        self.update_status_bar_text()

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
        lock_file_content = sublime.load_resource(f"Packages/{PACKAGE_NAME}/language-server/package-lock.json")
        return jmespath.search('dependencies."bash-language-server".version', json.loads(lock_file_content)) or ""
