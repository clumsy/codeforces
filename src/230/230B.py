from math import sqrt


prime = [True] * 1000001
prime[0] = prime[1] = False
for i in range(2, len(prime)):
    if prime[i]:
        for j in range(i * i, len(prime), i):
            prime[j] = False
n, a = int(input()), (int(i) for i in input().split())
for i in a:
    sr = int(sqrt(i))
    res = "YES" if sr * sr == i and prime[sr] else "NO"
    print(res)
