# Read the input numbers
x = list(map(int, input().split()))

# The largest number must be a + b + c
total_sum = max(x)
x.remove(total_sum)

# Remaining three are pair sums: a+b, a+c, b+c
ab, ac, bc = x

# Calculate individual numbers
a = total_sum - bc
b = total_sum - ac
c = total_sum - ab

print(a, b, c)
