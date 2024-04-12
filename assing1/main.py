# used for sha256 encryption
# secure hashing algorithm
# cryptographic hash function that outputs 256  bit long value.
# verify integrity of files by comparing the computed and original hash
# secure against attacks, verify transactions, create new blocks
import hashlib
import datetime as dt

# generate a block
class Block:
    # properties of block
    def __init__(self,index,timestamp,data,prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    # generate hash for the block using the properties
    def calc_hash(self):
        hash_str = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash)
        # hexadecimal format
        return hashlib.sha256(hash_str.encode()).hexdigest()

# contains all the blocks
class Blockchain:
    # create genesis block when an oject of blockchain is created
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, dt.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    # new_block is the block created with its properties
    def add_block(self,new_block):
        # adding prev_hash i.e hash of the last block
        new_block.prev_hash = self.get_latest_block().hash
        # generating hash for current block
        new_block.hash = new_block.calc_hash()
        # appending block in the chain
        self.chain.append(new_block)

    # validating block assuring it is tamper proof i.e if data changes, hash changes, making it easier to figure out who has made the change
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]

            if current_block.hash != current_block.calc_hash():
                return False

            if current_block.prev_hash != prev_block.hash:
                return False
        return True

bk = Blockchain()
bk.add_block(Block(1, dt.datetime.now(), "Data 1", ""))
bk.add_block(Block(2, dt.datetime.now(), "Data 2", ""))
bk.add_block(Block(3, dt.datetime.now(), "Data 3", ""))

for bk in bk.chain:
    print("Block #" + str(bk.index))
    print("Timestamp: " + str(bk.timestamp))
    print("Data: " + bk.data)
    print("Hash: " + bk.hash)
    print("Previous Hash: " + bk.prev_hash)
    print("\n")


