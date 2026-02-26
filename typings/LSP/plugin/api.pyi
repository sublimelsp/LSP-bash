from ..protocol import LSPAny
from .core.promise import Promise
from .core.protocol import Response
from typing import Any, Callable, TypeVar

__all__ = ['APIHandler', 'notification_handler', 'request_handler']

P = TypeVar('P', bound=LSPAny)
R = TypeVar('R', bound=LSPAny)

class APIHandler:
    """Trigger initialization of decorated API methods."""
    def __init__(self) -> None: ...

def notification_handler(method: str) -> Callable[[Callable[[Any, P], None]], Callable[[Any, P], None]]:
    """Decorator to mark a method as a handler for a specific LSP notification.

    Usage:
        ```py
        @notification_handler('eslint/status')
        def on_eslint_status(self, params: str) -> None:
            ...
        ```

    The decorated method will be called with the notification parameters whenever the specified
    notification is received from the language server. Notification handlers do not return a value.

    :param      method:             The LSP notification method name (e.g., 'eslint/status').
    :returns:   A decorator that registers the function as a notification handler.
    """
def request_handler(method: str) -> Callable[[Callable[[Any, P], Promise[R]]], Callable[[Any, P, int], Promise[Response[R]]]]:
    """Decorator to mark a method as a handler for a specific LSP request.

    Usage:
        ```py
        @request_handler('eslint/openDoc')
        def on_open_doc(self, params: TextDocumentIdentifier) -> Promise[bool]:
            ...
        ```

    The decorated method will be called with the request parameters whenever the specified
    request is received from the language server. The method must return a Promise that resolves
    to the response value. The framework will automatically send it back to the server.

    :param      method:             The LSP request method name (e.g., 'eslint/openDoc').
    :returns:   A decorator that registers the function as a request handler.
    """
