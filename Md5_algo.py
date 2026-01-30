import hashlib

# Function to compute MD5 hash
def compute_md5(message):
    md5_hash = hashlib.md5()          # Create MD5 object
    md5_hash.update(message.encode()) # Convert string to bytes
    return md5_hash.hexdigest()

# Main Program
text = input("Enter message: ")

digest = compute_md5(text)

print("\nMessage:", text)
print("MD5 Digest:", digest)
