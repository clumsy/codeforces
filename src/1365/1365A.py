t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    rs, cs = set(), set()
    for r in range(n):
        a = input().split()
        for c in range(m):
            if a[c] == "1":
                rs.add(r)
                cs.add(c)
    m = min(n - len(rs), m - len(cs))
    res = "Ashish" if m & 1 == 1 else "Vivek"
    print(res)
