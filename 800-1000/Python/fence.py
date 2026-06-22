# Vanya and Fence - Codeforces 677A

# Read n and h
n, h = map(int, input().split())

# Read the heights of friends
heights = list(map(int, input().split()))

width = 0
for x in heights:
    if x > h:
        width += 2
    else:
        width += 1

print(width)
