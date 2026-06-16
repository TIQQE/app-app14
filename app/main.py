import os

from fastapi import FastAPI, APIRouter

APP_SLUG = os.environ.get("APP_SLUG", "app")
APP_ENV = os.environ.get("APP_ENV", "dev")
PREFIX = f"/{APP_SLUG}-{APP_ENV}"

app = FastAPI()
router = APIRouter(prefix=PREFIX)


@router.get("/")
def root():
    return {"message": f"Hello from {APP_SLUG}!", "env": APP_ENV}


@router.get("/health")
def health():
    return {"status": "ok"}


app.include_router(router)
