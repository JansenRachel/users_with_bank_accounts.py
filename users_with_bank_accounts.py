class BankAccount:
    def __init__(self, int_rate = 0.025, balance = 0):
        self.rate = int_rate
        self.account_balance = balance


    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            # print("OK to withdraw")
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        print("Balance:", self.account_balance)
        return self

    # def transfer_money(from_name, to_name, amount):
    #     from_name.withdraw(amount)
    #     # print(self.account_balance)
    #     to_name.deposit(amount)

    def yeild_interest(self, int_rate):
        if self.account_balance > 0:
            amount = self.rate * self.account_balance
            self.account_balance += amount
            return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)


mitchell = User("Mitchell Caldwell", "mitchel@python.com")
kristy = User("Kristy Blair", "kristy@python.com")
darin = User("Darin James", "darin@python.com")

mitchell.account.deposit(250).deposit(550).deposit(100).withdraw(200).display_account_info()

kristy.account.deposit(200).deposit(250).withdraw(100).withdraw(175).display_account_info()

darin.account.deposit(800).withdraw(200).withdraw(300).withdraw(250).display_account_info()

# mitchell.account.transfer_money(darin, 100)
# mitchell.account.display_account_info()
# darin.account.display_account_info()