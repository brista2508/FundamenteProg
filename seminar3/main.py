from math import gcd

def simplify(a):
    d = gcd(a[0], a[1])
    return a[0] // d, a[1] // d

def test_simplify():
    assert simplify((2, 2)) == (1, 1)

def add(a, b):
    return simplify((a[0] * b[1] + a[1] * b[0], a[1] * b[1]))

def test_add():
    assert add((1, 2), (2, 3)) == (7, 6)
    assert add((1, 2), (1, 2)) == (1, 1)

def multiply(a, b):
    return simplify((a[0] * b[0], a[1] * b[1]))

def test_multiply():
    assert multiply((1, 2), (2, 3)) == (1, 3)
    assert multiply((1, 2), (1, 2)) == (1, 4)

def divide(a, b):
    return simplify((a[0] * b[1], a[1] * b[0]))

def test_divide():
    assert divide((1, 2), (2, 3)) == (3, 4)
    assert divide((1, 2), (1, 2)) == (1, 1)

def add_frac(fracs, frac):
    fracs.append(frac)

def sum_fracs(fracs):
    s = 0, 1

    for frac in fracs:
        s = add(s, frac)

    return s

def menu():
    return """
        1 - Add fraction
        2 - Sum fractions
        3 - Multiply fractions
        4 - Divide fractions
        0 - Exit
    """

def main():
    fracs = []

    while True:
        print(menu())
        opt = int(input('opt= '))

        if opt == 1:
            n = int(input('n= '))
            m = int(input('m= '))
            add_frac(fracs, (n, m))

        if opt == 2:
            s = sum_fracs(fracs)
            print('Sum= ', s)

        if opt == 3:
            n1 = int(input('n1= '))
            m1 = int(input('m1= '))
            n2 = int(input('n2= '))
            m2 = int(input('m2= '))
            result = multiply((n1, m1), (n2, m2))
            print('Product= ', result)

        if opt == 4:
            n1 = int(input('n1= '))
            m1 = int(input('m1= '))
            n2 = int(input('n2= '))
            m2 = int(input('m2= '))
            result = divide((n1, m1), (n2, m2))
            print('Quotient= ', result)

        if opt == 0:
            break

test_simplify()
test_add()
test_multiply()
test_divide()
main()
