# pip install pycryptodome
from Crypto.Cipher import AES
import base64

pad   = lambda s: s + (16 - len(s) % 16) * ' '
unpad = lambda s: s.rstrip()

def aes_encrypt(text, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(text).encode())).decode()

def aes_decrypt(ciphertext, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(ciphertext)).decode())


# ---- Test ----
text = "Pillai University"
key = "mysecretkey123"

cipher = aes_encrypt(text, key)
plain  = aes_decrypt(cipher, key)

print("\n--- AES Encryption & Decryption ---")
print("Plaintext  :", text)
print("Key        :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", plain)
