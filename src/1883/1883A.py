t = int(input())
for _ in range(t):
    s = (int(i if i != "0" else "10") for i in input())
    res, c = 0, 1
    for d in s:
        res += abs(d - c) + 1
        c = d
    print(res)
