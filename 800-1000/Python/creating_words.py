t = int(input())

while(t > 0) :
    s1, s2 = map(str, input().split())
    print(s2[0] + s1[1::], s1[0] + s2[1::])
    t -= 1