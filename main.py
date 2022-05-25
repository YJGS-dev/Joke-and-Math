from typing import Union, List
from fastapi import FastAPI, HTTPException, Query
from models import Joke
import requests
from uuid import UUID
from utils import LcmOfArray

app = FastAPI()

db: List[Joke] = []

@app.get("/joke/")
async def read_joke(path: str):
    api_url = {
                "Chuck": "https://api.chucknorris.io/jokes/random",
                "Dad": "https://icanhazdadjoke.com/"
            }
    api_url = api_url.get(path)
    if api_url:
        headers = {"Accept": "application/json"}
        response = requests.get(api_url, headers = headers)
        return response.json()
    else:
        raise HTTPException(status_code = 400, detail = "path params is required, values Dad or Chuck")
    
@app.post("/joke/")
async def create_joke(joke: Joke):
    db.append(joke)
    return {**joke.dict(), "message":"created"}

@app.put("/joke/{joke_id}")
async def update_joke(joke_id: UUID, joke: Joke):
    for item in db:
        if item.id == joke_id:
            if joke.joke is not None:
                item.joke = joke.joke
                return {**item.dict(), "message":"updated"}
    raise HTTPException(status_code = 404, detail = "Joke id doesn't exist")

@app.delete("/joke/{joke_id}")
async def delete_joke(joke_id: UUID):
    for item in db:
        if item.id == joke_id:
            temp = item
            db.remove(item)
            return {**temp.dict(), "message":"deleted"}
    raise HTTPException(status_code = 404, detail = "Joke id doesn't exist")

@app.get("/math/lcm/")
async def read_lcm(numbers: Union[List[int], None] = Query(default = None)):
    return LcmOfArray(numbers, 0)

@app.get("/math/increment/")
async def read_increment(number: int):
    return number + 1
