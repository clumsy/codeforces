MAX = 10**6
prime = [True] * MAX
prime[1] = False
for i in range(2, MAX):
    if prime[i]:
        for j in range(i * i, MAX, i):
            prime[j] = False

t = int(input())
for _ in range(t):
    d = int(input())
    for i in range(1 + d, MAX):
        if prime[i]:
            f = i
            break
    for i in range(f + d, MAX):
        if prime[i]:
            s = i
            break
    res = f * s
    print(res)
