n = int(input())
count = 0
max_count = 0
for _ in range(n) :
    x, y = map(int, input().split())
    count += y - x
    if count > max_count :
        max_count = count
print(max_count)
