import datetime

from car.service_checker.base import ServiceChecker


class LifetimeChecker(ServiceChecker):
    def __init__(self, years_threshold: int, last_service_date_utc: datetime.date):
        self._years_threshold = years_threshold
        self._last_service_date_utc = last_service_date_utc

    def needs_service(self) -> bool:
        service_threshold_date_utc = self._last_service_date_utc.replace(
            year=self._last_service_date_utc.year + self._years_threshold
        )
        return datetime.datetime.utcnow().date() >= service_threshold_date_utc
