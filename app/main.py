from fastapi import FastAPI, HTTPException
import validators
from . import schemas

app = FastAPI()
"""
API Endpoints
- / GET
- /url POST
- /{url_key} GET
- /admin/{secret_key} GET
- /admin/{secret_key} DELETE
"""
@app.get("/")
def read_root():
    return "Welcome to the URL shortener API"

def raise_bad_request(message: str):
    raise HTTPException(status_code=400, detail=message)


@app.post("/url")
def create_url(url: schemas.BaseURL):
    if not validators.url(url.target_url):
        raise_bad_request(message="The provided URL is invalid")
    return f"TODO: Create db entry for {url.target_url}"

