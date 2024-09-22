import pytest

from expanse.testing.client import TestClient
from expanse.testing.command_tester import CommandTester


@pytest.fixture()
def client() -> TestClient:
    from app.app import app

    return TestClient(app, raise_server_exceptions=True)


@pytest.fixture()
def command_tester() -> CommandTester:
    from app.app import app

    return CommandTester(app)
