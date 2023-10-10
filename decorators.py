#used to avoid repeatation
#without no change in function definition

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @property
    def get_name(self):

        return self.name
    @property
    def get_age(self):

        return self.age
    
obj=Student("hari",25)

print(obj.get_name)
print(obj.get_age)