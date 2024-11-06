import numpy as np

# Input the matrix
matrix = []
n = int(input("Enter the size of the matrix (n x n): "))
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert to numpy array and compute inverse
matrix = np.array(matrix)
try:
    inverse = np.linalg.inv(matrix)
    print("Inverse of the matrix:")
    print(inverse)
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted.")
