t = int(input())
while(t > 0) :
    n = int(input())
    arr = list(map(int, input().split()))
    print(-sum(arr))
    t -= 1