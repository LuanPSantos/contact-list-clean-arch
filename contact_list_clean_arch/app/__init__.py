__version__ = '0.1.0'

from fastapi import FastAPI, APIRouter

from contact_list_clean_arch.app.auth.router import user_authentiation_router
from contact_list_clean_arch.app.config.exception_handler import handle_contact_not_found_exception, handle_exception, \
    handle_user_not_found_exception
from contact_list_clean_arch.app.contact.exception.contact_not_found_exception import ContactNotFoundException
from contact_list_clean_arch.app.contact.router import get_contact_by_id_router, create_contact_router
from contact_list_clean_arch.app.config.db import Base, engine
from contact_list_clean_arch.app.user.exception.user_not_fount_exception import UserNotFoundException
from contact_list_clean_arch.app.user.router import create_user_router, get_user_by_id_router

Base.metadata.create_all(engine)


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(__application_router())

    # TODO achar um jeito que add por anotacao ou de uma forma melhor dessa forma

    application.add_exception_handler(ContactNotFoundException, handle_contact_not_found_exception)
    application.add_exception_handler(UserNotFoundException, handle_user_not_found_exception)
    application.add_exception_handler(Exception, handle_exception)

    return application


def __application_router() -> APIRouter:
    router = APIRouter()

    router.include_router(create_contact_router.router)
    router.include_router(get_contact_by_id_router.router)
    router.include_router(create_user_router.router)
    router.include_router(get_user_by_id_router.router)
    router.include_router(user_authentiation_router.router)

    return router
