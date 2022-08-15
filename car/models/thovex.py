from datetime import datetime
from typing import List

from car.component.battery.models.nubbin_battery import NubbinBattery
from car.component.engine.models.capulet_engine import CapuletEngine
from car.component.models.base import Component
from car.models.base import Car


class Thovex(Car):
    def __init__(
        self,
        last_service_date_utc: datetime.date,
        last_service_mileage: int,
        current_mileage: int,
    ):
        self._components = [
            NubbinBattery(last_service_date_utc),
            CapuletEngine(last_service_mileage, current_mileage),
        ]

    @property
    def components(self) -> List[Component]:
        return self._components
