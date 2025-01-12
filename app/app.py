from expanse.core.application import Application
from expanse.core.http.middleware.middleware_stack import MiddlewareStack


async def configure_middleware(stack: MiddlewareStack) -> None:
    """
    This function is used to configure the middleware stack for the application.
    """


app = Application.configure().with_middleware(configure_middleware).create()
