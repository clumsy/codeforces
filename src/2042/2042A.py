t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    for i in a:
        if i > k:
            break
        k -= i
    res = k
    print(res)
