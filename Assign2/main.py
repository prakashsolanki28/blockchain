# RSA algorithm used for encryption and decryption
# data used is numbers or string
# creators : RSA - Rivest, Shamir, Adleman : 1977

# each user has a pair of keys: public and private
# public: made available to anyone who wants to send a message to user and encrypt msg using it
# private: kept secret to decrypt the msg

# To encrypt a message, the sender uses the recipient’s public key to encrypt the message. To decrypt the message, the recipient uses their private key to decrypt it.
# signature(s) = m^d mod n
# verify signature = s^e mod n

from math import gcd
import random

def is_prime(num):
    if num<2:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

def generate_prime(min,max):
    prime = random.randint(min,max)
    while not is_prime(prime):
        prime = random.randint(min,max)
    return prime

def mod_inverse(e,phi):
    for d in range(3,phi):
        if (d * e) % phi == 1:
            return d
        # raise ValueError("mod inverse does not exist")

p,q = generate_prime(1000,5000), generate_prime(1000,5000)

while p == q:
    q = generate_prime(1000,5000)
# public
n = p * q
# totient: how many numbers are there which are <n and co-prime to n
phi_n = (p-1) * (q-1)
# gcd(e,phi_n)=1 ; 1<e<t
# selecting public key, e

# e = random.randint(3, phi_n-1)
# while gcd(e, phi_n) != 1:
#     e = random.randint(3,phi_n-1)

for i in range(2, phi_n):
    if gcd(i, phi_n) == 1:
        e = i
        break

d = mod_inverse(e,phi_n)
msg = "Hello World"
print("Original message:", msg)

# convert string to ASCII
# ord() returns ASCII value of s single character
# to convert string, iterate over each character in string
# list comprehension
msg_convert = [ord(ch) for ch in msg]

# cipher text(c) = m^e mod n
# (c^e) mod n
msg_encode = [pow(ch,e,n) for ch in msg_convert]

print("Encoded message :", msg_encode)
# decrypt(d) = c^d mod n
# msg_decode = (msg_encode ** d) % n
msg_decode = [pow(ch,d,n) for ch in msg_encode]
msg = "".join(chr(ch) for ch in msg_decode)
print("Decoded message: ",msg)
