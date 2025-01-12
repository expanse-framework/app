from expanse.routing.router import Router


def routes(router: Router) -> None:
    from app.http.controllers.welcome import WelcomeController

    router.get("/", WelcomeController.index)
