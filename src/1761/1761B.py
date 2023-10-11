t = int(input())
for _ in range(t):
    n, s = int(input()), [int(i) for i in input().split()]
    res = (
        n - (n - 2) // 2
        if n > 3 and n & 1 == 0 and all(s[i] == s[i & 1] for i in range(2, n))
        else n
    )
    print(res)
