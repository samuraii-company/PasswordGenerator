from fastapi import APIRouter, HTTPException, status

from fastapi.responses import JSONResponse

from core.generator import PasswordCredentials

from . import services


router = APIRouter(tags=["Password"], prefix="/api/v1/password")

MAX_SYMBOLS = 1000
MIN_SYMBOLS = 20


@router.get("/")
def generate_password(
    count: int = 20,
    numbers: bool = False,
    symbols: bool = False,
):
    """Generate Password"""

    if count > MAX_SYMBOLS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum password length 1000 symbols",
        )

    credentials = PasswordCredentials(
        count if count >= MIN_SYMBOLS else MIN_SYMBOLS, numbers, symbols
    )

    _password = services.create(credentials)

    return JSONResponse(content={"password": _password}, status_code=200)
