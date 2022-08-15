from car.component.models.engine import Engine
from car.service_checker.base import ServiceChecker
from car.service_checker.indicator_checker import IndicatorChecker


class SternmanEngine(Engine):
    def __init__(self, is_warning_indicator_on: bool) -> None:
        self._service_checker = IndicatorChecker(is_warning_indicator_on)

    @property
    def service_checker(self) -> ServiceChecker:
        return self._service_checker

    @service_checker.setter
    def service_checker(self, value):
        self._service_checker = value
