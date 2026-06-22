t = int(input())
while(t > 0) :
    a, b, c = list(map(int, input().split()))
    m1 = max(a, b, c)
    m2 = min(a, b, c)
    print(a + b + c - m1 - m2)
    t -= 1