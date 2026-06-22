t = int(input())
while(t > 0) :
    a, b, c, d = map(int, input().split())
    if (a == b and b == c and c == d and d == a) :
        print("YES")
    else :
        print("NO")
    t -= 1