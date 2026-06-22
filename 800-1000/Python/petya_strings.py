s1 = input().lower()
s2 = input().lower()
flag = 0
for i in range(0, len(s1)) :
    if (s1[i] > s2[i]) :
        print(1)
        flag = 1
        break
    elif (s2[i] > s1[i]) :
        print(-1)
        flag = 1
        break
if (flag == 0) :
    print(0)
