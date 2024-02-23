t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    b = sorted(int(i) for i in input().split())
    i = j = both = k1 = k2 = 0
    for v in range(1, k + 1):
        while i < n and a[i] < v:
            i += 1
        while j < m and b[j] < v:
            j += 1
        fst = i < n and a[i] == v
        snd = j < m and b[j] == v
        k1 += fst and not snd
        k2 += snd and not fst
        both += fst and snd
    res = "YES" if 2 * k1 <= k and 2 * k2 <= k and k1 + k2 + both == k else "NO"
    print(res)
