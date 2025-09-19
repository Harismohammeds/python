class BankAccount:
    def __init__(self, account_number, balance, name):
        self.__account_number = account_number
        self._balance = balance
        self.name = name

    def deposit(self, amount):
        self._balance += amount
        print("deposited", amount, "newbalance:", self._balance)

    def withdraw(self, amount):
        if amount > self._balance:
            print("not enough money")
        else:
            self._balance -= amount
            print("withdraw", amount, "new balance", self._balance)

    def show_details(self):
        print("account holder name:", self.name)
        print("account number:", self.__account_number)

acc = BankAccount(12345678, 1000, "Haris")
acc.deposit(200)
acc.withdraw(200)
