__name__ = "vutsuak"

import random

a = [random.randrange(1,1000) for i in range(10)]
a = sorted(a)
print a
X = int(input("enter the number to search"))
Lo = 0
Hi = 9
flg = 0
mid = Lo + ((Hi - Lo) / (a[Hi] - a[Lo])) * (X - a[Lo])
for i in a:
    mid = Lo + ((Hi - Lo) / (a[Hi] - a[Lo])) * (X - a[Lo])
    Mid_Value = a[mid]
    if X == Mid_Value:
        flg = 1
        print "number found at index = " + str(a.index(X))
        break
    elif X < Mid_Value:
        Hi = mid - 1
    else:
        Lo = mid + 1

if flg != 1:
    print "number not found in the array"
