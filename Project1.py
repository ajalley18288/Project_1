from Crypto.Cipher import AES

starterKey = bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
integer = 0

for i in range(16,777,215)
    integer = integer+1
    # key = starterKey.append(integer)
    # Test if deciphered message equals our plaintext mesage
    # if they do exit loop
    # if not del key[12,15]

key1 = key
key = 0 # reset the key for next test
integer = 0
for i in range(16,777,215)
    integer = integer+1
    # key = starterKey.append(integer)
    # Test if deciphered message equals our plaintext mesage
    # if they do exit loop
    # if not del key[12,15]
key2 = key
key = 0 # reset the key for next test
integer = 0
for i in range(16,777,215)
    integer = integer+1
    # key = starterKey.append(integer)
    # Test if deciphered message equals our plaintext mesage
    # if they do exit loop
    # if not del key[12,15]
key3 = key
key = 0 # reset the key for next test     

cipher = AES.new(key, AES.MODE_EAX);

