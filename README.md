# GitHub Actions + Docker + GitHub Container Registry (GHCR) Lab

## Overview

โปรเจกต์นี้เป็นการทดลองสร้าง CI/CD Pipeline เบื้องต้นด้วย GitHub Actions และ Docker โดยมีเป้าหมายเพื่อเรียนรู้กระบวนการ Build, Run และ Publish Docker Image ไปยัง GitHub Container Registry (GHCR)

### Architecture

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ├── Build Docker Image
    ├── Run Container
    └── Push Image
    │
    ▼
GitHub Container Registry (GHCR)
    │
    ▼
Ubuntu Server
    │
    ▼
Docker Pull & Run
```

---

## Objectives

* เรียนรู้การใช้งาน Git และ GitHub Workflow
* เรียนรู้ GitHub Actions Workflow
* สร้าง Docker Image จาก Source Code
* ทดสอบ Container บน GitHub Runner
* Push Docker Image ไปยัง GitHub Container Registry (GHCR)
* Pull และ Run Image จาก Ubuntu Server
* เตรียมความพร้อมสำหรับ Kubernetes และ Cloud Native Deployment

---

## Project Structure

```text
github/
├── app.py
├── Dockerfile
└── .github/
    └── workflows/
        ├── hello.yml
        ├── docker-build.yml
        └── docker-push.yml
```

---

## Source Code

### app.py

```python
print("Hello from Docker Container")
```

---

## Docker Configuration

### Dockerfile

```dockerfile
FROM python:3.12

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

---

## GitHub Actions Workflow

### Build Docker Image

```yaml
name: Docker Build

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Build Docker Image
        run: docker build -t demo-app .
```

---

### Build and Run Container

```yaml
name: Docker Build and Run

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Build Docker Image
        run: docker build -t demo-app .

      - name: Run Docker Container
        run: docker run demo-app
```

Expected Output:

```text
Hello from Docker Container
```

---

### Push Image to GitHub Container Registry

```yaml
name: Docker Push

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v4

      - name: Login GHCR
        run: |
          echo "${{ secrets.GITHUB_TOKEN }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin

      - name: Build Image
        run: |
          OWNER=$(echo "${{ github.repository_owner }}" | tr '[:upper:]' '[:lower:]')
          docker build -t ghcr.io/$OWNER/demo-app:latest .

      - name: Push Image
        run: |
          OWNER=$(echo "${{ github.repository_owner }}" | tr '[:upper:]' '[:lower:]')
          docker push ghcr.io/$OWNER/demo-app:latest
```

---

## GitHub Container Registry

Published Image:

```text
ghcr.io/aketana/demo-app:latest
```

Pull Image:

```bash
docker pull ghcr.io/aketana/demo-app:latest
```

Run Container:

```bash
docker run ghcr.io/aketana/demo-app:latest
```

Expected Output:

```text
Hello from Docker Container
```

---

## Ubuntu Validation

Environment:

* Hyper-V
* Ubuntu Server
* Docker Engine

Verification:

```bash
docker pull ghcr.io/aketana/demo-app:latest

docker run ghcr.io/aketana/demo-app:latest
```

Result:

```text
Hello from Docker Container
```

Successfully verified that the image built by GitHub Actions can be deployed and executed on an external Ubuntu environment.

---

## Key Learnings

### Git

* git clone
* git add
* git commit
* git push

### GitHub Actions

* Workflow Creation
* Runner Execution
* Build Automation

### Docker

* Dockerfile
* Docker Build
* Docker Run
* Image Lifecycle

### GitHub Container Registry

* Container Image Storage
* Image Distribution
* Registry Authentication

### Deployment Pipeline

```text
Code
  ↓
Git Push
  ↓
GitHub Actions
  ↓
Docker Build
  ↓
Docker Push (GHCR)
  ↓
Ubuntu Server
  ↓
Docker Pull
  ↓
Docker Run
```

## Conclusion

This project demonstrates a complete beginner-to-intermediate CI/CD workflow using GitHub Actions, Docker, and GitHub Container Registry. The workflow successfully automates image build, validation, publication, and deployment to an Ubuntu environment, forming a foundation for future Kubernetes and Cloud Native implementations.
