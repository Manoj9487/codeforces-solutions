t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    zeros = s.count('0')
    ones = n - zeros
        
    max_good_pairs = (zeros // 2) + (ones // 2)
    total_pairs = n // 2

    bad_pairs = total_pairs - k
        
    if 0 <= k <= total_pairs and bad_pairs <= min(zeros, ones):
        print("YES")
    else:
        print("NO")
