class Dress:
    data=[
        {"id":1,"name":"salwar","material":"rayon","price":3400},
        {"id":2,"name":"churidhar","material":"georgette","price":2400},
        {"id":3,"name":"skirt","material":"crepe","price":640},
        {"id":4,"name":"palazzo","material":"cotton","price":740},
        {"id":5,"name":"jeans","material":"semicotton","price":2000},
        {"id":6,"name":"tshirt","material":"baniyan","price":140},
    ]

    def get(self,*args,**kwargs):
        return self.data
    
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[ dr for dr in self.data if dr.get("id")==id]
        return record
    
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[ d for d in self.data if d.get("id")==id].pop()
        self.data.remove(obj)

    
obj=Dress()
obj.destroy(id=5)
#print(obj.get())
#print(obj.retrieve(id=5))
#obj.create(id=7,name="saree",material="silk",price=1400)
print(obj.get())
    

    