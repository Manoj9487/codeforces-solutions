t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    d = abs(b - a)
    moves = (d + 9) // 10 
    print(moves)
