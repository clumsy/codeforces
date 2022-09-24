t = int(input())
for _ in range(t):
    n = int(input())
    # if n is even: 1+n, 2+n-1, ... (n // 2 in total) => common length is n+1
    # if n is odd we have n // 2 from (even) n - 1 (all n in length) + 1 remaining n
    res = (n + 1) // 2
    print(res)
