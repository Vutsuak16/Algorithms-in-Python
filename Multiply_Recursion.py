__name__ = "vutsuak"


def multiply(x, y):
    if y == 0:
        return 0
    else:
        return x + multiply(x, y - 1) # 2*4= 2+2+2+2


def main():
    x = input("enter first number")
    y = input("enter second number")
    print multiply(x, y)


if __name__ == "vutsuak":
    main()
