from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from expanse.support.service_providers_list import ServiceProvidersList


class Config(BaseSettings):
    # The name of the application.
    # Configured with the `APP_NAME` environment variable.
    name: str = "Expanse"

    # Application environment
    #
    # The environment the application is running in.
    # Configured with the `APP_ENV` environment variable.
    env: str = "production"

    # Debug mode
    #
    # The debug mode mostly controls how the application behaves when an error
    # occurs. When debug mode is enabled, the application will display detailed
    # messages about the error, including a stack trace. When debug mode is disabled,
    # the application will display a generic error message instead.
    # Configured with the `APP_DEBUG` environment variable.
    debug: bool = False

    # Encryption key
    #
    # This key is used by the application for encryption and should be set
    # to a random, 32-character string or a base64-encoded 32 bytes prefixed with `base64:`.
    # This must be set prior to deploying the application.
    # Configured with the `APP_SECRET_KEY` environment variable.
    secret_key: str = ""

    # Service providers
    #
    # You can list here the service providers that you want to register automatically
    # in your application.
    providers: list[str] = Field(
        default=(
            ServiceProvidersList.default()
            .merge(
                [
                    # Package-provided providers
                ]
            )
            .merge(
                [
                    # Application service providers
                    "app.providers.app_service_provider.AppServiceProvider",
                    "app.providers.route_service_provider.RouteServiceProvider",
                ]
            )
            .to_list()
        )
    )

    model_config = SettingsConfigDict(env_prefix="app_")
