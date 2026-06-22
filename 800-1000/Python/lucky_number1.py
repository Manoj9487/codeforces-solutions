def is_lucky(num):
    while num > 0:
        digit = num % 10
        if digit not in (4, 7):
            return False
        num //= 10
    return True

n = int(input())

for i in range(1, n + 1):
    if n % i == 0 and is_lucky(i):
        print("YES")
        exit()

print("NO")
