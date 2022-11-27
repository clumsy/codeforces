n = int(input())
a = [int(i) for i in input().split()]
res = 0
for i in range(n - 2, -1, -1):
    if a[i] != a[-1]:
        res = i + 1
        break
print(res)
