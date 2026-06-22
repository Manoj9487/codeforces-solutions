s = input().strip()
letters = [x.strip() for x in s[1:-1].split(',') if x.strip()]
print(len(set(letters)))
