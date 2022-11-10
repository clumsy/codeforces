x1, x2, x3 = sorted(int(i) for i in input().split())
# it's always optimal to meet at the middle element
# otherwise we need to move both min/max and middle
# element towards the other one
res = x3 - x1
print(res)
