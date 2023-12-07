s, k = input(), int(input())
n, r = divmod(len(s), k)


def is_pali(p):
    lo, hi = 0, len(p) - 1
    while lo < hi:
        if p[lo] != p[hi]:
            return False
        lo += 1
        hi -= 1
    return True


res = (
    "YES" if r == 0 and all(is_pali(s[i * n : (i + 1) * n]) for i in range(k)) else "NO"
)
print(res)
