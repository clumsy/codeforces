x, y, z = (int(i) for i in input().split())
res = "0" if z == 0 and x == y else "?" if z >= abs(x - y) else "+" if x > y else "-"
print(res)
