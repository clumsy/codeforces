from collections import Counter

n, s = int(input()), Counter(int(i) for i in input().split())
res = s[4]
x = min(s[1], s[3])
s[1] -= x
s[3] -= x
res += x + s[3]
res += s[2] // 2
s[2] &= 1
s[1] -= min(s[1], 2 * s[2])
res += (s[2] > 0) + (s[1] + 3) // 4
print(res)
