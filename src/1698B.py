t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    if k == 1:
        input()  # does not matter
        print((n - 1) // 2)  # we can make maximum number of too tall piles
        continue
    a = [int(i) for i in input().split()]
    # does not change for k = 2+
    res = sum(1 for i in range(1, n - 1) if a[i] > a[i - 1] + a[i + 1])
    print(res)
