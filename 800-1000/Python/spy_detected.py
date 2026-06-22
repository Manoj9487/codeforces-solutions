t = int(input())

while(t > 0) :
    n = int(input())
    arr = list(map(int, input().split()))
    set1 = set(arr) 
    for i in set1 :
        if (arr.count(i) == 1) :
            print(arr.index(i) + 1)
            break
    t -= 1