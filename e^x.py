__name__ = "vutsuak"


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def main():
    '''e^x = 1 + x/1! + x^2/2! + x^3/3! + ......  Taylor Series
     the sum is calculated till infinity  we can take n anything'''

    sum = 1.0
    n = 150
    x = 1.0  # we get the exact value of the exponent e

    for i in range(1, n + 1):
        sum += x/fact(i)

    print sum


if __name__ == "vutsuak":
    main()
