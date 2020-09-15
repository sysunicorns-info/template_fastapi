from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.types import Receive, Scope, Send

from .config import Config, ConfigFactory
from .container import ApplicationContainer, application_container_proxy
from .service import service_container_proxy
# Load After Initialization of all Container
from .api import api_router, API_ROUTER_PREFIX


class Application(FastAPI):

    config: Config = None
    fastapi: FastAPI = None

    def __init__(self):
        self.config = ConfigFactory().get_config()

        application_container_proxy.factory(config=self.config)
        service_container_proxy.factory()

        self.fastapi = FastAPI(
            title=self.config.application_name,
            version=self.config.application_version,
            debug=True
        )

        self.fastapi.add_middleware(
            CORSMiddleware,
            allow_origins=self.config.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.fastapi.add_event_handler("startup", self.handle_event_startup)
        self.fastapi.add_event_handler("shutdown", self.handle_event_shutdown)

        self.fastapi.include_router(prefix=API_ROUTER_PREFIX, router=api_router)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        return await self.fastapi.__call__(scope=scope, receive=receive, send=send)

    async def handle_event_startup(self):
        print("startup")
        await application_container_proxy().database().init_pool();

    async def handle_event_shutdown(self):
        print("shutdown")
        await application_container_proxy().database().close_pool();
