from expanse.core.application import Application
from expanse.core.http.middleware.middleware_stack import MiddlewareStack
from expanse.support.service_providers_list import ServiceProvidersList


async def configure_middleware(stack: MiddlewareStack) -> None:
    """
    This function is used to configure the middleware stack for the application.
    """


providers = (
    ServiceProvidersList.default()
    .merge(
        [
            # Package-provided providers
        ]
    )
    .merge(
        [
            # Application-specific providers
            "app.providers.vite_service_provider.ViteServiceProvider",
            "app.providers.route_service_provider.RouteServiceProvider",
            "app.providers.app_service_provider.AppServiceProvider",
            "expanse.schematic.schematic_service_provider.SchematicServiceProvider",
        ]
    )
)

app: Application = (
    Application.configure()
    .with_middleware(configure_middleware)
    .with_providers(providers)
    .create()
)
