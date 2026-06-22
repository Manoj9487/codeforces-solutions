
n = int(input())
s = ""
i = 0
while i < n:
    if i == n - 1:
        if i % 2 != 0:
            s += "I love it"
        else:
            s += "I hate it"
    else:
        if i % 2 != 0:
            s += "I love that "
        else:
            s += "I hate that "
    i += 1
print(s)
