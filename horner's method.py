__name__ = "vutsuak"


def horner(poly, n, x):
    result = poly[0]
    for i in range(1, n):
        result = result * x + poly[i]
    print "the value of polynomial at x = " + str(x) + " is " + str(result)


def main():
    # Let us evaluate value of 2x3 - 6x2 + 2x - 1 for x = 3
    poly = [2, -6, 2, -1]
    x = 3
    n = len(poly)
    horner(poly, n, x)


if __name__ == "vutsuak":
    main()
