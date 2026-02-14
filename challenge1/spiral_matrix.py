import random

n = 6

matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]


print("Original Matrix:")
for row in matrix:
    print(row)

def spiral_order(matrix):
    n = len(matrix)
    result = []

    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        # Traverse top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


print("\nSpiral Order:")
print(spiral_order(matrix))
