s = input().strip()
s1 = input().strip()
s2 = input().strip()

combined = sorted(s + s1)
pile = sorted(s2)

if combined == pile:
    print("YES")
else:
    print("NO")
