t = int(input())
while(t > 0) :
    n = int(input())
    s = input()
    s1 = "Timur"
    flag = False
    if (n != 5) :
        flag = True
    else :
        for i in s1 :
            if i not in s :
                flag = True
                break
    if (flag) :
        print("NO")
    else :
        print("YES")

    t -= 1