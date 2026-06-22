s = input()

ans = ""
n = len(s)
i = 0
while(i < n) :
    if (s[i] == '-' and s[i + 1] == '.') :
        ans += '1'
        i += 2
    elif (s[i] == '-' and s[i + 1] == '-') :
        ans += '2'
        i += 2
    else :
       ans += '0'
       i += 1
print(ans)
