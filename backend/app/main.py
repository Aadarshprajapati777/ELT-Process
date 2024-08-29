from fastapi import FastAPI
from app.api.endpoints import files
from app.core.logging_config import logger
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Hey this is Aadarsh, Starting the ELT application.")
    yield
    logger.info("Application shutdown complete.")

app = FastAPI(lifespan=lifespan)

app.include_router(files.router, prefix="/api/v1")
