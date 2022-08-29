import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from datetime import datetime


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.3, 0.3, 0.4]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.4, 0.2, 0.3, 0.3]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())



class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.3, 0.5, 0.6, 0.6]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.3, 0.5]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())