from abc import ABC,abstractmethod
class BankingApp():
    @abstractmethod
    def fund_transfer(self):
        pass
    @abstractmethod
    def bal_enq(self):
        pass

class PhonePay(BankingApp):
    def fund_transfer(self):
        print("phone pay fund transfer")
    def bal_enq(self):
        print("bal_enq")

pp=PhonePay()
pp.fund_transfer()
pp.bal_enq()

    
