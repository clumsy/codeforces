s = input()
res = "CHAT WITH HER!" if len(set(s)) & 1 == 0 else "IGNORE HIM!"
print(res)
