from operator import mul
from functools import reduce

s = input()
q = s.count("?")
num_q = 10 ** (q - 1) * (9 if s[0] == "?" else 10) if q else 1
a = len(set(c for c in s if "A" <= c <= "Z"))
num_a = reduce(mul, range(10 - a + 1, 11), 1)
num_a = (num_a * 9) // 10 if "A" <= s[0] <= "Z" else num_a
res = num_q * num_a
print(res)
