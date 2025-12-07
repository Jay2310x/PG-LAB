def vigenere_encrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

text = input("\nEnter text for Vigenere Cipher: ")
key = input("Enter keyword: ")

encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
