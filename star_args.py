class Calculator:
    def add(self,*args):
        return sum(args)
obj=Calculator()
print(obj.add(10,20))