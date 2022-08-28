t = int(input())
for _ in range(t):
    n, B, x, y = (int(i) for i in input().split())
    a = [0] * n
    for i in range(n):
        a[i] = a[i - 1] + x if a[i - 1] + x <= B else a[i - 1] - y
    print(sum(a))
