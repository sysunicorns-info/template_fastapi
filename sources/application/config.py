from dataclasses import dataclass
import logging

VERSION_MAJOR=0
VERSION_MINOR=0
VERSION=f"v{VERSION_MAJOR}.{VERSION_MINOR}"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s # FRM: %(levelprefix)s %(message)s",
            "datefmt": "%Y/%m/%d %I:%M:%S",
            "use_colors": None,
        },
        "backend": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s # APP: %(levelprefix)s %(message)s",
            "datefmt": "%Y/%m/%d %I:%M:%S",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s # ACS: %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            "datefmt": "%Y/%m/%d %I:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "backend": {
            "formatter": "backend",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "backend": {"handlers": ["backend"], "level": "DEBUG"},
        "uvicorn": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
}

@dataclass
class Config():
    application_name: str
    application_version: str
    application_version_minor: int
    application_version_major: int
    server_host: str
    server_port: int
    server_log_level: str
    server_log_config: dict
    db_host: str
    db_user: str
    db_pwd: str
    db_name: str
    origins: list()

class ConfigFactory():

    config: Config

    def __init__(self):
        self.config = Config(
            application_name="Application",
            application_version=VERSION,
            application_version_minor=VERSION_MINOR,
            application_version_major=VERSION_MAJOR,
            server_host="0.0.0.0",
            server_port=8080,
            server_log_level=logging.DEBUG,
            server_log_config=LOGGING_CONFIG,
            db_host="",
            db_user="",
            db_pwd="",
            db_name="",
            origins = [
                "http://localhost:5000",
            ]
        )

    def get_config(self) -> Config:
        return self.config
