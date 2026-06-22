def bachgold(n):
    if n % 2 == 0:
        # n even: use all 2s
        k = n // 2
        primes = [2] * k
    else:
        # n odd: use one 3 and the rest 2s
        k = n // 2
        primes = [3] + [2] * (k - 1)
    print(k)
    print(' '.join(map(str, primes)))

# Example usage:
n = int(input())
bachgold(n)
