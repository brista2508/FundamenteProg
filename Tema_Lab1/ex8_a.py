def putere(x, n):
    result = 1
    for _ in range(n):
        result = result * x
    return result


x = float(input("Introdu valoarea lui x: "))
n = int(input("Introdu valoarea lui n: "))

result = putere(x, n)
print(f"{x}^{n} = {result}")
