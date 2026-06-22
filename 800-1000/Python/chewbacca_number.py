
n = input().strip()
s1 = ""
for idx, ch in enumerate(n):
    d = int(ch)
    if idx == 0 and d == 9:
        s1 += ch  # Keep leading 9
    elif d > 4:  # 5-8 → invert to 4-1
        s1 += str(9 - d)
    else:
        s1 += ch

print(s1.lstrip('0') or '0')  # Just in case all zeros (edge case)
