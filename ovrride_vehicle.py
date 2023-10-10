class Parent:
    vehicles=["passionpro","swift"]

    def properties(self):
        return self.vehicles
class Child(Parent):
    def properties(self):
        self.veh=super().properties()
        self.veh.append("hunter")
        return self.veh
ch=Child()
print(ch.properties())
    