t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    total = sum(int(i) for i in input().split())
    print(max(0, total - m))
