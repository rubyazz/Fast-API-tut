from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
	name:str
	price:float
	is_offer: Union[bool, None] = None


class Player(BaseModel):
	name:str
	description:str
	is_offer: Union[bool, None] = None
		

@app.get("/")
def read_root():
	return {"Hello":"world!"}

@app.get("/items/{item_id}")
def read_item(item_id : int, q: Union[str, None] = None):
	return {"item_id":item_id, "q":q}

@app.put("/items/{item_id}")
def read_item(item_id : int, item: Item):
	return {"item_name":item_name, "item_id":item_id}

@app.get("/routes")
def get_routes():
	return {"Cool ":"ROUTES"}




