from bisect import bisect_right

n = int(input())
a, b = 0, 1
fib = [a, b]
while a < 10e9:
    a, b = b, a + b
    fib.append(b)
res = None
for i in range(len(fib)):
    d = n - fib[i]
    if res is not None or d < 0:
        break
    lo, hi = i, bisect_right(fib, d) - 1
    while lo <= hi:
        diff = d - fib[lo] - fib[hi]
        if diff == 0:
            res = " ".join(str(j) for j in (fib[i], fib[lo], fib[hi]))
            break
        elif diff < 0:
            hi -= 1
        else:
            lo += 1
res = res if res is not None else "I'm too stupid to solve this problem"
print(res)
