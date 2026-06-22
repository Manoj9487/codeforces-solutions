
n = int(input()) 

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

lv1 = set(l1[1:])
lv2 = set(l2[1:])

lv_union = lv1 | lv2

if len(lv_union) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
