def accounts():
    account_1={
    "name":"yaser",
    "account_number":1,
    "balance":1,
    }
    account_2={
    "name":"arafath",
    "account_number":2,
    "balance":2
    }
    return [account_1,account_2]
    

def transaction(account_debited,account_credited,amount):
    if amount>account_debited["balance"]:
        print("*** error:account has insefficiant of balance ***")
    else:
        account_debited["balance"] =account_debited["balance"] - amount
        account_credited["balance"]=account_credited["balance"]+amount
    
    
    
def depposite(account,amount):
    account["balance"]=account["balance"]+amount
    
def with_draw(account,amount):
    account["balance"]=account["balance"]+amount
    
def check_account_balance(account):
    print("account balance : ",account["balance"])
    print("**********************************************************************")
    
def bank():
    [account1,account2] =accounts()
    action=0
    while action!=100:
        print("1:transaction\n2:depposite\n3:withdraw\n4:check_balance\n5:end_action\n")
        action=int(input("enter action : "))
        
        
        
        if action==1:
            amount=int(input("enter the amount to be transact : "))
            account_number_debited_account=int(input("enter the account number of debited account : "))
            account_number_credited_account=int(input("enter the account number of credited account : "))
            if account_number_debited_account==account1["account_number"] and account_number_credited_account==account2["account_number"]:
                transaction(account1,account2,amount)
            elif account_number_debited_account==account2["account_number"] and account_number_credited_account==account1["account_number"]:
                transaction(account2,account1,amount)
            else:
                print("enter a valid account number")
                
            
        elif action==2:
            amount=int(input("enter the amount to depposite : "))
            account_number=int(input("enter the account number : "))
            if account_number==account1["account_number"]:
                depposite(account1,amount)
            elif account_number==account2["account_number"]:
                depposite(account2,amount)
            else :
                print("enter a valid account_number")
                
        elif action==3:
            amount=int(input("enter the amount to depposite : "))
            account_number=int(input("enter the account number : "))
            if account_number==account1["account_number"]:
                with_draw(account1,amount)
            elif account_number==account2["account_number"]:
                with_draw(account2,amount)
            else :
                print("enter a valid account_number")
        elif action==4:
            account_number=int(input("account_number : "))
            if account_number==account1["account_number"]:
                check_account_balance(account1)
            elif account_number==account2["account_number"]:
                check_account_balance(account2)
        elif action==5:
            action=100
        
        else :
            print("enter a valid action")
    
    
bank()