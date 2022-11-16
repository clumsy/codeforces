t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    w = sorted(int(i) for i in input().split())
    if x == sum(w):
        print("NO")
    else:
        print("YES")
        res, lo, hi = [], 0, n - 1
        while lo <= hi:
            if w[lo] == x:
                v = w[hi]
                hi -= 1
            else:
                v = w[lo]
                lo += 1
            x -= v
            res.append(v)
        print(*res)
