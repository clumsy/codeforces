t = int(input())
for x in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    for i in range(1, n // 2 + 1):
        print(a[i], a[0])
