import hashlib
import time

class Transaction:
    def _init_(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def display_transaction(self):
        print(f"Timestamp: {self.timestamp}")
        print(f"Sender: {self.sender}")
        print(f"Recipient: {self.recipient}")
        print(f"Amount: {self.amount}")
        print("\n")

class Block:
    def _init_(self, index, prev_hash, timestamp, transactions, hash):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash

    def show_block(self):
        print(f"Block #{self.index}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Previous Hash: {self.prev_hash}")
        print("Transactions:")
        for transaction in self.transactions:
            transaction.display_transaction()
        print(f"Block Hash: {self.hash}")
        print("\n")

class Blockchain:
    def _init_(self):
        self.chain = [self.genesis()]

    def genesis(self):
        return Block(0, "0", time.time(), [], self.calc_hash(0, "0", time.time(), []))

    def calc_hash(self, index, prev_hash, timestamp, transactions):
        value = f"{index}{prev_hash}{timestamp}{transactions}"
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def new_block(self, transactions):
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_timestamp = time.time()
        new_hash = self.calc_hash(new_index, previous_block.hash, new_timestamp, transactions)
        new_block = Block(new_index, previous_block.hash, new_timestamp, transactions, new_hash)
        return new_block

    def AddBlock(self, new_block):
        self.chain.append(new_block)

blockchain = Blockchain()

transactions1 = [
    Transaction("Divya", "Khushi", 10.0),
    Transaction("Khushi", "Charlie", 5.0),
]
block1 = blockchain.new_block(transactions1)
blockchain.AddBlock(block1)

transactions2 = [
    Transaction("Charlie", "Divya", 8.0),
    Transaction("Khushi", "Divya", 3.0),
]
block2 = blockchain.new_block(transactions2)
blockchain.AddBlock(block2)

for block in blockchain.chain:
    block.show_block()
