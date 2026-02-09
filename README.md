
# teamsystem-backend-demo

## TeamSystem Backend Sample (FastAPI)

A minimal FastAPI backend service demonstrating:
- Health check endpoint
- Simple CRUD-style items endpoints
- Pytest test coverage
- Clean project structure

---

## Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Pytest

---

## API Endpoints

- **GET /health**  
  Health check endpoint

- **GET /items**  
  Returns item list

- **POST /items**  
  Creates a new item

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pytest

source .venv/bin/activate
uvicorn app.main:app --reload --port 8000

>>>>>>> 189afb2 (Add FastAPI health endpoint with pytest coverage)
