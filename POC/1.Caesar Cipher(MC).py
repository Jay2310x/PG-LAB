def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

text = input("Enter text for Caesar Cipher: ")
key = int(input("Enter shift key: "))

encrypted = caesar_encrypt(text, key)
decrypted = caesar_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
