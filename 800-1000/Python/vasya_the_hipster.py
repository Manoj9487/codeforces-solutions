a, b = map(int, input().split())
diff = a if a <= b else b
print(diff, abs(a - b) // 2)