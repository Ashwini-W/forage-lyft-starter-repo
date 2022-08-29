from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery
from tire import CarriganTires,OctoprimeTires

class CarFactory():
    @staticmethod
    def create_calliope(last_service_date, last_service_milage, current_milage,tire_wear):
        car_engine = CapuletEngine(last_service_milage, current_milage)
        car_battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(car_engine, car_battery,tires)

    @staticmethod
    def create_glissade(last_service_date, last_service_milage, current_milage,tire_wear):
        car_engine = WilloughbyEngine(last_service_milage, current_milage)
        car_battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(car_engine, car_battery,tires)

    @staticmethod
    def create_palindrome(last_service_date, warning_light_on,tire_wear):
        car_engine = SternmanEngine(warning_light_on)
        car_battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(car_engine, car_battery,tires)

    @staticmethod
    def create_rorschach(last_service_date, last_service_milage, current_milage,tire_wear):
        car_engine = WilloughbyEngine(last_service_milage, current_milage)
        car_battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(car_engine, car_battery,tires)

    @staticmethod
    def create_thovex(last_service_date, last_service_milage, current_milage,tire_wear),:
        car_engine = CapuletEngine(last_service_milage, current_milage)
        car_battery = NubbinBattery(last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(car_engine, car_battery,tires)