n = int(input())
# C.C.C.C
# .C.C.C.
# C.C.C.C
# .........
res = (n**2 + 1) // 2
print(res)
for i in range(n):
    print(("C." * (n // 2 + 1))[i & 1 : n + (i & 1)])
