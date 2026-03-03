class Account:
    name: str
    account_number: int
    balance: int

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance


ACCOUNTS = {1: Account("yaser", 1, 5), 2: Account("sreeri", 2, 10)}


def add_account():
    last = list(ACCOUNTS.keys())[-1]
    last = last + 1
    name = input("enter the account holder name")
    balance = int(input("enter the account balance"))

    account = Account(name, last, balance)
    ACCOUNTS[last] = account


def check_balance():
    account_number = int(input("enter account number : "))
    if account_number not in ACCOUNTS:
        print("enter a valid account number")
    else:
        balance = ACCOUNTS[account_number].balance
        print("account balance : ", balance)


def transaction():
    debit_account_number = int(input("enter account number of debited account : "))
    credit_account_number = int(
        input("enter account number u want to transact(credited account number) : ")
    )
    amount = int(input("enter the amount to transact : "))
    if credit_account_number not in ACCOUNTS or debit_account_number not in ACCOUNTS:
        if credit_account_number not in ACCOUNTS:
            print("enter a valid credited account number")
        else:
            print("enter a valid debited account number")
    elif (
        ACCOUNTS[debit_account_number].balance >= amount
        and credit_account_number in ACCOUNTS
        and debit_account_number in ACCOUNTS
    ):
        ACCOUNTS[debit_account_number].balance -= amount
        ACCOUNTS[credit_account_number].balance += amount

    else:
        print("error:your account has no available balance of " + str(amount))


def view_accounts():
    print("accounts:\n")
    for values in ACCOUNTS.values():
        print(values.__dict__)


def depposite():
    amount = int(input("enter amount to depposite"))
    account_number = int(input("enter the account number to depposite"))
    if account_number in ACCOUNTS and amount > 0:
        ACCOUNTS[account_number].balance += amount
    elif account_number not in ACCOUNTS:
        print("enter account number not valid")
    elif amount <= 0:
        print("enteer a valid amount")

    else:
        print("some error occured")


def withdraw():
    amount = int(input("enter amount to withdraw"))
    account_number = int(input("enter the account number to withdrae"))
    if (
        account_number in ACCOUNTS
        and amount > 0
        and amount <= ACCOUNTS[account_number].balance
    ):
        ACCOUNTS[account_number].balance -= amount
    elif account_number not in ACCOUNTS:
        print("entered account number not valid")
    elif amount <= 0:
        print("enteer a valid amount")
    elif amount > ACCOUNTS[account_number].balance:
        print(
            "youre account has not available of the balance\nyoure account balance : ",
            ACCOUNTS[account_number].balance,
        )

    else:
        print("some error occured")


def bank():
    action = 0
    while action != 100:
        print(
            "1:transaction\n2:depposite\n3:withdraw\n4:check_balance\n5:add account\n6:view accounts\n7:end action\n"
        )
        action = int(input("enter action : "))
        if action == 1:
            transaction()
        elif action == 2:
            depposite()
        elif action == 3:
            withdraw()
        elif action == 4:
            check_balance()
        elif action == 5:
            add_account()
        elif action == 6:
            view_accounts()
        elif action == 7:
            action = 100
            print("***********operations ended**********")
        else:
            print("\\\\\\\\\\\\\\\\\\enter a valid action///////////////")


bank()


dict = {1: 1, 3: 3, 2: 2}
