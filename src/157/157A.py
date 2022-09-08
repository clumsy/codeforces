n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
r = [sum(a[k][j] for j in range(n)) for k in range(n)]
c = [sum(a[i][k] for i in range(n)) for k in range(n)]
res = sum(1 for j in range(n) for i in range(n) if c[j] > r[i])
print(res)
