from collections import Counter
t = int(input())
while(t > 0) :
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    c = Counter(arr)

    if (c[k] > 0) :
        print("YES")
    else :
        print("NO")
    t -= 1