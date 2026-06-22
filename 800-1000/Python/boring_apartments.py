t = int(input())
while(t > 0) :
    x = int(input())
    val = int(str(x)[0])
    p = len(str(x))
    print(int((val - 1) * 10 + p*(p + 1) / 2 ))
    t -= 1