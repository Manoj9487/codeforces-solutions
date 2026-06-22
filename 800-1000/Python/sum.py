t = int(input())
while(t > 0) :
    a, b, c = map(int, input().split())
    m = max(a, b, c)
    if (a + b + c - m == m) :
        print("YES")
    else :
        print("NO")
    t -= 1