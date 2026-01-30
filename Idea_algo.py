# Short simplified IDEA-like encryption demo

def pad_blocks(s, n=8):
    return [s[i:i+n].ljust(n, '\0') for i in range(0, len(s), n)]

def xor_block(block, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(block, key))

def encrypt(text, key):
    return ''.join(xor_block(b, key[:8]) for b in pad_blocks(text))

def decrypt(cipher, key):
    return ''.join(xor_block(b, key[:8]) for b in pad_blocks(cipher)).rstrip('\0')

# Example
key = "12345678"
plaintext = "Hello IDEA Algorithm"

encrypted = encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Encrypted:", ''.join(f'{ord(c):02x}' for c in encrypted))
print("Decrypted:", decrypt(encrypted, key))
