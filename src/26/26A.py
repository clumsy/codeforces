n = int(input())
primes = [True] * (n + 1)
res = 0
for i in range(2, n + 1):
    if primes[i]:
        for j in range(i * i, n + 1, i):
            primes[j] = False
        for j in range(2, i):
            if i * j > n:
                break
            if primes[j]:
                p1 = i
                while p1 <= n:
                    p2 = j
                    while p1 * p2 <= n:
                        res += 1
                        p2 *= j
                    p1 *= i
print(res)
