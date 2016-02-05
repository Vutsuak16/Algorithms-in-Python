__name__ = "vutsuak"

import math

''' This is a script to check if a number is a fermat number or not and print all fermat's number in a range
 They are expressed as Fn= 2^(2^n) +1
 They have the property that except F0 and F1 all end in 7
 This property I will be utilizing'''


def check_fermats(n):
    F0 = 3
    F1 = 5

    if int(n) == F0 or int(n) == F1:
        print n + " is a Fermat's Number"
    elif n[-1] == "7":
        N = math.log(math.log(int(n) - 1) / math.log(2)) / math.log(2)
        if N.is_integer():
            print n + " is a Fermat's Number"
    else:
        pass


def main():
    for i in range(10000000):
        check_fermats(str(i))


if __name__ == "vutsuak":
    main()
