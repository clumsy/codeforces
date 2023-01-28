t = int(input())
for k in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    b = [int(i) for i in input().split()]
    res = "YES" if all(i + j <= x for i, j in zip(a, reversed(b))) else "NO"
    if k < t - 1:
        input()
    print(res)
