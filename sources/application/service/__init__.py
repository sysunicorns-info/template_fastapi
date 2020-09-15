from dependency_injector import containers, providers

from application.container import ApplicationContainer, application_container_proxy
from .monitor import MonitorService


class ServiceContainer(containers.DynamicContainer):
    monitor_service: MonitorService=providers.Singleton(MonitorService)

class ServiceContainerProxy():

    service_container: ServiceContainer = None

    def factory(self) -> None:
        self.service_container = ServiceContainer()
        self.service_container.monitor_service = providers.Singleton(
            MonitorService,
            database=application_container_proxy().database()
        )

    def __call__(self) -> ServiceContainer:
        return self.service_container

    def monitor_service(self) -> MonitorService:
        return self.service_container.monitor_service()

service_container_proxy = ServiceContainerProxy()
