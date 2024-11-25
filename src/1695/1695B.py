t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    if n & 1 == 1:
        res = "Mike"
    else:
        mi = 0
        for i in range(n):
            if a[i] < a[mi]:
                mi = i
        res = "Joe" if mi & 1 == 0 else "Mike"
    print(res)
