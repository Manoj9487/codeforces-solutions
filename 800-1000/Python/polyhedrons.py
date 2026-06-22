n = int(input())
ans = 0
while(n > 0) :
    s = input()
    if s == "Icosahedron" :
        ans += 20
    elif s == "Cube" :
        ans += 6
    elif s == "Tetrahedron" :
        ans += 4
    elif s == "Octahedron" :
        ans += 8
    else :
        ans += 12
    n -= 1
print(ans)