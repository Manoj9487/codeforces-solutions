n, k = map(int, input().split())
l = list(map(int, input().split()))
count = 0
for i in range(0, len(l)) :
    if l[i] >= l[k - 1] and l[i] > 0 :
        count += 1
print(count)