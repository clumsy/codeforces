t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = set(a)
    res = min(i for i in range(max(cnt) + 2) if i > max(cnt) or i not in cnt)
    print(res)
