n = int(input())
p = sorted(int(i) for i in input().split())
b, w = 1, 2
rb = rw = 0
for i in p:
    rb += abs(i - b)
    rw += abs(i - w)
    b += 2
    w += 2
res = min(rb, rw)
print(res)
