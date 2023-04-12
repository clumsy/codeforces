import re

n, s = int(input()), input()
res = re.compile("ogo(go)*").sub("***", s)
print(res)
