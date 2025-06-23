from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/")
def get_guardians():
    return {
        "message": "List of guardians"
    }