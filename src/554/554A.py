s = input()
# we can insert a new letter in n + 1 positions between letters in s
# for each letter in s we have 25 other letters that differ
# but we only have one unique for each letter in s
res = 25 * (len(s) + 1) + 1
print(res)
