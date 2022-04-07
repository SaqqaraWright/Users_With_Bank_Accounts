class BankAccount:
    all_accounts=[]
    # don't forget to add some default values for these parameters!
    def __init__(self, balance=0, int_rate=0.02):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self) 

    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        print(f"New Balance = {self.balance}")
        return self

    def withdraw(self, amount):
        if (self.balance>amount): #States that if balance is less than amount then deduct $5 and print insufficient funds
            self.balance-=amount
        else:
            self.balance-=5
            print(f"Insufficient funds: Charging a $5 fee")
        print(f"New Balance = {self.balance}")
        return self

    def display_account_info(self):
        print(f"balance:{self.balance}")
        return self
    def yield_interest(self):
        if(self.balance>0):
            self.balance+=(self.int_rate*self.balance) #yield_interest= total balance*int_rate* (amt of time money has been in acct i.e year(s))        
            print(f"N/A") #not really necessary
        print(self)
        return self

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.account={
                    "personal": BankAccount(0), "savings": BankAccount(0)
        }

barbara=User("Barbara", "Wyatt", "bw@coolmail.com")
barbara.account["personal"].deposit(1000) #Barbara is a user with a bank account, she is not a bank account
print(barbara.first_name)



