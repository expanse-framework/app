from pathlib import Path

from pydantic import Field
from pydantic import HttpUrl
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Config(BaseSettings):
    # The base URL for the static files.
    # This is useful when serving static files from a CDN.
    # Configured via the `STATIC_URL` environment variable.
    url: HttpUrl | None = None

    # The prefix for the static files.
    # Configured via the `STATIC_PREFIX` environment variable
    prefix: str = "/static"

    # The paths where the static files are located.
    # Configured via the `STATIC_PATHS` environment variable.
    paths: list[Path] = Field(default=[Path("static")])

    model_config = SettingsConfigDict(env_prefix="static_")
