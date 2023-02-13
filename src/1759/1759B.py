t = int(input())
for _ in range(t):
    m, s = (int(i) for i in input().split())
    b = sorted(int(i) for i in input().split())
    k, i = 1, 0
    while s > 0 or i < m:
        if i < m and b[i] == k:
            i += 1
        else:
            s -= k
        k += 1
    res = "YES" if s == 0 and i >= m else "NO"
    print(res)
