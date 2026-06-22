t = int(input())
while(t > 0) :
    s = input()
    c = 0
    s1 = "codeforces"
    for i in range(len(s1)) :
        if s[i] != s1[i] :
            c += 1
    print(c)

    t -= 1