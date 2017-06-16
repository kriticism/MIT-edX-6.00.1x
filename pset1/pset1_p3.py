#s = 'azcbobobegghakl'
count = 0
maxCount = 0
res = 0

for c in range(len(s) - 1):
    if (s[c] <= s[c + 1]):
        count += 1
        if count > maxCount:
            maxCount = count
            res = c + 1
    else:
        count = 0
start = res - maxCount
print('Longest substring in alphabetical order is:', s[start:res + 1])
