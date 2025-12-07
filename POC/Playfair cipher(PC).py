# ==========================
# Playfair Cipher in Python
# ==========================

import string

def prepare_key(key: str):
    """
    Prepare 5x5 Playfair key square from the given keyword.
    I and J are merged (J -> I).
    """
    key = key.upper()
    key = key.replace("J", "I")
    result = []

    for ch in key:
        if ch.isalpha() and ch not in result:
            result.append(ch)

    # Add remaining letters A-Z (except J because merged with I)
    for ch in string.ascii_uppercase:
        if ch == "J":
            continue
        if ch not in result:
            result.append(ch)

    # 5x5 matrix
    matrix = [result[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, ch):
    """Return (row, col) of character ch in key matrix."""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None

def prepare_plaintext(text: str):
    """
    Prepare plaintext for Playfair:
    - Uppercase
    - Remove non-letters
    - Replace J with I
    - Break into digraphs
    - Insert X between identical letters in a pair
    - Pad with X if length is odd
    """
    text = text.upper()
    text = ''.join(ch for ch in text if ch.isalpha())
    text = text.replace("J", "I")

    prepared = ""
    i = 0
    while i < len(text):
        ch1 = text[i]
        if i + 1 < len(text):
            ch2 = text[i + 1]
            if ch1 == ch2:
                prepared += ch1 + 'X'
                i += 1
            else:
                prepared += ch1 + ch2
                i += 2
        else:
            prepared += ch1 + 'X'
            i += 1

    return prepared

def playfair_encrypt(plaintext: str, matrix):
    ciphertext = ""
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            # Same row: shift right
            c1_new = (c1 + 1) % 5
            c2_new = (c2 + 1) % 5
            ciphertext += matrix[r1][c1_new] + matrix[r2][c2_new]
        elif c1 == c2:
            # Same column: shift down
            r1_new = (r1 + 1) % 5
            r2_new = (r2 + 1) % 5
            ciphertext += matrix[r1_new][c1] + matrix[r2_new][c2]
        else:
            # Rectangle: swap columns
            ciphertext += matrix[r1][c2] + matrix[r2][c1]

        i += 2

    return ciphertext

def playfair_decrypt(ciphertext: str, matrix):
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            # Same row: shift left
            c1_new = (c1 - 1) % 5
            c2_new = (c2 - 1) % 5
            plaintext += matrix[r1][c1_new] + matrix[r2][c2_new]
        elif c1 == c2:
            # Same column: shift up
            r1_new = (r1 - 1) % 5
            r2_new = (r2 - 1) % 5
            plaintext += matrix[r1_new][c1] + matrix[r2_new][c2]
        else:
            # Rectangle: swap columns
            plaintext += matrix[r1][c2] + matrix[r2][c1]

        i += 2

    return plaintext

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

# ------------- User interaction -------------
print("=== Playfair Cipher ===")
key = input("Enter keyword for key matrix: ")
matrix = prepare_key(key)

print("\nGenerated 5x5 key matrix (I/J combined):")
print_matrix(matrix)

pt = input("\nEnter plaintext: ")
prep_pt = prepare_plaintext(pt)
print("Prepared plaintext (digraphs):", " ".join(prep_pt[i:i+2] for i in range(0, len(prep_pt), 2)))

ct = playfair_encrypt(prep_pt, matrix)
print("\nCiphertext:", ct)

dec = playfair_decrypt(ct, matrix)
print("Decrypted (raw, includes X padding):", dec)
print("Decrypted pairs:", " ".join(dec[i:i+2] for i in range(0, len(dec), 2)))
