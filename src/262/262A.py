n, k = (int(i) for i in input().split())
a = input().split()
res = sum(1 for i in a if i.count("4") + i.count("7") <= k)
print(res)
