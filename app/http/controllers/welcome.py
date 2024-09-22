import sys

import expanse

from expanse.routing.responder import Responder


class WelcomeController:
    def index(self, responder: Responder):
        return responder.view(
            "welcome",
            {
                "expanse_version": expanse.__version__,
                "python_version": ".".join(str(v) for v in sys.version_info[:3]),
            },
        )