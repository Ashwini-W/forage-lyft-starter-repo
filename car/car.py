from servicable import Servicable


class Car(Servicable):
    def __init__(self, Engine,Battery,Tire):
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire
        
    def needs_service(self):
        pass
