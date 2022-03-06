from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode
from utils_demo import *

starterKey = bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
def funnyDecryptTime(ptxt,ctxt,nonce):
    percent = 0
    for i in range(16777215):
        key = starterKey + i.to_bytes(3,'big')
        pt = decryptor_CTR(ctxt = ctxt, nonce = nonce, key = key)
        if string_to_bytes(string_value = ptxt) == pt:

            print("Key: " + key.hex() + " Message: " + pt.decode('utf-8').encode('cp1252').decode('utf-8'))
            return None
        if (i%335544) == 0:
            print(str(percent) + "% of keys searched")
            print(key.hex() + " Key currently being run")
            percent = percent + 2;
            
 # Read in cipher, plaintext, and nonce 
for n in range(3):
    plaintext = input("Enter what file is the plaintext: ")
    plaintextFile = read_file(fn = plaintext)
    print(plaintextFile)
    ciphertext = input("Enter what file is the ciphertext: ")
    ciphertextFile = read_bytes(fn = ciphertext)
    nonce = input("Enter what file is the nonce: ")
    nonceFile = read_bytes(fn = nonce)
    funnyDecryptTime(plaintextFile,ciphertextFile,nonceFile)

