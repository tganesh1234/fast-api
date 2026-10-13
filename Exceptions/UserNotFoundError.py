from fastapi import HTTPException
from fastapi.responses import JSONResponse

class UserNotFoundError(HTTPException):
    def __init__(self, user_id: int):
        super().__init__(status_code=404, detail=f"User with ID {user_id} not found")


async def user_not_found_exception_handler(request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
