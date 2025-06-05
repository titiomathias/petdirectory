from fastapi import FastAPI

api = FastAPI(
    title="PetDirAPI",
    version="0.0.1"
)

@api.get("/")
def root():
    return {
        "message": "welcome to pet directory!"
    }