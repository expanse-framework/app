import pytest

from expanse.testing.client import TestClient
from expanse.testing.command_tester import CommandTester


@pytest.fixture(scope="session", autouse=True)
async def bootstrap() -> None:
    """
    Bootstrap the application for testing.
    """
    from app.app import app

    await app.bootstrap()

    app.config["app.env"] = "test"


@pytest.fixture()
def client() -> TestClient:
    from app.app import app

    return TestClient(app, raise_server_exceptions=True)


@pytest.fixture()
def command_tester() -> CommandTester:
    from app.app import app

    return CommandTester(app)
