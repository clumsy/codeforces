n = int(input())
res = n // 100
n %= 100
res += n // 20
n %= 20
res += n // 10
n %= 10
res += n // 5
n %= 5
res += n
print(res)