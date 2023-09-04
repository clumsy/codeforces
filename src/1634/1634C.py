t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    if k > 1 and n & 1 == 1:
        print("NO")
    else:
        print("YES")
        for i in range(1, n + 1):
            print(*range(i, i + k * n, n))
