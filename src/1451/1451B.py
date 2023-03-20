t = int(input())
for _ in range(t):
    n, q = (int(i) for i in input().split())
    s = [int(i) for i in input()]
    ones = [0] * n
    for i in range(n):
        ones[i] = (ones[i - 1] if i > 0 else 0) + (s[i] == 1)
    for _ in range(q):
        l, r = (int(i) for i in input().split())
        l, r = l - 1, r - 1
        res = (
            "YES"
            if (
                (l > 0 and ones[l - 1] != (0 if s[l] == 1 else l))
                or (
                    r < n - 1
                    and ones[n - 1] - ones[r] != (0 if s[r] == 1 else (n - r - 1))
                )
            )
            else "NO"
        )
        print(res)
