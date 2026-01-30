# pip install pycipher
from pycipher import Playfair
import string

# Proper Playfair key (no J, 25 letters)
key = "MONARCHYBDEFGIJKLPQSTUVWXYZ"
cipher = Playfair(key)

plaintext = "HEllO WORLD"
print("PT:", plaintext)

# Remove spaces & non-letters, convert to uppercase
plaintext = "".join(c for c in plaintext.upper() if c in string.ascii_uppercase)

encrypted = cipher.encipher(plaintext)
print("Encrypted:", encrypted)

decrypted = cipher.decipher(encrypted)
print("Decrypted:", decrypted)
