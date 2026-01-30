def clean(t): 
    return "".join(c for c in t.upper() if c.isalpha())

def vernam_encrypt(pt, key):
    pt, key = clean(pt), clean(key)
    if len(pt) != len(key):
        raise ValueError("Key length must equal plaintext length")
    return "".join(chr((ord(p)+ord(k)-130)%26 + 65) for p,k in zip(pt,key))

def vernam_decrypt(ct, key):
    ct, key = clean(ct), clean(key)
    return "".join(chr((ord(c)-ord(k)+26)%26 + 65) for c,k in zip(ct,key))


# ---- Test ----
pt = "HELLO"
key = "XMCKL"

ct = vernam_encrypt(pt, key)
print("Plaintext :", pt)
print("Key       :", key)
print("Ciphertext:", ct)
print("Decrypted :", vernam_decrypt(ct, key))
