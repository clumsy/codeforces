a, b, c = (int(i) for i in input().split())
n, x = int(input()), (int(i) for i in input().split())
res = 0
for i in x:
    res += 1 if b < i < c else 0
print(res)
