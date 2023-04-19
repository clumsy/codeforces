n, k = (int(i) for i in input().split())
f, t = [None] * n, [None] * n
for i in range(n):
    f[i], t[i] = (int(i) for i in input().split())


def rank(i):
    return f[i] - max(0, t[i] - k)


res = rank(max(range(n), key=rank))
print(res)
