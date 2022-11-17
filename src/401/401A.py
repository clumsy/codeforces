n, x = (int(i) for i in input().split())
s = sum(int(i) for i in input().split())
res = (abs(s) + x - 1) // x
print(res)
