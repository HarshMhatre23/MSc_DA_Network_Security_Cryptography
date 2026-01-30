import random
def power(base, exp, mod):
    return pow(base, exp, mod)
def generate_keys():
    p = 23      # Prime number (small for demonstration)
    g = 5       # Primitive root of p

    x = random.randint(1, p-2)   # Private key
    y = power(g, x, p)           # Public key

    return p, g, x, y

# Encryption
def encrypt(message, p, g, y):
    k = random.randint(1, p-2)   # Random session key
    a = power(g, k, p)
    b = (power(y, k, p) * message) % p
    return a, b

# Decryption
def decrypt(a, b, p, x):
    s = power(a, x, p)
    s_inv = pow(s, -1, p)        # Modular inverse
    message = (b * s_inv) % p
    return message

# Main Program
p, g, x, y = generate_keys()

print("Public Key (p, g, y):", p, g, y)
print("Private Key (x):", x)
msg = int(input("\nEnter message (number < p): "))
a, b = encrypt(msg, p, g, y)
print("\nEncrypted Ciphertext (a, b):", a, b)
decrypted_msg = decrypt(a, b, p, x)
print("Decrypted Message:", decrypted_msg)

