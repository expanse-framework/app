from expanse.http.response import Response
from expanse.routing.responder import Responder
from expanse.routing.router import Router


def welcome(responder: Responder) -> Response:
    from expanse import __version__

    return responder.json({"message": "Welcome to Expanse!", "version": __version__})


def routes(router: Router) -> None:
    with router.group("api", prefix="/api") as group:
        group.get("/welcome", welcome)
