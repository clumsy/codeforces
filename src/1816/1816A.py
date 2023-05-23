t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    if gcd(a, b) == 1:
        res = [(a, b)]
    else:
        res = [(a - 1, 1), (a, b)]
    print(len(res))
    for i in range(len(res)):
        print(*res[i])
