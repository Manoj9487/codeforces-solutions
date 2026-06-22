t = int(input())
for _ in range(t):
    s, k, m = map(int, input().split())

    # If Vadim leaves before first flip
    if m < k:
        print(max(0, s - m))
        continue

    # Number of flips Vadim performs: floor(m / k)
    flips = m // k

    # Remaining time after last flip Vadim performs
    rem = m % k

    # Sand falling right after the last flip Vadim does
    if flips % 2 == 1:
        # After odd flips: s - k (if positive)
        cur = max(0, s - k)
    else:
        # After even flips: min(s, k)
        cur = min(s, k)

    # Sand finishes cur minutes after last flip
    if rem >= cur:
        print(0)
    else:
        print(cur - rem)
