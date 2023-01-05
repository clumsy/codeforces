a = [int(i) for i in input().split()]
res = sum(a[int(c) - 1] for c in input())
print(res)
