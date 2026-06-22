t = int(input())
while(t > 0) :
    n, m, p, q = map(int, input().split())
    if p * m == q *(n - p - 1) :
        print("YES")
    else :
        print("NO")
    t -= 1