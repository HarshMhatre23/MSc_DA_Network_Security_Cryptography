import hmac
import hashlib

# Function to calculate HMAC-SHA1
def calculate_hmac_sha1(message, key):
    hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha1)
    return hmac_obj.hexdigest()

# Main Program
msg = input("Enter message: ")
secret_key = input("Enter secret key: ")

signature = calculate_hmac_sha1(msg, secret_key)

print("\nMessage:", msg)
print("Secret Key:", secret_key)
print("HMAC-SHA1 Signature:", signature)
