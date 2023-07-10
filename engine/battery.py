from abc import ABC

from car import Car

class Battery:
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        # Checks if the battery needs service based on the last service date
        today = datetime.today().date()
        service_due_date = self.last_service_date.replace(year=self.last_service_date.year + 3) 
        return today > service_due_date

