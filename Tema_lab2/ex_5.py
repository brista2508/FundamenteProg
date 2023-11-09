def filter_numbers_by_relation():
    input_numbers = input("Introdu o lista de numere de forma 'xy' separate prin spatii: ")
    relation = input("Introdu relatia (ex:, 'x=y*3', 'x/y=2', y/2=x, x+x=y, x<y): ")

    numbers = input_numbers.split()
    filtered_numbers = []

    for number in numbers:
        x, y = map(int, number)
        if relation == 'x=y*3' and x == y * 3:
            filtered_numbers.append(number)
        elif relation == 'x/y=2' and x / y == 2:
            filtered_numbers.append(number)
        elif relation == 'y/2=x' and y / 2 == x:
            filtered_numbers.append(number)
        elif relation == 'x+x=y' and x + x == y:
            filtered_numbers.append(number)
        elif relation == 'x<y' and x < y:
            filtered_numbers.append(number)

    result = ' '.join(filtered_numbers)
    print("Numerele filtrate:", result)


filter_numbers_by_relation()


# 12 23 54 12 38 76 34 21