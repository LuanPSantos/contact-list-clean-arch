
from starlette.requests import Request
from starlette.responses import JSONResponse

from contact_list_clean_arch.app.contact.exception.contact_not_found_exception import ContactNotFoundException
from contact_list_clean_arch.app.user.exception.user_not_fount_exception import UserNotFoundException


async def handle_contact_not_found_exception(request: Request, exc: ContactNotFoundException):
    print(request)
    print(exc)
    return JSONResponse(
        status_code=404,
        content={"message": f"Contact not found"},
    )


async def handle_user_not_found_exception(request: Request, exc: UserNotFoundException):
    print(request)
    print(exc)
    return JSONResponse(
        status_code=404,
        content={"message": f"User not found"},
    )


async def handle_exception(request: Request, exc: Exception):
    print(request)
    print(exc.__class__)
    return JSONResponse(
        status_code=500,
        content={"message": f"Unknown error"},
    )

