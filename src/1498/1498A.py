from itertools import count

t = int(input())
for _ in range(t):
    n = int(input())

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    res = next(x for x in count(n) if gcd(x, sum(int(i) for i in str(x))) != 1)
    print(res)
