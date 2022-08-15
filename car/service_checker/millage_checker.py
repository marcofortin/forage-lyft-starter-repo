from car.service_checker.base import ServiceChecker


class MileageChecker(ServiceChecker):
    def __init__(self, threshold: int, last_service_mileage: int, current_mileage: int):
        self._threshold = threshold
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage > self._threshold
