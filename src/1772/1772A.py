n = int(input())
for _ in range(n):
    res = sum(int(i) for i in input().split("+"))
    print(res)
