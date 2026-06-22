t = int(input())
while(t > 0) :
    n = int(input())
    s = input() 
    l = 0
    r = n - 1
    minlen = n

    while(l < r) :
        if (s[l] != s[r]) :
            minlen = min(minlen, r - l + 1 - 2)
            l += 1
            r -= 1
        elif (l == r) :
            minlen = 1
        elif (s[l] == s[r]) :
            minlen = min(minlen, r - l + 1)
            break 

    print(minlen)
    t -= 1