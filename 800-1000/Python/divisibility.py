t = int(input())
while(t > 0) :
    a, b = map(int, input().split())
    if (a % b != 0) :
        print(b - (a % b))
    else :
        print(0)
    t -= 1