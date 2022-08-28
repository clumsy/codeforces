t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    idx = sorted(range(n), key=lambda i: a[i])
    for i in idx:
        if k < a[i]:
            break
        k += b[i]
    print(k)
