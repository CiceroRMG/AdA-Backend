from abc import ABC, abstractmethod
from typing import List, Optional
from src.schemas.accommodation import AccommodationSchema

class AccommodationRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self, page: str = None) -> List[AccommodationSchema]:
        pass

    @abstractmethod
    def get_by_id(self, accommodation_id: int) -> Optional[AccommodationSchema]:
        pass

    @abstractmethod
    def get_by_city(self, city: str, page: str = None) -> List[AccommodationSchema]:
        pass
