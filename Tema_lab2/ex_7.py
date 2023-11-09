import math

def find_CMMMC_between_indices(numbers, from_index, to_index):
    if from_index < 0 or from_index >= len(numbers) or to_index < 0 or to_index >= len(numbers):
        return None

    num1 = numbers[from_index]
    num2 = numbers[to_index]

    CMMDC = math.gcd(num1, num2)

    CMMMC = num1 * num2 // CMMDC

    return CMMMC


input_numbers = input("Introdu o lista de numere de forma 'xy' separate prin spatii: ").split()
numbers = [int(x) for x in input_numbers]

from_index = int(input("Introduceți indexul 'de la': "))
to_index = int(input("Introduceți indexul 'catre': "))

CMMMC = find_CMMMC_between_indices(numbers, from_index, to_index)

if CMMMC:
    print("CMMMC între indicii {} și {} este: {}".format(from_index, to_index, CMMMC))
else:
    print("Indici invalizi. Introdu indici valizi în cadrul listei.")

# 12 23 54 12 38 76 34 21