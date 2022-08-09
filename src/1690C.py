t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(i) for i in input().split()]
    f = [int(i) for i in input().split()]
    for i in range(n):
        d = f[i] - max(s[i], f[i - 1] if i > 0 else 0)
        print(d, end=" ")
    print()
