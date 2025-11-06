from fastapi import FastAPI

app = FastAPI()

@app.get("/dev")

def read_cv():
    message = "Hellooooo, this's my first App FastAPI"
    return {message}
    