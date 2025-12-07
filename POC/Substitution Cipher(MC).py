# ================================
# Monoalphabetic Substitution Cipher
# ================================

import string

def generate_maps(key):
    """
    Create encrypt and decrypt dictionaries.
    key must be 26 uppercase letters, permutation of A-Z
    """
    alphabet = string.ascii_uppercase
    
    key = key.upper()
    encrypt_map = {}
    decrypt_map = {}
    
    for p, c in zip(alphabet, key):
        encrypt_map[p] = c
        decrypt_map[c] = p
    
    return encrypt_map, decrypt_map


def encrypt(plaintext, encrypt_map):
    plaintext = plaintext.upper()
    ciphertext = ""
    
    for ch in plaintext:
        if ch.isalpha():
            ciphertext += encrypt_map[ch]
        else:
            ciphertext += ch  # keep spaces, numbers, punctuations
    
    return ciphertext


def decrypt(ciphertext, decrypt_map):
    ciphertext = ciphertext.upper()
    plaintext = ""
    
    for ch in ciphertext:
        if ch.isalpha():
            plaintext += decrypt_map[ch]
        else:
            plaintext += ch
    
    return plaintext


# ----------------- User Input -----------------

print("=== Monoalphabetic Substitution Cipher ===")
key = input("Enter 26-letter key (e.g., QWERTYUIOPASDFGHJKLZXCVBNM): ").strip()

# Validate key
if len(key) != 26 or not key.isalpha() or len(set(key.upper())) != 26:
    print("Invalid key! Must be 26 unique letters.")
    exit()

encrypt_map, decrypt_map = generate_maps(key)

text = input("Enter plaintext: ")

cipher = encrypt(text, encrypt_map)
print("\nCiphertext:", cipher)

plain_again = decrypt(cipher, decrypt_map)
print("Decrypted:", plain_again)
