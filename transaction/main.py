import hashlib
import time

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def show(self):
        print(f"Timestamp: {self.timestamp}")
        print(f"Amount: {self.amount}")
        print(f"Sender: {self.sender.balance}")
        print(f"Recipient: {self.recipient.balance}")
        print("\n")

    def send_money(self):
        if self.sender.balance >= self.amount:
            self.sender.balance -= self.amount
            self.recipient.balance += self.amount
            print("Transaction successful")
        else:
            print("Transaction failed")
class Account:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance

class Block:
    def __init__(self, index, prev_hash, timestamp, transactions, hash):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash

    def show_block(self):
        print(f"Block #{self.index}")
        print("Transaction")
        self.transactions.show()
        print("\n")

class Blockchain:
    def __init__(self):
        self.chain = [self.genesis()]

    def genesis(self):
        transaction = Transaction(Account("Genesis", 1000), Account("Ishita",120),100)
        transaction.send_money()
        return Block(0, "0", time.time(), transaction, self.calc_hash(0, "0", time.time(), transaction))

    def calc_hash(self, index, prev_hash, timestamp, transactions):
        value = f"{index}{prev_hash}{timestamp}{transactions}"
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def new_block(self, transaction):
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_timestamp = time.time()
        new_hash = self.calc_hash(new_index, previous_block.hash, new_timestamp, transaction)
        new_block = Block(new_index, previous_block.hash, new_timestamp, transaction, new_hash)
        return new_block

    def AddBlock(self, new_block):
        self.chain.append(new_block)

blockchain = Blockchain()

transaction = Transaction(Account("Alice",500), Account("Rishika",300),1000)
transaction.send_money()
# transaction.show()
block1 = blockchain.new_block(transaction)
blockchain.AddBlock(block1)

for block in blockchain.chain:
    block.show_block()
