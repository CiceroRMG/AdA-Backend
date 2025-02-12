from fastapi.middleware.cors import CORSMiddleware
from src.db.init_db import init_db, reset_db
from fastapi import FastAPI
from src.routes import accommodation_route

reset_db()
init_db()

app = FastAPI(
    title="API de Acomodações",
    version="1.0.0",
    description="API REST para consulta de acomodações de temporada."
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accommodation_route.router)

