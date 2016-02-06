__name__ = "vutsuak"

'''Given two strings str1 and str2, find if str1 is a subsequence of str2.
 A subsequence is a sequence that can be derived from another sequence by deleting some elements
 without changing the order of the remaining elements (source: wiki). Expected time complexity is linear.
 ex:
Input: str2 = "AXY", str1 = "ADXCPY"
Output: True (str1 is a subsequence of str2)

Input: str2 = "AXY", str1 = "YADXCP"
Output: False (str1 is not a subsequence of str2)'''

s1 = raw_input("enter string 1")
s2 = raw_input("enter string 2")

# we check if s2 is a subsequence of s1
index = 0
s = ""
for i in s2:
    for j in range(index, len(s1)):
        if i == s1[j]:
            s += i
            index = j
            break

if s == s2:
    print s2 + " is a subsequence of " + s1
else:
    print s2 + " is  not a subsequence of " + s1
