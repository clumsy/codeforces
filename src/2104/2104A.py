t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    s = a + b + c
    res = (
        "YES"
        if s % 3 == 0 and max(a, b) <= s // 3 and c - s // 3 == 2 * s // 3 - (a + b)
        else "NO"
    )
    print(res)
