# bdd api lab

A production-grade backend testing framework built with **FastAPI**, **SQLAlchemy**, **Alembic**, and **pytest-bdd**, featuring:

- End-to-end (E2E) testing
- Behavior-driven development (BDD)
- Testcontainers-based ephemeral databases
- External API mocking
- Parallel test execution
- Coverage reporting

---

## 🚀 Features

- ✅ FastAPI REST APIs
- ✅ PostgreSQL with SQLAlchemy ORM
- ✅ Alembic migrations
- ✅ BDD testing with pytest-bdd
- ✅ Testcontainers for isolated test DB
- ✅ External API mocking using respx
- ✅ Parallel test execution (pytest-xdist)
- ✅ Code coverage reporting

---

## 🏗️ Project Structure

```

project/
│── app/
│   ├── main.py          # FastAPI app
│   ├── db.py            # DB setup
│   ├── models.py        # ORM models
│   ├── schemas.py       # Pydantic schemas
│   ├── deps.py          # dependencies
│   └── services/        # business logic
│
│── alembic/             # DB migrations
│── tests/
│   ├── features/        # Gherkin files
│   ├── test_*.py       # BDD + API tests
│   └── conftest.py      # fixtures (DB, client)
│
│── .env
│── requirements.txt
│── pytest.ini

````

---

## ⚙️ Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

---

### 2. Start PostgreSQL (Docker)

```bash
docker run -d \
  --name postgres-db \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  postgres:15
```

---

### 3. Configure environment

`.env`

```env
DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/mydatabase
```

---

### 4. Run migrations

```bash
alembic upgrade head
```

---

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Running Tests

### Run all tests

```bash
pytest -v
```

---

### Run specific tests

```bash
pytest -k external -v
```

---

### Run tests in parallel

```bash
pytest -n auto
```

---

## 🧬 BDD Example

```gherkin
Feature: Users API

  Scenario: Create and retrieve user
    When I create a user with name "Shrikant" and email "test@example.com"
    Then the response status should be 200

    When I call GET /users
    Then the response should contain email "test@example.com"
```

---

## 🔌 External API Mocking

External calls are mocked using `respx`:

```python
with respx.mock:
    respx.get("https://external-api.com/users").mock(
        return_value=httpx.Response(200, json=[...])
    )
```

---

## 🐳 Testcontainers

Tests use ephemeral PostgreSQL instances:

* Fresh DB per test session
* Optional isolation per worker (parallel runs)
* No dependency on local DB

---

## 📊 Coverage

### Run coverage

```bash
pytest --cov=app --cov-report=term-missing
```

### HTML report

```bash
pytest --cov=app --cov-report=html
open htmlcov/index.html
```

---

## ⚡ Key Concepts

* **Black-box testing** via API calls
* **BDD** for business workflows
* **Service layer abstraction** for external integrations
* **Database isolation** using Testcontainers
* **Parallel-safe test execution**

---

## 🧠 Design Philosophy

* Tests validate **behavior, not implementation**
* No direct DB access in tests
* External systems are **mocked, not called**
* Infrastructure is **ephemeral and reproducible**

---

## 🚀 Future Improvements

* CI pipeline integration (GitHub Actions)
* Async test support (`httpx.AsyncClient`)
* Retry & circuit breaker testing
* Contract/schema validation
* Load testing integration

---

## 📌 Requirements

* Python 3.10+
* Docker (for Testcontainers)
* PostgreSQL (optional for local dev)

---

## 🤝 Contributing

Feel free to open issues or submit PRs for improvements.
