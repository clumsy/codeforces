n, m, k = (int(i) for i in input().split())
p = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
c = (int(i) for i in input().split())
ma = [-1] * m
for i in range(n):
    sc = s[i] - 1
    ma[sc] = i if ma[sc] == -1 or p[i] > p[ma[sc]] else ma[sc]
res = sum(i - 1 != ma[s[i - 1] - 1] for i in c)
print(res)
