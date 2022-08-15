from car.component.models.engine import Engine
from car.service_checker.base import ServiceChecker
from car.service_checker.millage_checker import MileageChecker


class WilloughbyEngine(Engine):
    _MILEAGE_THRESHOLD: int = 60000

    def __init__(self, last_service_mileage: int, current_mileage: int) -> None:
        self._service_checker = MileageChecker(
            self._MILEAGE_THRESHOLD, last_service_mileage, current_mileage
        )

    @property
    def service_checker(self) -> ServiceChecker:
        return self._service_checker

    @service_checker.setter
    def service_checker(self, value):
        self._service_checker = value
