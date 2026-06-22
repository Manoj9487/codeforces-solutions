n, k = map(int, input().split())
time_left = 240 - k
i = 0
time_taken = 0
while(time_taken <= time_left and i <= n) :
    i += 1
    time_taken += 5 * i
print(i - 1)
