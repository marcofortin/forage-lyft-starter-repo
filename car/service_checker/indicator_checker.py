from car.service_checker.base import ServiceChecker


class IndicatorChecker(ServiceChecker):
    def __init__(self, is_warning_indicator_on: bool):
        self._is_warning_indicator_on = is_warning_indicator_on

    def needs_service(self) -> bool:
        return self._is_warning_indicator_on
