_, _, b = (int(i) for i in input().split())
h = sorted(int(i) for i in input().split())
res = h[b] - h[b - 1]
print(res)
