# pip install pycryptodome
from Crypto.Cipher import DES
import base64

pad = lambda s: s + (8 - len(s) % 8) * ' '
unpad = lambda s: s.rstrip()

def des_encrypt(text, key):
    key = key.ljust(8)[:8].encode()
    cipher = DES.new(key, DES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(text).encode())).decode()

def des_decrypt(ciphertext, key):
    key = key.ljust(8)[:8].encode()
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(ciphertext)).decode())


# ---- Test ----
text = "HELLO WORLD"
key = "secret12"

cipher = des_encrypt(text, key)
plain = des_decrypt(cipher, key)

print("\n--- DES Encryption & Decryption ---")
print("Plaintext  :", text)
print("Key        :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", plain)
