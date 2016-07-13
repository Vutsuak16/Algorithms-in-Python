__name__ = "vutsuak"

#logic : if digits(without last digit)-(2*last_digit )is divisible by  then number is divisible by 7
import random

n = random.randrange(1, 1000)
last_digit = n % 10
n = str(n)
print n
x = int(n[:-1])
if (x - (2 * last_digit)) % 7 == 0:
    print n + " is divisible by 7"
else:
    print n + " is not divisible by 7 "x

