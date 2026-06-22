t = int(input())
for i in range(t) :
    s = input()
    n = int(s)
    root = int(n ** 0.5)
    if root * root == n :
        print(0, root)
    else :
        print(-1)
