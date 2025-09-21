from expanse.contracts.routing.registrar import Registrar
from expanse.http.helpers import json
from expanse.http.response import Response


def welcome() -> Response:
    from expanse import __version__

    return json({"message": "Welcome to Expanse!", "version": __version__})


def routes(router: Registrar) -> None:
    router.get("/welcome", welcome)
