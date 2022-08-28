t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    even = sum(i & 1 for i in a[0:n:2])
    odd = sum(i & 1 for i in a[1:n:2])
    res = even % ((n + 1) // 2) == 0 and odd % (n // 2) == 0
    print("YES" if res else "NO")
