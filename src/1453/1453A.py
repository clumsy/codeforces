t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    b = set(int(i) for i in input().split())
    res = sum(i in b for i in a)
    print(res)
