class Employee:
    id:int
    name:str
    department:str
    gender:str

    def create(self,id,name,dept,gender):
        Employee.id=id
        self.name=name
        self.department=dept
        self.gender=gender

    def display_emp(self):

        print(self.id,self.name,self.department,self.gender)

    def __str__(self):
        return self.name

obj=Employee()
obj.create(1000,"hari","hr","male")
obj.display_emp()
print(obj)

            

    
