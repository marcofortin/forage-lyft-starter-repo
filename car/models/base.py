from abc import ABC, abstractmethod
from typing import List

from car.component.models.base import Component


class Car(ABC):
    @property
    @abstractmethod
    def components(self) -> List[Component]:
        pass

    def needs_service(self) -> bool:
        return any(component.needs_service() for component in self.components)
