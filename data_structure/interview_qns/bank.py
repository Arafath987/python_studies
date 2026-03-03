class Bank:

    def __init__(self, balance: list):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > len(self.balance):
            return False
        if account2 < 1 or account2 > len(self.balance):
            return False
        if self.balance[account1 - 1] < money:
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if len(self.balance) >= account > 0:
            self.balance[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if len(self.balance) >= account > 0 and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False


# Test the Bank class
bank = Bank([100, 200, 300])
print(bank.deposit(1, 50))  # True, balance becomes [150, 200, 300]
print(bank.withdraw(2, 100))  # True, balance becomes [150, 100, 300]
print(bank.transfer(1, 3, 50))  # True, balance becomes [100, 100, 350]
print(bank.transfer(1, 4, 10))  # False, account 4 doesn't exist
print(bank.balance)  # Final balances: [100, 100, 350]
