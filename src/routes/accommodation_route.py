from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas.accommodation import AccommodationSchema
from src.useCases.accommodation_usecase import AccommodationUseCase
from src.repositories.accommodation_repository import SQLAccommodationRepository

router = APIRouter()

@router.get("/accommodations", response_model=list[AccommodationSchema])
def list_accommodations(
    city: str | None = Query(None, description="Filtrar por city"),
    page: str = Query("1", description="Número da página"),
    db: Session = Depends(get_db)
):
    repository = SQLAccommodationRepository(db)
    use_case = AccommodationUseCase(repository)
    if city:
        accommodations = use_case.get_accommodations_by_location(city, page)
    else:
        accommodations = use_case.get_all_accommodations(page)
    return accommodations

@router.get("/accommodation/{accommodation_id}", response_model=AccommodationSchema)
def get_accommodation_by_id(
    accommodation_id: int,
    db: Session = Depends(get_db)
):
    repository = SQLAccommodationRepository(db)
    use_case = AccommodationUseCase(repository)
    accommodation = use_case.get_accommodation_by_id(accommodation_id)
    if not accommodation:
        raise HTTPException(status_code=404, detail="Acomodação não encontrada.")
    return accommodation
