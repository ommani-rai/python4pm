"""
fake banking system
parent class: User
    -> user details
child class: Bank
    -> deposit
    -> withdraw
    -> view balance
"""
class User:
    def __init__(self, name, age, gender):
        self.name = name # rahul
        self.age = age # 23
        self.gender = gender # male

    def view_detail(self):
        print("User Details:")
        print("")
        print("name: ", self.name)
        print("age: ", self.age)
        print("gender: ", self.gender)

# user = User("rahul", 23, "male")
# user.view_detail()

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def deposit(self, amount):
        self.balance = 5000
        self.amount = amount

        self.balance = self.balance + self.amount

        print("Your accout is updated.")
        print('Your new balance is: Rs.',self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.balance >= self.amount:
            self.balance = self.balance - self.amount

            print("You withdraw Rs.", self.amount)
            print("Your balance is reduced by: Rs.", self.amount)
            print("Your updated balance is Rs. ", self.balance)

        else:
            print("Insufficient fund | You have Rs.", self.balance)


bank = Bank("rhaul", 23, "male")
bank.deposit(1000)
bank.withdraw(3000)