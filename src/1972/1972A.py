t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    res = 0
    i = j = n - 1
    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            res += 1
        else:
            j -= 1
        i -= 1
    print(res)
