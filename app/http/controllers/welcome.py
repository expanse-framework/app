import sys

import expanse

from expanse.http.helpers import view
from expanse.http.response import Response
from expanse.routing.helpers import get


class WelcomeController:
    @get("/")
    def index(self) -> Response:
        return view(
            "welcome",
            data={
                "expanse_version": expanse.__version__,
                "python_version": ".".join(str(v) for v in sys.version_info[:3]),
            },
        )
