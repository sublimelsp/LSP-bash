import sublime_plugin
from .code_actions import CodeActionsOnFormatOnSaveTask as CodeActionsOnFormatOnSaveTask, CodeActionsOnSaveTask as CodeActionsOnSaveTask
from .formatting import FormatOnSaveTask as FormatOnSaveTask, WillSaveWaitTask as WillSaveWaitTask
from .lsp_task import LspTask as LspTask, LspTextCommandWithTasks as LspTextCommandWithTasks
from typing import Any

class LspSaveCommand(LspTextCommandWithTasks):
    """
    A command used as a substitute for native save command. Runs code actions and document
    formatting before triggering the native save command.
    """
    @property
    def tasks(self) -> list[type[LspTask]]: ...
    def on_before_tasks(self) -> None: ...
    def on_tasks_completed(self, **kwargs: dict[str, Any]) -> None: ...
    def _trigger_on_pre_save_async(self) -> None: ...

class LspSaveAllCommand(sublime_plugin.WindowCommand):
    def run(self, only_files: bool = False) -> None: ...
