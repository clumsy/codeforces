s, k = input(), int(input())
w = [int(i) for i in input().split()]
res = sum((i + 1) * w[ord(c) - ord("a")] for i, c in enumerate(s)) + max(w) * sum(
    i + 1 + len(s) for i in range(k)
)
print(res)
