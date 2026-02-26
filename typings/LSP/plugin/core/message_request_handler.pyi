import sublime
from ...protocol import MessageActionItem as MessageActionItem, MessageType, ShowMessageRequestParams as ShowMessageRequestParams
from .promise import PackagedTask as PackagedTask, Promise as Promise, ResolveFunc as ResolveFunc
from .views import show_lsp_popup as show_lsp_popup, text2html as text2html
from _typeshed import Incomplete

ICONS: dict[MessageType, str]

class MessageRequestHandler:
    view: Incomplete
    actions: Incomplete
    action_titles: Incomplete
    message: Incomplete
    message_type: Incomplete
    source: Incomplete
    _response_handled: bool
    def __init__(self, view: sublime.View, params: ShowMessageRequestParams, source: str) -> None: ...
    def show(self) -> Promise[MessageActionItem | None]: ...
    def _send_user_choice(self, resolve: ResolveFunc[MessageActionItem | None], href: int = -1) -> None: ...
