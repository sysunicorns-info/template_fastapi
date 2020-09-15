import uvicorn

from application.config import ConfigFactory
from application import Application

if __name__ == "__main__":
    # Config Loading
    _config = ConfigFactory().get_config()
    # Run Uvicorn Boostrap
    uvicorn.run("main:application", 
        host=_config.server_host,
        port=_config.server_port,
        log_level=_config.server_log_level,
        log_config=_config.server_log_config,
        lifespan="on"
    )
else:
    # Instanciate Application
    application = Application()
