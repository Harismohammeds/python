class bank_account:
    __bank_balance=30000
    def __init__(self):
        self.bank_balance=30000
        print("welcome")
    def _acc_num(self):
        print("Account number is AC-123456789")
    def acc_holder(self):
        print("Haris")
class withdraw(bank_account):
    def withdrawal(self,amount):
        if(amount<=self.bank_balance):
            self.bank_balance=self.bank_balance-amount
            print("withdrawal successful...Remaining balance is ",self.bank_balance)
class deposit(withdraw):
    def depo(self,amount):
        self.bank_balance=self.bank_balance+amount
        print("Deposit successful....current balance is ",self.bank_balance)
x=withdraw()
x.withdrawal(4000)
y=deposit()   
y.depo(3000)