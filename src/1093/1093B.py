t = int(input())
for _ in range(t):
    s = input()
    res = -1 if len(set(s)) == 1 else "".join(sorted(s))
    print(res)
