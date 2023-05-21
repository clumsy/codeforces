t = int(input())
for _ in range(t):
    s = input()
    res = 1
    for i, c in enumerate(s):
        if c == "0" and i == 0:
            res = 0
            break
        elif c == "?":
            res *= 9 + (i != 0)
    print(res)
