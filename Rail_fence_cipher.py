# short Rial fence
from pycipher import Railfence

text = "HELLO WORLD"
key = 3

cipher = Railfence(key).encipher(text)
plain  = Railfence(key).decipher(cipher)

print("Original Text :", text)
print("Encrypted Text:", cipher)
print("Decrypted Text:", plain)
