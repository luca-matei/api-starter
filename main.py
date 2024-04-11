import uvicorn

from fastapi import FastAPI

from v1.clients.redis import RedisSession

app = FastAPI()


@app.get("/")
def read_root():
    with RedisSession(db=0, decode="utf-8") as cache:
        cache.set("key", "value")
        print(cache.get("key"))

    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
