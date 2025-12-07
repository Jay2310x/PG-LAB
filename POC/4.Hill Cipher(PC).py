import math

# ---------- Helper functions ----------

def mod_inverse(a, m):
    """Return modular inverse of a under modulo m, or None if it doesn't exist."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_inverse_2x2(key):
    """
    Inverse of 2x2 matrix modulo 26.
    key = [[a,b],[c,d]]
    """
    a, b = key[0]
    c, d = key[1]

    det = a * d - b * c
    det_mod = det % 26

    det_inv = mod_inverse(det_mod, 26)
    if det_inv is None:
        return None  # Not invertible

    # Adjugate matrix
    inv = [
        [ d * det_inv % 26, (-b) * det_inv % 26],
        [(-c) * det_inv % 26,  a * det_inv % 26]
    ]
    return inv

def text_to_numbers(text):
    return [ord(ch) - 65 for ch in text]

def numbers_to_text(nums):
    return ''.join(chr(n + 65) for n in nums)

def clean_text(text):
    text = text.upper()
    return ''.join(ch for ch in text if ch.isalpha())


# ---------- Hill Cipher core functions ----------

def hill_encrypt(plaintext, key):
    """
    plaintext: string
    key: 2x2 matrix [[a,b],[c,d]]
    """
    plaintext = clean_text(plaintext)

    # Pad with 'X' if odd length
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    nums = text_to_numbers(plaintext)
    ciphertext_nums = []

    for i in range(0, len(nums), 2):
        v0 = nums[i]
        v1 = nums[i + 1]

        c0 = (key[0][0] * v0 + key[0][1] * v1) % 26
        c1 = (key[1][0] * v0 + key[1][1] * v1) % 26

        ciphertext_nums.extend([c0, c1])

    return numbers_to_text(ciphertext_nums)


def hill_decrypt(ciphertext, key):
    """
    ciphertext: string
    key: 2x2 matrix [[a,b],[c,d]]
    """
    ciphertext = clean_text(ciphertext)
    inv_key = matrix_inverse_2x2(key)

    if inv_key is None:
        raise ValueError("Key matrix is not invertible modulo 26. Choose another key.")

    nums = text_to_numbers(ciphertext)
    plaintext_nums = []

    for i in range(0, len(nums), 2):
        v0 = nums[i]
        v1 = nums[i + 1]

        p0 = (inv_key[0][0] * v0 + inv_key[0][1] * v1) % 26
        p1 = (inv_key[1][0] * v0 + inv_key[1][1] * v1) % 26

        plaintext_nums.extend([p0, p1])

    return numbers_to_text(plaintext_nums)


# ---------- User interaction ----------

print("=== Hill Cipher (2x2 Matrix) ===")
pt = input("Enter plaintext: ")

print("\nEnter key matrix elements (2x2) row-wise as 4 integers.")
print("Example for matrix [[3, 3], [2, 5]] enter: 3 3 2 5")
k1, k2, k3, k4 = map(int, input("Enter 4 numbers: ").split())

key_matrix = [[k1, k2],
              [k3, k4]]

# Encrypt
try:
    ct = hill_encrypt(pt, key_matrix)
    print("\nCiphertext:", ct)

    # Decrypt
    dec = hill_decrypt(ct, key_matrix)
    print("Decrypted (with any padding):", dec)

except ValueError as e:
    print("Error:", e)
