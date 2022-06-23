from fastapi import HTTPException

from contact_list_clean_arch.contact.exception.contact_not_found_exception import ContactNotFoundException


def with_exception_handler(run):
    try:
        return run()
    except ContactNotFoundException:
        raise HTTPException(status_code=404, detail="Contact not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e.__class__.__name__} - {e.args}")
