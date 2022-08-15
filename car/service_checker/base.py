from abc import ABC, abstractmethod


class ServiceChecker(ABC):
    @abstractmethod
    def needs_service(self):
        pass
