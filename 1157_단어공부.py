s = input()

letters = {}
for idx in range(len(s)):
    if s[idx].upper() in letters:
        letters[s[idx].upper()] += 1
    else:
        letters[s[idx].upper()] = 1

max_count = max(list(letters.values()))
most_frequent = []
for k, v in letters.items():
    if v == max_count:
        most_frequent.append(k)

if len(most_frequent) > 1:
    result = '?'
else:
    result = most_frequent[0]

print(result)
