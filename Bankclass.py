#Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
class Bank_Account():
    def __init__(self,acc_no,bal,date_open,cust_name):
        self.acc_no=acc_no
        self.bal=bal
        self.date_open=date_open
        self.cust_name=cust_name
        
    def deposit(self,amount):
        self.amount=amount
        self.bal=self.bal + self.amount
        return self.bal
    
    def withdraw(self,amount):
        self.amount=amount
        if self.amount <= self.bal:
            self.bal = self.bal-self.amount
            return self.bal
        else:
            print("Insufficien Balance,Not allowed to withdraw")
            
    def check_bal(self):
        return self.bal
    
acct=Bank_Account(12345678,50000,"11/11/2020","Vijay.J")
print("Account number is:",acct.acc_no)
print("Date of opening an Account is:", acct.date_open)    
print("Account Holder name is:",acct.cust_name)
acct.deposit(10000)
print("Balance(Deposit):",acct.check_bal())
acct.withdraw(3000)
print("Balance(withdraw):",acct.check_bal())

#Gross salary calculation
class Salary():
    def __init__(self, bs):
        self.bs = bs
        
    def da(self, da):
        self.da=da
        self.da = (self.bs) * (da) / 100
        return self.da
    
    def ha(self, ha):
        self.ha=ha
        self.ha = (self.bs) * (ha) / 100
        return self.ha
    
    def gross(self, da, ha):
        self.gross = self.bs + self.da + self.ha
        return self.gross
    
bs = 20000
salary = Salary(bs)
da = salary.da(40)
ha = salary.ha(20)
print(salary.gross(da, ha))