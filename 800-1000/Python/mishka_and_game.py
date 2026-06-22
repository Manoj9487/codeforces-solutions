n = int(input())
m1 = 0
c1 = 0
while(n > 0) :
    m, c = map(int, input().split())
    if (m > c) :
        m1 += 1
    elif (m < c) :
        c1 += 1
    n -= 1
if (m1 > c1) :
    print("Mishka")
elif (c1 > m1) :
    print("Chris")
else :
    print("Friendship is magic!^^")