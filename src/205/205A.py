n = int(input())
t = [int(i) for i in input().split()]
o = sorted(range(n), key=t.__getitem__)
res = 1 if n == 1 else o[0] + 1 if t[o[0]] != t[o[1]] else "Still Rozdil"
print(res)
