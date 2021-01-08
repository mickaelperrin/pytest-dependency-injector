from dependency_injector import containers, providers
from app.Config import Config


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(
        Config
    )