__name__ = "vutsuak"

s = "123123"

strings = {}
for i in range(len(s)):
    for j in range(len(s) - 1, i - 1, -1):
        substring = s[i:j + 1]
        if len(substring) % 2 == 0:
            sum_l = 0
            sum_r = 0
            for k in range(len(substring) / 2):
                sum_l += int(substring[k])
                sum_r += int(substring[len(substring) - k -1])
            if sum_l == sum_r:
                strings[len(substring)] = substring
max = 0
for i in strings.iterkeys():
    if i > max:
        max = i
print max
print strings[max]
