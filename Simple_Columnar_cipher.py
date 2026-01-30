# Simple Columnar Technique
from pycipher import ColTrans

plaintext = "WEAREDISCOVEREDFLEEATONCE"
key_list = [3, 1, 4, 2]

key = "".join(map(str, key_list))
cipher = ColTrans(key).encipher(plaintext)
decipher = ColTrans(key).decipher(cipher)

print("Original :", plaintext)
print("Encrypted:", cipher)
print("Decrypted :", decipher)
