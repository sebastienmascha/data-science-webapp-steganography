from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Properties to return to client
class Item(ItemBase):
    pass
