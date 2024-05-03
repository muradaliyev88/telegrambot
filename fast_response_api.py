from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name = None
    description = None


@app.post("/en_az", response_model=Item)
async def create_item(item: Item):
    return item


@app.post("/az_en", response_model=Item)
async def create_item(item: Item):
    return item