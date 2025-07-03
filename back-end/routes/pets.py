from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import APIRouter, Depends, HTTPException
from models.models import Pet
from models.pydantic_models import PetCreate, PetUpdate, PetResponse
from database import get_db

router = APIRouter()

@router.get("/")
async def get_pets(db: AsyncSession = Depends(get_db)):
    query = select(Pet)
    result = await db.execute(query)
    pets = result.scalars().all()

    return pets

@router.get("/{id}")
async def get_pet_by_id(id, db: AsyncSession = Depends(get_db)):
    query = select(Pet).where(Pet.id == id)
    result = db.execute(query)
    pet_db = result.scalars().first()
    pet = PetResponse.model_validate(pet_db)
    
    return {
        "pet": pet
    }

@router.post("/create")
async def create_pet(pet_data: PetCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_pet = Pet(
            nome = pet_data.nome,
            especie = pet_data.especie,
            raca = pet_data.raca,
            nascimento = pet_data.nascimento,
            peso = pet_data.peso,
            imagem = pet_data.imagem,
            tutor_email = pet_data.tutor_email
        )

        db.add(new_pet)
        await db.commit()
        await db.refresh(new_pet)

        return {"status": 200, "message": "Pet cadastrado com sucesso!", "id": new_pet.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.put("/update/")
async def update_pet_by_id(pet_data: PetUpdate, db: AsyncSession = Depends(get_db)):
    try:
        query = select(Pet).where(Pet.id == id)
        result = db.execute(query)
        pet = result.scalars().first()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    
    if not pet:
        raise HTTPException(status_code=400, detail="Pet não encontrado!")
    
    if pet_data.nome:
        pet.nome = pet_data.nome
    if pet_data.especie:
        pet.especie = pet_data.especie
    if pet_data.raca:
        pet.raca = pet_data.raca
    if pet_data.nascimento:
        pet.nascimento = pet_data.nascimento
    if pet_data.peso:
        pet.peso = pet_data.peso
    if pet_data.imagem:
        pet.imagem = pet_data.imagem

    await db.commit()
    await db.refresh(pet)

    return {"status": 200, "message": "Pet atualizado com sucesso!", "pet": pet}


@router.delete("/delete")
async def delete_pet_by_id(id: int, db: AsyncSession = Depends(get_db)):
    try:
        query = select(Pet).where(Pet.id == id)
        result = db.execute(query)
        pet = result.scalars().first()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    
    if not pet:
        raise HTTPException(status_code=400, detail="Pet não encontrado!")
    
    db.delete(pet)
    await db.commit()
    
    return {"status": 200, "message": "Pet deletado com sucesso!"}
