__version__ = '0.1.0'

from fastapi import FastAPI, APIRouter

from contact_list_clean_arch.app.contact.router import get_contact_by_id_router, create_contact_router
from contact_list_clean_arch.app.config.db import Base, engine

Base.metadata.create_all(engine)


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(__application_router())

    return application


def __application_router() -> APIRouter:
    router = APIRouter()

    router.include_router(create_contact_router.router)
    router.include_router(get_contact_by_id_router.router)

    return router
