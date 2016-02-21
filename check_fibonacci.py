__name__ = "vutsuak"


def isFibo(n):
    n1 = (5 * (n ** 2) + 4) ** (0.5)
    n2 = (5 * (n ** 2) - 4) ** (0.5)
    if n1.is_integer() or n2.is_integer():
        print str(n) + " is a fibonacci number"


def main():
    for i in range(1, 1600):
        isFibo(i)


if __name__ == "vutsuak":
    main()
