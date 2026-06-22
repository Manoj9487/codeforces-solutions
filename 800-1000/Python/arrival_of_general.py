n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
min_val = min(arr)

max_idx = arr.index(max_val)
min_idx = n - 1- arr[::-1].index(min_val)

swap = max_idx + n - 1 - min_idx

if max_idx > min_idx:
    swap -= 1

print(swap)