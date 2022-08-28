t = int(input())
for _ in range(t):
    _, z = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = max(i | z for i in a)
    print(res)
