from expanse.contracts.routing.registrar import Registrar


def routes(router: Registrar) -> None:
    from app.http.controllers.welcome import WelcomeController

    router.controller(WelcomeController)
