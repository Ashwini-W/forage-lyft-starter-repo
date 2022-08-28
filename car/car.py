from servicable import Servicable


class Car(Servicable):
    def __init__(self, Engine,Battery):
        self.engine = Engine
        self.battery = Battery
        
    def needs_service(self):
        pass
