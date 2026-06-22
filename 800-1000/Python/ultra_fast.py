# Read the two binary strings
a = input().strip()
b = input().strip()

# Compute the bitwise XOR digit by digit
result = ''.join('1' if x != y else '0' for x, y in zip(a, b))

# Output the result preserving leading zeros
print(result)
