from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="TeamSystem Backend Demo")

app.include_router(router)
