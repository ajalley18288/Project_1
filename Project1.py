from Cryptodome.Cipher import AES

starterKey = bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

for i in range(16,777,215):
    key1 = starterKey + i.to_bytes(3,'big')
    print(key1)
    # Test if deciphered message equals our plaintext mesage
    # if they do exit loop
    # if not reset key

for i in range(16,777,215):
    key2 = starterKey + i.to_bytes(3,'big')
    # Test if deciphered message equals our plaintext mesage
    # if they do exit loop
    
for i in range(16,777,215):
    key3 = starterKey + i.to_bytes(3,'big')
    # Test if deciphered message equals our plaintext mesage
    # if they do exit loop   

# cipher = AES.new(key, AES.MODE_EAX);

