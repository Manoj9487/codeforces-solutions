n = int(input())
count = 0
while(n > 0) :
    l = list(map(int, input().split()))
    if sum(l) >= 2 :
        count += 1
    n -= 1
print(count)