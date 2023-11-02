n, m, k = (int(i) for i in input().split())
x = [int(input()) for _ in range(m)]
f = int(input())
res = sum(bin(i ^ f)[2:].count("1") <= k for i in x)
print(res)
