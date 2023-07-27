s, ind = input().split(">"), 0
for c in s:
    if not c:
        continue
    closing = c.startswith("</")
    if closing:
        ind -= 2
    print(" " * ind + c + ">")
    if not closing:
        ind += 2
