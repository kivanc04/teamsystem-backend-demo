# TeamSystem Backend Demo (FastAPI)

A minimal backend service demonstrating a clean FastAPI structure with test coverage.

## Features
- Health check endpoint
- Simple items API (list + create + get by id)
- Pytest tests (fast, deterministic)
- Clean separation: routes, schemas, repository

## Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Pytest

## API Endpoints
- GET `/health` — Health check
- GET `/items` — List items
- POST `/items` — Create item
- GET `/items/{item_id}` — Get item by id

## Project Structure
- `app/main.py` — FastAPI app entry
- `app/routes.py` — API routes
- `app/schemas.py` — Pydantic models
- `app/repository.py` — in-memory data layer
- `tests/` — API tests

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

