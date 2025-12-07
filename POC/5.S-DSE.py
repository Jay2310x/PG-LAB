# -------------------- S-DES Implementation --------------------

# Permutation tables
P10     = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8      = [6, 3, 7, 4, 8, 5, 10, 9]
IP      = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV  = [4, 1, 3, 5, 7, 2, 8, 6]
EP      = [4, 1, 2, 3, 2, 3, 4, 1]
P4      = [2, 4, 3, 1]

# S-boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# ---------- Utility functions ----------

def permute(bits: str, table):
    """Rearrange bits according to a permutation table (1-based indices)."""
    return ''.join(bits[i - 1] for i in table)

def left_shift(bits: str, n: int):
    """Circular left shift."""
    return bits[n:] + bits[:n]

def sbox_lookup(bits4: str, sbox):
    """Lookup 4-bit input into 2-bit output using S-box."""
    row = int(bits4[0] + bits4[3], 2)   # first and last bit
    col = int(bits4[1:3], 2)            # middle two bits
    val = sbox[row][col]
    return format(val, '02b')

# ---------- Key generation ----------

def generate_subkeys(key10: str):
    """
    Generate K1 and K2 from 10-bit key.
    key10: '1010000010' (10 bits)
    """
    # Step 1: P10
    p10_key = permute(key10, P10)
    left, right = p10_key[:5], p10_key[5:]

    # Step 2: LS-1
    left1 = left_shift(left, 1)
    right1 = left_shift(right, 1)

    # Step 3: P8 -> K1
    k1 = permute(left1 + right1, P8)

    # Step 4: LS-2 (on result of LS-1)
    left2 = left_shift(left1, 2)
    right2 = left_shift(right1, 2)

    # Step 5: P8 -> K2
    k2 = permute(left2 + right2, P8)

    return k1, k2

# ---------- Round function fK ----------

def fk(bits8: str, subkey: str):
    """
    Feistel round function.
    bits8: 8-bit string (L(4) + R(4))
    subkey: 8-bit subkey
    """
    left = bits8[:4]
    right = bits8[4:]

    # 1. Expand and permute right half
    right_ep = permute(right, EP)  # 4 -> 8 bits

    # 2. XOR with subkey
    xored = format(int(right_ep, 2) ^ int(subkey, 2), '08b')

    # 3. Split and pass through S-boxes
    left4, right4 = xored[:4], xored[4:]
    s0_out = sbox_lookup(left4, S0)
    s1_out = sbox_lookup(right4, S1)

    # 4. Combine and permute with P4
    s_output = s0_out + s1_out  # 4 bits
    p4 = permute(s_output, P4)  # 4 bits

    # 5. XOR with left half
    left_new = format(int(left, 2) ^ int(p4, 2), '04b')

    # Output new 8 bits
    return left_new + right

# ---------- S-DES encryption/decryption for 8-bit block ----------

def sdes_encrypt_block(byte8: str, k1: str, k2: str):
    # Initial Permutation
    ip = permute(byte8, IP)

    # Round 1 with K1
    temp = fk(ip, k1)

    # Swap halves
    swapped = temp[4:] + temp[:4]

    # Round 2 with K2
    temp2 = fk(swapped, k2)

    # Inverse IP
    cipher = permute(temp2, IP_INV)
    return cipher

def sdes_decrypt_block(byte8: str, k1: str, k2: str):
    # Initial Permutation
    ip = permute(byte8, IP)

    # NOTE: keys are reversed for decryption
    temp = fk(ip, k2)

    # Swap halves
    swapped = temp[4:] + temp[:4]

    # Second round with K1
    temp2 = fk(swapped, k1)

    # Inverse IP
    plain = permute(temp2, IP_INV)
    return plain

# ---------- Helper: convert text <-> binary blocks ----------

def char_to_bin8(ch: str) -> str:
    """Convert character to 8-bit binary string."""
    return format(ord(ch), '08b')

def bin8_to_char(b: str) -> str:
    """Convert 8-bit binary string to character."""
    return chr(int(b, 2))

def sdes_encrypt_text(plaintext: str, key10: str) -> str:
    k1, k2 = generate_subkeys(key10)
    ciphertext = ""
    for ch in plaintext:
        b = char_to_bin8(ch)
        c_block = sdes_encrypt_block(b, k1, k2)
        ciphertext += bin8_to_char(c_block)
    return ciphertext

def sdes_decrypt_text(ciphertext: str, key10: str) -> str:
    k1, k2 = generate_subkeys(key10)
    plaintext = ""
    for ch in ciphertext:
        b = char_to_bin8(ch)
        p_block = sdes_decrypt_block(b, k1, k2)
        plaintext += bin8_to_char(p_block)
    return plaintext

# -------------------- User interaction --------------------

if __name__ == "__main__":
    print("=== Simplified DES (S-DES) ===")
    plaintext = input("Enter plaintext: ")

    key10 = input("Enter 10-bit key (e.g. 1010000010): ").strip()
    if len(key10) != 10 or any(bit not in '01' for bit in key10):
        print("Invalid key! Please enter exactly 10 bits (0/1).")
    else:
        # Encrypt
        ciphertext = sdes_encrypt_text(plaintext, key10)
        print("\nCiphertext (as characters):", ciphertext)

        # To also show binary form:
        cipher_bin = ' '.join(char_to_bin8(c) for c in ciphertext)
        print("Ciphertext (binary per char):", cipher_bin)

        # Decrypt
        decrypted = sdes_decrypt_text(ciphertext, key10)
        print("\nDecrypted text:", decrypted)
