res = "YES"
for _ in range(8):
    s = input()
    if s not in {"WBWBWBWB", "BWBWBWBW"}:
        res = "NO"
print(res)
