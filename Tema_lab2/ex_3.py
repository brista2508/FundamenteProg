def generate_largest_number(numbers):

    numbers.sort(key=str, reverse=True)
    largest_number = ''.join(map(str, numbers))

    return largest_number


input_numbers = input("Introdu o lista de numere de forma 'xy' separate prin spatii: ").split()
numbers = [int(x) for x in input_numbers]

largest_number = generate_largest_number(numbers)
print("Cel mai mare numar:", largest_number)

# 12 23 54 12 38 76 34 21