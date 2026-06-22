n, k, l, c, d, p, nl, np = map(int, input().split())
drink_ml = k * l
lemon_slices = c * d

print(min(drink_ml // nl, lemon_slices , p // np) // n)