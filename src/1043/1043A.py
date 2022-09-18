n, a = int(input()), [int(i) for i in input().split()]
# a1 + a2 + ... + an < k - a1 + k - a2 + ... + k - an
# 2*(a1 + a2 + ... + an) < nk
# 2*(a1 + a2 + ... + an)/n < k
k = (2 * sum(a) // n) + 1
res = max(k, max(a))
print(res)
