t = int(input())
while(t > 0) :
    n = int(input())
    if (n  >= 4 and n % 2 == 0) :
        print(n // 4 + 1)
    elif (n % 2 == 0) :
        print(n // 2)
    else :
        print(0)
    t -= 1