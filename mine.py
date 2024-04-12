import hashlib

nonce_limit = 100000000000
zeros = 4
def mine(index, data, prev_hash):
    for nonce in range(nonce_limit):
        base_text = str(index) + str(data) + str(prev_hash) + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeros):
            print(f"Nonce found: {nonce}")
            print(f"Hash with nonce: {hash_try}")
            return nonce
    return -1

def normal_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
index = 3
data = "Data 1"
prev_hash = "7d897d897as7ad8"

combined_text = str(index) + str(data) + str(prev_hash)
print(f"Normal Hash: {normal_hash(combined_text)}")
nonce = mine(index,data,prev_hash)
print(f"nonce & normal hash: {normal_hash(combined_text + str(nonce))}")

