n = int(input())
for i in range(-n, n + 1, 1):
    space = " " * (2 * abs(i))
    asc = " ".join(str(i) for i in range(n - abs(i) + 1))
    desc = " ".join(str(i) for i in reversed(range(n - abs(i))))
    res = space + asc + (" " + desc if desc else "")
    print(res)
