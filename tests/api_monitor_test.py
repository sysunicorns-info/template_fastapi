import pytest
import os
from fastapi.testclient import TestClient
from application.container import application_container_proxy
from application.database import Database


from main import application

def test_api_monitor_health():
    with TestClient(app=application) as client:
        response = client.get("/api/monitor/health")
        assert response.status_code == 200

def test_database_is_init():
    assert isinstance(application_container_proxy().database(), Database)
    with TestClient(app=application) as client:
        response = client.get("/api/monitor/health")
        assert response.status_code == 200
