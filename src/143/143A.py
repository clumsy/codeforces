r1, r2 = (int(i) for i in input().split())
c1, c2 = (int(i) for i in input().split())
d1, d2 = (int(i) for i in input().split())
# x1 y1
# x2 y2
# r1 + c1 - d1 - d2 = x1 - y2
# d1 = x1 + y2
x1 = (r1 + c1 - d2) // 2
y2 = d1 - x1
y1 = r1 - x1
x2 = r2 - y2
s = sorted(set([x1, y1, x2, y2]))
if (
    len(s) != 4
    or min(s) < 1
    or max(s) > 9
    or x1 + y1 != r1
    or x2 + y2 != r2
    or x1 + y2 != d1
    or x2 + y1 != d2
    or x1 + x2 != c1
    or y1 + y2 != c2
):
    print(-1)
else:
    print(x1, y1)
    print(x2, y2)
