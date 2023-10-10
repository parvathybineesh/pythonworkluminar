class Employee:
    data=[
        {"id":1,"name":"jhon","dept":"hr","salary":34000},
        {"id":2,"name":"hari","dept":"it","salary":24000},
        {"id":3,"name":"ravi","dept":"qa","salary":64000},
        {"id":4,"name":"vijay","dept":"hr","salary":74000},
        {"id":5,"name":"tom","dept":"it","salary":24000},
        {"id":6,"name":"vipin","dept":"qa","salary":14000},
        
    ]

    #return all employee records list
    #employee detail
    #add employe
    #edit
    #delete


    def get(self,*args,**kwargs):
        return self.data
    
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[ emp for emp in self.data if emp.get("id")==id]
        return record
    
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[ e for e in self.data if e.get("id")==id].pop()
        self.data.remove(obj)

    def update(self,id=None,*args,**kwargs):
        id=id
        obj=[ emp for emp in self.data if emp.get("id")==id][0]
        obj.update(kwargs)
        print("employee object updated")

obj=Employee()
#obj.destroy(id=4)
#print(obj.retrieve(id=4))
#obj.create(id=7,name="parvathy",dept="hr",salary=25000)
#print(obj.get())
obj.update(id=4,name="hari",salary=24000)
print(obj.retrieve(id=4))