from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode
from utils_demo import *



starterKey = bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
def funnyDecryptTime(ptxt,ctxt,nonce):
    percent = 0
    for i in range(16777215):
        key = starterKey + i.to_bytes(3,'big')
        pt = decryptor_CTR(ctxt = ctxt, nonce = nonce, key = key)
        if ptxt == pt:
            print("I have the golden ticket!")
            return None
        if (i%838860) == 0:
            print(str(percent) + "% done")
            percent = percent + 5;
            
 # Read in cipher, plaintext, and nonce 
for n in range(3):
    plaintext = input("Enter what file is the plaintext: ")
    plaintextFile = read_file(plaintext)
    print(plaintextFile)
    ciphertext = input("Enter what file is the ciphertext: ")
    ciphertextFile = read_bytes(ciphertext)
    nonce = input("Enter what file is the nonce: ")
    nonceFile = read_bytes(ciphertext)
    funnyDecryptTime(plaintextFile,ciphertextFile,nonceFile)

