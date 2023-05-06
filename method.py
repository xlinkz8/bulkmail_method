#create a method will add, debit a user and then delete a function
#create a bank account 
#add user with  initial balance 
#debit from the balance
#delete account



class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    
    def add(self,amount):
        self.balance += amount


    def debit(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("insufficient balance")

    def delete(self):
        self.balance = 0
        print("account balance deleted")


account = BankAccount(25000)
account.add(400)
print(account.balance)

account.debit(500)
print(account.balance)

account.delete()
print(account.balance)
