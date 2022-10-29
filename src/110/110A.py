n = input()
num_lucky = sum(1 for i in n if i in {"4", "7"})
is_lucky = all(c in {"4", "7"} for c in str(num_lucky))
res = "YES" if is_lucky else "NO"
print(res)
