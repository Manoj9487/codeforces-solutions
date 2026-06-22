# Read the 5x5 matrix
matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of '1'
for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1:
            row_pos = r + 1  # convert to 1-based indexing
            col_pos = c + 1

# Compute minimum moves to bring '1' to center (row 3, col 3)
moves = abs(row_pos - 3) + abs(col_pos - 3)
print(moves)
