n = int(input())

l = list(map(int, input().split()))
max = l[0]
min = l[0]
count = 0
for i in l :
    if i > max :
        count += 1
        max = i
    elif i < min :
        count += 1
        min = i
print(count)