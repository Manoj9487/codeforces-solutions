s = input()
v = "aeiouy"
s = s.lower()
for i in s :
    if i not in v :
        print(".", i, sep = "", end = "")
print("")