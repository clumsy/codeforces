a, b = input().lstrip("0"), input().lstrip("0")
diff = len(a) - len(b)
res = "="
if diff != 0:
    res = ">" if diff > 0 else "<"
else:
    for (
        a,
        b,
    ) in zip(a, b):
        diff = ord(a) - ord(b)
        if diff != 0:
            res = ">" if diff > 0 else "<"
            break
print(res)
