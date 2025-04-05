from expanse.contracts.routing.registrar import Registrar
from expanse.http.response import Response
from expanse.routing.responder import Responder


def welcome(responder: Responder) -> Response:
    from expanse import __version__

    return responder.json({"message": "Welcome to Expanse!", "version": __version__})


def routes(router: Registrar) -> None:
    router.get("/welcome", welcome)
