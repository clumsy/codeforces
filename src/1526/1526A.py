t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    for i in range(n):
        print(a[n + i], a[i], end=" ")
    print()
