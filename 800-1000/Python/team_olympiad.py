n = int(input())
arr = list(map(int, input().split()))
prog = []
maths = []
PE = []
for i in range(n) :
    if arr[i] == 1 :
        prog.append(i + 1)
    elif arr[i] == 2 :
        maths.append(i + 1)
    else :
        PE.append(i + 1)

w = min(len(prog), len(maths), len(PE))
print(w)

for i in range(w) :
    print(prog[i], maths[i], PE[i])