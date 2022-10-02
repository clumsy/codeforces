t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "Yes" if sum(i & 1 for i in a) == n else "No"
    print(res)
