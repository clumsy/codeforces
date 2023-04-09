n = int(input())
a, b = ([None] * n for _ in range(2))
changed, ordered = False, True
for i in range(n):
    a[i], b[i] = (int(i) for i in input().split())
    changed |= a[i] != b[i]
    ordered &= i == 0 or b[i] <= b[i - 1]
res = "rated" if changed else "maybe" if ordered else "unrated"
print(res)
