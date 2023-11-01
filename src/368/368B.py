n, m = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
uniq, val = set(), [0] * n
for i in range(n)[::-1]:
    uniq.add(a[i])
    val[i] = len(uniq)
for _ in range(m):
    li = int(input()) - 1
    res = val[li]
    print(res)
