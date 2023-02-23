t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    if n & 1 == 1:
        n -= 3
        res.append("7")
    res.extend(["1"] * (n // 2))
    res = "".join(res)
    print(res)
