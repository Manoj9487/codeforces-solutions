t = int(input())
while(t > 0) :
    arr = list(map(int, input().split()))
    count = 0
    for i in arr :
        if arr[0] < i :
            count += 1
    print(count)
    t -= 1