# pytest-poc
Doing POC for pytest and gherkin tests

`docker run -d  --name postgres-db   -e POSTGRES_USER=myuser   -e POSTGRES_PASSWORD=mypassword   -e POSTGRES_DB=mydatabase   -p 5432:5432   postgres:15`

`fastapi dev app/main.py`

`export DOCKER_HOST=unix:///var/run/docker.sock`
`unix:///Users/shrikantsonone/.docker/run/docker.sock`

`pytest --cov=app --cov-report=term-missing`
`pytest --cov=app --cov-report=html`