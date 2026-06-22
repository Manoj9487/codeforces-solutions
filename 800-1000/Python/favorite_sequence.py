t = int(input())
while(t > 0) :
    n = int(input())
    arr = list(map(int, input().split()))
    l = 0
    r = n - 1
    while(l < r) :
        print(arr[l], arr[r], end = " ")
        l += 1
        r -= 1
    
    if (l == r) :
        print(arr[l])

    t -= 1