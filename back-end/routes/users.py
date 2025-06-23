from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/signin")
def signin():
    return {
        "message": "List of guardians"
    }

@router.post("/signup")
def signup():
    return {
        "message": "List of guardians"
    }

