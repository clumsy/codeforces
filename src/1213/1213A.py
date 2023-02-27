n, x = int(input()), (int(i) for i in input().split())
odd = sum(i & 1 == 1 for i in x)
res = min(odd, n - odd)
print(res)
