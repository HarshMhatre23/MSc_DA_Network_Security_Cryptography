import random
# Step 1: Agree on a large prime number (p) and a primitive root modulo p (g)
# For simplicity, we use small numbers here, but in real-world applications, use large safe primes (1024+ bits)
p = 23   # prime number
g = 5    # primitive root modulo p
print(f"Public parameters: p = {p}, g = {g}")
# Step 2: Each party selects a private key
# Alice's private key
a = random.randint(1, p-2)
# Bob's private key
b = random.randint(1, p-2)
print(f"Alice's private key: {a}")
print(f"Bob's private key: {b}")
# Step 3: Compute public keys
A = pow(g, a, p)  # Alice's public key
B = pow(g, b, p)  # Bob's public key
print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")

# Step 4: Exchange public keys and compute the shared secret
# Alice computes
shared_secret_alice = pow(B, a, p)
# Bob computes
shared_secret_bob = pow(A, b, p)

print(f"Alice's computed shared secret: {shared_secret_alice}")
print(f"Bob's computed shared secret: {shared_secret_bob}")

# Step 5: Verify both are equal
if shared_secret_alice == shared_secret_bob:
    print(f"Symmetric key established: {shared_secret_alice}")
else:
    print("Error: shared secrets do not match!")
