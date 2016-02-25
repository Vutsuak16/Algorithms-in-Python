__name__ = "vutsuak"


def poly_multiply(p1, p2, len_p1, len_p2):
    product = (len_p1 + len_p2 - 1) * [0]
    for i in range(len_p1):
        for j in range(len_p2):
            product[i + j] += p1[i] * p2[j]
    return product


def print_poly(poly):
    for i in range(1, len(poly) + 1):
        print str(poly[i - 1]) + "x^" + str(i),
    print


def main():
    p1 = [5, 0, 10, 6]
    p2 = [1, 2, 4]
    print_poly(p1)
    print_poly(p2)
    product_poly = poly_multiply(p1, p2, len(p1), len(p2))
    print_poly(product_poly)


if __name__ == "vutsuak":
    main()
