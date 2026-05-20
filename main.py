from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

# Original message
data = b"Hello Cyber Security"

# Generate AES key
key = get_random_bytes(16)

# Create AES cipher
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt the data
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Encrypted Data:", ciphertext)

# Decrypt the data
decrypt_cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
plaintext = decrypt_cipher.decrypt(ciphertext)

print("Decrypted Data:", plaintext.decode())

# Generate SHA-256 hash
hash_value = hashlib.sha256(data).hexdigest()

print("SHA-256 Hash:", hash_value)
