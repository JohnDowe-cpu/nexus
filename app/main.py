from fastapi import FastAPI

app = FastAPI(title="Nexus")


@app.get("/")
def read_root():
    return {"message": "Nexus API is running"}