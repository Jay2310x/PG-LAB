import random
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(characters, frequencies):
    heap = []

    for i in range(len(characters)):
        heapq.heappush(heap, Node(characters[i], frequencies[i]))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root, code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code
        return

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)
    return codes


def average_code_length(codes, frequencies, characters):
    total = sum(frequencies)
    weighted_sum = 0
    for ch, code in codes.items():
        i = characters.index(ch)
        weighted_sum += len(code) * frequencies[i]
    return weighted_sum / total


# ---------- MAIN PROGRAM ----------

N = int(input("Enter number of characters: "))

characters = [chr(65 + i) for i in range(N)]  # A, B, C, ...
frequencies = [random.randint(1, 50) for _ in range(N)]

print("\nGenerated Characters:", characters)
print("Generated Frequencies:", frequencies)

root = build_huffman_tree(characters, frequencies)
codes = generate_codes(root)

print("\nHuffman Codes:")
for c in codes:
    print(c, ":", codes[c])

avg_len = average_code_length(codes, frequencies, characters)
print("\nAverage Code Length =", avg_len)
