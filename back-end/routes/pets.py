from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/")
def get_pets():
    return {
        "message": "List of guardians"
    }