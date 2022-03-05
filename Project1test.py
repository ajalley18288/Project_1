from Cryptodome.Cipher import AES
from utils_demo import *

starterKey = bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

encoding = ["utf8", "cp1525"]
 # Read in cipher, plaintext, and nonce 
for n in range(3):
    plaintext = input("Enter what file is the plaintext: ")
    f = open(plaintext, "r")
    plaintextFile = f.read()
    f.close()
    ciphertext = input("Enter what file is the ciphertext: ")
    f = open(ciphertext, encoding = "cp437")
    ciphertextFile = f.read()
    f.close()
    nonce = input("Enter what file is the nonce: ")
    f = open(nonce, encoding = "cp437")
    nonceFile = f.read()
    f.close()
    funnyDecryptTime(plaintextFile,ciphertextFile,nonceFile)

def funnyDecryptTime(ptxt,ctxt,nonce):
    for i in range(16,777,215):
        key1 = starterKey + i.to_bytes(3,'big')
        print(key1)
        if ptxt == decryptor_CTR(ctxt, nonce, key1):
            return None