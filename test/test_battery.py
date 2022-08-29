import unittest
import battery
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.today.replace(year=self.today.year - 5)
        nubbin_battery = NubbinBattery(last_service_date,self.today)
        self.assertTrue(nubbin_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=self.today.year - 1)
        n_battery = NubbinBattery(last_service_date,self.today)
        self.assertFalse(n_battery.needs_service())


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.today.replace(year=today.year - 4)
        spindler_battery = SpindlerBattery(last_service_date, self.today)
        self.assertTrue(spindler_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.today.replace(year=today.year - 1)
        s_battery = SpindlerBattery(last_service_date, self.today)
        self.assertFalse(s_battery.needs_service())