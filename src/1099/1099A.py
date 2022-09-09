w, h = (int(i) for i in input().split())
u1, d1 = (int(i) for i in input().split())
u2, d2 = (int(i) for i in input().split())
while h > 0:
    w += h
    if h == d1:
        w = max(w - u1, 0)
    if h == d2:
        w = max(w - u2, 0)
    h -= 1
print(w)
