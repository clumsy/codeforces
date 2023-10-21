t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    c = (int(i) for i in input().split())

    def apply(cur, y):
        for i in y:
            if (cur | i) & x != cur | i:
                break
            cur |= i
        return cur

    cur = apply(0, a)
    cur = apply(cur, b)
    cur = apply(cur, c)
    res = "YES" if cur == x else "NO"
    print(res)
