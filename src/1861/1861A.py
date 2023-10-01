primes = [True] * 100
primes[0] = primes[1] = False
for i in range(2, len(primes)):
    if primes:
        j = 2
        while i * j < len(primes):
            primes[i * j] = False
            j += 1
t = int(input())
for _ in range(t):
    s = input()
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            v = int(s[i] + s[j])
            if primes[v]:
                res = v
                break
    print(res)
