from typing import List, Optional
from src.repositories.accommodation_repository_interface import AccommodationRepositoryInterface
from src.schemas.accommodation import AccommodationSchema

class AccommodationUseCase:
    def __init__(self, repository: AccommodationRepositoryInterface) -> None:
        self.repo = repository

    def get_all_accommodations(self) -> List[AccommodationSchema]:
        return self.repo.get_all()

    def get_accommodations_by_location(self, city: str = None) -> List[AccommodationSchema]:
        return self.repo.get_by_city(city)

    def get_accommodation_by_id(self, id: int) -> Optional[AccommodationSchema]:
        accommodation = self.repo.get_by_id(id)
        return accommodation
