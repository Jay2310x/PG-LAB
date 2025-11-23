# Matrix Chain Multiplication using Dynamic Programming

def matrix_chain_order(dims):
    """
    dims: list of matrix dimensions.
          If there are n matrices, len(dims) = n + 1
          For example, if matrices are A1(10x20), A2(20x30), A3(30x40),
          then dims = [10, 20, 30, 40]
    """
    n = len(dims) - 1  # number of matrices

    # m[i][j] = minimum scalar multiplications needed to multiply matrices A[i..j]
    # k[i][j] = index at which the optimal split occurs
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    k = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # L is the chain length
    for L in range(2, n + 1):  # L = 2 to n
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            for x in range(i, j):
                # cost = cost of multiplying A[i..x] and A[x+1..j] + cost of multiplying results
                cost = m[i][x] + m[x + 1][j] + dims[i - 1] * dims[x] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    k[i][j] = x

    return m, k


def print_optimal_parens(k, i, j):
    """Utility to print optimal parenthesization."""
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(k, i, k[i][j])
        print_optimal_parens(k, k[i][j] + 1, j)
        print(")", end="")


# Example usage:
dims = [30, 35, 15, 5, 10, 20, 25]  # Example from standard DP textbooks
m, k = matrix_chain_order(dims)

print("Scalar Multiplication Table (m):")
for row in m[1:len(dims)]:
    print(row[1:len(dims)])

print("\nK Table (Split Positions):")
for row in k[1:len(dims)]:
    print(row[1:len(dims)])

print("\nOptimal Parenthesization:")
print_optimal_parens(k, 1, len(dims) - 1)

print(f"\n\nMinimum number of multiplications: {m[1][len(dims) - 1]}")
