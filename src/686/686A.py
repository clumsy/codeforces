n, x = (int(i) for i in input().split())
res = 0
for _ in range(n):
    sign, delta = input().split()
    delta = int(delta)
    if sign == "+":
        x += delta
    elif x >= delta:
        x -= delta
    else:
        res += 1
res = x, res
print(*res)
