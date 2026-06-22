t = int(input())
while(t > 0) :
    k = int(input())
    count = 0
    num = 1
    while(count < k) :
        if (num % 3 != 0 and num % 10 != 3) :
            count += 1
        if (count == k) :
            print(num)
            break 
        num += 1

    t -= 1