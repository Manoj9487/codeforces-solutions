n = int(input())
arr = list(map(int, input().split()))
large = max(arr)
arr.remove(large)
s = 0
for i in arr :
    s += (large - i)
print(s)