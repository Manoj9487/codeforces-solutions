import math
t = int(input())
for i in range(t) :
    n = int(input())
    arr = list(map(int, input().split()))

    flag = False

    for i in range(2, 100) :
        for j in arr:
            if math.gcd(j, i) == 1:
                print(i)
                flag = True
                break
        if (flag) :
            break
    if (not flag) :
        print(-1)
