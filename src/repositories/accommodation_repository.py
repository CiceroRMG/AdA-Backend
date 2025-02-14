from sqlalchemy.orm import Session
from src.models.accommodation import AccommodationModel
from src.repositories.accommodation_repository_interface import AccommodationRepositoryInterface
from src.schemas.accommodation import AccommodationSchema
from src.utils.normalize_string import normalize_string

class SQLAccommodationRepository(AccommodationRepositoryInterface):
    def __init__(self, db: Session, queryLimit: int = 12) -> None:
        self.db = db
        self.limit = queryLimit

    def get_all(self, page: str = "1") -> list[AccommodationSchema]:
        page_number = int(page) if page and page.isdigit() else 1
        offset = (page_number - 1) * self.limit

        models = self.db.query(AccommodationModel)\
            .offset(offset)\
            .limit(self.limit)\
            .all()
        return [AccommodationSchema.model_validate(model) for model in models]

    def get_by_id(self, accommodation_id: int) -> AccommodationSchema | None:
        model = self.db.query(AccommodationModel).filter(AccommodationModel.id == accommodation_id).first()
        return AccommodationSchema.model_validate(model) if model else None

    def get_by_city(self, city: str, page: str = "1") -> list[AccommodationSchema]:
        city = normalize_string(city)
        page_number = int(page) if page and page.isdigit() else 1
        offset = (page_number - 1) * self.limit

        models = self.db.query(AccommodationModel)\
            .filter(AccommodationModel.tag.ilike(f"%{city}%"))\
            .offset(offset)\
            .limit(self.limit)\
            .all()
        return [AccommodationSchema.model_validate(model) for model in models]
