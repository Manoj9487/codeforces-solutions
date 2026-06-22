
import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    
    seats = set()
    valid = True
    
    for i in range(n):
        seat = int(data[index])
        index += 1
        
        # First passenger can sit anywhere
        if i == 0:
            seats.add(seat)
            continue
        
        # Check if at least one neighbor is occupied
        if (seat - 1 in seats) or (seat + 1 in seats):
            seats.add(seat)
        else:
            valid = False
            # Skip remaining seats for this test case
            index += n - i - 1
            break
    
    print("YES" if valid else "NO")
