from dependency_injector import containers, providers

from .config import Config
from .database import Database


class ApplicationContainer(containers.DeclarativeContainer):
    database: Database = providers.Singleton(Database)


class ApplicationContainerProxy():

    application_container: ApplicationContainer = None

    def factory(self, config: Config):
        self.application_container = ApplicationContainer(
            database=Database(
                dsn=Database.dsn(
                    host=config.db_host,
                    user=config.db_user,
                    pwd=config.db_pwd,
                    name=config.db_name
                ),
                application_name=config.application_name
            )
        )
        return self.application_container

    def set(self, application_container: ApplicationContainer):
        self.application_container = application_container

    def __call__(self) -> ApplicationContainer:
        return self.application_container


application_container_proxy = ApplicationContainerProxy()
