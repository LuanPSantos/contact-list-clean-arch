
from starlette.requests import Request
from starlette.responses import JSONResponse

from contact_list_clean_arch.app.contact.exception.contact_not_found_exception import ContactNotFoundException


async def handle_contact_not_found_exception(request: Request, exc: ContactNotFoundException):
    print(request)
    print(exc)
    return JSONResponse(
        status_code=404,
        content={"message": f"Contact not found"},
    )


async def handle_exception(request: Request, exc: Exception):
    print(request)
    print(exc)
    return JSONResponse(
        status_code=500,
        content={"message": f"Unknown error"},
    )

