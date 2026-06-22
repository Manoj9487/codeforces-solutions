t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    place = 1
    temp = n
    while temp > 0:
        digit = temp % 10
        if digit != 0:
            ans.append(digit * place)
        temp //= 10
        place *= 10
    print(len(ans))
    print(*ans)
