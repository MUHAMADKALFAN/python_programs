class bank:
    def __init__(self,name,balance ):
        self.name=name
        self.balance=balance
       

    def display(self):
        print("Name",self.name)
        print("balance",self.balance)
  

    def getarea(self):
        self.crdit=int(input("Enter the RS:-"))
        self.balance+=self.crdit
        print(self.balance)

    def getarea1(self):
        self.debit=int(input("Ener the debit Rs:-"))
        self.balance-=self.debit
        print(self.balance)

bank1=bank("jon don",2500)
bank1.getarea()
bank1.getarea1()
# bank1.display()
.



