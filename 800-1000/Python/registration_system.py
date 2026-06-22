n = int(input())
users = dict()

for _ in range(n):
    name = input()
    if name not in users:
        print("OK")
        users[name] = 1
    else:
        print(f"{name}{users[name]}")
        users[f"{name}{users[name]}"] = 1
        users[name] += 1
