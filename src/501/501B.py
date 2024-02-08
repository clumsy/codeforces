n = int(input())
usr, res = [], []
for _ in range(n):
    old, new = input().split()
    try:
        i = res.index(old)
        res[i] = new
    except ValueError:
        res.append(new)
        usr.append(old)
print(len(res))
for u, a in zip(usr, res):
    print(u, a)
