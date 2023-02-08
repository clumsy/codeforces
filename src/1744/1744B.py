t = int(input())
for _ in range(t):
    n, q = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    e, res = 0, 0
    for i in a:
        res += i
        e += i & 1 == 0
    o = n - e
    for _ in range(q):
        type, x = (int(i) for i in input().split())
        if type == 0:
            res += e * x
            if x & 1 == 1:
                e, o = 0, n
        else:
            res += o * x
            if x & 1 == 1:
                e, o = n, 0
        print(res)
