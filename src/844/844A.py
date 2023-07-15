s, k = input(), int(input())
res = max(0, k - len(set(s))) if k <= len(s) else "impossible"
print(res)
