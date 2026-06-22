n = int(input())
val = 0
while(n > 0) :
    s = input()
    if (s == '++X' or s == 'X++') :
        val += 1
    else :
        val -= 1
    n -= 1
print(val)