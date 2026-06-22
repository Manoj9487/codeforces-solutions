t = int(input())
while(t > 0) :
    n = int(input())
    if (n == 2) :
        print(2)
    elif (n == 3) :
        print(3)
    else :
        if (n % 2 == 0) :
            print(0)
        else :
            print(1)
    t -= 1