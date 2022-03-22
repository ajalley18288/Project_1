# Project_1
Introduction
________________


        In the world of cyberspace, brute force attacks can be extremely helpful against individuals that use simple passwords or insecure encryption algorithms. A brute force attack is a cryptographic hack that aims at randomizing combinations of a targeted password until the correct key is guessed. The complexity of a password and encrypting algorithm being used can determine the likeliness of a brute force being successful. A complex password can be recognized with the following characteristics, 15 characters in length, including letters, numbers, a capitalized letter, and special characters. A strong encrypting algorithm can be recognized as one that uses a large number as is a cryptographic key. The bigger the key, the longer it would take for a brute force attack to break the code. 
        Students were introduced to the task of writing a program that would run an exhaustive brute force attack against a block cipher. A block cipher can be recognized as an encryption algorithm that is fixed on block size values. Block ciphers are most efficient when encrypting data of fixed, known, amounts and can be used in protocols such as SFTP, HTTPS, and FTPS. Therefore this experiment allowed students to better understand the importance of using standard encryption algorithms, as well as complex passwords. 
        For this particular experiment, three plaintext-ciphertext pairs are given to us with their corresponding nonces. A nonce is created with each corresponding encryption and functions as a value of adding a unique id to each time something is encrypted. The same nonce is needed for decryption and the nonce can be recognized as layered security to avoid replay attacks. Therefore a nonce is a key information needed in finding the encryption key. Users without the nonce are incapable of brute-forcing keys.
        We understand that the encryption algorithm used for the files is Advanced Encryption Standard-128. AES-128 functions as a symmetric encryption block cipher algorithm that encrypts at a chunk, or block size of 128 bits. The current standard and highest form of encryption is AES-256. As blocks are encrypted they are joined together to create the ciphertext. The project was limited to an encryption key space value of 24 bits, which corresponds to a maximum numerical value of 16,777,215. This number was calculated by using the following formula, 2n-1, n equaling 24. Meaning the first 104 bits of the encryption can be disregarded, assuming it is the same for the given plaintext messages. The information we know about the key is that the value of the first byte is equal to 1 as the rest of the first 13 bytes are equal to 0. This allows us to focus on the last three bytes through exhaustive search. Identifying the last three bytes would allow us to find the encrypted key used for the given plaintext-ciphertext pairs. The task can be summarized as writing a program that would identify a key used to encrypt a plaintext message. The following sections will expand upon our approach and how we managed to identify the encrypting keys.  


Description of Program
________________


        For our program, it is relatively simple when using the given functions from the setup program. First, we use the read functions which open the files and reads them into either a byte map or a string. 
  

After reading in the message the cipher and the nonce we begin the process of brute-forcing the key. We begin a loop that goes from 0 to 16,777,215. The iterator of the loop is then appended onto a byte array and sent to the decrypt function provided to us. This function does the aes decrypt function provided by cryptodome using the key that was just generated, the cipher, and the nonce value.
     
After the plaintext is returned it is compared to the default text that was read in at the beginning. It’s important to know that the decrypt function returns a bitstring/ byte array so the plaintext had to be converted before comparing. If the two values were equal we would output the key and the message at the end.
  

We did add some accessibility features that say how many keys have been searched because otherwise, the program searches on a blank screen and a line that outputs the current key when it does that to show that the keys are changing.
  



Struggles and Improvements
________________


Our biggest struggles were not particularly related to the assignment at hand. They were more related to reading in the files because we did not see the functions within the utils file and outputting the strings in a readable format. To solve the reading problem we simply began using the provided functions instead of trying to read them in manually. To solve the problem with outputs was slightly more tricky. This resulted from python assuming we were using a certain encoding and creating weird symbols when the strings were outputted. To solve this we would encode the strings using the cp1252 codec then decoding them again using utf-8 in order to make sure none of the symbols were lost. 
________________
Results and Analysis of Data with Screenshots
________________




Message 1
The following shows the output of decrypting the first message. Initially, the program script is run following the plaintext of message one, the ciphertext of message one, and the nonce of message one. The key is then calculated and presents the following plaintext message, ‘UNT is more than a university.”


  



Message 2
The following shows the output of decrypting the second message. Initially, the program script is run following the plaintext of message two, the ciphertext of message two, and the nonce of message two. The key is then calculated and presents the following plaintext message, ‘It’s your home away from home.”


  



Message 3
The following shows the output of decrypting the third message. Initially, the program script is run following the plaintext of message three, the ciphertext of message three, and the nonce of message three. The key is then calculated and presents the following plaintext message, ‘We Are the Mean Green Family.”


  



________________


References
________________
        ajalley18288. (2022, March 3). Project_1. GitHub. https://github.com/ajalley18288/Project_1
        PyCryptodome — PyCryptodome 3.9.9 documentation. (n.d.). Pycryptodome.readthedocs.io. https://pycryptodome.readthedocs.io/en/latest/src/introduction.html
‌
