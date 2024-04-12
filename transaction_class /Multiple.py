import time

class Transaction:
    def __init__(self, amount, date, sender, receiver):
        self.amount = amount
        self.date = date
        self.sender = sender
        self.receiver = receiver

    def send_money(self):
        if(self.amount > self.sender.balance):
            print("Insufficient funds")
            return False

        self.sender.balance -= self.amount
        self.receiver.balance += self.amount
        
        # add trancation in trancation.txt file each trancation (',' seperated)
        file = open("transaction.txt", "a")
        file.write(str(self.amount) + "," + str(self.date) + "," + self.sender.name + "," + self.receiver.name + "\n")
         

    def display_transaction(self):
        print("-------------------------")
        print("|\tTransaction Info\t|")
        print("-------------------------")
        print(f"| Amount: {self.amount}\t\t|")
        print(f"| Date:  {self.date}\t|")
        print(f"| Sender :  {self.sender.name}\t|")
        print(f"| Receiver :  {self.receiver.name}\t|")
        print("-------------------------")
        # print("Amount: ", self.amount)
        # print("Date: ", self.date)
        # print("Sender: ", self.sender.name)
        # print("Receiver: ", self.receiver.name)

class Account:
    def __init__(self, name,account_number,balance):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def display_account(self):
        print("-------------------------")
        print("|\tAccount Info\t|")
        print("-------------------------")
        print(f"| Name: {self.name}\t\t|")
        print(f"| Account Number:  {self.name}\t|")
        print(f"| Balance :  {self.balance}\t|")
        print("-------------------------")


# Create Account using User values
def create_account():
    name = input("Enter Name: ")
    account_number = input("Enter Account Number: ")
    balance = int(input("Enter Balance: "))
    account = Account(name, account_number, balance)
    return account

# Create Transaction using User values
def create_transaction(sender, receiver):
    amount = int(input("Enter Amount: "))
    date = time.strftime("%d/%m/%Y")
    transaction = Transaction(amount, date, sender, receiver)
    return transaction

def display_all_transaction():
    file = open("transaction.txt", "r")
    for line in file:
        transaction = line.split(",")
        print("-------------------------")
        print("|   Transaction Info    |")
        print("-------------------------")
        print(f"| Amount: {transaction[0]}\t\t|")
        print(f"| Date:  {transaction[1]}\t|")
        print(f"| Sender:  {transaction[2]}\t|")
        print(f"| Receiver: {transaction[3]}     |")
        print("-------------------------")

account1 = create_account()
account2 = create_account()

transaction1 = create_transaction(account1, account2)
transaction1.send_money()

transaction2 = create_transaction(account2, account1)
transaction2.send_money()

transaction1.display_transaction()
display_all_transaction()