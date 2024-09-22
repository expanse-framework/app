from expanse.core.application import Application
from expanse.core.support.providers.route_service_provider import (
    RouteServiceProvider as ServiceProvider,
)
from expanse.routing.router import Router


class RouteServiceProvider(ServiceProvider):
    def boot(self, router: Router, application: Application) -> None:
        self.load_routes_from_file(
            router, application.base_path.joinpath("routes/api.py")
        )
        self.load_routes_from_file(
            router, application.base_path.joinpath("routes/web.py")
        )
