n = input()
num = "47"
count = 0
for i in n :
    if i in num :
        count += 1
        
if count == 4 or count == 7 :
    print("YES")
else :
    print("NO")
