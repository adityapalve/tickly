from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to the URL shortener API"

"""
API Endpoints
- / GET
- /url POST
- /{url_key} GET
- /admin/{secret_key} GET
- /admin/{secret_key} DELETE

"""
