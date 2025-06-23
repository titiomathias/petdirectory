from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import guardians, pets, users

api = FastAPI(
    title="PetDirAPI",
    version="0.0.1"
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
def root():
    return {
        "message": "welcome to pet directory!"
    }


# Routes
api.include_router(guardians.router, prefix="/guardians", tags=["Guardians"])
api.include_router(pets.router, prefix="/pets", tags=["Pets"])
api.include_router(users.router, prefix="/users", tags=["Users Controller"])