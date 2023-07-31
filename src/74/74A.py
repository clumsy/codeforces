n = int(input())
ttl, res = {}, None
for _ in range(n):
    hdl, pls, mns, a, b, c, d, e = input().split()
    ttl[hdl] = 100 * int(pls) - 50 * int(mns) + sum(int(i) for i in (a, b, c, d, e))
    if res is None or ttl[hdl] > ttl[res]:
        res = hdl
print(res)
