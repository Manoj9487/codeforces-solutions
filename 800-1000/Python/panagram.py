n = int(input())
s = input()
s = s.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0
for i in alphabet :
    if i not in s :      
        count = 1
if count == 1 :
    print("NO")
else :
    print("YES")