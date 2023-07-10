import unittest
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.battery import Battery

class TestCalliope(unittest.TestCase):
    def test_needs_service(self):
        # Test the needs_service() method of Calliope engine and battery
        # Create an instance of Calliope
        last_service_date = ...
        current_mileage = ...
        last_service_mileage = ...
        car = Calliope(last_service_date, current_mileage, last_service_mileage)

        # Make assertions to validate the behavior of needs_service() method
        self.assertTrue(car.needs_service())
        self.assertFalse(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_needs_service(self):
        # Test the needs_service() method of Glissade engine and battery
        # Create an instance of Glissade
        last_service_date = ...
        current_mileage = ...
        last_service_mileage = ...
        car = Glissade(last_service_date, current_mileage, last_service_mileage)

        # Make assertions to validate the behavior of needs_service() method
        self.assertTrue(car.needs_service())
        self.assertFalse(car.needs_service())

class TestBattery(unittest.TestCase):
    def test_needs_service(self):
        # Test the needs_service() method of Battery
        # Create an instance of Battery
        last_service_date = ...
        warning_light_is_on = ...
        battery = Battery(last_service_date, warning_light_is_on)

        # Make assertions to validate the behavior of needs_service() method
        self.assertTrue(battery.needs_service())
        self.assertFalse(battery.needs_service())

class TestBattery(unittest.TestCase):
    def test_needs_service(self):
        # Testing the needs_service() method of Battery with the upgraded Spindler battery.
        # Created an instance of Battery.
        last_service_date = datetime.today().date().replace(year=datetime.today().year - 3)
        warning_light_is_on = False
        battery = Battery(last_service_date, warning_light_is_on)

        # Making assertions to validate the behavior of needs_service() method
        self.assertTrue(battery.needs_service())
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()

