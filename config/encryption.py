from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Config(BaseSettings):
    # The cipher method used for encryption. Currently, only aes-256-gcm is supported.
    # Configured via the `ENCRYPTION_CIPHER` environment variable.
    cipher: str = "aes-256-gcm"

    model_config = SettingsConfigDict(env_prefix="encryption_")
