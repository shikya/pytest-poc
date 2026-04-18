import pytest
import os
import subprocess
from testcontainers.postgres import PostgresContainer
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def postgres_container():
    container = PostgresContainer("postgres:15")
    container.start()

    db_url = container.get_connection_url()

    # Override env BEFORE app starts
    os.environ["DATABASE_URL"] = db_url

    subprocess.run(["alembic", "upgrade", "head"], check=True)

    yield db_url

    container.stop()

@pytest.fixture(scope="session")
def client(postgres_container):
    # Import AFTER env is set
    from app.main import app

    return TestClient(app)