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













# letters = {}
# for idx in range(len(s)):
#     if s[idx].upper() in letters:
#         letters[s[idx].upper()] += 1
#     else:
#         letters[s[idx].upper()] = 1
#
# for k, v in letters.items():
#     max_count = 0
#     if v > max_count:
#         max_count = v
#         most_frequent = k
# print(letters)
# if list(letters.keys()).count(k) > 1:
#     result = '?'
# else:
#     result = most_frequent
# print(result)




# s = input()
#
# letters = []
# for idx in range(len(s)):
#     if s[idx] in letters:
#         continue
#     elif s[idx].upper() in letters or s[idx].lower() in letters:
#         continue
#     else:
#         letters.append(s[idx].upper())
#
# counts = [0 for _ in range(len(letters))]
# for letter in s:
#     letter_idx = letters.index(letter.upper())
#     counts[letter_idx] += 1
#
# for i in range(len(counts)):
#     max_count = counts[0]
#     max_idx = 0
#     if max_count < counts[i]:
#         max_count = counts[i]
#         max_idx = i
#
# if counts.count(max_count) > 1:
#     result = '?'
# else:
#     result = letters[max_idx]
#
# print(result)