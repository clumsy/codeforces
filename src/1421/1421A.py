t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = (a ^ (a & b)) + (b ^ (a & b))
    print(res)