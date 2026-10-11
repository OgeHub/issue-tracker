from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.issue_tracker.api.router import router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to the Issue Tracker API!"}


app.include_router(router, prefix="/api")