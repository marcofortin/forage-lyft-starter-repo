import datetime

from car.component.models.battery import Battery
from car.service_checker.base import ServiceChecker
from car.service_checker.lifetime_checker import LifetimeChecker


class SpindlerBattery(Battery):
    _YEARS_THRESHOLD: int = 2

    def __init__(self, last_service_date_utc: datetime.date) -> None:
        self._service_checker = LifetimeChecker(
            self._YEARS_THRESHOLD, last_service_date_utc
        )

    @property
    def service_checker(self) -> ServiceChecker:
        return self._service_checker

    @service_checker.setter
    def service_checker(self, value):
        self._service_checker = value
