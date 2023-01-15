t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    ones = sum(i == 1 for i in a)
    twos = n - ones
    res = 2 * (twos & 1)
    ones -= res
    res = "NO" if ones < 0 or ones & 1 == 1 else "YES"
    print(res)
