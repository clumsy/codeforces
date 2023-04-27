n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
o = [i for i in range(1, k * n + 1) if i not in set(a)]
for i in range(k):
    print(a[i], *o[i * (n - 1) : (i + 1) * (n - 1)])
