from abc import ABC, abstractmethod

from car.service_checker.base import ServiceChecker


class Component(ABC):
    @property
    @abstractmethod
    def service_checker(self) -> ServiceChecker:
        pass

    def needs_service(self) -> bool:
        return self.service_checker.needs_service()
