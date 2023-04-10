s = input()
n = len(s)
left = right = 0
lo = hi = pivot = s.index("^")
while lo > 0 or hi < n - 1:
    if lo > 0:
        lo -= 1
        left += (pivot - lo) * int(s[lo]) if s[lo] != "=" else 0
    if hi < n - 1:
        hi += 1
        right += (hi - pivot) * int(s[hi]) if s[hi] != "=" else 0
res = "balance" if left == right else "left" if left > right else "right"
print(res)
