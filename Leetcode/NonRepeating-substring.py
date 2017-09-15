# Sliding window concept:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
s = "bbbbb"
sliding = {}
size = len(s)
maxlength = 0
for j in range(size):
    if s[j] not in sliding:
        sliding[s[j]] = j
    else:
        position = sliding[s[j]]
        length = j - position
        sliding = {}
        sliding[s[j]] = j
        if length > maxlength:
            maxlength = length
            
print (maxlength)