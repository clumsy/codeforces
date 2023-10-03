t = int(input())
for _ in range(t):
    n, a, q = (int(i) for i in input().split())
    s = input()
    res, j = 2 if a == n else 0, 0
    cur = a
    for c in s:
        j += c == "+"
        cur += 1 if c == "+" else -1
        if cur == n:
            res = 2
        elif a + j == n:
            res = max(res, 1)
    res = ["NO", "MAYBE", "YES"][res]
    print(res)
