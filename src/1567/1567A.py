t = int(input())
for _ in range(t):
    _, r = input(), input()
    res = "".join({"U": "D", "D": "U"}.get(c, c) for c in r)
    print(res)
