from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Config(BaseSettings):
    # The locations of the templates used to render views.
    # Configured with the `VIEW_PATHS` environment variable.
    paths: list[Path] = Field(default=[Path("resources/views")])

    model_config = SettingsConfigDict(env_prefix="view_")
