import hashlib
import datetime

class Node:
    def __init__(self, data, index, previous_hash=None):
        self.data = data
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now()
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_node = Node("Genesis Block", 0)
        self.chain.append(genesis_node)

    def add_node(self, data):
        index = len(self.chain)
        previous_hash = self.chain[index-1].hash
        node = Node(data, index, previous_hash)
        self.chain.append(node)

    def print_chain(self):
        for node in self.chain:
            print("Index:", node.index)
            print("Timestamp:", node.timestamp)
            print("Data:", node.data)
            print("Hash:", node.hash)
            print("Previous Hash:", node.previous_hash)
            print()


blockchain = Blockchain()
blockchain.add_node("First Block")
blockchain.add_node("Second Block")
blockchain.add_node("Third Block")
blockchain.print_chain()