n = int(input())
for _ in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - min(a)*m)
