n, a = int(input()), [int(i) for i in input().split()]
# 100x/ai = 100(Sai-1 + x)/Sn
# xSn = ai(Sai-1 + x)
# x = ai*Sai-1/(Sn - ai)
sn, si, res = sum(a), 0, set()
res = set([0])
for i in a:
    for x in range(1, i + 1):
        si += 1
        if (100 * x) // i == (100 * si) // sn:
            res.add((100 * x) // i)
res = sorted(res)
print(*res, sep="\n")
