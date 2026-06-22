t = int(input())
while(t > 0) :
    x, y, n = map(int, input().split())
    print(n - (n - y) % x)
    t -= 1

