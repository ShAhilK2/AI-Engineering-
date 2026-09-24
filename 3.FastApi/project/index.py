from fastapi import FastAPI


app = FastAPI()

@app.get("/ping")
def pingpong():
    return {"message" : "Working Ping Pong"}