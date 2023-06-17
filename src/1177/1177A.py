k = int(input())
m = 9
while k > len(str(m)) * (m - (m + 1) // 10 + 1):
    k -= len(str(m)) * (m - (m + 1) // 10 + 1)
    m = m * 10 + 9
n = len(str(m))
x = str((m // 10 + 1) + (k - 1) // n)
res = str(x)[(k - 1) % n]
print(res)
