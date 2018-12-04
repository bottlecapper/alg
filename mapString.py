
# Q: Give a list of strings, find the mapping from 1-26 for each string that maximize the value for each string.
# No distingulish between capital letter and lower case, other characters do not count.

string = 'jaoisdjfjpowqeirnoiwqnropwqnopfnoanwopnfwerpoiwqrnoqwrp'

hist = [0] * 26

for char in string:
    num = ord(char)
    if num >= 65 and num <= 90:
        num -= 65
    elif num >= 97 and num <= 122:
        num -= 97
    hist[num] += 1

print(hist)
idx = [i[0] for i in sorted(enumerate(hist), key=lambda x: x[1])]
# idx = np.argsort(hist)
print(idx)

def mapping(char):
    num = ord(char)
    if num >= 65 and num <= 90:
        num -= 65
    elif num >= 97 and num <= 122:
        num -= 97
    value = idx.index(num) + 1
    return value

sumValue = 0
for char in string:
    sumValue += mapping(char)

print(sumValue)
