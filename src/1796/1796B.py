t = int(input())
for _ in range(t):
    a, b = (input() for _ in range(2))
    if a[0] == b[0]:
        res = a[0] + "*"
    elif a[-1] == b[-1]:
        res = "*" + a[-1]
    else:
        match = set(a[i : i + 2] for i in range(len(a) - 1)) & set(
            b[i : i + 2] for i in range(len(b) - 1)
        )
        res = "*" + next(iter(match)) + "*" if match else None
    print("YES" if res else "NO")
    if res:
        print(res)
