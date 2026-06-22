t = int(input())
while(t > 0) :
    a, b = map(int, input().split())
    if a == b :
        print(0)
    else :
        ans = a ^ b
        if ans <= a:
            print(1)
            print(ans)
        else:
            print(-1)
    t -= 1
