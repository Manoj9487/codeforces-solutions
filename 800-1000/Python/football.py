s = input()
count_1 = 0
count_0 = 0
flag = False

for i in s:
    if i == "1":
        count_1 += 1
        count_0 = 0
    else:
        count_1 = 0
        count_0 += 1
    if count_0 == 7 or count_1 == 7:
        print("YES")
        flag = True
        break 

if not flag:
    print("NO")
