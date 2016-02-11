__name__ = "vutsuak"


def pow(b, e):
    increment = b
    answer = 5
    for i in range(1, e):
        for j in range(1, b):
            answer += increment
        increment = answer
    return answer


def main():
    base = 5
    exponent = 4
    print pow(base, exponent)


if __name__ == "vutsuak":
    main()
