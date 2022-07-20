__version__ = '0.1.0'

from fastapi import FastAPI, APIRouter
from requests import HTTPError

from contact_list_clean_arch.app.domain.auth.exception.unauthenticated_exception import UnauthenticatedException
from contact_list_clean_arch.app.domain.auth.exception.unauthorized_exception import UnauthorizedException
from contact_list_clean_arch.app.domain.auth.router import user_authentiation_router
from contact_list_clean_arch.app.config.exception.exception_handler import handle_contact_not_found_exception, \
    handle_exception, \
    handle_user_not_found_exception, handle_unauthorized_exception, handle_unauthenticated_exception, \
    handle_client_http_error
from contact_list_clean_arch.app.domain.contact.exception.contact_not_found_exception import ContactNotFoundException
from contact_list_clean_arch.app.domain.contact.router import get_contact_by_id_router
from contact_list_clean_arch.app.domain.contact.router import create_contact_router
from contact_list_clean_arch.app.config.db import Base, engine
from contact_list_clean_arch.app.domain.user.exception.user_not_fount_exception import UserNotFoundException
from contact_list_clean_arch.app.domain.user.router import create_user_router, get_user_by_id_router

Base.metadata.create_all(engine)


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(__application_router())

    # TODO achar um jeito que add por anotacao ou de uma forma melhor dessa forma

    __add_exception_handlers(application)

    return application


def __add_exception_handlers(application):
    application.add_exception_handler(ContactNotFoundException, handle_contact_not_found_exception)
    application.add_exception_handler(UserNotFoundException, handle_user_not_found_exception)
    application.add_exception_handler(UnauthorizedException, handle_unauthorized_exception)
    application.add_exception_handler(UnauthenticatedException, handle_unauthenticated_exception)
    application.add_exception_handler(HTTPError, handle_client_http_error)
    application.add_exception_handler(Exception, handle_exception)


def __application_router() -> APIRouter:
    router = APIRouter()

    router.include_router(create_contact_router.router)
    router.include_router(get_contact_by_id_router.router)
    router.include_router(create_user_router.router)
    router.include_router(get_user_by_id_router.router)
    router.include_router(user_authentiation_router.router)

    return router
