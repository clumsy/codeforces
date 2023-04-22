n = int(input())
res = []
for i in range(n):
    if all(int(i) not in [1, 3] for i in input().split()):
        res.append(i + 1)
print(len(res))
if res:
    print(*res)
