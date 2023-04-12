s, e = input().split()
n = int(input())
if n & 1 == 0:
    res = "undefined"
else:
    n %= 4
    cw = {
        "<": 0,
        "^": 1,
        ">": 2,
        "v": 3,
    }
    diff = (cw[e] - cw[s]) % 4
    res = "cw" if diff == n else "ccw"
print(res)
