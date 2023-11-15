n, k = (int(i) for i in input().split())
t = [tuple(int(i) for i in input().split()) for _ in range(n)]


def order(i):
    return -t[i][0], t[i][1]


ranks = sorted(range(n), key=order)
res = sum(c == t[ranks[k - 1]] for c in t)
print(res)
