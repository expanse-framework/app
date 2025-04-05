from expanse.contracts.routing.router import Router
from expanse.core.application import Application
from expanse.support.service_provider import ServiceProvider


class RouteServiceProvider(ServiceProvider):
    async def boot(self, router: Router, application: Application) -> None:
        with router.group("api", prefix="/api") as api:
            api.middleware("api").load_file(application.path("routes/api.py"))

        with router.group() as web:
            web.middleware("web").load_file(application.path("routes/web.py"))
