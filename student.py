
class Student:
    id:int
    name:str
    age:int
    course:str

    def __init__(self,id,name,age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course

    def display_Student(self):
        print(self.name,self.course)

    def __str__(self) -> str:
        return self.name

obj1=Student(100,"hari",25,"bca")
obj1.display_Student()

print(obj1)