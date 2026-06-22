t = int(input())
while(t > 0) :
    n = int(input())
    l = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in l :
        if i % 2 == 0 :
            even += 1
        else :
            odd += 1
    if (even > 0 and odd > 0) :
        l.sort()
        for i in l :
            print(i, end = " ")
    else :
        for i in l :
           print(i, end = " ")
    t -= 1