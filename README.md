# Flask CRUD API with Docker & GitHub Actions

A simple REST API built with **Flask** and **PostgreSQL**, containerized with **Docker**, and automated using **GitHub Actions**.

## 🚀 Tech Stack

- Python 3.12
- Flask
- PostgreSQL 17
- Docker & Docker Compose
- GitHub Actions
- GitHub Container Registry (GHCR)
- Pytest

## 📦 Features

- RESTful CRUD API
- PostgreSQL Database Integration
- Dockerized Application
- Automated Testing with Pytest
- CI/CD Pipeline with GitHub Actions
- Docker Image Publishing to GHCR
- Health Check Endpoint

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home Page |
| GET | `/health` | Health Check |
| GET | `/about` | About |
| GET | `/me` | Profile |
| GET | `/users` | Get All Users |
| GET | `/users/{id}` | Get User by ID |
| POST | `/users` | Create User |
| PUT | `/users/{id}` | Update User |
| DELETE | `/users/{id}` | Delete User |

## ▶️ Run Project

Start the application:

```bash
docker-compose up -d
```

Verify the application:

```bash
curl http://localhost:5000/health
```

## 🧪 Run Tests

```bash
make test
```

or

```bash
docker-compose exec app python -m pytest -v
```

Current Result:

```
12 Tests Passed ✅
```

## 🚢 Deploy Latest Image

```bash
make deploy
```

## 📁 Project Structure

```text
.
├── app.py
├── database.py
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── database/
│   └── init.sql
├── tests/
│   └── test_api.py
└── .github/
    └── workflows/
```

## ✅ Project Status

- ✔ CRUD API
- ✔ PostgreSQL Integration
- ✔ Docker & Docker Compose
- ✔ GitHub Actions CI
- ✔ GitHub Container Registry (GHCR)
- ✔ Automated Testing (12/12 Passed)
