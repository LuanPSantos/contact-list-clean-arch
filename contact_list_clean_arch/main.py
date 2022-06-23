import uvicorn

from contact_list_clean_arch import create_application


application = create_application()


def start():
    uvicorn.run("contact_list_clean_arch.main:application", host="0.0.0.0", port=8000, reload=True)
