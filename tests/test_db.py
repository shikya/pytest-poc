def test_db_connection(postgres_container):
    assert "postgresql" in postgres_container