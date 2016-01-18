__name__ = "vutsuak"

import random

input_arr = [random.randrange(0, 10) for i in range(10)]
print input_arr
count_arr = []

for i in range(10):
    count_arr.append(input_arr.count(i))
count_aux = list(count_arr)  # very important to use list
for i in range(10):
    sum = 0
    for j in count_aux[:i + 1]:
        sum += j
    count_arr[i] = sum

output = [None] * (len(input_arr) + 1)

for i in input_arr:
    output[count_arr[i]] = i
    count_arr[i] -= 1

for i in output:
    if i is not None:
        print i,