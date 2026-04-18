import pytest
import os
import subprocess
from testcontainers.postgres import PostgresContainer
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text

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
@pytest.fixture(scope="function", autouse=True)
def clean_db(postgres_container):
    db_url = os.environ["DATABASE_URL"]
    engine = create_engine(db_url)

    with engine.connect() as conn:
        # Disable FK checks temporarily
        conn.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE"))

    yield