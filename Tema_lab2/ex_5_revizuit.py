def filter_numbers_by_relation(numbers, relation):
    filtered_numbers = []

    for number in numbers:
        x, y = map(int, number)
        try:
            if eval(relation):
                filtered_numbers.append(number)
        except:
            continue

    return filtered_numbers

input_numbers = input("Introduceți o listă de numere sub forma 'xy', separate de spațiu: ").split()
relation = input("Introduceți relația dorită (de ex. 'x == y * 3', 'x / y == 2'): ")

filtered_numbers = filter_numbers_by_relation(input_numbers, relation)

if filtered_numbers:
    print("Numerele care respectă relația:", ' '.join(filtered_numbers))
else:
    print("Niciun număr nu respectă relația sau relația introdusă este incorectă.")


# 12 23 54 12 38 76 34 21