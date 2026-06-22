# Read number of test cases
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    carpet = [input().strip() for _ in range(n)]
    target = 'vika'
    col = 0
    success = True
    for ch in target:
        found = False
        while col < m:
            # Check all rows in the current column
            for row in range(n):
                if carpet[row][col] == ch:
                    found = True
                    col += 1  # move to the next column for next letter
                    break
            if found:
                break
            col += 1  # Check next column if not found in this one
        if not found:
            success = False
            break
    print('YES' if success else 'NO')
