w1, h1, w2, h2 = (int(i) for i in input().split())
w1, h1, w2, h2 = (w2, h2, w1, h1) if w2 > w1 else w1, h1, w2, h2
res = (w1 + 2) * (h1 + 2) + (w2 + 2) * h2 - w1 * h1 - w2 * h2
print(res)
