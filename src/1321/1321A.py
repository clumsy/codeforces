n = int(input())
r = (int(i) for i in input().split())
b = (int(i) for i in input().split())
rs, bs = 0, 0
for r, b in zip(r, b):
    rs += r > b
    bs += b > r
res = -1 if rs == 0 else (bs + rs) // rs
print(res)
