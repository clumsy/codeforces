lo, hi = (int(i) for i in input().split())


def count(x):
    if x <= 0:
        return 0
    i = 2  # 1_0, 1_1, 1_00, 1_01
    s = prv = nxt = 0
    while nxt < x:
        nxt = int("".join("7" if d == "1" else "4" for d in bin(i)[3:]))
        s += nxt * (min(nxt, x) - prv)
        prv = nxt
        i += 1
    return s


res = count(hi) - count(lo - 1)
print(res)
