class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Eroare: Suma depusă trebuie să fie pozitivă!")
        else:
            self._balance += amount
            print(f"A fost depusă suma de {amount}. Sold actual: {self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Eroare: Suma retrasă trebuie să fie pozitivă!")
        elif amount > self._balance:
            print("Eroare: Fonduri insuficiente pentru retragere!")
        else:
            self._balance -= amount
            print(f"A fost retrasă suma de {amount}. Sold actual: {self._balance}")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.deposit(-50)
print(f"Sold final: {account.get_balance()}")
