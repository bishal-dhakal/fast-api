from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas,database, models
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=["users"]
)

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request,db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(database.get_db)):
    return user.get_user(id,db)