n, S = (int(i) for i in input().split())
res = S // n + (S % n > 0)  # math.ceil(S / n)
print(res)
