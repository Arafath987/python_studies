from collections import OrderedDict


class Account:
    name: str
    account_number: int
    balance: int


ACCOUNTS = OrderedDict()
ACCOUNTS = {123: Account("yaser", 123, 10000), 124: Account("sreehari", 124, 10000)}
last_account_number = 124


def add_account(name):
    last_account_number = +1
    ACCOUNTS[last_account_number] = Account(name, last_account_number, 0)
    return ACCOUNTS[last_account_number]


def withdraw(account_number):
    debite_amount = int(input("enter the amount to withdraw"))
    ACCOUNTS[account_number].balance = -debite_amount
    return ACCOUNTS[account_number].balance


def depposite(account_number):
    credit_amount = int(input("enter the amount to depposite"))
    ACCOUNTS[account_number].balance = +credit_amount
    return ACCOUNTS[account_number].balance


def transaction(account_number_debit, account_number_credit):
    transaction_amount = int(input("enter the amount to transact"))
    ACCOUNTS[account_number_debit].balance = -transaction_amount
    ACCOUNTS[account_number_credit].balance = +transaction_amount
    return ACCOUNTS[account_number_debit].balance


def view_balance(account_number):
    return ACCOUNTS[account_number].balance


def view_account_detail(account_number):
    return ACCOUNTS[account_number]


def bank():
    select = 0
    while select != 7:
        print(
            "1:add_account,2:withdraw,3:depposite,4:transaction,5:view_balance,6:view_account_detail,7:close"
        )
        try:
            select = int(input("Select option: "))
        except ValueError:
            print("Invalid input. Choose a number!")
            continue

        if select == 1:
            name=int(input("enter the name of account holder"))
            add_account(name)
        elif select == 2:
            a=withdraw(account_number=int(input("enter the withdraw account number")))
            
        elif select == 3:
            print("Depositing money...")
        elif select == 4:
            print("Performing transaction...")
        elif select == 5:
            print("Viewing balance...")
        elif select == 6:
            print("Viewing account details...")
        elif select == 7:
            print("Closing app...")
        else:
            print("Invalid option. Try again!")
