# vault-fastapi

## Project Structure

```text
vault-fastapi/
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- database.py
|   |-- auth.py
|   |-- models.py
|-- tests/
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- README.md
```

## Setup

Make sure to replace placeholder values in the code (like passwords, tokens) with your actual credentials.

## How to Execute

Build and run the Docker containers:

```sh
docker-compose up

# docker-compose down
```

Visit [http://localhost:8000] in your browser to test the FastAPI application.

## How to Test

Run the tests using pytest:

```sh
pytest tests
```
