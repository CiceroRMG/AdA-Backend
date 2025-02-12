from sqlalchemy.orm import Session
from src.models.accommodation import AccommodationModel
from src.repositories.accommodation_repository_interface import AccommodationRepositoryInterface
from src.schemas.accommodation import AccommodationSchema

class SQLAccommodationRepository(AccommodationRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[AccommodationSchema]:
        models = self.db.query(AccommodationModel).all()
        return [AccommodationSchema.model_validate(model) for model in models]

    def get_by_id(self, accommodation_id: int) -> AccommodationSchema | None:
        model = self.db.query(AccommodationModel).filter(AccommodationModel.id == accommodation_id).first()
        return AccommodationSchema.model_validate(model) if model else None

    def get_by_city(self, city: str) -> list[AccommodationSchema]:
        models = self.db.query(AccommodationModel).filter(
            AccommodationModel.location.ilike(f"%{city}%")
        ).all()
        return [AccommodationSchema.model_validate(model) for model in models]
