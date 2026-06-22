# cook your dish here
t = int(input("ENTER : "))
while t > 0:
    s = input("Enter :")
    girls = 0
    boys = 0
    count = 0
    stop = False
    for ch in s:
        if ch == "G":
            girls += 1
        elif ch == "B" :
            boys += 1
        count += 1  

        if boys > 2 * girls:
            print(count)
            stop = True
            break
    if not stop :
        print(count)
    t -= 1
