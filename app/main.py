from typing import Union
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

from app.api.v1.routes import router as v1_router

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


@app.get("/", status_code=status.HTTP_201_CREATED)
async def create_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="ID must be positive")
    return {"message": "Item created"}

app.include_router(v1_router, prefix="/api/v1", tags=["v1"])
app.include_router(v1_router, prefix="/api/v1", tags=["v1"])

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"name": item.name, "item_id": item_id}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

