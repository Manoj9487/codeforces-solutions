t = int(input())
while(t > 0) :
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    check_dist = [arr[i + 1] - arr[i] for i in range(0, n-1)]
    check_dist.append((x - arr[n - 1]) * 2)
    check_dist.append(arr[0] - 0)
    print(max(check_dist))
    t -= 1