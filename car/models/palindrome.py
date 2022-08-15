from datetime import datetime
from typing import List

from car.component.battery.models.spindler_battery import SpindlerBattery
from car.component.engine.models.sternman_engine import SternmanEngine
from car.component.models.base import Component
from car.models.base import Car


class Palindrome(Car):
    def __init__(
        self, last_service_date_utc: datetime.date, is_warning_indicator_on: bool
    ):
        self._components = [
            SpindlerBattery(last_service_date_utc),
            SternmanEngine(is_warning_indicator_on),
        ]

    @property
    def components(self) -> List[Component]:
        return self._components
