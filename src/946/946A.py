n, a = int(input()), (int(i) for i in input().split())
res = 0
for i in a:
    res += -i if i < 0 else i
print(res)
