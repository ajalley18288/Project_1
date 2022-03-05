from Cryptodome.Cipher import AES
from utils_demo import *

starterKey = bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        else:

            decrypted += c

    return decrypted
    
encoding = ["utf8", "cp1525"]

for i in range(16,777,215):
    key1 = starterKey + i.to_bytes(3,'big')
    print(key1)
    # Read in cipher, plaintext, and nonce file
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
    ciphertextFile = f.read()
    f.close()
    try:
       cipher = AES.new(key1, AES.MODE_CTR, string_to_bytes(nonce))
       decrypted_message = cipher.decrypt(ciphertextFile)
    except ValueError as KeyError:
        print("Maybe next time")
    # decrypt using cipher = AES.new(key1, AES.MODE_CTR, nonce)
    # decrypted_message = cipher_decrypt(ciphertextFile, i)
    if decrypted_message == plaintextFile: 
        print("For key {}, decrypted text: {}".format(i, decrypted_message))
    # if decrypted_message == m1.txt
        # quit loop and display key 

for i in range(16,777,215):
    key2 = starterKey + i.to_bytes(3,'big')
    # Test if deciphered message equals our plaintext mesage
    plaintext = input("Enter what file is the plaintext: ")
    ciphertext = input("Enter what file is the ciphertext: ")

    decrypted_message = cipher_decrypt(ciphertext, i)
    print("For key {}, decrypted text: {}".format(i, plaintext))
    # if they do exit loop
    
for i in range(16,777,215):
    key3 = starterKey + i.to_bytes(3,'big')
    # Test if deciphered message equals our plaintext mesage
    plaintext = input("Enter what file is the plaintext: ")
    ciphertext = input("Enter what file is the ciphertext: ")

    decrypted_message = cipher_decrypt(ciphertext, i)
    print("For key {}, decrypted text: {}".format(i, plaintext))
    # if they do exit loop   

# cipher = AES.new(key, AES.MODE_EAX);