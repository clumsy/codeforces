n = int(input())
lucky = (i for i in range(1, 1001) if all(c in "47" for c in str(i)))
res = "YES" if any(n % i == 0 for i in lucky) else "NO"
print(res)
