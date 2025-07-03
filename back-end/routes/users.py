from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import APIRouter, Depends, HTTPException
from models.models import Tutor
from models.pydantic_models import TutorCreate, TutorLogin
from database import get_db
from passlib.context import CryptContext
from datetime import timedelta
from auth import authenticate_user, create_access_token, validate_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

@router.post("/signin")
async def signin(tutor_login: TutorLogin, db: AsyncSession = Depends(get_db)):
    tutor = await authenticate_user(db, tutor_login.email, tutor_login.senha)

    if not tutor:
        raise HTTPException(status_code=400, detail="E-mail ou senha incorretos")
    
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": str(tutor.email)}, expires_delta=access_token_expires
    )

    return {
        "status": 200, "access_token": access_token, "token_type": "bearer"
    }


@router.post("/signup")
async def signup(tutor_data: TutorCreate, db: AsyncSession = Depends(get_db)):
    try:
        query = select(Tutor).where(Tutor.email == tutor_data.email)
        result = await db.execute(query)
        existing_tutor = result.scalars().first()

        if existing_tutor:
            raise HTTPException(status_code=400, detail="E-mail já cadastrado!")
        
        new_tutor = Tutor(
            email = tutor_data.email,
            nome = tutor_data.nome,
            senha = pwd_context.hash(tutor_data.senha),
            telefone = tutor_data.telefone
        )

        db.add(new_tutor)
        await db.commit()
        await db.refresh(new_tutor)

        return {"status": 200, "message": "Tutor cadastrado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.post("/validate-token/{token}")
async def validate(token: str):
    result = await validate_token(token)
    
    return result