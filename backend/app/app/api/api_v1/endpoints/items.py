import sys
from typing import Any

from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/")
async def read_my_endpoint_root():
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    message = f"Hello from Seb! FastAPI is running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}



@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    item: schemas.Item,
) -> Any:
    """
    Create new item.
    """
    return item
