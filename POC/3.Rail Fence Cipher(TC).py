def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    row, step = 0, 1

    for char in text:
        fence[row].append(char)
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step
    
    encrypted = "".join("".join(row) for row in fence)
    return encrypted


def rail_fence_decrypt(cipher, rails):
    # Determine zig-zag pattern positions
    pattern = [[] for _ in range(rails)]
    row, step = 0, 1

    for _ in cipher:
        pattern[row].append('*')
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    # Fill cipher text into pattern
    index = 0
    for r in range(rails):
        for j in range(len(pattern[r])):
            pattern[r][j] = cipher[index]
            index += 1

    # Read in zig-zag
    result = ""
    row, step = 0, 1
    for _ in cipher:
        result += pattern[row].pop(0)
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step
    return result


text = input("\nEnter text for Rail Fence Cipher: ")
rails = int(input("Enter number of rails: "))

encrypted = rail_fence_encrypt(text, rails)
decrypted = rail_fence_decrypt(encrypted, rails)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
