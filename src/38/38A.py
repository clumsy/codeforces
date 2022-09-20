n = int(input())
d = [int(i) for i in input().split()]
a, b = (int(i) for i in input().split())
res = sum(d[i] for i in range(a - 1, b - 1))
print(res)
