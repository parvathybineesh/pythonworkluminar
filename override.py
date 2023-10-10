class Bike:
    def start(self):
        print("kicker start")
    def breaking(self):
        print("drum break")
class HeroHondaSplendor(Bike):
    def start(self):
        print("self start")
    def breaking(self):
        print("abs breaking")
hobj=HeroHondaSplendor()
hobj.start()
hobj.breaking()

