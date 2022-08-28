from datetime import datetime
from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date,current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def needs_service(self):
        years = self.current_date - self.last_service_date
        if years < 2:
            return False
        else:
            return True