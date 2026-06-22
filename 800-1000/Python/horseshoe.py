l = list(map(int, input().split()))
need = len(l) - len(set(l))
print(need)