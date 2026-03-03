class Account:
    user_name: str
    password: str
    tweets: list

    def __init__(self, user_name, password, tweets, id):
        self.id = (id,)
        self.user_name = (user_name,)
        self.password = (password,)
        self.tweets = tweets


ACCOUNTS: dict


def create_accounts(name, password):
    if name not in ACCOUNTS:
        if ACCOUNTS == 0:
            id = 1
        else:
            id = id + 1
            ACCOUNTS[name] = Account(id=id, user_name=name, password=password)

    else:
        print("user name is already exist")


def login_verification(name, password):
    if name not in dict:
        print("enter a valid user name")
        return 0
    elif ACCOUNTS[name].password != password:
        print("entered password is invalid")
        return 0
    elif name in ACCOUNTS and ACCOUNTS[name].password == password:
        print("login successful")
        return 1


def post_tweet():
    print("enter youre name")


def twitter_logined():
    action = 0
    while action != 100:
        print("1:post tweet\n2:view profiles")
        action = int(input("enter a action : "))
        if action == 1:
            post_tweet()
        if action == 2:
            view_profile()
        if action == 3:
            logout()


def twitter():
    login = 0
    while login != 100:
        print("1:create account\n2:login account\n3:close page")
        login = int(input("enter a number"))
        if login == 1:
            name = input("enter the user name")
            password = input("enter the password")
            create_accounts(name, password)
        elif login == 2:
            name = input("enter the user name")
            password = input("enter the password")
            verified = login_verification(name, password)
            if verified == 0:
                print("try again")
            elif verified == 1:
                print("youre login to account")
            else:
                print("some errror in verofication")
        elif login == 3:
            login = 100
            print("thanks for using twitter")
