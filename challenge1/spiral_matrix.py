import random

n = 5  # You can change this

# Create an empty n x n matrix
matrix = [[0] * n for _ in range(n)]

print("Original Matrix:")
for row in matrix:
    print(row)

n = 5 # You can change this

matrix = [[0] * n for _ in range(n)]

num = 1
top, bottom = 0, n - 1
left, right = 0, n - 1

while top <= bottom and left <= right:
    # Fill top row
    for col in range(left, right + 1):
        matrix[top][col] = num
        num += 1
    top += 1

    # Fill right column
    for row in range(top, bottom + 1):
        matrix[row][right] = num
        num += 1
    right -= 1

    # Fill bottom row
    if top <= bottom:
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
        bottom -= 1

    # Fill left column
    if left <= right:
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = num
            num += 1
        left += 1

print("Generated Snail Matrix:")
for row in matrix:
    print(row)

