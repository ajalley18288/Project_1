from Cryptodome.Cipher import AES

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





for i in range(16,777,215):
    key1 = starterKey + i.to_bytes(3,'big')
    print(key1)
    # Test if deciphered message equals our plaintext mesage
    plaintext = input("Enter what file is the plaintext: ")
    ciphertext = input("Enter what file is the ciphertext: ")

    decrypted_message = cipher_decrypt(ciphertext, i)
    print("For key {}, decrypted text: {}".format(i, plaintext))

    # if they do exit loop
    # if not reset key

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

