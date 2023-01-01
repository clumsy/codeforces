n, a = int(input()), (int(i) for i in input().split())
twos = sum(i == 2 for i in a)
res = min(twos, n - twos)
res += (n - twos - res) // 3
print(res)
