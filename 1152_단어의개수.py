s = input()

count = 0
idx = 0
while idx < len(s):
    if s[idx] == ' ':
        idx += 1
    else:
        count += 1
        new_idx = idx
        while new_idx < len(s) and s[new_idx] != ' ':
            new_idx += 1
        idx = new_idx
print(count)


