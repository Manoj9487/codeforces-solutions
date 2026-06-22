t = int(input())
while(t > 0) :
    n, k = map(int, input().split())
    s = input()
    l = 0
    c = 0
    while(l < n) :
        if (s[l] == 'B') :
            l += k
            c += 1 
        else :
            l += 1
    print(c)
    t -= 1