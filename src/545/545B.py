a, b = (input() for _ in range(2))
cnt = sum(i != j for i, j in zip(a, b))
if cnt & 1 == 1:
    res = "impossible"
else:
    cnt /= 2
    res = []
    for i, j in zip(a, b):
        res.append(i if i == j else i if cnt > 0 else j)
        cnt -= i != j
    res = "".join(res)
print(res)
